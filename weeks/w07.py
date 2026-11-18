"""
WEEK 7 · Loops  (level: very easy)
Programme: for and while · break, continue · practical uses such as computing averages.
"""
from syllabus import L

WEEK = {
    "objectives": L(
        [
            "**Repeat** an action with a `for` loop and `range()`.",
            "**Go through** a series of values with `for`.",
            "**Repeat** while a condition is true with `while`.",
            "**Stop** or **skip** a turn with `break` and `continue`.",
            "**Compute** a total and an average with a loop.",
        ],
        [
            "**Répéter** une action avec une boucle `for` et `range()`.",
            "**Parcourir** une série de valeurs avec `for`.",
            "**Répéter** tant qu'une condition est vraie avec `while`.",
            "**Arrêter** ou **sauter** un tour avec `break` et `continue`.",
            "**Calculer** un total et une moyenne avec une boucle.",
        ],
        [
            "**يكرّر** إجراءً بحلقة `for` و`range()`.",
            "**يمرّ** على سلسلة من القيم بواسطة `for`.",
            "**يكرّر** ما دام الشرط صحيحاً بواسطة `while`.",
            "**يوقف** الحلقة أو **يتخطّى** دورة بواسطة `break` و`continue`.",
            "**يحسب** مجموعاً ومتوسطاً باستعمال حلقة.",
        ],
    ),

    "lesson": L(
r'''
### 1. Why loops?
To display 1 to 100, we will not write 100 `print()`! A **loop** repeats the work for us.

### 2. The for loop with range()
```python
for n in range(1, 6):
    print(n)
```
Displays 1, 2, 3, 4, 5.
- `range(1, 6)` gives the numbers **from 1 to 5** (the last one, 6, is not included).
- `range(5)` gives 0, 1, 2, 3, 4.
- Like `if`: `:` at the end, and 4 spaces inside.

### 3. Going through a series of values
```python
sales = [120, 150, 90]
for s in sales:
    print(s)
```
`sales` is a **list** (we will study lists in week 10). The loop takes the values **one by one**.

### 4. Total and average: the accumulator
We start a **total at 0**, then we add each value.
```python
sales = [120, 150, 90, 140]
total = 0
for s in sales:
    total = total + s
average = total / len(sales)
print(total, average)          # 500 125.0
```
`len(sales)` = how many values (here 4).

### 5. The while loop
`while` repeats **as long as** the condition is true.
```python
savings = 1000
years = 0
while savings < 1500:
    savings = savings * 1.10
    years = years + 1
print(years)                    # 5
```
⚠️ Something must change inside, otherwise the loop never stops.

### 6. break and continue
- `break` → **stop** the loop now.
- `continue` → **skip** this turn and go to the next one.
```python
for n in range(1, 10):
    if n == 5:
        break
    print(n)                    # 1 2 3 4
```

> **Remember:** `for` when you know how many times; `while` when you wait for a condition.
''',
r'''
### 1. Pourquoi des boucles ?
Pour afficher de 1 à 100, on ne va pas écrire 100 `print()` ! Une **boucle** répète le travail pour nous.

### 2. La boucle for avec range()
```python
for n in range(1, 6):
    print(n)
```
Affiche 1, 2, 3, 4, 5.
- `range(1, 6)` donne les nombres **de 1 à 5** (le dernier, 6, n'est pas inclus).
- `range(5)` donne 0, 1, 2, 3, 4.
- Comme `if` : `:` à la fin, et 4 espaces à l'intérieur.

### 3. Parcourir une série de valeurs
```python
sales = [120, 150, 90]
for s in sales:
    print(s)
```
`sales` est une **liste** (nous étudierons les listes en semaine 10). La boucle prend les valeurs **une par une**.

### 4. Total et moyenne : l'accumulateur
On commence avec un **total à 0**, puis on ajoute chaque valeur.
```python
sales = [120, 150, 90, 140]
total = 0
for s in sales:
    total = total + s
average = total / len(sales)
print(total, average)          # 500 125.0
```
`len(sales)` = combien de valeurs (ici 4).

### 5. La boucle while
`while` répète **tant que** la condition est vraie.
```python
savings = 1000
years = 0
while savings < 1500:
    savings = savings * 1.10
    years = years + 1
print(years)                    # 5
```
⚠️ Quelque chose doit changer à l'intérieur, sinon la boucle ne s'arrête jamais.

### 6. break et continue
- `break` → **arrêter** la boucle tout de suite.
- `continue` → **sauter** ce tour et passer au suivant.
```python
for n in range(1, 10):
    if n == 5:
        break
    print(n)                    # 1 2 3 4
```

> **À retenir :** `for` quand on sait combien de fois ; `while` quand on attend une condition.
''',
r'''
### 1. لماذا الحلقات؟
لعرض الأعداد من 1 إلى 100 لن نكتب 100 تعليمة `print()`! **الحلقة** تكرّر العمل بدلاً منا.

### 2. حلقة for مع range()
```python
for n in range(1, 6):
    print(n)
```
تعرض 1، 2، 3، 4، 5.
- `range(1, 6)` تعطي الأعداد **من 1 إلى 5** (العدد الأخير 6 غير مشمول).
- `range(5)` تعطي 0، 1، 2، 3، 4.
- مثل `if`: النقطتان `:` في النهاية، و4 مسافات بالداخل.

### 3. المرور على سلسلة من القيم
```python
sales = [120, 150, 90]
for s in sales:
    print(s)
```
`sales` هي **قائمة** (سندرس القوائم في الأسبوع 10). تأخذ الحلقة القيم **واحدة تلو الأخرى**.

### 4. المجموع والمتوسط: المُراكِم
نبدأ **بمجموع يساوي 0** ثم نضيف كل قيمة.
```python
sales = [120, 150, 90, 140]
total = 0
for s in sales:
    total = total + s
average = total / len(sales)
print(total, average)          # 500 125.0
```
`len(sales)` = عدد القيم (هنا 4).

### 5. حلقة while
`while` تكرّر **ما دام** الشرط صحيحاً.
```python
savings = 1000
years = 0
while savings < 1500:
    savings = savings * 1.10
    years = years + 1
print(years)                    # 5
```
⚠️ يجب أن يتغيّر شيء ما بالداخل، وإلا فلن تتوقف الحلقة أبداً.

### 6. break و continue
- `break` ← **أوقف** الحلقة فوراً.
- `continue` ← **تخطَّ** هذه الدورة وانتقل إلى التالية.
```python
for n in range(1, 10):
    if n == 5:
        break
    print(n)                    # 1 2 3 4
```

> **تذكّر:** `for` عندما نعرف عدد المرات، و`while` عندما ننتظر تحقق شرط.
'''),

    "examples": [
        {
            "title": L("Monthly payments", "Les mensualités", "الأقساط الشهرية"),
            "explain": L("A student pays 2500 DZD per month for 6 months. The loop writes each month and the amount paid so far.",
                         "Un étudiant paie 2500 DA par mois pendant 6 mois. La boucle écrit chaque mois et le montant déjà payé.",
                         "يدفع طالب 2500 دج شهرياً لمدة 6 أشهر. تكتب الحلقة كل شهر والمبلغ المدفوع حتى الآن."),
            "code": '''monthly = 2500
paid = 0
for month in range(1, 7):
    paid = paid + monthly
    print("Month", month, "- paid so far:", paid, "DZD")
''',
        },
        {
            "title": L("Average of the sales", "Moyenne des ventes", "متوسط المبيعات"),
            "explain": L("The accumulator `total` starts at 0 and grows at each turn. Add a value to the list and run again.",
                         "L'accumulateur `total` commence à 0 et grandit à chaque tour. Ajoute une valeur à la liste et relance.",
                         "المُراكِم `total` يبدأ من 0 ويكبر في كل دورة. أضف قيمة إلى القائمة وأعد التشغيل."),
            "code": '''sales = [120, 150, 90, 140]

total = 0
for s in sales:
    total = total + s

print("Total:", total)
print("Average:", total / len(sales))
''',
        },
        {
            "title": L("Savings with while", "Une épargne avec while", "الادخار مع while"),
            "explain": L("How many years to go from 1000 to 1500 DZD with 10 % per year? The loop stops by itself.",
                         "Combien d'années pour passer de 1000 à 1500 DA avec 10 % par an ? La boucle s'arrête toute seule.",
                         "كم سنة نحتاج للانتقال من 1000 إلى 1500 دج بنسبة 10 % سنوياً؟ الحلقة تتوقف وحدها."),
            "code": '''savings = 1000
years = 0
while savings < 1500:
    savings = savings * 1.10
    years = years + 1
    print("Year", years, ":", round(savings, 2))

print("Goal reached after", years, "years")
''',
        },
    ],

    "exercises": [
        {
            "title": L("Count from 1 to 5", "Compter de 1 à 5", "العدّ من 1 إلى 5"),
            "task": L("Use a `for` loop to display the numbers 1 to 5, one per line.",
                      "Utilise une boucle `for` pour afficher les nombres de 1 à 5, un par ligne.",
                      "استعمل حلقة `for` لعرض الأعداد من 1 إلى 5، عدد في كل سطر."),
            "starter": "for n in range(...):\n    print(n)\n",
            "expected": "1\n2\n3\n4\n5",
            "hint": L("`range(1, 6)`: the last number is not included.", "`range(1, 6)` : le dernier nombre n'est pas inclus.",
                      "`range(1, 6)`: العدد الأخير غير مشمول."),
            "solution": "for n in range(1, 6):\n    print(n)\n",
        },
        {
            "title": L("Total of the week", "Total de la semaine", "مجموع الأسبوع"),
            "task": L("A shop's daily sales are in the list. Compute the total with a loop and display it.",
                      "Les ventes quotidiennes d'un magasin sont dans la liste. Calcule le total avec une boucle et affiche-le.",
                      "المبيعات اليومية لمتجر موجودة في القائمة. احسب المجموع بحلقة ثم اعرضه."),
            "starter": "sales = [3200, 4100, 2800, 5000, 3900]\n\ntotal = 0\nfor s in sales:\n    # add s to total\n\nprint(total)\n",
            "expected": "19000",
            "hint": L("Inside the loop: `total = total + s`", "Dans la boucle : `total = total + s`", "داخل الحلقة: `total = total + s`"),
            "solution": "sales = [3200, 4100, 2800, 5000, 3900]\n\ntotal = 0\nfor s in sales:\n    total = total + s\n\nprint(total)\n",
        },
        {
            "title": L("When will the price double?", "Quand le prix va-t-il doubler ?", "متى يتضاعف السعر؟"),
            "task": L("A price of **100** DZD increases by **20 %** each year. With a `while` loop, find how many years until it reaches **200** or more. Display the number of years.",
                      "Un prix de **100** DA augmente de **20 %** chaque année. Avec une boucle `while`, trouve combien d'années il faut pour atteindre **200** ou plus. Affiche le nombre d'années.",
                      "سعر **100** دج يرتفع بـ **20 %** كل سنة. باستعمال حلقة `while` جد عدد السنوات اللازمة ليبلغ **200** أو أكثر. اعرض عدد السنوات."),
            "starter": "price = 100\nyears = 0\n\nwhile price < 200:\n    # increase the price by 20 %\n    # add 1 to years\n\nprint(years)\n",
            "expected": "4",
            "hint": L("`price = price * 1.20` and `years = years + 1`", "`price = price * 1.20` et `years = years + 1`",
                      "`price = price * 1.20` و`years = years + 1`"),
            "solution": "price = 100\nyears = 0\n\nwhile price < 200:\n    price = price * 1.20\n    years = years + 1\n\nprint(years)\n",
        },
    ],

    "quiz": [
        {"q": L("Which numbers does `range(1, 4)` give?", "Quels nombres donne `range(1, 4)` ?", "ما الأعداد التي تعطيها `range(1, 4)`؟"),
         "options": ["1, 2, 3, 4", "0, 1, 2, 3", "4", "1, 2, 3"], "answer": 3,
         "explain": L("The last number (4) is not included.", "Le dernier nombre (4) n'est pas inclus.", "العدد الأخير (4) غير مشمول.")},
        {"q": L("Which numbers does `range(3)` give?", "Quels nombres donne `range(3)` ?", "ما الأعداد التي تعطيها `range(3)`؟"),
         "options": ["1, 2, 3", "0, 1, 2", "0, 1, 2, 3", "3"], "answer": 1,
         "explain": L("It starts at 0 and stops before 3.", "Elle commence à 0 et s'arrête avant 3.", "تبدأ من 0 وتتوقف قبل 3.")},
        {"q": L("To compute a total, the accumulator starts at…", "Pour calculer un total, l'accumulateur commence à…",
                "لحساب مجموع، يبدأ المُراكِم من…"),
         "options": L(["0", "1", "the first value", "100"], ["0", "1", "la première valeur", "100"], ["0", "1", "القيمة الأولى", "100"]),
         "answer": 0,
         "explain": L("We start at 0, then add each value.", "On part de 0, puis on ajoute chaque valeur.", "نبدأ من 0 ثم نضيف كل قيمة.")},
        {"q": L("`while` repeats…", "`while` répète…", "`while` تكرّر…"),
         "options": L(["exactly 10 times", "as long as the condition is true", "only once", "until the computer stops"],
                      ["exactement 10 fois", "tant que la condition est vraie", "une seule fois", "jusqu'à l'arrêt de l'ordinateur"],
                      ["10 مرات بالضبط", "ما دام الشرط صحيحاً", "مرة واحدة فقط", "إلى أن يتوقف الحاسوب"]),
         "answer": 1,
         "explain": L("The loop stops when the condition becomes false.", "La boucle s'arrête quand la condition devient fausse.",
                      "تتوقف الحلقة عندما يصبح الشرط خاطئاً.")},
        {"q": L("Which word stops a loop immediately?", "Quel mot arrête une boucle tout de suite ?", "ما الكلمة التي توقف الحلقة فوراً؟"),
         "options": ["continue", "stop", "break", "end"], "answer": 2,
         "explain": L("`break` stops; `continue` skips one turn.", "`break` arrête ; `continue` saute un tour.", "`break` توقف، و`continue` تتخطى دورة.")},
        {"q": L("`len([5, 8, 2])` gives…", "`len([5, 8, 2])` donne…", "`len([5, 8, 2])` تعطي…"),
         "options": ["15", "8", "2", "3"], "answer": 3,
         "explain": L("`len()` counts the values: there are 3.", "`len()` compte les valeurs : il y en a 3.", "`len()` تعدّ القيم: هناك 3.")},
    ],
}
