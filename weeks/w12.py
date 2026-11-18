"""
WEEK 12 · Object-oriented programming (OOP)  (level: very easy)
Programme: classes and objects · attributes and methods · applied example: a financial company model.
"""
from syllabus import L

WEEK = {
    "objectives": L(
        [
            "**Explain** the difference between a **class** (the model) and an **object** (a real example).",
            "**Create** a class with `__init__` and **attributes**.",
            "**Add** a **method** (a function inside the class).",
            "**Create** several objects from the same class.",
            "**Model** a company with its revenue, costs and profit.",
        ],
        [
            "**Expliquer** la différence entre une **classe** (le modèle) et un **objet** (un exemple réel).",
            "**Créer** une classe avec `__init__` et des **attributs**.",
            "**Ajouter** une **méthode** (une fonction dans la classe).",
            "**Créer** plusieurs objets à partir de la même classe.",
            "**Modéliser** une entreprise avec ses recettes, ses coûts et son bénéfice.",
        ],
        [
            "**يشرح** الفرق بين **الفئة** (النموذج) و**الكائن** (مثال حقيقي).",
            "**ينشئ** فئة بـ `__init__` و**خصائص**.",
            "**يضيف** **طريقة** (دالة داخل الفئة).",
            "**ينشئ** عدة كائنات من الفئة نفسها.",
            "**ينمذج** شركة بمداخيلها وتكاليفها وربحها.",
        ],
    ),

    "lesson": L(
r'''
### 1. Class and object: the mould and the cakes
- A **class** is a **model** (a mould).
- An **object** is a **real thing** made from the model (a cake).

Example: the class `Company` describes what every company has. "Sonatrach", "Cevital" or "My Shop" are **objects**.

### 2. Attributes and methods
| | Meaning | Company example |
|---|---|---|
| **Attribute** | what the object **has** (data) | name, revenue, costs |
| **Method** | what the object **does** (function) | compute the profit |

### 3. Writing a class
```python
class Company:
    def __init__(self, name, revenue, costs):
        self.name = name
        self.revenue = revenue
        self.costs = costs
```
- `class` + name (with a capital letter) + `:`
- `__init__` runs automatically when we create an object. It fills the attributes.
- `self` means **"this object"**.

### 4. Creating objects
```python
shop = Company("My Shop", 800000, 650000)
print(shop.name)        # My Shop
print(shop.revenue)     # 800000
```
We read an attribute with a **dot**: `object.attribute`.

### 5. Adding a method
```python
class Company:
    def __init__(self, name, revenue, costs):
        self.name = name
        self.revenue = revenue
        self.costs = costs

    def profit(self):
        return self.revenue - self.costs

shop = Company("My Shop", 800000, 650000)
print(shop.profit())    # 150000
```
A method always receives `self` first. We call it with brackets: `shop.profit()`.

### 6. Many objects, one model
```python
a = Company("Alpha", 500000, 420000)
b = Company("Beta", 900000, 950000)
print(a.profit())       # 80000
print(b.profit())       # -50000  (a loss)
```

> **Remember:** class = model; object = real example; attribute = data; method = action.
''',
r'''
### 1. Classe et objet : le moule et les gâteaux
- Une **classe** est un **modèle** (un moule).
- Un **objet** est une **chose réelle** fabriquée à partir du modèle (un gâteau).

Exemple : la classe `Company` décrit ce que possède toute entreprise. « Sonatrach », « Cevital » ou « Mon magasin » sont des **objets**.

### 2. Attributs et méthodes
| | Signification | Exemple entreprise |
|---|---|---|
| **Attribut** | ce que l'objet **possède** (données) | nom, recettes, coûts |
| **Méthode** | ce que l'objet **fait** (fonction) | calculer le bénéfice |

### 3. Écrire une classe
```python
class Company:
    def __init__(self, name, revenue, costs):
        self.name = name
        self.revenue = revenue
        self.costs = costs
```
- `class` + nom (avec une majuscule) + `:`
- `__init__` s'exécute automatiquement à la création d'un objet. Elle remplit les attributs.
- `self` veut dire **« cet objet »**.

### 4. Créer des objets
```python
shop = Company("My Shop", 800000, 650000)
print(shop.name)        # My Shop
print(shop.revenue)     # 800000
```
On lit un attribut avec un **point** : `objet.attribut`.

### 5. Ajouter une méthode
```python
class Company:
    def __init__(self, name, revenue, costs):
        self.name = name
        self.revenue = revenue
        self.costs = costs

    def profit(self):
        return self.revenue - self.costs

shop = Company("My Shop", 800000, 650000)
print(shop.profit())    # 150000
```
Une méthode reçoit toujours `self` en premier. On l'appelle avec des parenthèses : `shop.profit()`.

### 6. Plusieurs objets, un seul modèle
```python
a = Company("Alpha", 500000, 420000)
b = Company("Beta", 900000, 950000)
print(a.profit())       # 80000
print(b.profit())       # -50000  (une perte)
```

> **À retenir :** classe = modèle ; objet = exemple réel ; attribut = donnée ; méthode = action.
''',
r'''
### 1. الفئة والكائن: القالب والحلويات
- **الفئة** (class) هي **نموذج** (قالب).
- **الكائن** (object) هو **شيء حقيقي** مصنوع من النموذج (قطعة حلوى).

مثال: الفئة `Company` تصف ما تملكه كل شركة. و«سوناطراك» و«سيفيتال» و«متجري» هي **كائنات**.

### 2. الخصائص والطرق
| | المعنى | مثال الشركة |
|---|---|---|
| **الخاصية** | ما **يملكه** الكائن (بيانات) | الاسم، المداخيل، التكاليف |
| **الطريقة** | ما **يفعله** الكائن (دالة) | حساب الربح |

### 3. كتابة فئة
```python
class Company:
    def __init__(self, name, revenue, costs):
        self.name = name
        self.revenue = revenue
        self.costs = costs
```
- `class` + الاسم (بحرف كبير) + `:`
- `__init__` تُنفَّذ تلقائياً عند إنشاء كائن، وتملأ الخصائص.
- `self` تعني **«هذا الكائن»**.

### 4. إنشاء كائنات
```python
shop = Company("My Shop", 800000, 650000)
print(shop.name)        # My Shop
print(shop.revenue)     # 800000
```
نقرأ الخاصية **بنقطة**: `object.attribute`.

### 5. إضافة طريقة
```python
class Company:
    def __init__(self, name, revenue, costs):
        self.name = name
        self.revenue = revenue
        self.costs = costs

    def profit(self):
        return self.revenue - self.costs

shop = Company("My Shop", 800000, 650000)
print(shop.profit())    # 150000
```
تستقبل الطريقة دائماً `self` أولاً، ونستدعيها بالأقواس: `shop.profit()`.

### 6. كائنات كثيرة ونموذج واحد
```python
a = Company("Alpha", 500000, 420000)
b = Company("Beta", 900000, 950000)
print(a.profit())       # 80000
print(b.profit())       # -50000  (a loss)
```

> **تذكّر:** الفئة = نموذج، الكائن = مثال حقيقي، الخاصية = بيانات، الطريقة = إجراء.
'''),

    "examples": [
        {
            "title": L("The Company model", "Le modèle Company", "نموذج الشركة"),
            "explain": L("One class, two companies. Each object keeps its own data.",
                         "Une classe, deux entreprises. Chaque objet garde ses propres données.",
                         "فئة واحدة وشركتان، وكل كائن يحتفظ ببياناته."),
            "code": '''class Company:
    def __init__(self, name, revenue, costs):
        self.name = name
        self.revenue = revenue
        self.costs = costs

    def profit(self):
        return self.revenue - self.costs

a = Company("Alpha", 500000, 420000)
b = Company("Beta", 900000, 950000)

print(a.name, "profit:", a.profit())
print(b.name, "profit:", b.profit())
''',
        },
        {
            "title": L("More methods: margin and status", "Plus de méthodes : marge et situation", "طرق إضافية: الهامش والوضعية"),
            "explain": L("A method can use another method and take a decision.",
                         "Une méthode peut utiliser une autre méthode et prendre une décision.",
                         "يمكن لطريقة أن تستعمل طريقة أخرى وأن تتخذ قراراً."),
            "code": '''class Company:
    def __init__(self, name, revenue, costs):
        self.name = name
        self.revenue = revenue
        self.costs = costs

    def profit(self):
        return self.revenue - self.costs

    def margin(self):
        return round(self.profit() / self.revenue * 100, 1)

    def status(self):
        if self.profit() >= 0:
            return "profitable"
        return "in loss"

c = Company("PyDZ Shop", 800000, 650000)
print(c.name, "-", c.status(), "- margin:", c.margin(), "%")
''',
        },
        {
            "title": L("A bank account that changes", "Un compte bancaire qui change", "حساب بنكي يتغيّر"),
            "explain": L("Methods can change the attributes: deposit and withdraw money.",
                         "Les méthodes peuvent modifier les attributs : déposer et retirer de l'argent.",
                         "يمكن للطرق أن تغيّر الخصائص: إيداع المال وسحبه."),
            "code": '''class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Not enough money!")

acc = Account("Sara", 10000)
acc.deposit(5000)
acc.withdraw(3000)
acc.withdraw(50000)
print(acc.owner, "has", acc.balance, "DZD")
''',
        },
    ],

    "exercises": [
        {
            "title": L("Create an object", "Crée un objet", "أنشئ كائناً"),
            "task": L('Create a product `p` named `"Phone"` with the price `45000`, then display its price.',
                      'Crée un produit `p` nommé `"Phone"` au prix de `45000`, puis affiche son prix.',
                      'أنشئ منتجاً `p` اسمه `"Phone"` وسعره `45000` ثم اعرض سعره.'),
            "starter": 'class Product:\n    def __init__(self, name, price):\n        self.name = name\n        self.price = price\n\n# create p, then display p.price\n',
            "expected": "45000",
            "hint": L('`p = Product("Phone", 45000)` then `print(p.price)`', '`p = Product("Phone", 45000)` puis `print(p.price)`',
                      '`p = Product("Phone", 45000)` ثم `print(p.price)`'),
            "solution": 'class Product:\n    def __init__(self, name, price):\n        self.name = name\n        self.price = price\n\np = Product("Phone", 45000)\nprint(p.price)\n',
        },
        {
            "title": L("Value of the stock", "Valeur du stock", "قيمة المخزون"),
            "task": L("Complete the method `total_value()` so it returns price × quantity. The program displays the value of 20 chairs at 3500 DZD.",
                      "Complète la méthode `total_value()` pour qu'elle renvoie prix × quantité. Le programme affiche la valeur de 20 chaises à 3500 DA.",
                      "أكمل الطريقة `total_value()` حتى تُرجع السعر × الكمية. يعرض البرنامج قيمة 20 كرسياً بسعر 3500 دج."),
            "starter": 'class Item:\n    def __init__(self, price, quantity):\n        self.price = price\n        self.quantity = quantity\n\n    def total_value(self):\n        return ...\n\nchairs = Item(3500, 20)\nprint(chairs.total_value())\n',
            "expected": "70000",
            "hint": L("`return self.price * self.quantity` (do not forget `self.`)", "`return self.price * self.quantity` (n'oublie pas `self.`)",
                      "`return self.price * self.quantity` (لا تنسَ `self.`)"),
            "solution": 'class Item:\n    def __init__(self, price, quantity):\n        self.price = price\n        self.quantity = quantity\n\n    def total_value(self):\n        return self.price * self.quantity\n\nchairs = Item(3500, 20)\nprint(chairs.total_value())\n',
        },
        {
            "title": L("The financial company", "L'entreprise financière", "الشركة المالية"),
            "task": L("Add a method `profit()` to `Company` (revenue − costs). Display the profit of a company with revenue 1200000 and costs 950000.",
                      "Ajoute une méthode `profit()` à `Company` (recettes − coûts). Affiche le bénéfice d'une entreprise avec 1200000 de recettes et 950000 de coûts.",
                      "أضف طريقة `profit()` إلى `Company` (المداخيل − التكاليف). اعرض ربح شركة مداخيلها 1200000 وتكاليفها 950000."),
            "starter": 'class Company:\n    def __init__(self, name, revenue, costs):\n        self.name = name\n        self.revenue = revenue\n        self.costs = costs\n\n    # add the method profit here\n\nc = Company("Delta", 1200000, 950000)\nprint(c.profit())\n',
            "expected": "250000",
            "hint": L("`def profit(self):` then `return self.revenue - self.costs`", "`def profit(self):` puis `return self.revenue - self.costs`",
                      "`def profit(self):` ثم `return self.revenue - self.costs`"),
            "solution": 'class Company:\n    def __init__(self, name, revenue, costs):\n        self.name = name\n        self.revenue = revenue\n        self.costs = costs\n\n    def profit(self):\n        return self.revenue - self.costs\n\nc = Company("Delta", 1200000, 950000)\nprint(c.profit())\n',
        },
    ],

    "quiz": [
        {"q": L("A class is…", "Une classe est…", "الفئة هي…"),
         "options": L(["A model to create objects", "A list of numbers", "An error", "A file"],
                      ["Un modèle pour créer des objets", "Une liste de nombres", "Une erreur", "Un fichier"],
                      ["نموذج لإنشاء الكائنات", "قائمة أعداد", "خطأ", "ملف"]),
         "answer": 0,
         "explain": L("Like a mould; objects are made from it.", "Comme un moule ; on fabrique des objets à partir d'elle.",
                      "مثل القالب، نصنع منه الكائنات.")},
        {"q": L("In a `Company` object, `revenue` is…", "Dans un objet `Company`, `revenue` est…", "في كائن `Company`، `revenue` هي…"),
         "options": L(["a method", "an attribute", "a class", "a loop"], ["une méthode", "un attribut", "une classe", "une boucle"],
                      ["طريقة", "خاصية", "فئة", "حلقة"]),
         "answer": 1,
         "explain": L("It is data that the object has.", "C'est une donnée que l'objet possède.", "إنها بيانات يملكها الكائن.")},
        {"q": L("When does `__init__` run?", "Quand `__init__` s'exécute-t-elle ?", "متى تُنفَّذ `__init__`؟"),
         "options": L(["When the object is created", "Never", "At the end of the program", "Only when we print"],
                      ["À la création de l'objet", "Jamais", "À la fin du programme", "Seulement quand on affiche"],
                      ["عند إنشاء الكائن", "أبداً", "في نهاية البرنامج", "عند العرض فقط"]),
         "answer": 0,
         "explain": L("It fills the attributes of the new object.", "Elle remplit les attributs du nouvel objet.", "تملأ خصائص الكائن الجديد.")},
        {"q": L("What does `self` mean?", "Que veut dire `self` ?", "ماذا تعني `self`؟"),
         "options": L(["The class name", "This object", "The computer", "The user"], ["Le nom de la classe", "Cet objet", "L'ordinateur", "L'utilisateur"],
                      ["اسم الفئة", "هذا الكائن", "الحاسوب", "المستخدم"]),
         "answer": 1,
         "explain": L("`self` is the object we are working on.", "`self` est l'objet sur lequel on travaille.", "`self` هو الكائن الذي نعمل عليه.")},
        {"q": L("How do you call the method `profit` of the object `c`?", "Comment appeler la méthode `profit` de l'objet `c` ?",
                "كيف نستدعي الطريقة `profit` للكائن `c`؟"),
         "options": ["profit(c)", "c.profit", "c.profit()", "Company.profit"], "answer": 2,
         "explain": L("Object, dot, method name and brackets.", "Objet, point, nom de la méthode et parenthèses.", "الكائن ثم نقطة ثم اسم الطريقة والأقواس.")},
        {"q": L("revenue = 500000, costs = 600000. `profit()` returns…", "recettes = 500000, coûts = 600000. `profit()` renvoie…",
                "المداخيل = 500000 والتكاليف = 600000. `profit()` تُرجع…"),
         "options": ["100000", "-100000", "1100000", "0"], "answer": 1,
         "explain": L("500000 − 600000 = −100000: a loss.", "500000 − 600000 = −100000 : une perte.", "500000 − 600000 = −100000: خسارة.")},
    ],
}
