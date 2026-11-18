"""
WEEK 4 · Variables and data types  (level: very easy)
Programme: data types (int, float, str, bool) · defining variables and naming rules · simple programs.
"""
from syllabus import L

WEEK = {
    "objectives": L(
        [
            "**Create** a variable and give it a value with `=`.",
            "**Recognise** the 4 basic types: `int`, `float`, `str`, `bool`.",
            "**Find** the type of a value with `type()`.",
            "**Choose** good variable names that follow the rules.",
            "**Write** a small program with variables.",
        ],
        [
            "**Créer** une variable et lui donner une valeur avec `=`.",
            "**Reconnaître** les 4 types de base : `int`, `float`, `str`, `bool`.",
            "**Trouver** le type d'une valeur avec `type()`.",
            "**Choisir** de bons noms de variables qui respectent les règles.",
            "**Écrire** un petit programme avec des variables.",
        ],
        [
            "**ينشئ** متغيراً ويعطيه قيمة بالرمز `=`.",
            "**يتعرّف** على الأنواع الأربعة الأساسية: `int` و`float` و`str` و`bool`.",
            "**يعرف** نوع قيمة بواسطة `type()`.",
            "**يختار** أسماء متغيرات جيدة تحترم القواعد.",
            "**يكتب** برنامجاً صغيراً يستعمل المتغيرات.",
        ],
    ),

    "lesson": L(
r'''
### 1. What is a variable?
A **variable** is a **box with a name**. We put a value inside, and we use the name to find it again.
```python
price = 2500
```
- `price` is the **name** of the box.
- `=` means **"put inside"** (it is not "equal" like in maths).
- `2500` is the **value**.

```python
price = 2500
print(price)        # displays 2500
```

### 2. Changing the value
A variable can change. The new value **replaces** the old one.
```python
stock = 40
stock = 35
print(stock)        # displays 35
```

### 3. The 4 basic types
| Type | Name | Examples |
|---|---|---|
| `int` | whole number | `19`, `2026`, `-5` |
| `float` | decimal number | `3.5`, `0.19`, `1250.75` |
| `str` | text (string) | `"Algeria"`, `"Sara"` |
| `bool` | true or false | `True`, `False` |

⚠️ In Python, decimals use a **dot**: `3.5` ✅ and not `3,5` ❌

### 4. Knowing the type
```python
print(type(19))        # <class 'int'>
print(type(3.5))       # <class 'float'>
print(type("Sara"))    # <class 'str'>
print(type(True))      # <class 'bool'>
```

### 5. Naming rules
| ✅ Allowed | ❌ Forbidden | Why |
|---|---|---|
| `price` | `2price` | cannot start with a number |
| `unit_price` | `unit price` | no spaces (use `_`) |
| `total2` | `total-2` | no `-` sign |
| `vat_rate` | `print` | Python's own words are reserved |

**Good habit:** choose clear names: `unit_price` is better than `x`.

### 6. A small program
```python
product = "Laptop"
unit_price = 85000
quantity = 3
total = unit_price * quantity
print(product, total)
```

> **Remember:** a variable = a name + a value. The type depends on the value.
''',
r'''
### 1. Qu'est-ce qu'une variable ?
Une **variable** est une **boîte avec un nom**. On met une valeur dedans, et on utilise le nom pour la retrouver.
```python
price = 2500
```
- `price` est le **nom** de la boîte.
- `=` veut dire **« mettre dedans »** (ce n'est pas « égal » comme en maths).
- `2500` est la **valeur**.

```python
price = 2500
print(price)        # affiche 2500
```

### 2. Changer la valeur
Une variable peut changer. La nouvelle valeur **remplace** l'ancienne.
```python
stock = 40
stock = 35
print(stock)        # affiche 35
```

### 3. Les 4 types de base
| Type | Nom | Exemples |
|---|---|---|
| `int` | nombre entier | `19`, `2026`, `-5` |
| `float` | nombre décimal | `3.5`, `0.19`, `1250.75` |
| `str` | texte (chaîne) | `"Algeria"`, `"Sara"` |
| `bool` | vrai ou faux | `True`, `False` |

⚠️ En Python, les décimales utilisent un **point** : `3.5` ✅ et non `3,5` ❌

### 4. Connaître le type
```python
print(type(19))        # <class 'int'>
print(type(3.5))       # <class 'float'>
print(type("Sara"))    # <class 'str'>
print(type(True))      # <class 'bool'>
```

### 5. Règles de nommage
| ✅ Autorisé | ❌ Interdit | Pourquoi |
|---|---|---|
| `price` | `2price` | ne commence pas par un chiffre |
| `unit_price` | `unit price` | pas d'espace (utilise `_`) |
| `total2` | `total-2` | pas de signe `-` |
| `vat_rate` | `print` | les mots de Python sont réservés |

**Bonne habitude :** choisis des noms clairs : `unit_price` est mieux que `x`.

### 6. Un petit programme
```python
product = "Laptop"
unit_price = 85000
quantity = 3
total = unit_price * quantity
print(product, total)
```

> **À retenir :** une variable = un nom + une valeur. Le type dépend de la valeur.
''',
r'''
### 1. ما هو المتغير؟
**المتغير** هو **صندوق له اسم**. نضع فيه قيمة، ونستعمل الاسم لنجدها من جديد.
```python
price = 2500
```
- `price` هو **اسم** الصندوق.
- `=` تعني **«ضع في»** (وليست «يساوي» كما في الرياضيات).
- `2500` هي **القيمة**.

```python
price = 2500
print(price)        # displays 2500
```

### 2. تغيير القيمة
يمكن للمتغير أن يتغيّر، والقيمة الجديدة **تعوّض** القديمة.
```python
stock = 40
stock = 35
print(stock)        # displays 35
```

### 3. الأنواع الأربعة الأساسية
| النوع | الاسم | أمثلة |
|---|---|---|
| `int` | عدد صحيح | `19`، `2026`، `-5` |
| `float` | عدد عشري | `3.5`، `0.19`، `1250.75` |
| `str` | نص (سلسلة حروف) | `"Algeria"`، `"Sara"` |
| `bool` | صحيح أو خطأ | `True`، `False` |

⚠️ في Python نستعمل **النقطة** للأعداد العشرية: `3.5` ✅ وليس `3,5` ❌

### 4. معرفة النوع
```python
print(type(19))        # <class 'int'>
print(type(3.5))       # <class 'float'>
print(type("Sara"))    # <class 'str'>
print(type(True))      # <class 'bool'>
```

### 5. قواعد التسمية
| ✅ مسموح | ❌ ممنوع | السبب |
|---|---|---|
| `price` | `2price` | لا يبدأ برقم |
| `unit_price` | `unit price` | دون مسافات (استعمل `_`) |
| `total2` | `total-2` | دون الرمز `-` |
| `vat_rate` | `print` | كلمات Python محجوزة |

**عادة جيدة:** اختر أسماء واضحة: `unit_price` أفضل من `x`.

### 6. برنامج صغير
```python
product = "Laptop"
unit_price = 85000
quantity = 3
total = unit_price * quantity
print(product, total)
```

> **تذكّر:** المتغير = اسم + قيمة، والنوع يتعلّق بالقيمة.
'''),

    "examples": [
        {
            "title": L("A box with a name", "Une boîte avec un nom", "صندوق له اسم"),
            "explain": L("The value of `stock` changes. Which value is displayed at the end?",
                         "La valeur de `stock` change. Quelle valeur est affichée à la fin ?",
                         "قيمة `stock` تتغيّر. ما القيمة المعروضة في النهاية؟"),
            "code": '''stock = 40
print("Stock at the start:", stock)

stock = 35          # 5 units were sold
print("Stock now:", stock)
''',
        },
        {
            "title": L("The 4 types", "Les 4 types", "الأنواع الأربعة"),
            "explain": L("`type()` tells the type of each value. Try other values.",
                         "`type()` donne le type de chaque valeur. Essaie d'autres valeurs.",
                         "`type()` تعطي نوع كل قيمة. جرّب قيماً أخرى."),
            "code": '''age = 19
vat_rate = 0.19
country = "Algeria"
is_student = True

print(type(age))
print(type(vat_rate))
print(type(country))
print(type(is_student))
''',
        },
        {
            "title": L("A product sheet", "Une fiche produit", "بطاقة منتج"),
            "explain": L("Variables make the program easy to read and to change. Change the quantity and run again.",
                         "Les variables rendent le programme facile à lire et à modifier. Change la quantité et relance.",
                         "المتغيرات تجعل البرنامج سهل القراءة والتعديل. غيّر الكمية وأعد التشغيل."),
            "code": '''product = "Laptop"
unit_price = 85000
quantity = 3

total = unit_price * quantity
print("Product:", product)
print("Quantity:", quantity)
print("Total:", total, "DZD")
''',
        },
    ],

    "exercises": [
        {
            "title": L("My first variables", "Mes premières variables", "متغيراتي الأولى"),
            "task": L("Create `name = \"Sara\"` and `age = 19`, then display them with **one** `print()`. Expected: `Sara 19`",
                      "Crée `name = \"Sara\"` et `age = 19`, puis affiche-les avec **un seul** `print()`. Attendu : `Sara 19`",
                      "أنشئ `name = \"Sara\"` و`age = 19` ثم اعرضهما بـ `print()` **واحدة**. المنتظر: `Sara 19`"),
            "starter": "# Create the two variables\n\n\n# Display them\n",
            "expected": "Sara 19",
            "hint": L("`print(name, age)`", "`print(name, age)`", "`print(name, age)`"),
            "solution": 'name = "Sara"\nage = 19\nprint(name, age)\n',
        },
        {
            "title": L("What type is it?", "Quel est le type ?", "ما هو النوع؟"),
            "task": L("Display the type of the value `3.5`.", "Affiche le type de la valeur `3.5`.", "اعرض نوع القيمة `3.5`."),
            "starter": "# Use type() inside print()\n",
            "expected": "<class 'float'>",
            "hint": L("`print(type(3.5))`", "`print(type(3.5))`", "`print(type(3.5))`"),
            "solution": "print(type(3.5))\n",
        },
        {
            "title": L("The bill", "La facture", "الفاتورة"),
            "task": L("A notebook costs **1200** DZD. A student buys **3**. Store them in `price` and `quantity`, compute `total`, then display it.",
                      "Un cahier coûte **1200** DA. Un étudiant en achète **3**. Range-les dans `price` et `quantity`, calcule `total`, puis affiche-le.",
                      "ثمن الكراس **1200** دج. اشترى طالب **3** كراريس. ضعهما في `price` و`quantity`، واحسب `total` ثم اعرضه."),
            "starter": "price = \nquantity = \n\ntotal = \nprint(total)\n",
            "expected": "3600",
            "hint": L("`total = price * quantity`", "`total = price * quantity`", "`total = price * quantity`"),
            "solution": "price = 1200\nquantity = 3\n\ntotal = price * quantity\nprint(total)\n",
        },
    ],

    "quiz": [
        {"q": L("In `price = 2500`, what does `=` mean?", "Dans `price = 2500`, que veut dire `=` ?", "في `price = 2500`، ماذا تعني `=`؟"),
         "options": L(["Put the value 2500 in price", "Compare price and 2500", "Add 2500", "Display 2500"],
                      ["Mettre la valeur 2500 dans price", "Comparer price et 2500", "Ajouter 2500", "Afficher 2500"],
                      ["ضع القيمة 2500 في price", "قارن price و2500", "أضف 2500", "اعرض 2500"]),
         "answer": 0,
         "explain": L("`=` puts a value in a variable.", "`=` met une valeur dans une variable.", "`=` تضع قيمة في متغير.")},
        {"q": L("What is the type of `0.19`?", "Quel est le type de `0.19` ?", "ما نوع `0.19`؟"),
         "options": ["int", "str", "float", "bool"], "answer": 2,
         "explain": L("A number with a dot is a `float`.", "Un nombre avec un point est un `float`.", "العدد الذي فيه نقطة هو `float`.")},
        {"q": L("What is the type of `\"2026\"`?", "Quel est le type de `\"2026\"` ?", "ما نوع `\"2026\"`؟"),
         "options": ["int", "str", "float", "bool"], "answer": 1,
         "explain": L("With quotes, it is a text (`str`), even if it contains numbers.",
                      "Avec des guillemets, c'est un texte (`str`), même s'il contient des chiffres.",
                      "مع علامات التنصيص هو نص (`str`) حتى لو احتوى على أرقام.")},
        {"q": L("Which variable name is correct?", "Quel nom de variable est correct ?", "أي اسم متغير صحيح؟"),
         "options": ["2total", "unit price", "unit_price", "total-2"], "answer": 2,
         "explain": L("No number at the start, no space, no `-`.", "Pas de chiffre au début, pas d'espace, pas de `-`.",
                      "لا رقم في البداية، ولا مسافة، ولا `-`.")},
        {"q": L("`stock = 40` then `stock = 35`. What does `print(stock)` display?",
                "`stock = 40` puis `stock = 35`. Qu'affiche `print(stock)` ?", "`stock = 40` ثم `stock = 35`. ماذا تعرض `print(stock)`؟"),
         "options": ["40", "75", "35", "40 35"], "answer": 2,
         "explain": L("The new value replaces the old one.", "La nouvelle valeur remplace l'ancienne.", "القيمة الجديدة تعوّض القديمة.")},
        {"q": L("Which values are of type `bool`?", "Quelles valeurs sont de type `bool` ?", "ما القيم من نوع `bool`؟"),
         "options": ["\"yes\" / \"no\"", "1 / 0", "True / False", "on / off"], "answer": 2,
         "explain": L("A `bool` is `True` or `False` (with a capital letter).", "Un `bool` vaut `True` ou `False` (avec une majuscule).",
                      "`bool` قيمته `True` أو `False` (بحرف كبير).")},
    ],
}
