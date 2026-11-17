# PyDZ — learn Python week by week (FR / EN / AR)

Created by **Dr. BADREDDINE Amina**.

PyDZ follows the **ministerial programme** of *Programming Basics 1* (first year, semester 1), week by week (15 weeks), in **French, English and Arabic**.

## Files
| File | Content |
|---|---|
| `app.py` | Interface: pages, design, navigation |
| `syllabus.py` | Official programme: module sheet, axes, assessment, the 15 weekly titles |
| `i18n.py` | All interface texts in the three languages + author details (name, e-mail) |
| `runner.py` | The in-browser Python editor (Pyodide) |
| `weeks/w01.py` | Content of week 1 (lesson, examples, exercises, quiz) in 3 languages |
| `assets/pydz-icon.svg`, `assets/pydz-icon.png` | PyDZ icon (page and browser tab) |
| `.streamlit/config.toml` | Colours (blue / orange) |
| `requirements.txt` | `streamlit>=1.45` |

## Add a new week
Copy `weeks/w01.py` to `weeks/w02.py` (w03.py, …) and replace the content. Each text is written as
`L("English", "Français", "العربية")`. The week appears automatically as **Available**; weeks without a file show **In preparation** with their programme content.

## Run on your computer
```bash
pip install streamlit
streamlit run app.py
```
Opens at http://localhost:8501. Add `?lang=ar`, `?lang=en` or `?lang=fr` to the link to open the platform directly in one language.
The default language is set by `DEFAULT_LANG` at the top of `app.py`.

## Put it online for free
1. Create a public GitHub repository and upload **all files and folders** (including `weeks/`, `assets/` and `.streamlit/`).
2. Go to https://share.streamlit.io → **Create app** → choose the repository and `app.py` → **Deploy**.
3. Share the link with your students.

## How the code runs
Students' code runs inside their own browser with Pyodide (Python compiled to WebAssembly): nothing to install, works on phones. An internet connection is needed the first time.
