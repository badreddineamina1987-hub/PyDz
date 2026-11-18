"""
===============================================================================
 PyDZ · Learn Python, week by week · trilingual platform (FR / EN / AR)
 Created by Dr. BADREDDINE Amina

 Follows the ministerial programme (first year, semester 1), week by week.

 Files
   app.py        interface (this file)
   syllabus.py   official programme: module sheet + the 15 weeks
   i18n.py       interface texts in English, French and Arabic
   runner.py     in-browser Python runner (Pyodide)
   weeks/wNN.py  content of each week (lesson, examples, exercises, quiz)
   assets/       PyDZ icon (SVG for the page, PNG for the browser tab)

 Run locally:   pip install streamlit   then   streamlit run app.py
===============================================================================
"""
import base64
import html
import importlib
import re
from pathlib import Path

import streamlit as st

from i18n import AUTHOR, LANGS, UI, T, runner_texts
from runner import code_runner
from syllabus import MODULE, WEEKS

HERE = Path(__file__).parent
DEFAULT_LANG = "fr"          # language shown on first visit: "fr", "en" or "ar"
PRICE_DZD = None             # yearly premium price shown on the home page, e.g. 2500 (None = not shown)
PREMIUM_LOCK = False         # False = everything visible (review mode) · True = exercises and quizzes need a code

st.set_page_config(page_title="PyDZ · Learn Python", page_icon=str(HERE / "assets" / "pydz-icon.png"), layout="wide",
                   initial_sidebar_state="collapsed")


# -----------------------------------------------------------------------------
# Content loading
# -----------------------------------------------------------------------------
@st.cache_resource
def load_contents():
    """Return {week number: content dict} for every weeks/wNN.py file that exists."""
    found = {}
    for w in WEEKS:
        name = f"weeks.w{w['n']:02d}"
        if (HERE / "weeks" / f"w{w['n']:02d}.py").exists():
            found[w["n"]] = importlib.import_module(name).WEEK
    return found


CONTENT = load_contents()


@st.cache_resource
def logo_uri():
    data = (HERE / "assets" / "pydz-icon.svg").read_bytes()
    return "data:image/svg+xml;base64," + base64.b64encode(data).decode()


def md_inline(text):
    """Tiny markdown to HTML converter (bold and inline code) for text inside HTML cards."""
    s = html.escape(str(text))
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    return s


def esc(text):
    return html.escape(str(text))


# -----------------------------------------------------------------------------
# State
# -----------------------------------------------------------------------------
PAGES = ["home", "weeks", "syllabus", "play", "progress", "about"]
NAV_LABEL = {"home": "nav_home", "weeks": "nav_weeks", "syllabus": "nav_syllabus", "play": "nav_play",
             "progress": "nav_progress", "about": "nav_about"}
SECTIONS = ["objectives", "lesson", "examples", "exercises", "quiz"]


def init_state():
    ss = st.session_state
    if "lang" not in ss:
        q = st.query_params.get("lang")
        ss.lang = q if q in LANGS else DEFAULT_LANG
    ss.setdefault("page", "home")
    ss.setdefault("week", 1)
    ss.setdefault("section", "objectives")
    ss.setdefault("quiz_best", {})      # week -> (score, total)
    ss.setdefault("solved", set())      # "w1-e0", ...
    if "access_until" not in ss:
        ss.access_until = None
        q = st.query_params.get("code")
        if q:
            try_unlock(q)


def go(page, week=None, section="objectives"):
    ss = st.session_state
    ss.page = page
    ss.nav = page if page in PAGES else "weeks"
    if week is not None:
        ss.week = week
        ss.section = section
        ss[f"sec_{week}"] = section


def week_done(n):
    best = st.session_state.quiz_best.get(n)
    return bool(best) and best[0] * 2 >= best[1]


def weeks_done():
    return sum(week_done(w["n"]) for w in WEEKS)


# -----------------------------------------------------------------------------
# Premium access (free: objectives, lesson, first example · premium: the rest)
# Codes live in the app's Secrets (Streamlit Cloud: App settings -> Secrets):
#   [access_codes]
#   "PYDZ-7K2M-QX" = "2027-11-30"      # code = last day of access
# -----------------------------------------------------------------------------
def _codes():
    try:
        return {str(k).strip().upper(): str(v) for k, v in st.secrets["access_codes"].items()}
    except Exception:
        return {}


def check_code(code):
    """Return ("ok", end_date) / ("expired", end_date) / ("bad", None)."""
    import datetime as _dt
    code = (code or "").strip().upper()
    end = _codes().get(code)
    if not code or end is None:
        return "bad", None
    try:
        end_d = _dt.date.fromisoformat(end)
    except ValueError:
        return "bad", None
    return ("ok" if end_d >= _dt.date.today() else "expired"), end_d


def has_access():
    return (not PREMIUM_LOCK) or bool(st.session_state.get("access_until"))


def try_unlock(code):
    status, end = check_code(code)
    if status == "ok":
        st.session_state.access_until = end.isoformat()
        st.query_params["code"] = code.strip().upper()   # stays in the link: a refresh keeps access
    return status, end


def next_week():
    for w in WEEKS:
        if w["n"] in CONTENT and not week_done(w["n"]):
            return w
    return WEEKS[0]


# -----------------------------------------------------------------------------
# Style
# -----------------------------------------------------------------------------
def inject_css(lang):
    rtl = lang == "ar"
    font = '"Cairo", "Inter", sans-serif' if rtl else '"Inter", "Cairo", sans-serif'
    head = '"Cairo", sans-serif' if rtl else '"Lexend", "Inter", sans-serif'
    css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700;800&family=Inter:wght@400;500;600;700&family=Cairo:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap');
