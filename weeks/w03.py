"""
WEEK 3 · Writing a first simple program in Python  (level: very easy)
Programme: "Hello, World!" · syntax basics · running the program and fixing simple errors.
"""
from syllabus import L

WEEK = {
    "objectives": L(
        [
            "**Write** and run the program `Hello, World!`.",
            "**Display** text and numbers with `print()`.",
            "**Add** comments with `#`.",
            "**Respect** the basic rules of Python writing (syntax).",
            "**Read** an error message and **fix** a simple error.",
        ],
        [
            "**Écrire** et exécuter le programme `Hello, World!`.",
            "**Afficher** du texte et des nombres avec `print()`.",
            "**Ajouter** des commentaires avec `#`.",
            "**Respecter** les règles de base de l'écriture Python (la syntaxe).",
            "**Lire** un message d'erreur et **corriger** une erreur simple.",
        ],
        [
            "**يكتب** وينفّذ برنامج `Hello, World!`.",
            "**يعرض** النصوص والأعداد بواسطة `print()`.",
            "**يضيف** تعليقات بالرمز `#`.",
            "**يحترم** القواعد الأساسية لكتابة Python (التركيب).",
            "**يقرأ** رسالة خطأ و**يصحّح** خطأً بسيطاً.",
        ],
    ),

    "lesson": L(
r'''
### 1. The first program
The tradition: the first program of every programmer displays **Hello, World!**
```python
print("Hello, World!")
```
- `print` means **display**.
- What we display goes **between brackets** `( )`.
- A text goes **between quotes** `" "`.

### 2. Text and numbers
| We write | We see | Why |
|---|---|---|
| `print("Hello")` | Hello | text → with quotes |
| `print(2026)` | 2026 | number → without quotes |
| `print(5 + 3)` | 8 | Python calculates |
| `print("5 + 3")` | 5 + 3 | it is a text, no calculation |

### 3. Several things on one line
Separate them with a **comma**. Python adds a space between them.
```python
print("Price:", 1500, "DZD")
```
Result: `Price: 1500 DZD`

### 4. Comments
A line that starts with `#` is a **comment**. Python ignores it. It is a note for humans.
```python
# This program displays a welcome message
print("Welcome!")
```

### 5. The rules (syntax)
- Python is **case-sensitive**: `print` ✅ but `Print` ❌
- Every opening bracket needs a closing bracket: `print("Hi")` ✅ `print("Hi"` ❌
- Quotes go in pairs: `"Hi"` ✅ `"Hi` ❌
- One instruction per line, starting at the **beginning of the line** (no space before).

### 6. Errors are normal!
When something is wrong, Python shows an **error message**. Read it from the bottom:
- the **line number** tells you **where**;
- the **type** of error tells you **what**.

| Error | Meaning | Example |
|---|---|---|
| `SyntaxError` | The writing is wrong | missing bracket or quote |
| `NameError` | Python does not know this word | `Print` instead of `print` |
| `IndentationError` | A space at the wrong place | a space before `print` |

> **Remember:** an error is not a failure. Read the message, fix, run again.
''',
r'''
### 1. Le premier programme
La tradition : le premier programme de tout programmeur affiche **Hello, World!**
```python
print("Hello, World!")
```
- `print` veut dire **afficher**.
- Ce qu'on affiche se met **entre parenthèses** `( )`.
- Un texte se met **entre guillemets** `" "`.

### 2. Texte et nombres
| On écrit | On voit | Pourquoi |
|---|---|---|
| `print("Bonjour")` | Bonjour | texte → avec guillemets |
| `print(2026)` | 2026 | nombre → sans guillemets |
| `print(5 + 3)` | 8 | Python calcule |
| `print("5 + 3")` | 5 + 3 | c'est un texte, pas de calcul |

### 3. Plusieurs choses sur une ligne
On les sépare par une **virgule**. Python ajoute un espace entre elles.
```python
print("Price:", 1500, "DZD")
```
Résultat : `Price: 1500 DZD`

### 4. Les commentaires
Une ligne qui commence par `#` est un **commentaire**. Python l'ignore. C'est une note pour les humains.
```python
# Ce programme affiche un message de bienvenue
print("Welcome!")
```

### 5. Les règles (la syntaxe)
- Python fait la différence entre **majuscules et minuscules** : `print` ✅ mais `Print` ❌
- Chaque parenthèse ouverte doit être fermée : `print("Hi")` ✅ `print("Hi"` ❌
- Les guillemets vont par deux : `"Hi"` ✅ `"Hi` ❌
- Une instruction par ligne, au **début de la ligne** (pas d'espace avant).

### 6. Les erreurs sont normales !
Quand quelque chose ne va pas, Python affiche un **message d'erreur**. Lis-le en partant du bas :
- le **numéro de ligne** te dit **où** ;
- le **type** d'erreur te dit **quoi**.

| Erreur | Signification | Exemple |
|---|---|---|
| `SyntaxError` | L'écriture est fausse | parenthèse ou guillemet manquant |
| `NameError` | Python ne connaît pas ce mot | `Print` au lieu de `print` |
| `IndentationError` | Un espace au mauvais endroit | un espace avant `print` |

> **À retenir :** une erreur n'est pas un échec. Lis le message, corrige, relance.
''',
r'''
### 1. البرنامج الأول
جرت العادة أن يعرض أول برنامج لكل مبرمج عبارة **Hello, World!**
```python
print("Hello, World!")
```
- `print` تعني **اعرض**.
- ما نريد عرضه نضعه **بين قوسين** `( )`.
- النص نضعه **بين علامتي تنصيص** `" "`.

### 2. النصوص والأعداد
| نكتب | نرى | لماذا |
|---|---|---|
| `print("Hello")` | Hello | نص ← مع علامات التنصيص |
| `print(2026)` | 2026 | عدد ← دون علامات التنصيص |
| `print(5 + 3)` | 8 | Python تحسب |
| `print("5 + 3")` | 5 + 3 | هذا نص، لا يوجد حساب |

### 3. عدة أشياء في سطر واحد
نفصل بينها **بفاصلة**، وتضيف Python مسافة بينها.
```python
print("Price:", 1500, "DZD")
```
النتيجة: `Price: 1500 DZD`

### 4. التعليقات
السطر الذي يبدأ بالرمز `#` هو **تعليق**، تتجاهله Python. إنه ملاحظة للبشر.
```python
# This program displays a welcome message
print("Welcome!")
```

### 5. القواعد (التركيب)
- Python تفرّق بين **الحروف الكبيرة والصغيرة**: `print` ✅ لكن `Print` ❌
- كل قوس مفتوح يجب أن يُغلق: `print("Hi")` ✅ `print("Hi"` ❌
- علامات التنصيص تأتي مثنى: `"Hi"` ✅ `"Hi` ❌
- تعليمة واحدة في كل سطر، تبدأ من **أول السطر** (دون مسافة قبلها).

### 6. الأخطاء أمر طبيعي!
عندما يكون هناك خلل، تعرض Python **رسالة خطأ**. اقرأها من الأسفل:
- **رقم السطر** يخبرك **أين** الخطأ؛
- **نوع** الخطأ يخبرك **ما هو**.

| الخطأ | المعنى | مثال |
|---|---|---|
| `SyntaxError` | الكتابة خاطئة | قوس أو علامة تنصيص ناقصة |
| `NameError` | Python لا تعرف هذه الكلمة | `Print` بدل `print` |
| `IndentationError` | مسافة في غير مكانها | مسافة قبل `print` |

> **تذكّر:** الخطأ ليس فشلاً. اقرأ الرسالة، صحّح، ثم أعد التشغيل.
'''),

    "examples": [
        {
            "title": L("Hello, World!", "Hello, World!", "Hello, World!"),
            "explain": L("Run it, then change the message and run again.",
                         "Exécute-le, puis change le message et relance.",
                         "نفّذه، ثم غيّر الرسالة وأعد التشغيل."),
            "code": '''# My first program
print("Hello, World!")
print("I am a student in economics.")
''',
        },
        {
            "title": L("Text, numbers and commas", "Texte, nombres et virgules", "النصوص والأعداد والفواصل"),
            "explain": L("Compare the line with quotes and the line without quotes.",
                         "Compare la ligne avec guillemets et la ligne sans guillemets.",
                         "قارن بين السطر الذي فيه علامات التنصيص والسطر الذي ليس فيه."),
            "code": '''print("5 + 3")      # a text
print(5 + 3)        # a calculation
print("Price:", 1500, "DZD")
print("Total:", 1500 * 2, "DZD")
''',
        },
        {
            "title": L("Find and fix the error", "Trouve et corrige l'erreur", "اكتشف الخطأ وصحّحه"),
            "explain": L("Run it: Python shows a `SyntaxError`. A quote is missing. Add it and run again.",
                         "Exécute : Python affiche une `SyntaxError`. Il manque un guillemet. Ajoute-le et relance.",
                         "نفّذ: تعرض Python خطأ `SyntaxError`. هناك علامة تنصيص ناقصة. أضفها وأعد التشغيل."),
            "error_ok": True,   # the error is the point of this example
            "code": '''print("Welcome to PyDZ)
''',
        },
    ],

    "exercises": [
        {
            "title": L("Hello, World!", "Hello, World!", "Hello, World!"),
            "task": L("Display exactly: `Hello, World!`", "Affiche exactement : `Hello, World!`", "اعرض بالضبط: `Hello, World!`"),
            "starter": "# Write your program here\n",
            "expected": "Hello, World!",
            "hint": L("`print(\"...\")` with the text between quotes.", "`print(\"...\")` avec le texte entre guillemets.",
                      "`print(\"...\")` مع النص بين علامتي تنصيص."),
            "solution": 'print("Hello, World!")\n',
        },
        {
            "title": L("An invoice line", "Une ligne de facture", "سطر في فاتورة"),
            "task": L("Display `Total: 1500 DZD` using **one** `print()` with **commas** (the number 1500 without quotes).",
                      "Affiche `Total: 1500 DZD` avec **un seul** `print()` et des **virgules** (le nombre 1500 sans guillemets).",
                      "اعرض `Total: 1500 DZD` باستعمال `print()` **واحدة** مع **فواصل** (العدد 1500 دون علامات تنصيص)."),
            "starter": "# Use commas between the parts\n",
            "expected": "Total: 1500 DZD",
            "hint": L("Three parts: `\"Total:\"`, `1500` and `\"DZD\"`.", "Trois parties : `\"Total:\"`, `1500` et `\"DZD\"`.",
                      "ثلاثة أجزاء: `\"Total:\"` و`1500` و`\"DZD\"`."),
            "solution": 'print("Total:", 1500, "DZD")\n',
        },
        {
            "title": L("Fix the two errors", "Corrige les deux erreurs", "صحّح الخطأين"),
            "task": L("This program has **two** errors. Fix them so it displays `Welcome` then `PyDZ`.",
                      "Ce programme contient **deux** erreurs. Corrige-les pour qu'il affiche `Welcome` puis `PyDZ`.",
                      "يحتوي هذا البرنامج على **خطأين**. صحّحهما ليعرض `Welcome` ثم `PyDZ`."),
            "starter": 'Print("Welcome")\nprint("PyDZ)\n',
            "expected": "Welcome\nPyDZ",
            "hint": L("Line 1: capital letter. Line 2: a missing quote.", "Ligne 1 : une majuscule. Ligne 2 : un guillemet manquant.",
                      "السطر 1: حرف كبير. السطر 2: علامة تنصيص ناقصة."),
            "solution": 'print("Welcome")\nprint("PyDZ")\n',
        },
    ],

    "quiz": [
        {"q": L("Which instruction displays a message?", "Quelle instruction affiche un message ?", "ما التعليمة التي تعرض رسالة؟"),
         "options": ["display()", "show()", "print()", "write()"], "answer": 2,
         "explain": L("`print()` displays on the screen.", "`print()` affiche à l'écran.", "`print()` تعرض على الشاشة.")},
        {"q": L("What does `print(4 + 6)` display?", "Qu'affiche `print(4 + 6)` ?", "ماذا تعرض `print(4 + 6)`؟"),
         "options": L(["4 + 6", "10", "46", "An error"], ["4 + 6", "10", "46", "Une erreur"], ["4 + 6", "10", "46", "خطأ"]), "answer": 1,
         "explain": L("No quotes: Python calculates.", "Pas de guillemets : Python calcule.", "لا توجد علامات تنصيص: Python تحسب.")},
        {"q": L("What does `print(\"4 + 6\")` display?", "Qu'affiche `print(\"4 + 6\")` ?", "ماذا تعرض `print(\"4 + 6\")`؟"),
         "options": L(["4 + 6", "10", "46", "An error"], ["4 + 6", "10", "46", "Une erreur"], ["4 + 6", "10", "46", "خطأ"]), "answer": 0,
         "explain": L("With quotes, it is a text: no calculation.", "Avec des guillemets, c'est un texte : pas de calcul.",
                      "مع علامات التنصيص هو نص: لا يوجد حساب.")},
        {"q": L("Which sign starts a comment?", "Quel signe commence un commentaire ?", "ما الرمز الذي يبدأ به التعليق؟"),
         "options": ["//", "#", "--", "*"], "answer": 1,
         "explain": L("In Python, comments start with `#`.", "En Python, les commentaires commencent par `#`.",
                      "في Python تبدأ التعليقات بالرمز `#`.")},
        {"q": L("`Print(\"Hi\")` gives an error. Why?", "`Print(\"Hi\")` donne une erreur. Pourquoi ?", "`Print(\"Hi\")` يعطي خطأً. لماذا؟"),
         "options": L(["The text is too short", "Python is case-sensitive: it must be `print`", "Quotes are forbidden", "Brackets are forbidden"],
                      ["Le texte est trop court", "Python distingue majuscules et minuscules : il faut `print`", "Les guillemets sont interdits", "Les parenthèses sont interdites"],
                      ["النص قصير جداً", "Python تفرّق بين الحروف الكبيرة والصغيرة: يجب كتابة `print`", "علامات التنصيص ممنوعة", "الأقواس ممنوعة"]),
         "answer": 1,
         "explain": L("Python does not know `Print`: it is a `NameError`.", "Python ne connaît pas `Print` : c'est une `NameError`.",
                      "Python لا تعرف `Print`: إنه خطأ `NameError`.")},
        {"q": L("Which line is correct?", "Quelle ligne est correcte ?", "أي سطر صحيح؟"),
         "options": ['print("Hello)', 'print("Hello")', 'print "Hello"', 'print(Hello"'], "answer": 1,
         "explain": L("Brackets closed and quotes in pairs.", "Parenthèses fermées et guillemets par deux.",
                      "الأقواس مغلقة وعلامات التنصيص مثنى.")},
    ],
}
