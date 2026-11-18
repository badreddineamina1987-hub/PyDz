"""
WEEK 5 · Arithmetic operations and mathematical functions  (level: very easy)
Programme: + - * / % · the math library · simple economic problems.
"""
from syllabus import L

WEEK = {
    "objectives": L(
        [
            "**Use** the operations `+  -  *  /  //  %  **`.",
            "**Know** the order of operations and use brackets.",
            "**Round** a result with `round()`.",
            "**Use** the `math` library (square root, etc.).",
            "**Solve** simple economic problems: VAT, discount, profit, interest.",
        ],
        [
            "**Utiliser** les opérations `+  -  *  /  //  %  **`.",
            "**Connaître** l'ordre des opérations et utiliser les parenthèses.",
            "**Arrondir** un résultat avec `round()`.",
            "**Utiliser** la bibliothèque `math` (racine carrée, etc.).",
            "**Résoudre** des problèmes économiques simples : TVA, remise, bénéfice, intérêts.",
        ],
        [
            "**يستعمل** العمليات `+  -  *  /  //  %  **`.",
            "**يعرف** أولوية العمليات ويستعمل الأقواس.",
            "**يقرّب** نتيجة بواسطة `round()`.",
            "**يستعمل** مكتبة `math` (الجذر التربيعي وغيره).",
            "**يحلّ** مسائل اقتصادية بسيطة: الرسم على القيمة المضافة، التخفيض، الربح، الفوائد.",
        ],
    ),

    "lesson": L(
r'''
### 1. The operations
| Sign | Operation | Example | Result |
|---|---|---|---|
| `+` | addition | `7 + 2` | 9 |
| `-` | subtraction | `7 - 2` | 5 |
| `*` | multiplication | `7 * 2` | 14 |
| `/` | division | `7 / 2` | 3.5 |
| `//` | whole division | `7 // 2` | 3 |
| `%` | remainder | `7 % 2` | 1 |
| `**` | power | `7 ** 2` | 49 |

💡 `/` always gives a decimal: `10 / 2` gives `5.0`.

### 2. The order of operations
Like in maths: first `**`, then `*` and `/`, then `+` and `-`.
```python
print(2 + 3 * 4)       # 14
print((2 + 3) * 4)     # 20
```
👉 When in doubt, use **brackets**.

### 3. Rounding
```python
print(round(2.6789, 2))    # 2.68  (2 decimals)
print(round(2.6789))       # 3     (no decimals)
```

### 4. The math library
A **library** is a box of ready-made tools. We open it with `import`.
```python
import math
print(math.sqrt(16))    # square root: 4.0
print(math.pi)          # 3.141592...
```

### 5. Economics with Python
**Price including VAT (19 %)**
```python
price = 2000
price_ttc = price * 1.19       # 2380.0
```
**Discount of 15 %**
```python
new_price = 4000 * (1 - 0.15)  # 3400.0
```
**Profit**
```python
profit = revenue - costs
```
**Growth rate (%)**
```python
growth = (new - old) / old * 100
```
**Compound interest:** capital × (1 + rate) ** years
```python
final = 100000 * (1 + 0.05) ** 3
```

> **Remember:** write the formula in words first, then translate it into Python.
''',
r'''
### 1. Les opérations
| Signe | Opération | Exemple | Résultat |
|---|---|---|---|
| `+` | addition | `7 + 2` | 9 |
| `-` | soustraction | `7 - 2` | 5 |
| `*` | multiplication | `7 * 2` | 14 |
| `/` | division | `7 / 2` | 3.5 |
| `//` | division entière | `7 // 2` | 3 |
| `%` | reste | `7 % 2` | 1 |
| `**` | puissance | `7 ** 2` | 49 |

💡 `/` donne toujours un décimal : `10 / 2` donne `5.0`.

### 2. L'ordre des opérations
Comme en maths : d'abord `**`, puis `*` et `/`, puis `+` et `-`.
```python
print(2 + 3 * 4)       # 14
print((2 + 3) * 4)     # 20
```
👉 En cas de doute, utilise des **parenthèses**.

### 3. Arrondir
```python
print(round(2.6789, 2))    # 2.68  (2 décimales)
print(round(2.6789))       # 3     (sans décimale)
```

### 4. La bibliothèque math
Une **bibliothèque** est une boîte d'outils prêts à l'emploi. On l'ouvre avec `import`.
```python
import math
print(math.sqrt(16))    # racine carrée : 4.0
print(math.pi)          # 3.141592...
```

### 5. L'économie avec Python
**Prix TTC (TVA 19 %)**
```python
price = 2000
price_ttc = price * 1.19       # 2380.0
```
**Remise de 15 %**
```python
new_price = 4000 * (1 - 0.15)  # 3400.0
```
**Bénéfice**
```python
profit = revenue - costs
```
**Taux de croissance (%)**
```python
growth = (new - old) / old * 100
```
**Intérêts composés :** capital × (1 + taux) ** années
```python
final = 100000 * (1 + 0.05) ** 3
```

> **À retenir :** écris d'abord la formule en mots, puis traduis-la en Python.
''',
r'''
### 1. العمليات
| الرمز | العملية | مثال | النتيجة |
|---|---|---|---|
| `+` | الجمع | `7 + 2` | 9 |
| `-` | الطرح | `7 - 2` | 5 |
| `*` | الضرب | `7 * 2` | 14 |
| `/` | القسمة | `7 / 2` | 3.5 |
| `//` | القسمة الصحيحة | `7 // 2` | 3 |
| `%` | باقي القسمة | `7 % 2` | 1 |
| `**` | القوة (الأس) | `7 ** 2` | 49 |

💡 `/` تعطي دائماً عدداً عشرياً: `10 / 2` تعطي `5.0`.

### 2. أولوية العمليات
كما في الرياضيات: أولاً `**`، ثم `*` و`/`، ثم `+` و`-`.
```python
print(2 + 3 * 4)       # 14
print((2 + 3) * 4)     # 20
```
👉 عند الشك، استعمل **الأقواس**.

### 3. التقريب
```python
print(round(2.6789, 2))    # 2.68  (2 decimals)
print(round(2.6789))       # 3     (no decimals)
```

### 4. مكتبة math
**المكتبة** صندوق أدوات جاهزة، نفتحه بالأمر `import`.
```python
import math
print(math.sqrt(16))    # square root: 4.0
print(math.pi)          # 3.141592...
```

### 5. الاقتصاد مع Python
**السعر بالرسم (TVA بنسبة 19 %)**
```python
price = 2000
price_ttc = price * 1.19       # 2380.0
```
**تخفيض بنسبة 15 %**
```python
new_price = 4000 * (1 - 0.15)  # 3400.0
```
**الربح**
```python
profit = revenue - costs
```
**معدل النمو (%)**
```python
growth = (new - old) / old * 100
```
**الفائدة المركّبة:** رأس المال × (1 + المعدل) ** عدد السنوات
```python
final = 100000 * (1 + 0.05) ** 3
```

> **تذكّر:** اكتب الصيغة بالكلمات أولاً، ثم ترجمها إلى Python.
'''),

    "examples": [
        {
            "title": L("The 7 operations", "Les 7 opérations", "العمليات السبع"),
            "explain": L("Change `a` and `b` and look at the results.", "Change `a` et `b` et observe les résultats.",
                         "غيّر `a` و`b` ولاحظ النتائج."),
            "code": '''a = 7
b = 2
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // b =", a // b)
print("a % b  =", a % b)
print("a ** b =", a ** b)
''',
        },
        {
            "title": L("VAT and discount", "TVA et remise", "الرسم والتخفيض"),
            "explain": L("A shop applies VAT, then a sale discount. Change the price or the rates.",
                         "Un magasin applique la TVA, puis une remise de soldes. Change le prix ou les taux.",
                         "يطبّق متجر الرسم على القيمة المضافة ثم تخفيضاً. غيّر السعر أو النسب."),
            "code": '''price_ht = 2000          # price before tax (DZD)
vat_rate = 0.19
discount = 0.15

price_ttc = price_ht * (1 + vat_rate)
sale_price = price_ttc * (1 - discount)

print("Price incl. VAT:", price_ttc)
print("Price after discount:", round(sale_price, 2))
''',
        },
        {
            "title": L("Savings with interest", "Une épargne avec intérêts", "ادخار بالفوائد"),
            "explain": L("100 000 DZD placed at 5 % per year. How much after 3 years? And after 10 years?",
                         "100 000 DA placés à 5 % par an. Combien après 3 ans ? Et après 10 ans ?",
                         "100000 دج مودعة بفائدة 5 % سنوياً. كم تصبح بعد 3 سنوات؟ وبعد 10 سنوات؟"),
            "code": '''capital = 100000
rate = 0.05
years = 3

final = capital * (1 + rate) ** years
print("After", years, "years:", round(final, 2), "DZD")
print("Interest earned:", round(final - capital, 2), "DZD")
''',
        },
    ],

    "exercises": [
        {
            "title": L("Price including VAT", "Prix TTC", "السعر بالرسم"),
            "task": L("A product costs **2000** DZD before tax. VAT is **19 %**. Display the price including VAT.",
                      "Un produit coûte **2000** DA hors taxe. La TVA est de **19 %**. Affiche le prix TTC.",
                      "ثمن منتج **2000** دج دون رسم. الرسم على القيمة المضافة **19 %**. اعرض السعر بالرسم."),
            "starter": "price = 2000\n\n# price including VAT = price * (1 + 0.19)\n",
            "expected": "2380.0",
            "hint": L("`print(price * 1.19)`", "`print(price * 1.19)`", "`print(price * 1.19)`"),
            "solution": "price = 2000\nprint(price * 1.19)\n",
        },
        {
            "title": L("The sales", "Les soldes", "التخفيضات"),
            "task": L("A jacket costs **4000** DZD. The discount is **15 %**. Display the new price.",
                      "Une veste coûte **4000** DA. La remise est de **15 %**. Affiche le nouveau prix.",
                      "ثمن سترة **4000** دج والتخفيض **15 %**. اعرض السعر الجديد."),
            "starter": "price = 4000\ndiscount = 0.15\n\n",
            "expected": "3400.0",
            "hint": L("`price * (1 - discount)`", "`price * (1 - discount)`", "`price * (1 - discount)`"),
            "solution": "price = 4000\ndiscount = 0.15\n\nprint(price * (1 - discount))\n",
        },
        {
            "title": L("Compound interest", "Intérêts composés", "الفائدة المركّبة"),
            "task": L("**100000** DZD at **5 %** per year for **3** years. Display the final amount rounded to 2 decimals.",
                      "**100000** DA à **5 %** par an pendant **3** ans. Affiche le montant final arrondi à 2 décimales.",
                      "**100000** دج بفائدة **5 %** سنوياً لمدة **3** سنوات. اعرض المبلغ النهائي مقرّباً إلى رقمين بعد الفاصلة."),
            "starter": "capital = 100000\nrate = 0.05\nyears = 3\n\n",
            "expected": "115762.5",
            "hint": L("`round(capital * (1 + rate) ** years, 2)`", "`round(capital * (1 + rate) ** years, 2)`",
                      "`round(capital * (1 + rate) ** years, 2)`"),
            "solution": "capital = 100000\nrate = 0.05\nyears = 3\n\nprint(round(capital * (1 + rate) ** years, 2))\n",
        },
    ],

    "quiz": [
        {"q": L("What does `7 // 2` give?", "Que donne `7 // 2` ?", "ماذا تعطي `7 // 2`؟"),
         "options": ["3.5", "3", "1", "14"], "answer": 1,
         "explain": L("`//` keeps only the whole part.", "`//` garde seulement la partie entière.", "`//` تحتفظ بالجزء الصحيح فقط.")},
        {"q": L("What does `7 % 2` give?", "Que donne `7 % 2` ?", "ماذا تعطي `7 % 2`؟"),
         "options": ["3", "0.07", "1", "3.5"], "answer": 2,
         "explain": L("`%` gives the remainder: 7 = 2 × 3 + **1**.", "`%` donne le reste : 7 = 2 × 3 + **1**.", "`%` تعطي الباقي: 7 = 2 × 3 + **1**.")},
        {"q": L("What does `2 + 3 * 4` give?", "Que donne `2 + 3 * 4` ?", "ماذا تعطي `2 + 3 * 4`؟"),
         "options": ["20", "14", "24", "9"], "answer": 1,
         "explain": L("Multiplication first: 3 × 4 = 12, then + 2.", "La multiplication d'abord : 3 × 4 = 12, puis + 2.",
                      "الضرب أولاً: 3 × 4 = 12، ثم + 2.")},
        {"q": L("How do you write 5 to the power 3?", "Comment écrire 5 puissance 3 ?", "كيف نكتب 5 أس 3؟"),
         "options": ["5 ^ 3", "5 ** 3", "5 * 3", "pow 5 3"], "answer": 1,
         "explain": L("The power sign is `**`.", "Le signe de puissance est `**`.", "رمز القوة هو `**`.")},
        {"q": L("Price 1000 DZD with 19 % VAT: which formula?", "Prix 1000 DA avec 19 % de TVA : quelle formule ?",
                "السعر 1000 دج مع رسم 19 %: ما الصيغة؟"),
         "options": ["1000 + 19", "1000 * 19", "1000 * 1.19", "1000 / 1.19"], "answer": 2,
         "explain": L("Adding 19 % = multiplying by 1.19.", "Ajouter 19 % = multiplier par 1,19.", "إضافة 19 % = الضرب في 1.19.")},
        {"q": L("What must we write before using `math.sqrt()`?", "Que faut-il écrire avant d'utiliser `math.sqrt()` ?",
                "ماذا يجب أن نكتب قبل استعمال `math.sqrt()`؟"),
         "options": ["open math", "import math", "use math", "math()"], "answer": 1,
         "explain": L("`import math` opens the library.", "`import math` ouvre la bibliothèque.", "`import math` تفتح المكتبة.")},
    ],
}
