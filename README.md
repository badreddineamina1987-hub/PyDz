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

## Free and premium content
- **Free:** objectives, lessons and the first example of every week, plus the playground.
- **Premium (1 year):** the other examples, exercises and quizzes.

Students unlock premium content with an **access code**. Codes are kept secret in Streamlit, never in GitHub:
1. On share.streamlit.io, open your app → **⋮ → Settings → Secrets**.
2. Write one line per student: the code, then the last day of access:
```toml
[access_codes]
"PYDZ-7K2M-QX" = "2027-11-30"
"PYDZ-A93F-LD" = "2027-12-15"
```
3. Click **Save**. The code works at once; after its date it stops working.

To stop a code, delete its line.

**Review mode:** at the top of `app.py`, `PREMIUM_LOCK = False` shows everything to everyone (useful while you review the content). Set it to `True` to lock the premium content. To show the price on the home page, set `PRICE_DZD` at the top of `app.py` (for example `PRICE_DZD = 2500`).