:root { --blue:#1e5ba8; --blue-d:#0b3a75; --navy:#0b1f3a; --orange:#ff7a1a; --orange-d:#e8650a; --yellow:#ffd43b;
        --bg:#f4f8fd; --line:#e1e9f4; --muted:#5b6b82; --soft:#eaf2fc; --osoft:#fff1e6; }
html, body, p, li, label, input, textarea, button, [data-testid="stMarkdownContainer"] { font-family: __FONT__; }
h1, h2, h3, h4 { font-family: __HEAD__ !important; color: var(--navy); letter-spacing: -.01em; }
[data-testid="stAppViewContainer"] { background:
    radial-gradient(900px 420px at 85% -5%, #ffe6d1 0, rgba(255,230,209,0) 70%),
    radial-gradient(900px 500px at 0% 0%, #dfeafa 0, rgba(223,234,250,0) 70%), var(--bg); }
[data-testid="stHeader"] { background: transparent; height: 0; }
[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] { display: none; }
[data-testid="stToolbar"] { display: none; }
.block-container { padding-top: 1rem; max-width: 1240px; }
code, pre { font-family: "JetBrains Mono", Consolas, monospace !important; }
[data-testid="stMarkdownContainer"] code { unicode-bidi: isolate; direction: ltr; color: var(--blue-d); background: var(--soft);
    border-radius: 6px; padding: 1px 6px; }
[data-testid="stMarkdownContainer"] pre { direction: ltr; text-align: left; unicode-bidi: isolate; }
[data-testid="stMarkdownContainer"] pre code { color: inherit; background: transparent; padding: 0; }

/* ---------- top navigation ---------- */
.st-key-topnav { background: #fff; border-radius: 20px; padding: 10px 18px; box-shadow: 0 6px 24px rgba(11,31,58,.07);
    border: 1px solid var(--line); margin-bottom: 18px; }
.brand { display: flex; align-items: center; gap: 12px; }
.brand img { height: 46px; }
.brand .b1 { font-family: "Lexend", sans-serif; font-weight: 800; font-size: 1.55rem; color: var(--navy); line-height: 1.05; letter-spacing: -.02em; }
.brand .b1 span { color: var(--orange); }
.brand .b2 { font-size: .78rem; color: var(--muted); white-space: nowrap; }
.st-key-topnav [data-testid="stButtonGroup"] { justify-content: center; }
.st-key-topnav button[data-variant="segmented_control"] { border: 0 !important; background: transparent !important;
    color: var(--navy) !important; border-radius: 12px !important; padding: 6px 11px; box-shadow: none !important; min-height: 40px; }
.st-key-topnav button[data-variant="segmented_control"] p { font-weight: 600; font-size: .93rem; }
.st-key-topnav button[data-variant="segmented_control"][aria-checked="true"] { background: var(--osoft) !important; }
.st-key-topnav button[data-variant="segmented_control"][aria-checked="true"] p { color: var(--orange-d) !important; }
.st-key-topnav button[data-variant="segmented_control"]:hover p { color: var(--orange-d); }
.st-key-topnav [data-baseweb="select"] > div { border-radius: 12px; border-color: var(--line); font-weight: 600; }

/* ---------- buttons ---------- */
.stButton button, .stDownloadButton button { border-radius: 12px; font-weight: 600; min-height: 44px; }
[data-testid="stBaseButton-primary"] { background: var(--orange); border: 1px solid var(--orange); color: #fff;
    box-shadow: 0 6px 16px rgba(255,122,26,.28); text-transform: uppercase; letter-spacing: .03em; }
[data-testid="stBaseButton-primary"]:hover { background: var(--orange-d); border-color: var(--orange-d); color: #fff; }
[data-testid="stBaseButton-secondary"] { background: #fff; border: 1px solid #cfdbec; color: var(--navy); }
[data-testid="stBaseButton-secondary"]:hover { border-color: var(--blue); color: var(--blue); }

/* ---------- hero ---------- */
.tag { display: inline-flex; align-items: center; gap: 8px; background: var(--soft); color: var(--blue-d);
    border-radius: 10px; padding: 7px 14px; font-weight: 600; font-size: .92rem; }
.tag.o { background: var(--osoft); color: var(--orange-d); }
.hero h1 { font-size: clamp(2.1rem, 3.5vw, 3.25rem); line-height: 1.08; font-weight: 800; margin: 18px 0 14px 0; }
.hero h1 .l3 { color: var(--orange); }
.hero h1 .l2 { color: var(--blue); }
.hero p { font-size: 1.1rem; color: #33445e; line-height: 1.65; max-width: 600px; }
.stats { display: flex; gap: 30px; margin-top: 12px; flex-wrap: wrap; }
.stats b { display: block; font-family: __HEAD__; font-size: 1.8rem; color: var(--navy); }
.stats span { color: var(--muted); font-size: .9rem; }
.stats .o b { color: var(--orange); }
.showcase { position: relative; padding: 26px 8px 8px 8px; }
.shcard { background: #fff; border-radius: 28px; padding: 22px; transform: rotate(-2deg);
    box-shadow: 0 24px 60px rgba(11,31,58,.14); border: 1px solid var(--line); }
.shcard .top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; }
.spark { color: var(--blue); font-size: 1.6rem; }
.star { position: absolute; top: -6px; right: 14px; font-size: 2.6rem; color: var(--yellow);
    text-shadow: 0 0 1px #e0a800; transform: rotate(12deg); }
[dir=rtl] .star, .rtl .star { right: auto; left: 14px; }
.win { background: #0f1b2d; border-radius: 18px; overflow: hidden; direction: ltr; text-align: left; }
.win .bar { display: flex; gap: 7px; padding: 12px 14px; background: #16253b; }
.win .bar i { width: 11px; height: 11px; border-radius: 50%; display: inline-block; }
.win .code { padding: 16px 18px 20px 18px; color: #dbe7f7; font-size: .95rem; line-height: 1.8; font-family: "JetBrains Mono", monospace; white-space: pre; overflow-x: auto; }
.win .k { color: #ff9d57; } .win .s { color: #ffd43b; } .win .c { color: #6f87a8; } .win .p { color: #7cb3ff; } .win .o { color: #9ef0b5; }
.shcard .meta { margin-top: 16px; }
.shcard .wk { font-size: .82rem; font-weight: 700; color: var(--orange-d); letter-spacing: .05em; text-transform: uppercase; }
.shcard .tt { font-family: __HEAD__; font-weight: 700; font-size: 1.25rem; color: var(--navy); margin: 4px 0 12px 0; }
.pbar { height: 9px; background: var(--soft); border-radius: 99px; overflow: hidden; }
.pbar > div { height: 100%; background: linear-gradient(90deg, var(--blue), var(--orange)); border-radius: 99px; }
.plabel { font-size: .85rem; color: var(--muted); margin-top: 7px; }

/* ---------- section titles ---------- */
.sect { margin: 46px 0 16px 0; }
.sect h2 { font-size: 2.1rem; font-weight: 800; margin: 12px 0 0 0; }
.squig { display: block; margin-top: 6px; }

/* ---------- week cards ---------- */
div[class*="st-key-wk_"] { background: #fff; border: 1px solid var(--line); border-radius: 22px; padding: 10px 10px 12px 10px;
    box-shadow: 0 4px 16px rgba(11,31,58,.05); transition: transform .15s, box-shadow .15s; gap: .5rem; }
div[class*="st-key-wk_"]:hover { transform: translateY(-3px); box-shadow: 0 14px 30px rgba(11,31,58,.10); }
.wtop { border-radius: 16px; height: 104px; position: relative; overflow: hidden; display: flex; align-items: center;
    justify-content: center; direction: ltr; }
.wtop.blue { background: linear-gradient(135deg, #1e5ba8 0%, #0b3a75 100%); }
.wtop.orange { background: linear-gradient(135deg, #ff9a3c 0%, #ff6a00 100%); }
.wtop .tok { font-family: "JetBrains Mono", monospace; font-weight: 700; font-size: 1.25rem; color: #fff;
    background: rgba(255,255,255,.14); border: 1px solid rgba(255,255,255,.28); border-radius: 12px; padding: 6px 12px; }
.wtop .num { position: absolute; bottom: -18px; right: 6px; font-family: "Lexend", sans-serif; font-weight: 800; font-size: 4.6rem;
    color: rgba(255,255,255,.16); line-height: 1; }
.wtop .st { position: absolute; top: 9px; left: 9px; font-size: .7rem; font-weight: 700; border-radius: 99px; padding: 2px 9px;
    background: rgba(255,255,255,.92); color: var(--navy); font-family: "Inter", "Cairo", sans-serif; }
.wtop .st.ok { background: #19a463; color: #fff; }
.wtop .st.soon { background: rgba(255,255,255,.25); color: #fff; }
.wbody { padding: 10px 4px 22px 4px; min-height: 128px; }
.wlbl { font-size: .76rem; font-weight: 700; color: var(--orange-d); letter-spacing: .05em; text-transform: uppercase; }
.wttl { font-family: __HEAD__; font-weight: 600; font-size: 1rem; color: var(--navy); line-height: 1.35; margin-top: 3px; }

/* ---------- how it works ---------- */
.steps { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 14px; }
.step { background: #fff; border: 1px solid var(--line); border-radius: 20px; padding: 18px; }
.step .n { width: 38px; height: 38px; border-radius: 12px; display: flex; align-items: center; justify-content: center;
    font-weight: 800; color: #fff; background: var(--blue); font-family: "Lexend", sans-serif; margin-bottom: 10px; }
.step:nth-child(even) .n { background: var(--orange); }
.step b { display: block; color: var(--navy); font-size: 1.02rem; margin-bottom: 4px; }
.step span { color: var(--muted); font-size: .92rem; }

/* ---------- week page ---------- */
.banner { border-radius: 26px; padding: 28px 30px; color: #fff; position: relative; overflow: hidden; margin-bottom: 16px; }
.banner.blue { background: linear-gradient(120deg, #0b3a75 0%, #1e5ba8 60%, #2f74c9 100%); }
.banner.orange { background: linear-gradient(120deg, #e8650a 0%, #ff7a1a 55%, #ff9a3c 100%); }
.banner .big { position: absolute; right: 24px; bottom: -36px; font-family: "Lexend", sans-serif; font-weight: 800; font-size: 9rem;
    color: rgba(255,255,255,.12); line-height: 1; }
.rtl .banner .big { right: auto; left: 24px; }
.banner .wl { font-weight: 700; letter-spacing: .06em; text-transform: uppercase; font-size: .85rem; opacity: .9; }
.banner h1 { color: #fff !important; font-size: 2.1rem; margin: 6px 0 14px 0; max-width: 820px; }
.banner .chips { display: flex; flex-wrap: wrap; gap: 8px; max-width: 900px; }
.banner .chip { background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.3); border-radius: 99px; padding: 5px 13px; font-size: .88rem; }
.banner .pb { font-size: .78rem; opacity: .85; margin-bottom: 8px; font-weight: 600; }
.st-key-secnav button[data-variant="segmented_control"] { padding: 8px 16px; min-height: 44px; background: #fff; }
.st-key-secnav button[data-variant="segmented_control"] p { font-weight: 600; }
.st-key-secnav button[data-variant="segmented_control"][aria-checked="true"] { background: var(--navy) !important; border-color: var(--navy) !important; }
.st-key-secnav button[data-variant="segmented_control"][aria-checked="true"] p { color: #fff !important; }
.card { background: #fff; border: 1px solid var(--line); border-radius: 22px; padding: 22px 26px; }
div[class*="st-key-panel"] { background: #fff; border: 1px solid var(--line); border-radius: 22px; padding: 22px 26px; }
.goals { list-style: none; padding: 0 !important; margin: 10px 0 0 0; }
.goals li { display: flex; gap: 12px; align-items: flex-start; padding: 12px 0; border-bottom: 1px dashed var(--line); line-height: 1.6; }
.goals li:last-child { border-bottom: 0; }
.goals .ck { flex: 0 0 30px; height: 30px; border-radius: 10px; background: var(--osoft); color: var(--orange-d);
    display: flex; align-items: center; justify-content: center; font-weight: 800; }
.goals code, .task code, .wttl code { background: var(--soft); color: var(--blue-d); border-radius: 6px; padding: 1px 6px; font-size: .88em;
    unicode-bidi: isolate; direction: ltr; }
div[class*="st-key-task_"] { background: var(--osoft); border: 1px solid #ffd9bd; border-radius: 16px; padding: 14px 18px; }
.task { background: var(--osoft); border: 1px solid #ffd9bd; border-radius: 16px; padding: 14px 18px; margin: 6px 0 14px 0; }
.soon-box { background: #fff; border: 2px dashed #cfdbec; border-radius: 22px; padding: 26px; }
.soon-box li { margin-bottom: 8px; }

/* ---------- premium ---------- */
.lockbox { display: flex; gap: 18px; align-items: flex-start; background: linear-gradient(135deg, #fff 0%, #fff6ee 100%);
    border: 1px solid #ffd9bd; border-radius: 22px; padding: 22px 26px; margin-bottom: 8px; }
.lockbox .lk { flex: 0 0 54px; height: 54px; border-radius: 16px; background: var(--orange); color: #fff; font-size: 1.6rem;
    display: flex; align-items: center; justify-content: center; box-shadow: 0 8px 18px rgba(255,122,26,.3); }
.lockbox h3 { margin: 10px 0 4px 0; }
.lockbox p { margin: 4px 0; color: #33445e; }
.lockbox ul { margin: 6px 0 0 0; }
.offer { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
@media (max-width: 800px) { .offer { grid-template-columns: 1fr; } }
.plan { background: #fff; border: 1px solid var(--line); border-radius: 24px; padding: 24px 26px; }
.plan.pro { background: linear-gradient(140deg, #0b3a75 0%, #1e5ba8 100%); color: #fff; border: 0; box-shadow: 0 18px 40px rgba(11,58,117,.25); }
.plan h3 { margin: 0 0 4px 0; font-size: 1.5rem; }
.plan.pro h3 { color: #fff !important; }
.plan .per { color: var(--muted); font-weight: 600; }
.plan.pro .per { color: #ffd2b0; }
.plan ul { list-style: none; padding: 0; margin: 14px 0 0 0; }
.plan li { padding: 7px 0; display: flex; gap: 10px; }
.plan li::before { content: "✓"; font-weight: 800; color: var(--blue); }
.plan.pro li::before { color: var(--orange); }
.build ul { list-style: none; padding: 0; }
.build li { padding: 8px 0; border-bottom: 1px dashed var(--line); }
.build li b { color: var(--orange-d); }

/* ---------- misc ---------- */
.kv { display: grid; grid-template-columns: minmax(150px, 34%) 1fr; gap: 0; }
.kv div { padding: 10px 4px; border-bottom: 1px solid var(--line); }
.kv div:nth-child(odd) { color: var(--muted); font-weight: 600; }
.axis { display: flex; gap: 12px; align-items: center; padding: 9px 0; border-bottom: 1px dashed var(--line); }
.axis b { flex: 0 0 34px; height: 34px; border-radius: 10px; background: var(--soft); color: var(--blue-d); display: flex;
    align-items: center; justify-content: center; }
table.wt { width: 100%; border-collapse: collapse; }
table.wt td { padding: 10px 8px; border-bottom: 1px solid var(--line); vertical-align: top; }
table.wt td:first-child { white-space: nowrap; font-weight: 700; color: var(--orange-d); width: 1%; }
table.wt .pt { color: var(--muted); font-size: .9rem; }
.eval { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
.ebox { border-radius: 18px; padding: 18px; color: #fff; }
.ebox.b { background: var(--blue); } .ebox.o { background: var(--orange); }
.ebox b { font-family: "Lexend", sans-serif; font-size: 2.2rem; display: block; }
[data-testid="stMetric"] { background: #fff; border: 1px solid var(--line); border-radius: 18px; padding: 14px 18px; }
.footer { text-align: center; color: #7b889c; font-size: .82rem; margin-top: 46px; padding: 18px 0 6px 0; border-top: 1px solid var(--line); }
.footer a { color: var(--blue); text-decoration: none; }
div[data-testid="stForm"] { background: #fff; border-radius: 22px; border: 1px solid var(--line); padding: 10px 18px; }
[data-testid="stExpander"] details { border-radius: 14px; background: #fff; }
button[data-variant="pills"] { background: #fff; }
button[data-variant="pills"][aria-checked="true"] { background: var(--soft) !important; border-color: var(--blue) !important; }
button[data-variant="pills"][aria-checked="true"] p { color: var(--blue-d) !important; font-weight: 600; }
</style>
""".replace("__FONT__", font).replace("__HEAD__", head)
    if rtl:
        css += """
<style>
[data-testid="stMain"] .block-container { direction: rtl; }
[data-testid="stMarkdownContainer"], [data-testid="stWidgetLabel"], .stRadio label, .stCheckbox label { text-align: right; }
[data-testid="stMarkdownContainer"] ul, [data-testid="stMarkdownContainer"] ol { padding-right: 1.4em; padding-left: 0; }
[data-testid="stMarkdownContainer"] th, [data-testid="stMarkdownContainer"] td { text-align: right; }
.wtop .st { left: auto; right: 9px; }
.wtop .num { right: auto; left: 6px; }
[data-testid="stMarkdownContainer"] li { text-align: right; }
/* each code line takes its own direction: Arabic pseudo-code reads right-to-left, Python stays left-to-right */
[data-testid="stCode"] code { display: block; unicode-bidi: plaintext; text-align: start; }
</style>
"""
    st.markdown(css, unsafe_allow_html=True)


SQUIG = ('<svg class="squig" width="150" height="14" viewBox="0 0 150 14"><path d="M2 9 C 22 1, 38 1, 56 7 S 92 13, 110 6 '
         'S 140 3, 148 8" stroke="#ff7a1a" stroke-width="4" fill="none" stroke-linecap="round"/></svg>')


def section_title(tag, title, orange=False):
    st.markdown(f'<div class="sect"><span class="tag {"o" if orange else ""}">✦ {esc(tag)}</span>'
                f'<h2>{esc(title)}</h2>{SQUIG}</div>', unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# Top navigation and footer
# -----------------------------------------------------------------------------
def top_nav(lang):
    ss = st.session_state
    if ss.get("nav") not in PAGES:
        ss.nav = ss.page if ss.page in PAGES else "weeks"
    with st.container(key="topnav"):
        c1, c2, c3 = st.columns([2.1, 7, 1.45], vertical_alignment="center")
        with c1:
            st.markdown(f'<div class="brand"><img src="{logo_uri()}" alt="PyDZ"><div>'
                        f'<div class="b1">Py<span>DZ</span></div>'
                        f'<div class="b2">{esc(UI["brand_sub"][lang])}</div></div></div>', unsafe_allow_html=True)
        with c2:
            st.segmented_control("nav", PAGES, key="nav", label_visibility="collapsed",
                                 format_func=lambda p: UI[NAV_LABEL[p]][lang], on_change=_nav_changed)
        with c3:
            st.selectbox("lang", list(LANGS), key="lang", label_visibility="collapsed",
                         format_func=lambda k: f"🌐 {LANGS[k]}", on_change=_lang_changed)


def _nav_changed():
    ss = st.session_state
    if ss.nav is None:                  # clicking the active item again would deselect it
        ss.nav = ss.page if ss.page in PAGES else "weeks"
    ss.page = ss.nav


def _lang_changed():
    st.query_params["lang"] = st.session_state.lang


def footer(lang):
    st.markdown(
        f'<div class="footer">© 2026 <b>PyDZ</b> · {esc(UI["footer"][lang])}<br>'
        f'{esc(UI["created_by"][lang])} {esc(T(AUTHOR["name"], lang))} · '
        f'<a href="mailto:{AUTHOR["email"]}">{AUTHOR["email"]}</a></div>', unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# Week cards
# -----------------------------------------------------------------------------
def week_card(w, lang, key_prefix="wk_"):
    n = w["n"]
    if week_done(n):
        status, cls = UI["done"][lang], "ok"
    elif n in CONTENT:
        status, cls = UI["available"][lang], ""
    else:
        status, cls = UI["soon"][lang], "soon"
    with st.container(key=f"{key_prefix}{n}"):
        st.markdown(
            f'<div class="wtop {w["tone"]}"><span class="st {cls}">{esc(status)}</span>'
            f'<span class="tok">{esc(w["token"])}</span><span class="num">{n:02d}</span></div>'
            f'<div class="wbody"><div class="wlbl">{esc(UI["week_n"][lang].format(n=n))}</div>'
            f'<div class="wttl">{esc(T(w["title"], lang))}</div></div>', unsafe_allow_html=True)
        st.button(UI["open"][lang] + (" ←" if lang == "ar" else " →"), key=f"btn_{key_prefix}{n}",
                  on_click=go, args=("week", n), use_container_width=True)


def week_grid(lang, key_prefix="wk_"):
    per_row = 5
    for start in range(0, len(WEEKS), per_row):
        cols = st.columns(per_row, gap="small")
        for col, w in zip(cols, WEEKS[start:start + per_row]):
            with col:
                week_card(w, lang, key_prefix)


# -----------------------------------------------------------------------------
# PAGE: home
# -----------------------------------------------------------------------------
DEMO_CODE = '''# PyDZ · final project preview: sales report of a small shop
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [182000, 165500, 210300, 198750, 240100, 226400]   # DZD

def average(values):
    return sum(values) / len(values)

total = sum(sales)
best = months[sales.index(max(sales))]
worst = months[sales.index(min(sales))]

print("=" * 34)
print("   SALES REPORT · FIRST HALF")
print("=" * 34)
for month, amount in zip(months, sales):
    bar = "#" * (amount // 20000)
    print(f"{month}  {amount:>8,} DZD  {bar}")
print("-" * 34)
print(f"Total     : {total:,} DZD")
print(f"Average   : {average(sales):,.0f} DZD")
print(f"Best month: {best}   Worst month: {worst}")
growth = (sales[-1] - sales[0]) / sales[0] * 100
print(f"Growth Jan -> Jun: {growth:.1f} %")
'''


def page_home(lang):
    nw = next_week()
    done = weeks_done()
    left, right = st.columns([1.15, 1], gap="large", vertical_alignment="center")
    with left:
        st.markdown(
            f'<div class="hero"><span class="tag">✦ {esc(UI["hero_tag"][lang])}</span>'
            f'<h1>{esc(UI["hero_l1"][lang])}<br><span class="l2">{esc(UI["hero_l2"][lang])}</span><br>'
            f'<span class="l3">{esc(UI["hero_l3"][lang])}</span></h1><p>{esc(UI["hero_sub"][lang])}</p></div>',
            unsafe_allow_html=True)
        b1, b2, _ = st.columns([1.25, 1.1, .4])
        label = UI["cta_start"][lang] if done == 0 else UI["cta_continue"][lang].format(n=nw["n"])
        b1.button(label, type="primary", on_click=go, args=("week", nw["n"]), use_container_width=True)
        b2.button(UI["cta_syllabus"][lang], on_click=go, args=("syllabus",), use_container_width=True)
        st.markdown(
            f'<div class="stats"><div><b>15</b><span>{esc(UI["stat_weeks"][lang])}</span></div>'
            f'<div class="o"><b>3</b><span>{esc(UI["stat_langs"][lang])}</span></div>'
            f'<div><b>0</b><span>{esc(UI["stat_install"][lang])}</span></div></div>', unsafe_allow_html=True)
    with right:
        pct = round(done / len(WEEKS) * 100)
        hero_code = "<br>".join([
            f'<span class="c"># PyDZ · week {nw["n"]:02d}</span>',
            '<span class="p">gdp</span> = [<span class="o">18.2</span>, <span class="o">19.1</span>, <span class="o">20.4</span>]',
            '<span class="p">growth</span> = (gdp[-<span class="o">1</span>] - gdp[<span class="o">0</span>]) / gdp[<span class="o">0</span>]',
            '<span class="k">print</span>(<span class="s">f"Growth: {growth:.1%}"</span>)',
            '<span class="c">&gt;&gt;&gt; Growth: 12.1%</span>'])
        st.markdown(
            f'''<div class="showcase {"rtl" if lang == "ar" else ""}"><span class="star">☆</span><div class="shcard">
<div class="top"><span class="tag">{esc(UI["next_tag"][lang])}</span><span class="spark">✦</span></div>
<div class="win"><div class="bar"><i style="background:#ff5f57"></i><i style="background:#febc2e"></i><i style="background:#28c840"></i></div>
<div class="code">{hero_code}</div></div>
<div class="meta"><div class="wk">{esc(UI["week_n"][lang].format(n=nw["n"]))}</div>
<div class="tt">{esc(T(nw["title"], lang))}</div>
<div class="pbar"><div style="width:{max(pct, 3)}%"></div></div>
<div class="plabel">{esc(UI["progress_label"][lang].format(d=done))}</div></div></div></div>''',
            unsafe_allow_html=True)

    section_title(UI["journey_tag"][lang], UI["journey_title"][lang])
    week_grid(lang)

    section_title(UI["build_tag"][lang], UI["build_title"][lang], orange=True)
    d1, d2 = st.columns([1, 1.5], gap="large")
    with d1:
        pts = "".join(f"<li><b>→</b> {esc(p)}</li>" for p in UI["build_points"][lang])
        st.markdown(f'<div class="build"><p style="font-size:1.05rem;line-height:1.65">{md_inline(UI["build_text"][lang])}</p>'
                    f'<ul>{pts}</ul></div>', unsafe_allow_html=True)
    with d2:
        code_runner(DEMO_CODE, runner_texts(lang), lang == "ar", uid="home-demo", max_lines=30)

    section_title(UI["offer_tag"][lang], UI["offer_title"][lang])
    free = "".join(f"<li>{esc(x)}</li>" for x in UI["free_list"][lang])
    pro = "".join(f"<li>{esc(x)}</li>" for x in UI["premium_list"][lang])
    st.markdown(f'<div class="offer"><div class="plan"><h3>{esc(UI["free_name"][lang])}</h3><span class="per">0 DZD</span><ul>{free}</ul></div>'
                f'<div class="plan pro"><h3>{esc(UI["premium"][lang])} ✦</h3><span class="per">{(f"{PRICE_DZD:,}".replace(",", " ") + " DZD · ") if PRICE_DZD else ""}{esc(UI["per_year"][lang])}</span>'
                f'<ul>{pro}</ul></div></div>', unsafe_allow_html=True)

    section_title(UI["how_tag"][lang], UI["how_title"][lang], orange=True)
    steps = "".join(f'<div class="step"><div class="n">{i}</div><b>{esc(a)}</b><span>{esc(b)}</span></div>'
                    for i, (a, b) in enumerate(UI["how_steps"][lang], 1))
    st.markdown(f'<div class="steps">{steps}</div>', unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# PAGE: all weeks
# -----------------------------------------------------------------------------
def page_weeks(lang):
    section_title(UI["journey_tag"][lang], UI["journey_title"][lang])
    week_grid(lang, key_prefix="wkall_")


# -----------------------------------------------------------------------------
# PAGE: one week
# -----------------------------------------------------------------------------
def render_objectives(c, lang):
    items = "".join(f'<li><span class="ck">✓</span><span>{md_inline(x)}</span></li>' for x in T(c["objectives"], lang))
    st.markdown(f'<div class="card"><h3 style="margin:0">{esc(UI["after_week"][lang])}</h3>'
                f'<ul class="goals">{items}</ul></div>', unsafe_allow_html=True)


def render_lesson(c, lang):
    with st.container(key="panel_lesson"):
        st.markdown(T(c["lesson"], lang))


def render_locked(lang, items_html=""):
    """Card shown instead of premium content, with the access-code form."""
    st.markdown(
        f'<div class="lockbox"><div class="lk">🔒</div><div><span class="tag o">{esc(UI["premium"][lang])}</span>'
        f'<h3>{esc(UI["lock_title"][lang])}</h3><p>{esc(UI["lock_text"][lang])}</p>{items_html}</div></div>',
        unsafe_allow_html=True)
    with st.form(f"unlock_{st.session_state.page}_{st.session_state.week}_{len(items_html)}", border=False):
        c1, c2 = st.columns([3, 1.3], vertical_alignment="bottom")
        code = c1.text_input(UI["code_label"][lang], placeholder="PYDZ-XXXX-XX")
        sent = c2.form_submit_button(UI["code_btn"][lang], type="primary", use_container_width=True)
    if sent:
        status, end = try_unlock(code)
        if status == "ok":
            st.rerun()
        elif status == "expired":
            st.error(UI["code_expired"][lang].format(d=end.isoformat()))
        else:
            st.error(UI["code_bad"][lang])
    st.caption(f'{UI["how_to_buy"][lang]} {AUTHOR["email"]}')


def render_examples(c, n, lang):
    exs = c["examples"]
    locked = not has_access()
    labels = [("🔒 " if locked and i > 0 else "") + f'{UI["example"][lang]} {i + 1} · {T(e["title"], lang)}'
              for i, e in enumerate(exs)]
    i = st.pills(UI["example"][lang], list(range(len(exs))), format_func=lambda k: labels[k], default=0,
                 key=f"ex_pick_{n}", label_visibility="collapsed")
    i = 0 if i is None else i
    if locked and i > 0:
        render_locked(lang, f'<p><b>{esc(UI["lock_has_more_ex"][lang].format(n=len(exs) - 1))}</b></p>')
        return
    e = exs[i]
    st.markdown(f"#### {T(e['title'], lang)}")
    st.markdown(T(e["explain"], lang))
    code_runner(e["code"], runner_texts(lang), lang == "ar", uid=f"w{n}-x{i}", stdin=e.get("stdin", ""))


def render_exercises(c, n, lang):
    exs = c["exercises"]
    ss = st.session_state
    if not has_access():
        items = "".join(f"<li>{esc(T(e['title'], lang))}</li>" for e in exs)
        render_locked(lang, f'<p><b>{esc(UI["lock_has_ex"][lang].format(n=len(exs)))}</b></p><ul>{items}</ul>')
        return
    labels = [("✅ " if f"w{n}-e{i}" in ss.solved else "") + f'{UI["exercise"][lang]} {i + 1} · {T(e["title"], lang)}'
              for i, e in enumerate(exs)]
    i = st.pills(UI["exercise"][lang], list(range(len(exs))), format_func=lambda k: labels[k], default=0,
                 key=f"exo_pick_{n}", label_visibility="collapsed")
    i = 0 if i is None else i
    e = exs[i]
    with st.container(key=f"task_{n}_{i}"):
        st.markdown(f"**{UI['task'][lang]}**\n\n{T(e['task'], lang)}")
    code_runner(e["starter"], runner_texts(lang), lang == "ar", uid=f"w{n}-e{i}", stdin=e.get("stdin", ""),
                expected=e["expected"])
    c1, c2 = st.columns(2)
    with c1:
        with st.expander("💡 " + UI["hint"][lang]):
            st.markdown(T(e["hint"], lang))
    with c2:
        with st.expander("🔑 " + UI["solution"][lang]):
            st.caption(UI["solution_note"][lang])
            st.code(e["solution"], language="python")
    key = f"w{n}-e{i}"
    val = st.checkbox(UI["mark_solved"][lang], value=key in ss.solved, key=f"chk_{key}")
    if val:
        ss.solved.add(key)
    else:
        ss.solved.discard(key)


def render_quiz(c, n, lang):
    qs = c["quiz"]
    if not has_access():
        render_locked(lang, f'<p><b>{esc(UI["lock_has_quiz"][lang].format(n=len(qs)))}</b></p>')
        return
    st.caption(UI["quiz_intro"][lang] + " " + UI["pass_note"][lang])
    with st.form(f"quiz_{n}"):
        answers = []
        for i, q in enumerate(qs):
            opts = T(q["options"], lang)
            a = st.radio(f"**{i + 1}. {T(q['q'], lang)}**", list(range(len(opts))), index=None,
                         format_func=lambda k, o=opts: o[k], key=f"q_{n}_{i}")
            answers.append(a)
        sent = st.form_submit_button(UI["submit"][lang], type="primary")
    if sent:
        if any(a is None for a in answers):
            st.warning(UI["unanswered"][lang])
            return
        score = sum(a == q["answer"] for a, q in zip(answers, qs))
        best = st.session_state.quiz_best.get(n, (0, len(qs)))
        st.session_state.quiz_best[n] = (max(score, best[0]), len(qs))
        (st.success if score * 2 >= len(qs) else st.info)(
            UI["score"][lang].format(s=score, n=len(qs)) + " · " + (UI["great"][lang] if score == len(qs) else UI["keep"][lang]
                                                                   if score * 2 < len(qs) else ""))
        for i, (a, q) in enumerate(zip(answers, qs)):
            opts = T(q["options"], lang)
            if a == q["answer"]:
                st.markdown(f"✅ **{i + 1}.** {UI['correct'][lang]}. {T(q['explain'], lang)}")
            else:
                st.markdown(f"❌ **{i + 1}.** {UI['wrong'][lang]} **{opts[q['answer']]}**. {T(q['explain'], lang)}")


def page_week(lang):
    ss = st.session_state
    n = ss.week
    w = WEEKS[n - 1]
    c = CONTENT.get(n)
    chips = "".join(f'<span class="chip">{esc(p)}</span>' for p in T(w["points"], lang))
    st.markdown(
        f'<div class="{"rtl" if lang == "ar" else ""}"><div class="banner {w["tone"]}"><span class="big">{n:02d}</span>'
        f'<div class="wl">{esc(UI["week_n"][lang].format(n=n))} · {esc(UI["done"][lang] if week_done(n) else (UI["available"][lang] if c else UI["soon"][lang]))}</div>'
        f'<h1>{esc(T(w["title"], lang))}</h1>'
        + (f'<div class="pb">{esc(UI["programme_box"][lang])}</div><div class="chips">{chips}</div>' if chips else "")
        + '</div></div>', unsafe_allow_html=True)

    if c is None:
        pts = "".join(f"<li>{esc(p)}</li>" for p in T(w["points"], lang)) or f"<li>{esc(T(w['title'], lang))}</li>"
        st.markdown(f'<div class="soon-box"><h3 style="margin-top:0">⏳ {esc(UI["soon"][lang])}</h3>'
                    f'<p>{esc(UI["soon_text"][lang])}</p><ul>{pts}</ul></div>', unsafe_allow_html=True)
    else:
        key = f"sec_{n}"
        if ss.get(key) not in SECTIONS:
            ss[key] = "objectives"
        with st.container(key="secnav"):
            icons = {"objectives": "🎯", "lesson": "📖", "examples": "💻", "exercises": "✏️", "quiz": "📝"}
            sec = st.segmented_control("sec", SECTIONS, key=key, label_visibility="collapsed",
                                       format_func=lambda s: f"{icons[s]} {UI['sec_' + s][lang]}"
                                       + (" 🔒" if s in ("exercises", "quiz") and not has_access() else ""))
        if ss.get("access_until"):
            st.caption("✅ " + UI["code_ok"][lang].format(d=ss.access_until))
        sec = sec or "objectives"
        if sec == "objectives":
            render_objectives(c, lang)
        elif sec == "lesson":
            render_lesson(c, lang)
        elif sec == "examples":
            render_examples(c, n, lang)
        elif sec == "exercises":
            render_exercises(c, n, lang)
        else:
            render_quiz(c, n, lang)

    st.write("")
    a, b, d = st.columns(3)
    prev_lbl = ("→ " if lang == "ar" else "← ") + UI["prev"][lang]
    next_lbl = UI["next"][lang] + (" ←" if lang == "ar" else " →")
    if n > 1:
        a.button(prev_lbl, on_click=go, args=("week", n - 1), use_container_width=True)
    b.button("▦ " + UI["back"][lang], on_click=go, args=("weeks",), use_container_width=True)
    if n < len(WEEKS):
        d.button(next_lbl, on_click=go, args=("week", n + 1), use_container_width=True, type="primary")


# -----------------------------------------------------------------------------
# PAGE: syllabus
# -----------------------------------------------------------------------------
def page_syllabus(lang):
    section_title(UI["syl_sub"][lang], UI["syl_title"][lang])
    c1, c2 = st.columns([1.1, 1], gap="large")
    with c1:
        rows = [("f_field", T(MODULE["field"], lang)), ("f_branch", T(MODULE["branch"], lang)),
                ("f_level", T(MODULE["level"], lang)), ("f_semester", T(MODULE["semester"], lang)),
                ("f_unit", T(MODULE["unit"], lang)), ("f_credits", f'{MODULE["credits"]} / {MODULE["coef"]}'),
                ("f_volume", T(MODULE["volume"], lang))]
        kv = "".join(f"<div>{esc(UI[k][lang])}</div><div>{esc(v)}</div>" for k, v in rows)
        st.markdown(f'<div class="card"><h3 style="margin-top:0">{esc(UI["syl_id"][lang])}</h3><div class="kv">{kv}</div></div>',
                    unsafe_allow_html=True)
        st.write("")
        pre = "".join(f"<li>{esc(p)}</li>" for p in T(MODULE["prereq"], lang))
        outc = "".join(f'<li><span class="ck">✓</span><span>{esc(p)}</span></li>' for p in T(MODULE["outcomes"], lang))
        st.markdown(f'<div class="card"><h3 style="margin-top:0">{esc(UI["syl_prereq"][lang])}</h3><ul>{pre}</ul>'
                    f'<h3>{esc(UI["syl_goal"][lang])}</h3><p style="line-height:1.7">{esc(T(MODULE["goal"], lang))}</p>'
                    f'<h3>{esc(UI["syl_outcomes"][lang])}</h3><ul class="goals">{outc}</ul></div>', unsafe_allow_html=True)
    with c2:
        axes = "".join(f'<div class="axis"><b>{i}</b><span>{esc(a)}</span></div>' for i, a in enumerate(T(MODULE["axes"], lang), 1))
        st.markdown(f'<div class="card"><h3 style="margin-top:0">{esc(UI["syl_axes"][lang])}</h3>{axes}</div>', unsafe_allow_html=True)
        st.write("")
        ev = MODULE["assessment"]
        ca = "".join(f"<div>{esc(T(k, lang))}</div><div><b>{v}</b></div>" for k, v in MODULE["ca_detail"])
        st.markdown(
            f'<div class="card"><h3 style="margin-top:0">{esc(UI["syl_eval"][lang])}</h3><div class="eval">'
            f'<div class="ebox b"><b>{ev[0][1]}</b>{esc(T(ev[0][0], lang))}</div>'
            f'<div class="ebox o"><b>{ev[1][1]}</b>{esc(T(ev[1][0], lang))}</div></div>'
            f'<h4>{esc(UI["syl_ca"][lang])}</h4><div class="kv">{ca}</div>'
            f'<p style="color:var(--muted);font-size:.9rem;margin-top:12px">{esc(UI["syl_exam_note"][lang])}</p></div>',
            unsafe_allow_html=True)
    st.write("")
    rows = "".join(f'<tr><td>{esc(UI["week_n"][lang].format(n=w["n"]))}</td><td><b>{esc(T(w["title"], lang))}</b>'
                   f'<div class="pt">{esc(" · ".join(T(w["points"], lang)))}</div></td></tr>' for w in WEEKS)
    st.markdown(f'<div class="card"><h3 style="margin-top:0">{esc(UI["syl_weekly"][lang])}</h3><table class="wt">{rows}</table></div>',
                unsafe_allow_html=True)
    st.write("")
    pw = "".join(f"<li>{esc(p)}</li>" for p in T(MODULE["personal_work"], lang))
    st.markdown(f'<div class="card"><h3 style="margin-top:0">{esc(UI["syl_personal"][lang])}</h3><ul>{pw}</ul></div>',
                unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# PAGE: playground
# -----------------------------------------------------------------------------
TEMPLATES = {
    "tpl_blank": "# Write your Python code here\n\n",
    "tpl_hello": 'print("Hello, Python!")\nprint("Bonjour, Python !")\nprint("مرحباً، Python!")\n',
    "tpl_vat": 'price_ht = 2500        # price before tax (DZD)\nvat_rate = 0.19        # 19 %\n\n'
               'price_ttc = price_ht * (1 + vat_rate)\nprint("Price incl. VAT:", price_ttc, "DZD")\n',
    "tpl_input": 'name = input("Your name: ")\nyear = int(input("Year of birth: "))\nprint(f"Hello {name}, you are about {2026 - year} years old.")\n',
}


def page_play(lang):
    section_title(UI["play_text"][lang], UI["play_title"][lang], orange=True)
    k = st.pills(UI["template"][lang], list(TEMPLATES), default="tpl_hello", format_func=lambda t: UI[t][lang],
                 key="tpl_pick")
    k = k or "tpl_blank"
    stdin = "Amina\n2006\n" if k == "tpl_input" else ""
    code_runner(TEMPLATES[k], runner_texts(lang), lang == "ar", uid=f"play-{k}", stdin=stdin, max_lines=30)


# -----------------------------------------------------------------------------
# PAGE: progress
# -----------------------------------------------------------------------------
def page_progress(lang):
    ss = st.session_state
    section_title(UI["progress_note"][lang], UI["progress_title"][lang])
    total_ex = sum(len(c["exercises"]) for c in CONTENT.values())
    qb = ss.quiz_best
    avg = (sum(s / t for s, t in qb.values()) / len(qb) * 100) if qb else 0
    m1, m2, m3 = st.columns(3)
    m1.metric(UI["weeks_done"][lang], f"{weeks_done()} / {len(WEEKS)}")
    m2.metric(UI["ex_solved"][lang], f"{len(ss.solved)} / {total_ex}")
    m3.metric(UI["avg_score"][lang], f"{avg:.0f} %")
    rows = []
    for w in WEEKS:
        n = w["n"]
        c = CONTENT.get(n)
        q = qb.get(n)
        solved = sum(1 for s in ss.solved if s.startswith(f"w{n}-"))
        rows.append({UI["col_week"][lang]: f"{n:02d} · {T(w['title'], lang)}",
                     UI["col_quiz"][lang]: f"{q[0]} / {q[1]}" if q else "—",
                     UI["col_ex"][lang]: f"{solved} / {len(c['exercises'])}" if c else "—"})
    st.dataframe(rows, use_container_width=True, hide_index=True)
    csv = "﻿" + ",".join(rows[0].keys()) + "\n" + "\n".join(
        ",".join('"' + str(v).replace('"', '""') + '"' for v in r.values()) for r in rows)
    c1, c2 = st.columns(2)
    c1.download_button(UI["download"][lang], csv.encode("utf-8"), "python1_progress.csv", "text/csv", use_container_width=True)
    if c2.button(UI["reset_progress"][lang], use_container_width=True):
        ss.quiz_best = {}
        ss.solved = set()
        st.rerun()


# -----------------------------------------------------------------------------
# PAGE: about
# -----------------------------------------------------------------------------
def page_about(lang):
    section_title("PyDZ", UI["about_title"][lang])
    c1, c2 = st.columns([1.4, 1], gap="large")
    with c1:
        with st.container(key="panel_about"):
            st.markdown(UI["about_text"][lang])
            st.markdown(f"#### {UI['tech_title'][lang]}")
            st.markdown(UI["tech_text"][lang])
    with c2:
        st.markdown(
            f'<div class="card" style="text-align:center"><img src="{logo_uri()}" style="height:96px">'
            f'<div class="brand" style="justify-content:center;margin-top:10px"><div class="b1" style="font-size:2.2rem">Py<span>DZ</span></div></div>'
            f'<div class="stats" style="justify-content:center;margin-top:18px"><div><b>15</b><span>{esc(UI["stat_weeks"][lang])}</span></div>'
            f'<div class="o"><b>3</b><span>{esc(UI["stat_langs"][lang])}</span></div>'
            f'<div><b>0</b><span>{esc(UI["stat_install"][lang])}</span></div></div>'
            f'<p style="color:var(--muted);margin-top:16px">{esc(UI["contact"][lang])}: '
            f'<a href="mailto:{AUTHOR["email"]}">{AUTHOR["email"]}</a></p></div>', unsafe_allow_html=True)


# -----------------------------------------------------------------------------
def main():
    init_state()
    lang = st.session_state.lang
    inject_css(lang)
    top_nav(lang)
    page = st.session_state.page
    {"home": page_home, "weeks": page_weeks, "week": page_week, "syllabus": page_syllabus, "play": page_play,
     "progress": page_progress, "about": page_about}.get(page, page_home)(lang)
    footer(lang)


main()
