"""
WEEK 10 · Lists and tuples  (level: very easy)
Programme: defining lists and tuples · operations on lists and iteration · storing economic data.
"""
from syllabus import L

WEEK = {
    "objectives": L(
        [
            "**Create** a list and **read** its values by position.",
            "**Add**, **change** and **remove** values in a list.",
            "**Use** `len()`, `sum()`, `max()`, `min()` and `sort()`.",
            "**Go through** a list with a `for` loop.",
            "**Know** the difference between a list and a tuple.",
        ],
        [
            "**Créer** une liste et **lire** ses valeurs par position.",
            "**Ajouter**, **modifier** et **supprimer** des valeurs dans une liste.",
            "**Utiliser** `len()`, `sum()`, `max()`, `min()` et `sort()`.",
            "**Parcourir** une liste avec une boucle `for`.",
            "**Connaître** la différence entre une liste et un tuple.",
        ],
        [
            "**ينشئ** قائمة و**يقرأ** قيمها حسب الموقع.",
            "**يضيف** و**يغيّر** و**يحذف** قيماً في القائمة.",
            "**يستعمل** `len()` و`sum()` و`max()` و`min()` و`sort()`.",
            "**يمرّ** على قائمة بحلقة `for`.",
            "**يعرف** الفرق بين القائمة والصف (tuple).",
        ],
    ),

    "lesson": L(
r'''
### 1. What is a list?
A **list** keeps **several values** in one variable, in order, between **square brackets** `[ ]`.
```python
sales = [120, 150, 90, 140]
months = ["Jan", "Feb", "Mar", "Apr"]
```

### 2. Reading a value
Like strings, positions start at **0**.
```python
print(sales[0])      # 120  (the first)
print(sales[-1])     # 140  (the last)
print(sales[1:3])    # [150, 90]
```

### 3. Changing a list
| Action | Code | Result |
|---|---|---|
| add at the end | `sales.append(200)` | `[120, 150, 90, 140, 200]` |
| change a value | `sales[0] = 125` | first value becomes 125 |
| remove a value | `sales.remove(90)` | 90 is removed |
| sort | `sales.sort()` | from small to big |

### 4. Quick calculations
```python
sales = [120, 150, 90, 140]
print(len(sales))    # 4    how many values
print(sum(sales))    # 500  total
print(max(sales))    # 150  biggest
print(min(sales))    # 90   smallest
print(sum(sales) / len(sales))   # 125.0  average
```

### 5. Going through a list
```python
for s in sales:
    print(s)
```
To have the position too, use `range(len(...))`:
```python
for i in range(len(months)):
    print(months[i], sales[i])
```

### 6. Tuples: lists that cannot change
A **tuple** uses **round brackets** `( )`. Once created, it **cannot be changed**.
```python
point = (2026, 3.5)       # (year, inflation %)
print(point[0])           # 2026
```
| List `[ ]` | Tuple `( )` |
|---|---|
| can change | cannot change |
| sales of the month | fixed data: a date, coordinates |

> **Remember:** list = `[ ]` and changeable; tuple = `( )` and fixed.
''',
r'''
### 1. Qu'est-ce qu'une liste ?
Une **liste** garde **plusieurs valeurs** dans une seule variable, dans l'ordre, entre **crochets** `[ ]`.
```python
sales = [120, 150, 90, 140]
months = ["Jan", "Feb", "Mar", "Apr"]
```

### 2. Lire une valeur
Comme pour les chaînes, les positions commencent à **0**.
```python
print(sales[0])      # 120  (la première)
print(sales[-1])     # 140  (la dernière)
print(sales[1:3])    # [150, 90]
```

### 3. Modifier une liste
| Action | Code | Résultat |
|---|---|---|
| ajouter à la fin | `sales.append(200)` | `[120, 150, 90, 140, 200]` |
| changer une valeur | `sales[0] = 125` | la première valeur devient 125 |
| supprimer une valeur | `sales.remove(90)` | 90 est supprimé |
| trier | `sales.sort()` | du plus petit au plus grand |

### 4. Calculs rapides
```python
sales = [120, 150, 90, 140]
print(len(sales))    # 4    combien de valeurs
print(sum(sales))    # 500  total
print(max(sales))    # 150  la plus grande
print(min(sales))    # 90   la plus petite
print(sum(sales) / len(sales))   # 125.0  moyenne
```

### 5. Parcourir une liste
```python
for s in sales:
    print(s)
```
Pour avoir aussi la position, utilise `range(len(...))` :
```python
for i in range(len(months)):
    print(months[i], sales[i])
```

### 6. Les tuples : des listes qui ne changent pas
Un **tuple** utilise des **parenthèses** `( )`. Une fois créé, il **ne peut plus être modifié**.
```python
point = (2026, 3.5)       # (année, inflation %)
print(point[0])           # 2026
```
| Liste `[ ]` | Tuple `( )` |
|---|---|
| peut changer | ne peut pas changer |
| ventes du mois | données fixes : une date, des coordonnées |

> **À retenir :** liste = `[ ]` et modifiable ; tuple = `( )` et fixe.
''',
r'''
### 1. ما هي القائمة؟
**القائمة** تحفظ **عدة قيم** في متغير واحد، بالترتيب، بين **قوسين مربعين** `[ ]`.
```python
sales = [120, 150, 90, 140]
months = ["Jan", "Feb", "Mar", "Apr"]
```

### 2. قراءة قيمة
كما في النصوص، تبدأ المواقع من **0**.
```python
print(sales[0])      # 120  (the first)
print(sales[-1])     # 140  (the last)
print(sales[1:3])    # [150, 90]
```

### 3. تعديل القائمة
| الإجراء | الكود | النتيجة |
|---|---|---|
| إضافة في النهاية | `sales.append(200)` | `[120, 150, 90, 140, 200]` |
| تغيير قيمة | `sales[0] = 125` | القيمة الأولى تصبح 125 |
| حذف قيمة | `sales.remove(90)` | تُحذف 90 |
| الترتيب | `sales.sort()` | من الأصغر إلى الأكبر |

### 4. حسابات سريعة
```python
sales = [120, 150, 90, 140]
print(len(sales))    # 4    how many values
print(sum(sales))    # 500  total
print(max(sales))    # 150  biggest
print(min(sales))    # 90   smallest
print(sum(sales) / len(sales))   # 125.0  average
```

### 5. المرور على القائمة
```python
for s in sales:
    print(s)
```
للحصول على الموقع أيضاً، استعمل `range(len(...))`:
```python
for i in range(len(months)):
    print(months[i], sales[i])
```

### 6. الصفوف (tuples): قوائم لا تتغيّر
**الصف** يستعمل **قوسين عاديين** `( )`، وبعد إنشائه **لا يمكن تعديله**.
```python
point = (2026, 3.5)       # (year, inflation %)
print(point[0])           # 2026
```
| القائمة `[ ]` | الصف `( )` |
|---|---|
| يمكن أن تتغيّر | لا يمكن أن يتغيّر |
| مبيعات الشهر | بيانات ثابتة: تاريخ، إحداثيات |

> **تذكّر:** القائمة = `[ ]` وقابلة للتعديل، والصف = `( )` وثابت.
'''),

    "examples": [
        {
            "title": L("A list of sales", "Une liste de ventes", "قائمة مبيعات"),
            "explain": L("Read, add and change values. Watch the list after each step.",
                         "Lire, ajouter et modifier des valeurs. Observe la liste après chaque étape.",
                         "قراءة القيم وإضافتها وتغييرها. لاحظ القائمة بعد كل خطوة."),
            "code": '''sales = [120, 150, 90, 140]
print("Start:", sales)
print("First month:", sales[0])

sales.append(200)        # a new month
print("After append:", sales)

sales[2] = 95            # correction of month 3
print("After correction:", sales)
''',
        },
        {
            "title": L("Statistics in one line each", "Des statistiques en une ligne chacune", "إحصاءات في سطر واحد لكل منها"),
            "explain": L("Algeria's GDP growth (%) for a few years (example values). Python computes in a second.",
                         "Croissance du PIB de l'Algérie (%) sur quelques années (valeurs d'exemple). Python calcule en une seconde.",
                         "نمو الناتج المحلي الإجمالي للجزائر (%) لعدة سنوات (قيم للتوضيح). تحسب Python في ثانية."),
            "code": '''growth = [1.0, -5.1, 3.4, 3.2, 4.1]   # example values

print("Number of years:", len(growth))
print("Highest:", max(growth))
print("Lowest:", min(growth))
print("Average:", round(sum(growth) / len(growth), 2))

growth.sort()
print("Sorted:", growth)
''',
        },
        {
            "title": L("Two lists side by side", "Deux listes côte à côte", "قائمتان جنباً إلى جنب"),
            "explain": L("`months[i]` and `sales[i]` go together. A tuple keeps fixed information.",
                         "`months[i]` et `sales[i]` vont ensemble. Un tuple garde une information fixe.",
                         "`months[i]` و`sales[i]` متلازمتان، والصف يحفظ معلومة ثابتة."),
            "code": '''months = ["Jan", "Feb", "Mar"]
sales = [182000, 165500, 210300]
shop = ("PyDZ Shop", "Boumerdes")      # tuple: fixed

print("Shop:", shop[0], "-", shop[1])
for i in range(len(months)):
    print(months[i], ":", sales[i], "DZD")
''',
        },
    ],

    "exercises": [
        {
            "title": L("Add a price", "Ajoute un prix", "أضف سعراً"),
            "task": L("Add `200` at the end of the list with `append()`, then display the list.",
                      "Ajoute `200` à la fin de la liste avec `append()`, puis affiche la liste.",
                      "أضف `200` في نهاية القائمة بـ `append()` ثم اعرض القائمة."),
            "starter": "prices = [120, 80, 150]\n\n",
            "expected": "[120, 80, 150, 200]",
            "hint": L("`prices.append(200)` then `print(prices)`", "`prices.append(200)` puis `print(prices)`", "`prices.append(200)` ثم `print(prices)`"),
            "solution": "prices = [120, 80, 150]\n\nprices.append(200)\nprint(prices)\n",
        },
        {
            "title": L("Highest and lowest", "Le plus haut et le plus bas", "الأعلى والأدنى"),
            "task": L("Display the highest and the lowest exchange rate with **one** `print()`.",
                      "Affiche le taux de change le plus haut et le plus bas avec **un seul** `print()`.",
                      "اعرض أعلى وأدنى سعر صرف بـ `print()` **واحدة**."),
            "starter": "rates = [134.2, 135.8, 133.9, 136.4]\n\n",
            "expected": "136.4 133.9",
            "hint": L("`print(max(rates), min(rates))`", "`print(max(rates), min(rates))`", "`print(max(rates), min(rates))`"),
            "solution": "rates = [134.2, 135.8, 133.9, 136.4]\n\nprint(max(rates), min(rates))\n",
        },
        {
            "title": L("Average of the exports", "Moyenne des exportations", "متوسط الصادرات"),
            "task": L("Display the average of the list `exports` (use `sum()` and `len()`).",
                      "Affiche la moyenne de la liste `exports` (utilise `sum()` et `len()`).",
                      "اعرض متوسط القائمة `exports` (استعمل `sum()` و`len()`)."),
            "starter": "exports = [40, 35, 50, 45]\n\n",
            "expected": "42.5",
            "hint": L("`sum(exports) / len(exports)`", "`sum(exports) / len(exports)`", "`sum(exports) / len(exports)`"),
            "solution": "exports = [40, 35, 50, 45]\n\nprint(sum(exports) / len(exports))\n",
        },
    ],

    "quiz": [
        {"q": L("Which brackets create a list?", "Quels signes créent une liste ?", "ما الأقواس التي تنشئ قائمة؟"),
         "options": ["( )", "[ ]", "{ }", "< >"], "answer": 1,
         "explain": L("Lists use square brackets `[ ]`.", "Les listes utilisent des crochets `[ ]`.", "القوائم تستعمل الأقواس المربعة `[ ]`.")},
        {"q": L("`sales = [10, 20, 30]`. What is `sales[1]`?", "`sales = [10, 20, 30]`. Que vaut `sales[1]` ?", "`sales = [10, 20, 30]`. ما قيمة `sales[1]`؟"),
         "options": ["10", "30", "20", "1"], "answer": 2,
         "explain": L("Positions start at 0: position 1 is the second value.", "Les positions commencent à 0 : la position 1 est la 2e valeur.",
                      "المواقع تبدأ من 0: الموقع 1 هو القيمة الثانية.")},
        {"q": L("Which instruction adds a value at the end?", "Quelle instruction ajoute une valeur à la fin ?", "ما التعليمة التي تضيف قيمة في النهاية؟"),
         "options": ["sales.add(5)", "sales.append(5)", "sales.push(5)", "sales + 5"], "answer": 1,
         "explain": L("`append()` adds at the end.", "`append()` ajoute à la fin.", "`append()` تضيف في النهاية.")},
        {"q": L("`sum([10, 20, 30])` gives…", "`sum([10, 20, 30])` donne…", "`sum([10, 20, 30])` تعطي…"),
         "options": ["3", "30", "60", "102030"], "answer": 2,
         "explain": L("10 + 20 + 30 = 60.", "10 + 20 + 30 = 60.", "10 + 20 + 30 = 60.")},
        {"q": L("What is special about a tuple?", "Qu'a de particulier un tuple ?", "ما الذي يميّز الصف (tuple)؟"),
         "options": L(["It cannot be changed", "It only holds text", "It is always empty", "It sorts itself"],
                      ["Il ne peut pas être modifié", "Il ne contient que du texte", "Il est toujours vide", "Il se trie tout seul"],
                      ["لا يمكن تعديله", "لا يحتوي إلا على نصوص", "يكون دائماً فارغاً", "يرتّب نفسه بنفسه"]),
         "answer": 0,
         "explain": L("A tuple is fixed once created.", "Un tuple est fixe une fois créé.", "الصف ثابت بعد إنشائه.")},
        {"q": L("`len([5, 8, 2, 7])` gives…", "`len([5, 8, 2, 7])` donne…", "`len([5, 8, 2, 7])` تعطي…"),
         "options": ["22", "8", "4", "7"], "answer": 2,
         "explain": L("There are 4 values.", "Il y a 4 valeurs.", "هناك 4 قيم.")},
    ],
}
