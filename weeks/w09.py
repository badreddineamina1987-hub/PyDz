"""
WEEK 9 · Working with strings  (level: very easy)
Programme: what strings are and how to manipulate them · basic functions (slice, upper, lower) · analysing text data.
"""
from syllabus import L

WEEK = {
    "objectives": L(
        [
            "**Create** a string and **join** strings with `+`.",
            "**Take** one letter or a part of a text (index and slice).",
            "**Use** `len()`, `upper()`, `lower()`, `replace()`.",
            "**Cut** a text into words with `split()` and **search** with `in`.",
            "**Build** a clear message with an f-string.",
        ],
        [
            "**Créer** une chaîne et **coller** des chaînes avec `+`.",
            "**Prendre** une lettre ou un morceau de texte (indice et découpage).",
            "**Utiliser** `len()`, `upper()`, `lower()`, `replace()`.",
            "**Couper** un texte en mots avec `split()` et **chercher** avec `in`.",
            "**Construire** un message clair avec une f-string.",
        ],
        [
            "**ينشئ** نصاً و**يلصق** النصوص بالرمز `+`.",
            "**يأخذ** حرفاً أو جزءاً من نص (الفهرس والتقطيع).",
            "**يستعمل** `len()` و`upper()` و`lower()` و`replace()`.",
            "**يقسّم** نصاً إلى كلمات بـ `split()` و**يبحث** بـ `in`.",
            "**يبني** رسالة واضحة باستعمال f-string.",
        ],
    ),

    "lesson": L(
r'''
### 1. What is a string?
A **string** (`str`) is a text between quotes.
```python
city = "Boumerdes"
```
Joining strings with `+`:
```python
first = "Sara"
last = "Benali"
print(first + " " + last)       # Sara Benali
```

### 2. Length: len()
```python
print(len("Algeria"))           # 7 letters
```

### 3. One letter: the index
Each letter has a **position** (index). ⚠️ We start counting at **0**.
| A | l | g | e | r | i | a |
|---|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
```python
word = "Algeria"
print(word[0])      # A
print(word[-1])     # a   (-1 = the last letter)
```

### 4. A part of the text: slice
`text[start:end]` takes from `start` up to `end` (**not included**).
```python
code = "DZ-2026-INV"
print(code[0:2])    # DZ
print(code[3:7])    # 2026
```

### 5. Useful functions
| Function | What it does | Example | Result |
|---|---|---|---|
| `upper()` | capital letters | `"dzd".upper()` | DZD |
| `lower()` | small letters | `"SARA".lower()` | sara |
| `replace(a, b)` | replaces a by b | `"10,5".replace(",", ".")` | 10.5 |
| `split()` | cuts into words | `"oil price up".split()` | ['oil', 'price', 'up'] |
| `in` | is it inside? | `"oil" in "oil price"` | True |

### 6. f-strings: clean messages
Put `f` before the quotes, and variables between `{ }`.
```python
name = "Sara"
total = 3600
print(f"{name} must pay {total} DZD")
```
Result: `Sara must pay 3600 DZD`

> **Remember:** counting starts at 0, and the end of a slice is not included.
''',
r'''
### 1. Qu'est-ce qu'une chaîne ?
Une **chaîne** (`str`) est un texte entre guillemets.
```python
city = "Boumerdes"
```
Coller des chaînes avec `+` :
```python
first = "Sara"
last = "Benali"
print(first + " " + last)       # Sara Benali
```

### 2. La longueur : len()
```python
print(len("Algeria"))           # 7 lettres
```

### 3. Une lettre : l'indice
Chaque lettre a une **position** (indice). ⚠️ On commence à compter à **0**.
| A | l | g | e | r | i | a |
|---|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
```python
word = "Algeria"
print(word[0])      # A
print(word[-1])     # a   (-1 = la dernière lettre)
```

### 4. Un morceau de texte : le découpage
`text[début:fin]` prend de `début` jusqu'à `fin` (**non incluse**).
```python
code = "DZ-2026-INV"
print(code[0:2])    # DZ
print(code[3:7])    # 2026
```

### 5. Fonctions utiles
| Fonction | Ce qu'elle fait | Exemple | Résultat |
|---|---|---|---|
| `upper()` | majuscules | `"dzd".upper()` | DZD |
| `lower()` | minuscules | `"SARA".lower()` | sara |
| `replace(a, b)` | remplace a par b | `"10,5".replace(",", ".")` | 10.5 |
| `split()` | coupe en mots | `"oil price up".split()` | ['oil', 'price', 'up'] |
| `in` | est-ce dedans ? | `"oil" in "oil price"` | True |

### 6. Les f-strings : des messages propres
Mets `f` avant les guillemets, et les variables entre `{ }`.
```python
name = "Sara"
total = 3600
print(f"{name} must pay {total} DZD")
```
Résultat : `Sara must pay 3600 DZD`

> **À retenir :** on compte à partir de 0, et la fin d'un découpage n'est pas incluse.
''',
r'''
### 1. ما هو النص؟
**النص** (`str`) هو كتابة بين علامتي تنصيص.
```python
city = "Boumerdes"
```
لصق النصوص بالرمز `+`:
```python
first = "Sara"
last = "Benali"
print(first + " " + last)       # Sara Benali
```

### 2. الطول: len()
```python
print(len("Algeria"))           # 7 letters
```

### 3. حرف واحد: الفهرس
لكل حرف **موقع** (فهرس). ⚠️ نبدأ العدّ من **0**.
| A | l | g | e | r | i | a |
|---|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
```python
word = "Algeria"
print(word[0])      # A
print(word[-1])     # a   (-1 = the last letter)
```

### 4. جزء من النص: التقطيع
`text[start:end]` يأخذ من `start` إلى `end` (**غير مشمول**).
```python
code = "DZ-2026-INV"
print(code[0:2])    # DZ
print(code[3:7])    # 2026
```

### 5. دوال مفيدة
| الدالة | ماذا تفعل | مثال | النتيجة |
|---|---|---|---|
| `upper()` | حروف كبيرة | `"dzd".upper()` | DZD |
| `lower()` | حروف صغيرة | `"SARA".lower()` | sara |
| `replace(a, b)` | تعوّض a بـ b | `"10,5".replace(",", ".")` | 10.5 |
| `split()` | تقسّم إلى كلمات | `"oil price up".split()` | ['oil', 'price', 'up'] |
| `in` | هل هو موجود؟ | `"oil" in "oil price"` | True |

### 6. f-strings: رسائل واضحة
ضع `f` قبل علامات التنصيص، والمتغيرات بين `{ }`.
```python
name = "Sara"
total = 3600
print(f"{name} must pay {total} DZD")
```
النتيجة: `Sara must pay 3600 DZD`

> **تذكّر:** العدّ يبدأ من 0، ونهاية التقطيع غير مشمولة.
'''),

    "examples": [
        {
            "title": L("Letters and pieces", "Lettres et morceaux", "حروف وأجزاء"),
            "explain": L("An invoice code contains the country, the year and the type. We take each part with a slice.",
                         "Un code de facture contient le pays, l'année et le type. On prend chaque partie par découpage.",
                         "رمز الفاتورة يحتوي على البلد والسنة والنوع. نأخذ كل جزء بالتقطيع."),
            "code": '''code = "DZ-2026-INV"

print("Length:", len(code))
print("First letter:", code[0])
print("Country:", code[0:2])
print("Year:", code[3:7])
print("Type:", code[8:11])
''',
        },
        {
            "title": L("Cleaning data", "Nettoyer des données", "تنظيف البيانات"),
            "explain": L("Data typed by people is often messy. We clean it with `upper()`, `replace()` and `strip()` (removes spaces at the ends).",
                         "Les données tapées à la main sont souvent sales. On les nettoie avec `upper()`, `replace()` et `strip()` (enlève les espaces aux bords).",
                         "البيانات المكتوبة يدوياً تكون غالباً غير منظمة. ننظفها بـ `upper()` و`replace()` و`strip()` (تحذف المسافات في الطرفين)."),
            "code": '''currency = "  dzd "
amount = "1250,50"

currency = currency.strip().upper()
amount = amount.replace(",", ".")

print(currency)
print(amount)
print(float(amount) * 2)
''',
        },
        {
            "title": L("Analysing a headline", "Analyser un titre de presse", "تحليل عنوان صحفي"),
            "explain": L("`split()` cuts the text into words. Then we count and search.",
                         "`split()` coupe le texte en mots. Ensuite on compte et on cherche.",
                         "`split()` تقسّم النص إلى كلمات، ثم نعدّ ونبحث."),
            "code": '''headline = "Oil prices rise and the dinar stays stable"

words = headline.split()
print("Words:", words)
print("Number of words:", len(words))
print("Talks about oil?", "oil" in headline.lower())
print(f"The headline has {len(headline)} characters.")
''',
        },
    ],

    "exercises": [
        {
            "title": L("In capital letters", "En majuscules", "بالحروف الكبيرة"),
            "task": L("Display the variable `country` in capital letters.", "Affiche la variable `country` en majuscules.",
                      "اعرض المتغير `country` بالحروف الكبيرة."),
            "starter": 'country = "algeria"\n\n',
            "expected": "ALGERIA",
            "hint": L("`print(country.upper())`", "`print(country.upper())`", "`print(country.upper())`"),
            "solution": 'country = "algeria"\n\nprint(country.upper())\n',
        },
        {
            "title": L("Find the year", "Trouve l'année", "استخرج السنة"),
            "task": L("From `code = \"DZ-2026-INV\"`, display only the year `2026` with a slice.",
                      "À partir de `code = \"DZ-2026-INV\"`, affiche seulement l'année `2026` par découpage.",
                      "من `code = \"DZ-2026-INV\"` اعرض السنة `2026` فقط بالتقطيع."),
            "starter": 'code = "DZ-2026-INV"\n\n',
            "expected": "2026",
            "hint": L("The year starts at position 3 and ends before 7: `code[3:7]`.", "L'année commence à la position 3 et finit avant 7 : `code[3:7]`.",
                      "السنة تبدأ من الموقع 3 وتنتهي قبل 7: `code[3:7]`."),
            "solution": 'code = "DZ-2026-INV"\n\nprint(code[3:7])\n',
        },
        {
            "title": L("Count the words", "Compte les mots", "عدّ الكلمات"),
            "task": L("Display the number of words in the sentence.", "Affiche le nombre de mots de la phrase.", "اعرض عدد الكلمات في الجملة."),
            "starter": 'sentence = "the price of oil is rising"\n\n',
            "expected": "6",
            "hint": L("`len(sentence.split())`", "`len(sentence.split())`", "`len(sentence.split())`"),
            "solution": 'sentence = "the price of oil is rising"\n\nprint(len(sentence.split()))\n',
        },
    ],

    "quiz": [
        {"q": L("`word = \"Python\"`. What is `word[0]`?", "`word = \"Python\"`. Que vaut `word[0]` ?", "`word = \"Python\"`. ما قيمة `word[0]`؟"),
         "options": ["y", "P", "n", "Python"], "answer": 1,
         "explain": L("Counting starts at 0: the first letter.", "On compte à partir de 0 : la première lettre.", "العدّ يبدأ من 0: الحرف الأول.")},
        {"q": L("`word = \"Python\"`. What is `word[-1]`?", "`word = \"Python\"`. Que vaut `word[-1]` ?", "`word = \"Python\"`. ما قيمة `word[-1]`؟"),
         "options": ["P", "o", "h", "n"], "answer": 3,
         "explain": L("`-1` is the last letter.", "`-1` est la dernière lettre.", "`-1` هو الحرف الأخير.")},
        {"q": L("What does `\"Boumerdes\"[0:4]` give?", "Que donne `\"Boumerdes\"[0:4]` ?", "ماذا تعطي `\"Boumerdes\"[0:4]`؟"),
         "options": ["Boum", "Boume", "oume", "B"], "answer": 0,
         "explain": L("From 0 to 4, 4 not included: 4 letters.", "De 0 à 4, 4 non inclus : 4 lettres.", "من 0 إلى 4، و4 غير مشمول: 4 حروف.")},
        {"q": L("What does `len(\"DZD\")` give?", "Que donne `len(\"DZD\")` ?", "ماذا تعطي `len(\"DZD\")`؟"),
         "options": ["2", "3", "4", "DZD"], "answer": 1,
         "explain": L("3 characters.", "3 caractères.", "3 حروف.")},
        {"q": L("Which function puts a text in small letters?", "Quelle fonction met un texte en minuscules ?", "ما الدالة التي تحوّل النص إلى حروف صغيرة؟"),
         "options": ["upper()", "small()", "lower()", "split()"], "answer": 2,
         "explain": L("`lower()` → small letters; `upper()` → capitals.", "`lower()` → minuscules ; `upper()` → majuscules.",
                      "`lower()` ← حروف صغيرة، `upper()` ← حروف كبيرة.")},
        {"q": L("`total = 500`. What does `print(f\"Total: {total} DZD\")` display?",
                "`total = 500`. Qu'affiche `print(f\"Total: {total} DZD\")` ?", "`total = 500`. ماذا تعرض `print(f\"Total: {total} DZD\")`؟"),
         "options": L(["Total: {total} DZD", "Total: 500 DZD", "f Total: 500 DZD", "An error"], ["Total: {total} DZD", "Total: 500 DZD", "f Total: 500 DZD", "Une erreur"], ["Total: {total} DZD", "Total: 500 DZD", "f Total: 500 DZD", "خطأ"]), "answer": 1,
         "explain": L("In an f-string, `{total}` is replaced by its value.", "Dans une f-string, `{total}` est remplacé par sa valeur.",
                      "في f-string يُعوَّض `{total}` بقيمته.")},
    ],
}
