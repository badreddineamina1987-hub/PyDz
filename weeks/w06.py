"""
WEEK 6 · Program flow control: conditional statements  (level: very easy)
Programme: if, else, elif · logical operators (and, or, not) · practical exercises.
"""
from syllabus import L

WEEK = {
    "objectives": L(
        [
            "**Compare** two values with `==  !=  >  <  >=  <=`.",
            "**Write** a decision with `if` and `else`.",
            "**Handle** several cases with `elif`.",
            "**Combine** conditions with `and`, `or`, `not`.",
            "**Respect** the indentation (the spaces at the start of the line).",
        ],
        [
            "**Comparer** deux valeurs avec `==  !=  >  <  >=  <=`.",
            "**Écrire** une décision avec `if` et `else`.",
            "**Gérer** plusieurs cas avec `elif`.",
            "**Combiner** des conditions avec `and`, `or`, `not`.",
            "**Respecter** l'indentation (les espaces en début de ligne).",
        ],
        [
            "**يقارن** بين قيمتين بالرموز `==  !=  >  <  >=  <=`.",
            "**يكتب** قراراً بواسطة `if` و`else`.",
            "**يعالج** عدة حالات بواسطة `elif`.",
            "**يجمع** بين الشروط بواسطة `and` و`or` و`not`.",
            "**يحترم** الإزاحة (المسافات في بداية السطر).",
        ],
    ),

    "lesson": L(
r'''
### 1. Comparing
A comparison gives `True` or `False`.
| Sign | Meaning | Example | Result |
|---|---|---|---|
| `==` | equal | `5 == 5` | True |
| `!=` | different | `5 != 3` | True |
| `>` | greater | `5 > 3` | True |
| `<` | smaller | `5 < 3` | False |
| `>=` | greater or equal | `10 >= 10` | True |
| `<=` | smaller or equal | `9 <= 10` | True |

⚠️ `=` puts a value in a variable. `==` **compares**.

### 2. if … else
```python
mark = 12
if mark >= 10:
    print("Pass")
else:
    print("Fail")
```
- After the condition: **two points** `:`
- The lines inside start with **4 spaces** (indentation). This is how Python knows what belongs to `if`.

### 3. Several cases: elif
`elif` means "else if". Python tests from top to bottom and stops at the **first** true condition.
```python
mark = 15
if mark >= 16:
    print("Very good")
elif mark >= 14:
    print("Good")
elif mark >= 10:
    print("Pass")
else:
    print("Fail")
```
Result: `Good`

### 4. and, or, not
| Word | True when… | Example |
|---|---|---|
| `and` | **both** conditions are true | `age >= 18 and income >= 30000` |
| `or` | **at least one** is true | `day == "Fri" or day == "Sat"` |
| `not` | the condition is false | `not is_open` |

### 5. An economic example: a bank loan
```python
age = 25
income = 45000
if age >= 18 and income >= 30000:
    print("Loan accepted")
else:
    print("Loan refused")
```

> **Remember:** `if` condition `:` → 4 spaces → action.
''',
r'''
### 1. Comparer
Une comparaison donne `True` ou `False`.
| Signe | Signification | Exemple | Résultat |
|---|---|---|---|
| `==` | égal | `5 == 5` | True |
| `!=` | différent | `5 != 3` | True |
| `>` | plus grand | `5 > 3` | True |
| `<` | plus petit | `5 < 3` | False |
| `>=` | plus grand ou égal | `10 >= 10` | True |
| `<=` | plus petit ou égal | `9 <= 10` | True |

⚠️ `=` met une valeur dans une variable. `==` **compare**.

### 2. if … else
```python
mark = 12
if mark >= 10:
    print("Pass")
else:
    print("Fail")
```
- Après la condition : **deux-points** `:`
- Les lignes à l'intérieur commencent par **4 espaces** (indentation). C'est ainsi que Python sait ce qui appartient au `if`.

### 3. Plusieurs cas : elif
`elif` veut dire « sinon si ». Python teste de haut en bas et s'arrête à la **première** condition vraie.
```python
mark = 15
if mark >= 16:
    print("Very good")
elif mark >= 14:
    print("Good")
elif mark >= 10:
    print("Pass")
else:
    print("Fail")
```
Résultat : `Good`

### 4. and, or, not
| Mot | Vrai quand… | Exemple |
|---|---|---|
| `and` | les **deux** conditions sont vraies | `age >= 18 and income >= 30000` |
| `or` | **au moins une** est vraie | `day == "Fri" or day == "Sat"` |
| `not` | la condition est fausse | `not is_open` |

### 5. Un exemple économique : un prêt bancaire
```python
age = 25
income = 45000
if age >= 18 and income >= 30000:
    print("Loan accepted")
else:
    print("Loan refused")
```

> **À retenir :** `if` condition `:` → 4 espaces → action.
''',
r'''
### 1. المقارنة
تعطي المقارنة `True` أو `False`.
| الرمز | المعنى | مثال | النتيجة |
|---|---|---|---|
| `==` | يساوي | `5 == 5` | True |
| `!=` | يختلف عن | `5 != 3` | True |
| `>` | أكبر من | `5 > 3` | True |
| `<` | أصغر من | `5 < 3` | False |
| `>=` | أكبر من أو يساوي | `10 >= 10` | True |
| `<=` | أصغر من أو يساوي | `9 <= 10` | True |

⚠️ `=` تضع قيمة في متغير، أما `==` **فتقارن**.

### 2. if … else
```python
mark = 12
if mark >= 10:
    print("Pass")
else:
    print("Fail")
```
- بعد الشرط: **نقطتان** `:`
- الأسطر بالداخل تبدأ بـ **4 مسافات** (الإزاحة)، وبها تعرف Python ما الذي ينتمي إلى `if`.

### 3. عدة حالات: elif
`elif` تعني «وإلا إذا». تختبر Python من الأعلى إلى الأسفل وتتوقف عند **أول** شرط صحيح.
```python
mark = 15
if mark >= 16:
    print("Very good")
elif mark >= 14:
    print("Good")
elif mark >= 10:
    print("Pass")
else:
    print("Fail")
```
النتيجة: `Good`

### 4. and و or و not
| الكلمة | صحيح عندما… | مثال |
|---|---|---|
| `and` | يكون **الشرطان** صحيحين | `age >= 18 and income >= 30000` |
| `or` | يكون **أحدهما على الأقل** صحيحاً | `day == "Fri" or day == "Sat"` |
| `not` | يكون الشرط خاطئاً | `not is_open` |

### 5. مثال اقتصادي: قرض بنكي
```python
age = 25
income = 45000
if age >= 18 and income >= 30000:
    print("Loan accepted")
else:
    print("Loan refused")
```

> **تذكّر:** `if` الشرط `:` ← 4 مسافات ← الإجراء.
'''),

    "examples": [
        {
            "title": L("Pass or fail", "Admis ou ajourné", "ناجح أم راسب"),
            "explain": L("Try `mark = 9`, then `mark = 10`.", "Essaie `mark = 9`, puis `mark = 10`.", "جرّب `mark = 9` ثم `mark = 10`."),
            "code": '''mark = 12

if mark >= 10:
    print("Pass")
else:
    print("Fail")
''',
        },
        {
            "title": L("Several cases with elif", "Plusieurs cas avec elif", "عدة حالات مع elif"),
            "explain": L("A shop gives a discount depending on the amount of the purchase. Change `amount`.",
                         "Un magasin donne une remise selon le montant de l'achat. Change `amount`.",
                         "يمنح متجر تخفيضاً حسب مبلغ الشراء. غيّر `amount`."),
            "code": '''amount = 12000      # DZD

if amount >= 20000:
    discount = 0.10
elif amount >= 10000:
    discount = 0.05
else:
    discount = 0

print("Discount:", discount * 100, "%")
print("To pay:", amount * (1 - discount), "DZD")
''',
        },
        {
            "title": L("and / or", "and / or", "and / or"),
            "explain": L("The shop is open on working days, but closed on Friday **or** Saturday. Change the day.",
                         "Le magasin est ouvert en semaine, mais fermé le vendredi **ou** le samedi. Change le jour.",
                         "المتجر مفتوح في أيام العمل، ومغلق يوم الجمعة **أو** السبت. غيّر اليوم."),
            "code": '''day = "Friday"

if day == "Friday" or day == "Saturday":
    print("The shop is closed")
else:
    print("The shop is open")
''',
        },
    ],

    "exercises": [
        {
            "title": L("In stock?", "En stock ?", "متوفر في المخزون؟"),
            "task": L("If `quantity` is `0`, display `Out of stock`, otherwise display `Available`. Here `quantity = 0`.",
                      "Si `quantity` vaut `0`, affiche `Out of stock`, sinon affiche `Available`. Ici `quantity = 0`.",
                      "إذا كانت `quantity` تساوي `0` اعرض `Out of stock`، وإلا اعرض `Available`. هنا `quantity = 0`."),
            "starter": "quantity = 0\n\nif quantity == ...:\n    print(\"...\")\nelse:\n    print(\"...\")\n",
            "expected": "Out of stock",
            "hint": L("Compare with `==` (two signs).", "Compare avec `==` (deux signes).", "قارن بـ `==` (رمزان)."),
            "solution": 'quantity = 0\n\nif quantity == 0:\n    print("Out of stock")\nelse:\n    print("Available")\n',
        },
        {
            "title": L("The mention", "La mention", "التقدير"),
            "task": L("Complete with `elif`: 16 or more → `Very good`, 14 or more → `Good`, 10 or more → `Pass`, otherwise `Fail`. With `mark = 15`, it displays `Good`.",
                      "Complète avec `elif` : 16 ou plus → `Very good`, 14 ou plus → `Good`, 10 ou plus → `Pass`, sinon `Fail`. Avec `mark = 15`, on obtient `Good`.",
                      "أكمل بـ `elif`: 16 فأكثر ← `Very good`، 14 فأكثر ← `Good`، 10 فأكثر ← `Pass`، وإلا `Fail`. مع `mark = 15` نحصل على `Good`."),
            "starter": 'mark = 15\n\nif mark >= 16:\n    print("Very good")\n# add the other cases here\n',
            "expected": "Good",
            "hint": L("Add `elif mark >= 14:`, `elif mark >= 10:` and `else:`.", "Ajoute `elif mark >= 14:`, `elif mark >= 10:` et `else:`.",
                      "أضف `elif mark >= 14:` و`elif mark >= 10:` و`else:`."),
            "solution": 'mark = 15\n\nif mark >= 16:\n    print("Very good")\nelif mark >= 14:\n    print("Good")\nelif mark >= 10:\n    print("Pass")\nelse:\n    print("Fail")\n',
        },
        {
            "title": L("The bank loan", "Le prêt bancaire", "القرض البنكي"),
            "task": L("The loan is accepted if `age >= 18` **and** `income >= 30000`. Display `Loan accepted` or `Loan refused`.",
                      "Le prêt est accepté si `age >= 18` **et** `income >= 30000`. Affiche `Loan accepted` ou `Loan refused`.",
                      "يُقبل القرض إذا كان `age >= 18` **و** `income >= 30000`. اعرض `Loan accepted` أو `Loan refused`."),
            "starter": "age = 25\nincome = 45000\n\n",
            "expected": "Loan accepted",
            "hint": L("`if age >= 18 and income >= 30000:`", "`if age >= 18 and income >= 30000:`", "`if age >= 18 and income >= 30000:`"),
            "solution": 'age = 25\nincome = 45000\n\nif age >= 18 and income >= 30000:\n    print("Loan accepted")\nelse:\n    print("Loan refused")\n',
        },
    ],

    "quiz": [
        {"q": L("Which sign compares two values?", "Quel signe compare deux valeurs ?", "ما الرمز الذي يقارن بين قيمتين؟"),
         "options": ["=", "==", ":", "=>"], "answer": 1,
         "explain": L("`==` compares; `=` gives a value.", "`==` compare ; `=` donne une valeur.", "`==` تقارن، أما `=` فتعطي قيمة.")},
        {"q": L("What comes at the end of the `if` line?", "Que met-on à la fin de la ligne `if` ?", "ماذا نضع في نهاية سطر `if`؟"),
         "options": [";", ".", ":", ","], "answer": 2,
         "explain": L("Two points `:`, then the indented lines.", "Deux-points `:`, puis les lignes indentées.", "نقطتان `:` ثم الأسطر المُزاحة.")},
        {"q": L("`mark = 15`. Which message is displayed?\n`if mark >= 16: \"A\"` · `elif mark >= 14: \"B\"` · `elif mark >= 10: \"C\"`",
                "`mark = 15`. Quel message s'affiche ?\n`if mark >= 16: \"A\"` · `elif mark >= 14: \"B\"` · `elif mark >= 10: \"C\"`",
                "`mark = 15`. ما الرسالة المعروضة؟\n`if mark >= 16: \"A\"` · `elif mark >= 14: \"B\"` · `elif mark >= 10: \"C\"`"),
         "options": ["A", "B", "C", "B and C"], "answer": 1,
         "explain": L("Python stops at the first true condition: 15 >= 14.", "Python s'arrête à la première condition vraie : 15 >= 14.",
                      "تتوقف Python عند أول شرط صحيح: 15 >= 14.")},
        {"q": L("`True and False` gives…", "`True and False` donne…", "`True and False` تعطي…"),
         "options": ["True", "False"], "answer": 1,
         "explain": L("`and` needs both to be true.", "`and` demande que les deux soient vrais.", "`and` تتطلب أن يكون الاثنان صحيحين.")},
        {"q": L("`True or False` gives…", "`True or False` donne…", "`True or False` تعطي…"),
         "options": ["True", "False"], "answer": 0,
         "explain": L("`or` needs at least one true.", "`or` demande au moins un vrai.", "`or` تكفيها قيمة صحيحة واحدة.")},
        {"q": L("How many spaces start the lines inside an `if`?", "Combien d'espaces au début des lignes dans un `if` ?",
                "كم مسافة في بداية الأسطر داخل `if`؟"),
         "options": ["0", "1", "4", "10"], "answer": 2,
         "explain": L("The usual indentation is 4 spaces.", "L'indentation habituelle est de 4 espaces.", "الإزاحة المعتادة 4 مسافات.")},
    ],
}
