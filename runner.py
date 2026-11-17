"""In-browser Python runner: CodeMirror editor + Pyodide in a Web Worker."""
import hashlib
import json

import streamlit as st
import streamlit.components.v1 as components

RUNNER_HTML = r"""<!doctype html>
<html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/theme/material-darker.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/addon/edit/matchbrackets.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/addon/edit/closebrackets.min.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&family=Inter:wght@400;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; }
  body { margin: 0; padding: 2px; background: transparent;
         font-family: "Inter", "Cairo", system-ui, sans-serif; color: #0b1f3a; }
  .card { border: 1px solid #dbe5f1; border-radius: 18px; background: #ffffff; overflow: hidden;
          box-shadow: 0 1px 3px rgba(0,0,0,.05); }
  .head { display: flex; align-items: center; justify-content: space-between; padding: 9px 16px;
          background: #f3f7fc; border-bottom: 1px solid #e3ebf5; font-weight: 600; font-size: 14px; }
  .head .ttl { display: flex; align-items: center; gap: 8px; }
  .head .ttl .ic { color: #ff7a1a; font-family: "JetBrains Mono", monospace; }
  .pill { background: #e6eefa; color:#1e4e8c; font-weight:700; border-radius: 999px; padding: 2px 11px; font-size: 12px; direction: ltr; }
  .ed { margin: 12px 14px 0 14px; border-radius: 14px; overflow: hidden; direction: ltr; }
  .CodeMirror { font-family: "JetBrains Mono", Consolas, monospace; font-size: 14px; line-height: 21px;
                height: auto; background: #0f1b2d; }
  .CodeMirror-gutters { background: #0f1b2d; border-right: 1px solid #1e2d45; }
  textarea.fallback { width: 100%; font-family: "JetBrains Mono", monospace; font-size: 14px;
                      background: #0f1b2d; color: #eeffff; border: 0; padding: 10px; }
  .stdin { margin: 10px 14px 0 14px; }
  .stdin label { display: block; font-size: 12.5px; color: #5b6472; margin-bottom: 4px; }
  .stdin textarea { width: 100%; height: 58px; resize: vertical; direction: ltr; border: 1px solid #d3deec;
                    border-radius: 10px; padding: 6px 10px; font-family: "JetBrains Mono", monospace;
                    font-size: 13px; background: #fff; }
  .bar { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; padding: 10px 14px; }
  button { font-family: inherit; font-size: 14px; border-radius: 12px; border: 1px solid #d3deec;
           background: #fff; padding: 7px 14px; cursor: pointer; color: #374151; }
  button:hover { background: #f3f7fc; }
  button:disabled { opacity: .45; cursor: default; }
  button.run { background: #ff7a1a; border-color: #ff7a1a; color: #fff; font-weight: 700; padding: 7px 20px; }
  button.run:hover { background: #e8650a; }
  button.stop { border-color: #e2a5a5; color: #a33; }
  .status { font-size: 12.5px; color: #6b7280; }
  .outwrap { margin: 0 14px 14px 14px; }
  .outhead { font-size: 12.5px; color: #6b7280; margin-bottom: 4px; }
  pre.out { margin: 0; height: __OUTH__px; overflow: auto; background: #0f172a; color: #e5e7eb;
            border-radius: 12px; padding: 10px 12px; font-family: "JetBrains Mono", monospace; font-size: 13px;
            line-height: 1.5; white-space: pre-wrap; word-break: break-word; direction: ltr; text-align: left; }
  pre.out .err { color: #fca5a5; }
  pre.out .muted { color: #94a3b8; }
  .verdict { margin: 0 14px 14px 14px; border-radius: 12px; padding: 9px 12px; font-size: 14px; display: none; }
  .verdict.ok { display: block; background: #e7f6ec; color: #1d6b3a; border: 1px solid #b8e2c6; }
  .verdict.bad { display: block; background: #fdeeee; color: #8a2020; border: 1px solid #f2c3c3; }
  .verdict pre { margin: 6px 0 0 0; direction: ltr; text-align: left; background: #fff; border-radius: 8px;
                 padding: 6px 10px; font-family: "JetBrains Mono", monospace; font-size: 13px; color: #0b1f3a; }
  [dir=rtl] { font-family: "Cairo", "Inter", system-ui, sans-serif; }
</style></head>
<body>
<div class="card" id="card">
  <div class="head"><span class="ttl"><span class="ic">&lt;&gt;</span><span id="t-title"></span></span><span class="pill">Python</span></div>
  <div class="ed" id="ed"></div>
  <div class="stdin" id="stdinBox" style="display:none"><label id="t-stdin" dir="auto"></label><textarea id="stdin" spellcheck="false"></textarea></div>
  <div class="bar">
    <button class="run" id="btnRun">▶ <span id="t-run"></span></button>
    <button class="stop" id="btnStop" disabled>■ <span id="t-stop"></span></button>
    <button id="btnReset">↺ <span id="t-reset"></span></button>
    <button id="btnCopy">⧉ <span id="t-copy"></span></button>
    <span class="status" id="status"></span>
  </div>
  <div class="outwrap"><div class="outhead" id="t-output"></div><pre class="out" id="out"></pre></div>
  <div class="verdict" id="verdict"></div>
</div>

<script id="worker-src" type="text/js-worker">
const BASE = "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/";
self.importScripts(BASE + "pyodide.js");
let py = null, lines = [], li = 0;
const PRELUDE = [
  "import builtins, linecache, sys, _bridge",
  "def _web_input(prompt=''):",
  "    value = _bridge.next_line()",
  "    if value is None:",
  "        raise EOFError('No value left for input(): type the values in the Program input box, one per line.')",
  "    print(str(prompt) + str(value))",
  "    return str(value)",
  "builtins.input = _web_input",
  "def _run_user(code):",
  "    linecache.cache['main.py'] = (len(code), None, code.splitlines(True), 'main.py')",
  "    namespace = {'__name__': '__main__'}",
  "    try:",
  "        exec(compile(code, 'main.py', 'exec'), namespace)",
  "    finally:",
  "        sys.stdout.flush()",
  "        sys.stderr.flush()",
].join("\n");
function cleanTraceback(msg) {
  const src = String(msg).split("\n"), out = [];
  let skip = false;
  for (const l of src) {
    if (/^\s*File "/.test(l)) {
      skip = l.indexOf('File "main.py"') === -1;
      if (!skip) out.push(l);
      continue;
    }
    if (skip && /^\s{4}/.test(l)) continue;
    skip = false;
    out.push(l);
  }
  return out.join("\n").trim();
}
const ready = (async () => {
  py = await loadPyodide({ indexURL: BASE });
  py.registerJsModule("_bridge", { next_line: () => (li < lines.length ? lines[li++] : null) });
  await py.runPythonAsync(PRELUDE);
  self.postMessage({ type: "ready" });
})().catch(e => self.postMessage({ type: "fatal", text: String(e) }));
self.onmessage = async (ev) => {
  await ready;
  if (!py) return;
  const code = ev.data.code, stdin = ev.data.stdin || "";
  lines = stdin.replace(/\r/g, "").split("\n");
  if (lines.length && lines[lines.length - 1] === "") lines.pop();
  li = 0;
  const decOut = new TextDecoder(), decErr = new TextDecoder();
  py.setStdout({ write: buf => { self.postMessage({ type: "out", text: decOut.decode(buf, { stream: true }) }); return buf.length; } });
  py.setStderr({ write: buf => { self.postMessage({ type: "err", text: decErr.decode(buf, { stream: true }) }); return buf.length; } });
  let ok = true;
  try {
    await py.loadPackagesFromImports(code, { messageCallback: m => self.postMessage({ type: "status", text: m }) });
    py.globals.get("_run_user")(code);
  } catch (e) {
    ok = false;
    self.postMessage({ type: "err", text: cleanTraceback(e && e.message ? e.message : e) + "\n" });
  }
  self.postMessage({ type: "done", ok: ok });
};
</script>

<script>
const P = __PAYLOAD__;
const $ = id => document.getElementById(id);
document.getElementById("card").setAttribute("dir", P.dir);
for (const k of ["title", "run", "stop", "reset", "copy", "output", "stdin"]) $("t-" + k).textContent = P.t[k];
$("status").textContent = P.t.first_run;

// ---------- editor (CodeMirror, with a plain textarea as fallback) ----------
const KEY = "pyplat:" + P.key;
let saved = null;
try { saved = localStorage.getItem(KEY); } catch (e) {}
let editor = null, fallback = null;
if (window.CodeMirror) {
  editor = CodeMirror($("ed"), {
    value: saved !== null ? saved : P.code, mode: "python", theme: "material-darker",
    lineNumbers: true, indentUnit: 4, tabSize: 4, matchBrackets: true, autoCloseBrackets: true,
    viewportMargin: Infinity,
    extraKeys: {
      "Tab": cm => cm.somethingSelected() ? cm.indentSelection("add") : cm.replaceSelection("    ", "end"),
      "Shift-Tab": cm => cm.indentSelection("subtract"),
      "Ctrl-Enter": () => run(), "Cmd-Enter": () => run()
    }
  });
  editor.setSize(null, P.editorHeight);
  editor.on("change", () => { try { localStorage.setItem(KEY, editor.getValue()); } catch (e) {} });
} else {
  fallback = document.createElement("textarea");
  fallback.className = "fallback"; fallback.spellcheck = false;
  fallback.style.height = P.editorHeight + "px";
  fallback.value = saved !== null ? saved : P.code;
  fallback.addEventListener("input", () => { try { localStorage.setItem(KEY, fallback.value); } catch (e) {} });
  $("ed").appendChild(fallback);
}
const getCode = () => editor ? editor.getValue() : fallback.value;
const setCode = v => editor ? editor.setValue(v) : (fallback.value = v);

if (P.showStdin) { $("stdinBox").style.display = "block"; $("stdin").value = P.stdin; }

// ---------- output helpers ----------
const out = $("out");
let outLen = 0, collected = "";
function write(text, cls) {
  if (outLen > 20000) return;
  outLen += text.length;
  if (cls !== "err") collected += text;
  const span = document.createElement("span");
  if (cls) span.className = cls;
  span.textContent = outLen > 20000 ? text + "\n… (output truncated)" : text;
  out.appendChild(span);
  out.scrollTop = out.scrollHeight;
}
function norm(s) { return s.replace(/\r/g, "").split("\n").map(x => x.replace(/\s+$/, "")); }
function check() {
  if (P.expected === null) return;
  const got = norm(collected.trim()), exp = norm(P.expected.trim()).filter(x => x.trim() !== "");
  let i = 0, ok = true;
  for (const e of exp) {
    while (i < got.length && got[i].indexOf(e) === -1) i++;
    if (i >= got.length) { ok = false; break; }
    i++;
  }
  const v = $("verdict");
  if (ok) { v.className = "verdict ok"; v.textContent = P.t.check_ok; }
  else {
    v.className = "verdict bad"; v.textContent = P.t.check_bad;
    const pre = document.createElement("pre"); pre.textContent = P.expected; v.appendChild(pre);
  }
}

// ---------- worker management ----------
let worker = null, running = false, t0 = 0, readyFlag = false;
function makeWorker() {
  const src = document.getElementById("worker-src").textContent;
  const w = new Worker(URL.createObjectURL(new Blob([src], { type: "text/javascript" })));
  w.onmessage = ev => {
    const m = ev.data;
    if (m.type === "ready") { readyFlag = true; $("status").textContent = P.t.running; }
    else if (m.type === "status") { $("status").textContent = m.text; }
    else if (m.type === "out") write(m.text);
    else if (m.type === "err") write(m.text, "err");
    else if (m.type === "fatal") { write(P.t.load_fail + "\n" + m.text + "\n", "err"); finish(false); worker = null; readyFlag = false; }
    else if (m.type === "done") finish(m.ok);
  };
  w.onerror = e => { write(P.t.load_fail + "\n", "err"); finish(false); worker = null; readyFlag = false; };
  return w;
}
function finish(ok) {
  running = false;
  $("btnRun").disabled = false; $("btnStop").disabled = true;
  if (outLen === 0) write(P.t.no_output, "muted");
  $("status").textContent = P.t.done.replace("{t}", ((performance.now() - t0) / 1000).toFixed(2));
  check();
}
function run() {
  if (running) return;
  running = true; out.textContent = ""; outLen = 0; collected = "";
  $("verdict").className = "verdict"; $("verdict").textContent = "";
  $("btnRun").disabled = true; $("btnStop").disabled = false;
  if (!worker) { worker = makeWorker(); readyFlag = false; }
  $("status").textContent = readyFlag ? P.t.running : P.t.loading;
  t0 = performance.now();
  worker.postMessage({ code: getCode(), stdin: P.showStdin ? $("stdin").value : "" });
}
$("btnRun").onclick = run;
$("btnStop").onclick = () => {
  if (worker) worker.terminate();
  worker = null; readyFlag = false; running = false;
  $("btnRun").disabled = false; $("btnStop").disabled = true;
  write("\n■ " + P.t.stopped + "\n", "muted");
  $("status").textContent = P.t.stopped;
};
$("btnReset").onclick = () => {
  setCode(P.code);
  try { localStorage.removeItem(KEY); } catch (e) {}
  if (P.showStdin) $("stdin").value = P.stdin;
  out.textContent = ""; outLen = 0; collected = "";
  $("verdict").className = "verdict";
};
$("btnCopy").onclick = () => {
  const text = getCode();
  const done = () => { const s = $("t-copy"); s.textContent = P.t.copied; setTimeout(() => s.textContent = P.t.copy, 1400); };
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).then(done).catch(() => legacyCopy(text, done));
  } else legacyCopy(text, done);
};
function legacyCopy(text, done) {
  const ta = document.createElement("textarea"); ta.value = text; document.body.appendChild(ta);
  ta.select(); try { document.execCommand("copy"); done(); } catch (e) {} ta.remove();
}
</script>
</body></html>
"""


def code_runner(code, texts, rtl, uid, stdin="", expected=None, show_stdin=None, max_lines=24):
    """Display an editable, runnable Python cell (Pyodide runs in the learner's browser)."""
    code = code.strip("\n")
    if show_stdin is None:
        show_stdin = bool(stdin) or "input(" in code
    n_lines = code.count("\n") + 1
    editor_h = min(max(n_lines, 5), max_lines) * 21 + 10
    out_h = 200
    payload = {
        "code": code, "stdin": stdin, "expected": expected, "showStdin": show_stdin,
        "editorHeight": editor_h, "dir": "rtl" if rtl else "ltr",
        "key": hashlib.md5((uid + code).encode("utf-8")).hexdigest()[:16],
        "t": texts,
    }
    page = (RUNNER_HTML.replace("__OUTH__", str(out_h))
            .replace("__PAYLOAD__", json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")))
    height = 44 + 12 + editor_h + (92 if show_stdin else 0) + 58 + 22 + out_h + (70 if expected else 0) + 26
    if hasattr(st, "iframe"):
        st.iframe(page, height=height)
    else:
        components.html(page, height=height, scrolling=False)
