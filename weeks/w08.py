"""
WEEK 8 · Functions  (level: very easy)
Programme: defining and using functions · parameters and return values · functions for recurring problems.
"""
from syllabus import L

WEEK = {
    "objectives": L(
        [
            "**Explain** why we use functions.",
            "**Define** a function with `def` and **call** it.",
            "**Give** values to a function through **parameters**.",
            "**Get** a result back with `return`.",
            "**Build** small functions for economic calculations.",
        ],
        [
            "**Expliquer** pourquoi on utilise des fonctions.",
            "**Définir** une fonction avec `def` et l'**appeler**.",
            "**Donner** des valeurs à une fonction grâce aux **paramètres**.",
            "**Récupérer** un résultat avec `return`.",
            "**Construire** de petites fonctions pour des calculs économiques.",
        ],
        [
            "**يشرح** سبب استعمال الدوال.",
            "**يعرّف** دالة بواسطة `def` و**يستدعيها**.",
            "**يعطي** قيماً للدالة عبر **المعاملات**.",
            "**يسترجع** نتيجة بواسطة `return`.",
            "**يبني** دوالاً صغيرة للحسابات الاقتصادية.",
        ],
    ),

    "lesson": L(
r'''
### 1. Why functions?
You compute the VAT of many products. Instead of writing the same formula again and again, you write it **once** in a **function**, and you **use it** as many times as you want.

A function is like a **machine**: you put something in, it gives you a result.

### 2. Defining and calling
```python
def say_hello():
    print("Hello!")

say_hello()      # call
say_hello()      # call again
```
- `def` = **define** a function.
- Then the name, brackets `()` and `:`.
- The inside lines start with 4 spaces.
- The function works only when we **call** it: `say_hello()`.

### 3. Parameters: giving values
```python
def greet(name):
    print("Hello", name)

greet("Sara")     # Hello Sara
greet("Yacine")   # Hello Yacine
```
`name` is a **parameter**: a variable that receives the value we give.

### 4. return: giving back a result
```python
def vat(price):
    return price * 1.19

p = vat(1000)
print(p)          # 1190.0
```
- `return` **sends back** the result.
- We can keep it in a variable, or display it.

| print inside | return |
|---|---|
| only displays | gives a value we can reuse |

### 5. Several parameters
```python
def profit(revenue, costs):
    return revenue - costs

print(profit(80000, 55000))     # 25000
```
The values are given **in the same order** as the parameters.

### 6. Useful functions already in Python
`print()`, `len()`, `round()`, `sum()`, `max()`, `min()`, `type()`… are functions too!

> **Remember:** `def` name(parameters): → 4 spaces → `return` result.
''',
r'''
### 1. Pourquoi des fonctions ?
Tu calcules la TVA de nombreux produits. Au lieu d'écrire la même formule encore et encore, tu l'écris **une fois** dans une **fonction**, et tu l'**utilises** autant de fois que tu veux.

Une fonction est comme une **machine** : tu mets quelque chose dedans, elle te donne un résultat.

### 2. Définir et appeler
```python
def say_hello():
    print("Hello!")

say_hello()      # appel
say_hello()      # nouvel appel
```
- `def` = **définir** une fonction.
- Puis le nom, des parenthèses `()` et `:`.
- Les lignes à l'intérieur commencent par 4 espaces.
- La fonction ne travaille que quand on l'**appelle** : `say_hello()`.

### 3. Les paramètres : donner des valeurs
```python
def greet(name):
    print("Hello", name)

greet("Sara")     # Hello Sara
greet("Yacine")   # Hello Yacine
```
`name` est un **paramètre** : une variable qui reçoit la valeur qu'on donne.

### 4. return : rendre un résultat
```python
def vat(price):
    return price * 1.19

p = vat(1000)
print(p)          # 1190.0
```
- `return` **renvoie** le résultat.
- On peut le garder dans une variable, ou l'afficher.

| print à l'intérieur | return |
|---|---|
| affiche seulement | donne une valeur réutilisable |

### 5. Plusieurs paramètres
```python
def profit(revenue, costs):
    return revenue - costs

print(profit(80000, 55000))     # 25000
```
Les valeurs sont données **dans le même ordre** que les paramètres.

### 6. Des fonctions déjà présentes dans Python
`print()`, `len()`, `round()`, `sum()`, `max()`, `min()`, `type()`… sont aussi des fonctions !

> **À retenir :** `def` nom(paramètres): → 4 espaces → `return` résultat.
''',
r'''
### 1. لماذا الدوال؟
تحسب الرسم على القيمة المضافة لمنتجات كثيرة. بدل أن تكتب الصيغة نفسها مرات ومرات، تكتبها **مرة واحدة** في **دالة**، ثم **تستعملها** كلما أردت.

الدالة مثل **آلة**: تضع فيها شيئاً فتعطيك نتيجة.

### 2. التعريف والاستدعاء
```python
def say_hello():
    print("Hello!")

say_hello()      # call
say_hello()      # call again
```
- `def` = **عرّف** دالة.
- ثم الاسم، والقوسان `()` والنقطتان `:`.
- الأسطر بالداخل تبدأ بـ 4 مسافات.
- لا تعمل الدالة إلا عندما **نستدعيها**: `say_hello()`.

### 3. المعاملات: إعطاء قيم
```python
def greet(name):
    print("Hello", name)

greet("Sara")     # Hello Sara
greet("Yacine")   # Hello Yacine
```
`name` **معامل**: متغير يستقبل القيمة التي نعطيها.

### 4. return: إرجاع نتيجة
```python
def vat(price):
    return price * 1.19

p = vat(1000)
print(p)          # 1190.0
```
- `return` **تُرجع** النتيجة.
- يمكن حفظها في متغير أو عرضها.

| print بالداخل | return |
|---|---|
| تعرض فقط | تعطي قيمة يمكن إعادة استعمالها |

### 5. عدة معاملات
```python
def profit(revenue, costs):
    return revenue - costs

print(profit(80000, 55000))     # 25000
```
تُعطى القيم **بنفس ترتيب** المعاملات.

### 6. دوال موجودة مسبقاً في Python
`print()` و`len()` و`round()` و`sum()` و`max()` و`min()` و`type()`… كلها دوال أيضاً!

> **تذكّر:** `def` الاسم(المعاملات): ← 4 مسافات ← `return` النتيجة.
'''),

    "examples": [
        {
            "title": L("A VAT machine", "Une machine à TVA", "آلة لحساب الرسم"),
            "explain": L("One function, used for three products.", "Une seule fonction, utilisée pour trois produits.",
                         "دالة واحدة، تُستعمل لثلاثة منتجات."),
            "code": '''def vat(price):
    return price * 1.19

print("Book:", vat(1000))
print("Phone:", vat(45000))
print("Laptop:", vat(85000))
''',
        },
        {
            "title": L("Profit and margin", "Bénéfice et marge", "الربح والهامش"),
            "explain": L("Two functions with two parameters each. The margin uses the result of the profit.",
                         "Deux fonctions avec deux paramètres chacune. La marge utilise le résultat du bénéfice.",
                         "دالتان لكل منهما معاملان، والهامش يستعمل نتيجة الربح."),
            "code": '''def profit(revenue, costs):
    return revenue - costs

def margin(revenue, costs):
    return profit(revenue, costs) / revenue * 100

print("Profit:", profit(80000, 55000), "DZD")
print("Margin:", round(margin(80000, 55000), 1), "%")
''',
        },
        {
            "title": L("A function with a decision", "Une fonction avec une décision", "دالة فيها قرار"),
            "explain": L("A function can contain `if`. Try other marks.", "Une fonction peut contenir un `if`. Essaie d'autres notes.",
                         "يمكن للدالة أن تحتوي على `if`. جرّب علامات أخرى."),
            "code": '''def result(mark):
    if mark >= 10:
        return "Pass"
    else:
        return "Fail"

print(12, result(12))
print(8, result(8))
print(10, result(10))
''',
        },
    ],

    "exercises": [
        {
            "title": L("Price including VAT", "Prix TTC", "السعر بالرسم"),
            "task": L("Complete the function `vat(price)` so it **returns** the price × 1.19. The program displays `vat(1000)`.",
                      "Complète la fonction `vat(price)` pour qu'elle **renvoie** le prix × 1,19. Le programme affiche `vat(1000)`.",
                      "أكمل الدالة `vat(price)` حتى **تُرجع** السعر × 1.19. البرنامج يعرض `vat(1000)`."),
            "starter": "def vat(price):\n    # return the price with VAT\n\nprint(vat(1000))\n",
            "expected": "1190.0",
            "hint": L("`return price * 1.19`", "`return price * 1.19`", "`return price * 1.19`"),
            "solution": "def vat(price):\n    return price * 1.19\n\nprint(vat(1000))\n",
        },
        {
            "title": L("Average of 3 marks", "Moyenne de 3 notes", "معدل 3 علامات"),
            "task": L("Write a function `average(a, b, c)` that returns the average of three marks. Display `average(10, 14, 12)`.",
                      "Écris une fonction `average(a, b, c)` qui renvoie la moyenne de trois notes. Affiche `average(10, 14, 12)`.",
                      "اكتب دالة `average(a, b, c)` تُرجع معدل ثلاث علامات. اعرض `average(10, 14, 12)`."),
            "starter": "def average(a, b, c):\n    \n\nprint(average(10, 14, 12))\n",
            "expected": "12.0",
            "hint": L("`return (a + b + c) / 3`", "`return (a + b + c) / 3`", "`return (a + b + c) / 3`"),
            "solution": "def average(a, b, c):\n    return (a + b + c) / 3\n\nprint(average(10, 14, 12))\n",
        },
        {
            "title": L("Profit function", "Fonction bénéfice", "دالة الربح"),
            "task": L("Write `profit(revenue, costs)` that returns revenue − costs. Display `profit(80000, 55000)`.",
                      "Écris `profit(revenue, costs)` qui renvoie recettes − coûts. Affiche `profit(80000, 55000)`.",
                      "اكتب `profit(revenue, costs)` التي تُرجع المداخيل − التكاليف. اعرض `profit(80000, 55000)`."),
            "starter": "# define the function, then display the result\n",
            "expected": "25000",
            "hint": L("`def profit(revenue, costs):` then `return revenue - costs`", "`def profit(revenue, costs):` puis `return revenue - costs`",
                      "`def profit(revenue, costs):` ثم `return revenue - costs`"),
            "solution": "def profit(revenue, costs):\n    return revenue - costs\n\nprint(profit(80000, 55000))\n",
        },
    ],

    "quiz": [
        {"q": L("Which word defines a function?", "Quel mot définit une fonction ?", "ما الكلمة التي تعرّف دالة؟"),
         "options": ["function", "def", "define", "func"], "answer": 1,
         "explain": L("`def` starts a function.", "`def` commence une fonction.", "`def` تبدأ بها الدالة.")},
        {"q": L("When does the code inside a function run?", "Quand le code d'une fonction s'exécute-t-il ?", "متى يُنفَّذ الكود داخل الدالة؟"),
         "options": L(["When it is defined", "When it is called", "Never", "At the end of the program"],
                      ["Quand elle est définie", "Quand elle est appelée", "Jamais", "À la fin du programme"],
                      ["عند تعريفها", "عند استدعائها", "أبداً", "في نهاية البرنامج"]),
         "answer": 1,
         "explain": L("We must call it: `name()`.", "Il faut l'appeler : `name()`.", "يجب استدعاؤها: `name()`.")},
        {"q": L("What does `return` do?", "Que fait `return` ?", "ماذا تفعل `return`؟"),
         "options": L(["Displays a text", "Sends back a result", "Stops Python", "Deletes the function"],
                      ["Affiche un texte", "Renvoie un résultat", "Arrête Python", "Supprime la fonction"],
                      ["تعرض نصاً", "تُرجع نتيجة", "توقف Python", "تحذف الدالة"]),
         "answer": 1,
         "explain": L("`return` gives back a value we can reuse.", "`return` rend une valeur réutilisable.", "`return` تُرجع قيمة يمكن إعادة استعمالها.")},
        {"q": L("In `def vat(price):`, what is `price`?", "Dans `def vat(price):`, qu'est-ce que `price` ?", "في `def vat(price):` ما هو `price`؟"),
         "options": L(["A parameter", "A loop", "A library", "A comment"], ["Un paramètre", "Une boucle", "Une bibliothèque", "Un commentaire"],
                      ["معامل", "حلقة", "مكتبة", "تعليق"]),
         "answer": 0,
         "explain": L("It receives the value given when calling.", "Il reçoit la valeur donnée lors de l'appel.", "يستقبل القيمة المعطاة عند الاستدعاء.")},
        {"q": L("`def double(x): return x * 2`. What does `print(double(7))` display?",
                "`def double(x): return x * 2`. Qu'affiche `print(double(7))` ?", "`def double(x): return x * 2`. ماذا تعرض `print(double(7))`؟"),
         "options": ["7", "72", "9", "14"], "answer": 3,
         "explain": L("7 × 2 = 14.", "7 × 2 = 14.", "7 × 2 = 14.")},
        {"q": L("Which of these is a function already in Python?", "Laquelle est une fonction déjà présente dans Python ?",
                "أيّ مما يلي دالة موجودة مسبقاً في Python؟"),
         "options": ["vat()", "profit()", "len()", "average()"], "answer": 2,
         "explain": L("`len()` is built in; the others we write ourselves.", "`len()` est intégrée ; les autres, on les écrit nous-mêmes.",
                      "`len()` مدمجة، أما الأخرى فنكتبها بأنفسنا.")},
    ],
}
