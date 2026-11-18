"""
WEEK 11 · Dictionaries and sets  (level: very easy)
Programme: the concept of dictionaries and sets · adding, deleting, searching · representing related data.
"""
from syllabus import L

WEEK = {
    "objectives": L(
        [
            "**Create** a dictionary of **keys** and **values**.",
            "**Read** a value with its key.",
            "**Add**, **change** and **delete** an entry.",
            "**Search** a key with `in` and **go through** a dictionary.",
            "**Remove** duplicates with a **set**.",
        ],
        [
            "**Créer** un dictionnaire de **clés** et de **valeurs**.",
            "**Lire** une valeur grâce à sa clé.",
            "**Ajouter**, **modifier** et **supprimer** une entrée.",
            "**Chercher** une clé avec `in` et **parcourir** un dictionnaire.",
            "**Supprimer** les doublons avec un **ensemble** (set).",
        ],
        [
            "**ينشئ** قاموساً من **المفاتيح** و**القيم**.",
            "**يقرأ** قيمة بواسطة مفتاحها.",
            "**يضيف** و**يغيّر** و**يحذف** عنصراً.",
            "**يبحث** عن مفتاح بـ `in` و**يمرّ** على القاموس.",
            "**يحذف** التكرارات باستعمال **مجموعة** (set).",
        ],
    ),

    "lesson": L(
r'''
### 1. What is a dictionary?
In a real dictionary, you look for a **word** to find its **meaning**. In Python, you look for a **key** to find its **value**.
```python
product = {"name": "Laptop", "price": 85000, "stock": 12}
```
- Curly brackets `{ }`
- Each entry: `key: value`
- Entries separated by commas

### 2. Reading a value
```python
print(product["price"])     # 85000
print(product["name"])      # Laptop
```
We use the **key**, not a position.

### 3. Adding, changing, deleting
| Action | Code |
|---|---|
| add | `product["brand"] = "Condor"` |
| change | `product["price"] = 80000` |
| delete | `del product["stock"]` |

### 4. Searching and going through
```python
if "price" in product:
    print("The price is known")

for key, value in product.items():
    print(key, ":", value)
```

### 5. Related data: a stock
A dictionary links information together:
```python
stock = {"apples": 50, "oranges": 30, "dates": 80}
print(stock["dates"])              # 80
print(sum(stock.values()))         # 160  total units
```

### 6. Sets: no duplicates
A **set** keeps each value **only once**.
```python
clients = ["Ali", "Sara", "Ali", "Omar", "Sara"]
unique = set(clients)
print(unique)            # {'Ali', 'Sara', 'Omar'}  (order may change)
print(len(unique))       # 3 different clients
```

| Type | Brackets | Example |
|---|---|---|
| list | `[ ]` | `[120, 150]` |
| tuple | `( )` | `(2026, 3.5)` |
| dictionary | `{ key: value }` | `{"price": 2500}` |
| set | `{ }` values only | `{"Ali", "Sara"}` |

> **Remember:** dictionary = key → value; set = no duplicates.
''',
r'''
### 1. Qu'est-ce qu'un dictionnaire ?
Dans un vrai dictionnaire, on cherche un **mot** pour trouver sa **définition**. En Python, on cherche une **clé** pour trouver sa **valeur**.
```python
product = {"name": "Laptop", "price": 85000, "stock": 12}
```
- Des accolades `{ }`
- Chaque entrée : `clé: valeur`
- Les entrées séparées par des virgules

### 2. Lire une valeur
```python
print(product["price"])     # 85000
print(product["name"])      # Laptop
```
On utilise la **clé**, pas une position.

### 3. Ajouter, modifier, supprimer
| Action | Code |
|---|---|
| ajouter | `product["brand"] = "Condor"` |
| modifier | `product["price"] = 80000` |
| supprimer | `del product["stock"]` |

### 4. Chercher et parcourir
```python
if "price" in product:
    print("The price is known")

for key, value in product.items():
    print(key, ":", value)
```

### 5. Des données liées : un stock
Un dictionnaire relie des informations entre elles :
```python
stock = {"apples": 50, "oranges": 30, "dates": 80}
print(stock["dates"])              # 80
print(sum(stock.values()))         # 160  unités au total
```

### 6. Les ensembles : pas de doublons
Un **ensemble** (set) garde chaque valeur **une seule fois**.
```python
clients = ["Ali", "Sara", "Ali", "Omar", "Sara"]
unique = set(clients)
print(unique)            # {'Ali', 'Sara', 'Omar'}  (l'ordre peut changer)
print(len(unique))       # 3 clients différents
```

| Type | Signes | Exemple |
|---|---|---|
| liste | `[ ]` | `[120, 150]` |
| tuple | `( )` | `(2026, 3.5)` |
| dictionnaire | `{ clé: valeur }` | `{"price": 2500}` |
| ensemble | `{ }` valeurs seules | `{"Ali", "Sara"}` |

> **À retenir :** dictionnaire = clé → valeur ; ensemble = pas de doublons.
''',
r'''
### 1. ما هو القاموس؟
في القاموس الحقيقي نبحث عن **كلمة** لنجد **معناها**. وفي Python نبحث عن **مفتاح** لنجد **قيمته**.
```python
product = {"name": "Laptop", "price": 85000, "stock": 12}
```
- أقواس معقوفة `{ }`
- كل عنصر: `مفتاح: قيمة`
- العناصر مفصولة بفواصل

### 2. قراءة قيمة
```python
print(product["price"])     # 85000
print(product["name"])      # Laptop
```
نستعمل **المفتاح** وليس الموقع.

### 3. الإضافة والتغيير والحذف
| الإجراء | الكود |
|---|---|
| إضافة | `product["brand"] = "Condor"` |
| تغيير | `product["price"] = 80000` |
| حذف | `del product["stock"]` |

### 4. البحث والمرور
```python
if "price" in product:
    print("The price is known")

for key, value in product.items():
    print(key, ":", value)
```

### 5. بيانات مترابطة: مخزون
يربط القاموس المعلومات ببعضها:
```python
stock = {"apples": 50, "oranges": 30, "dates": 80}
print(stock["dates"])              # 80
print(sum(stock.values()))         # 160  total units
```

### 6. المجموعات: دون تكرار
**المجموعة** (set) تحفظ كل قيمة **مرة واحدة فقط**.
```python
clients = ["Ali", "Sara", "Ali", "Omar", "Sara"]
unique = set(clients)
print(unique)            # {'Ali', 'Sara', 'Omar'}  (order may change)
print(len(unique))       # 3 different clients
```

| النوع | الأقواس | مثال |
|---|---|---|
| قائمة | `[ ]` | `[120, 150]` |
| صف | `( )` | `(2026, 3.5)` |
| قاموس | `{ key: value }` | `{"price": 2500}` |
| مجموعة | `{ }` قيم فقط | `{"Ali", "Sara"}` |

> **تذكّر:** القاموس = مفتاح ← قيمة، والمجموعة = دون تكرار.
'''),

    "examples": [
        {
            "title": L("A product card", "Une fiche produit", "بطاقة منتج"),
            "explain": L("Read, change and add information. Each piece of information has a clear name (the key).",
                         "Lire, modifier et ajouter des informations. Chaque information a un nom clair (la clé).",
                         "قراءة المعلومات وتغييرها وإضافتها. لكل معلومة اسم واضح (المفتاح)."),
            "code": '''product = {"name": "Laptop", "price": 85000, "stock": 12}

print("Price:", product["price"])
product["price"] = 80000          # promotion
product["brand"] = "Condor"       # new information
print(product)
''',
        },
        {
            "title": L("A shop's stock", "Le stock d'un magasin", "مخزون متجر"),
            "explain": L("We go through the dictionary and warn when the stock is low (less than 40).",
                         "On parcourt le dictionnaire et on prévient quand le stock est bas (moins de 40).",
                         "نمرّ على القاموس وننبّه عندما يكون المخزون منخفضاً (أقل من 40)."),
            "code": '''stock = {"apples": 50, "oranges": 30, "dates": 80, "figs": 15}

for fruit, qty in stock.items():
    if qty < 40:
        print(fruit, ":", qty, "-> order more!")
    else:
        print(fruit, ":", qty)

print("Total units:", sum(stock.values()))
''',
        },
        {
            "title": L("How many different clients?", "Combien de clients différents ?", "كم عدد الزبائن المختلفين؟"),
            "explain": L("The list has 7 purchases, but some clients came back. A set keeps each name once.",
                         "La liste contient 7 achats, mais certains clients sont revenus. Un ensemble garde chaque nom une fois.",
                         "تحتوي القائمة على 7 مشتريات، لكن بعض الزبائن عادوا. المجموعة تحفظ كل اسم مرة واحدة."),
            "code": '''purchases = ["Ali", "Sara", "Ali", "Omar", "Sara", "Lina", "Ali"]

clients = set(purchases)
print("Purchases:", len(purchases))
print("Different clients:", len(clients))
print("Is Lina a client?", "Lina" in clients)
''',
        },
    ],

    "exercises": [
        {
            "title": L("Read a price", "Lire un prix", "قراءة سعر"),
            "task": L("Display the price of the product, using its key.", "Affiche le prix du produit, grâce à sa clé.",
                      "اعرض سعر المنتج باستعمال مفتاحه."),
            "starter": 'product = {"name": "Laptop", "price": 95000}\n\n',
            "expected": "95000",
            "hint": L('`print(product["price"])`', '`print(product["price"])`', '`print(product["price"])`'),
            "solution": 'product = {"name": "Laptop", "price": 95000}\n\nprint(product["price"])\n',
        },
        {
            "title": L("Add a fruit", "Ajoute un fruit", "أضف فاكهة"),
            "task": L('Add `"oranges"` with the value `30` to the stock, then display the dictionary.',
                      'Ajoute `"oranges"` avec la valeur `30` au stock, puis affiche le dictionnaire.',
                      'أضف `"oranges"` بالقيمة `30` إلى المخزون ثم اعرض القاموس.'),
            "starter": 'stock = {"apples": 50}\n\n',
            "expected": "{'apples': 50, 'oranges': 30}",
            "hint": L('`stock["oranges"] = 30`', '`stock["oranges"] = 30`', '`stock["oranges"] = 30`'),
            "solution": 'stock = {"apples": 50}\n\nstock["oranges"] = 30\nprint(stock)\n',
        },
        {
            "title": L("Different clients", "Clients différents", "زبائن مختلفون"),
            "task": L("Display how many **different** clients there are in the list.",
                      "Affiche combien de clients **différents** il y a dans la liste.",
                      "اعرض عدد الزبائن **المختلفين** في القائمة."),
            "starter": 'clients = ["Ali", "Sara", "Ali", "Omar", "Sara"]\n\n',
            "expected": "3",
            "hint": L("`len(set(clients))`", "`len(set(clients))`", "`len(set(clients))`"),
            "solution": 'clients = ["Ali", "Sara", "Ali", "Omar", "Sara"]\n\nprint(len(set(clients)))\n',
        },
    ],

    "quiz": [
        {"q": L("In `{\"price\": 2500}`, what is `\"price\"`?", "Dans `{\"price\": 2500}`, qu'est-ce que `\"price\"` ?",
                "في `{\"price\": 2500}` ما هو `\"price\"`؟"),
         "options": L(["The key", "The value", "A list", "A function"], ["La clé", "La valeur", "Une liste", "Une fonction"],
                      ["المفتاح", "القيمة", "قائمة", "دالة"]),
         "answer": 0,
         "explain": L("`key: value` → \"price\" is the key, 2500 the value.", "`clé: valeur` → \"price\" est la clé, 2500 la valeur.",
                      "`مفتاح: قيمة` ← \"price\" هو المفتاح و2500 القيمة.")},
        {"q": L("How do you read the value of the key `\"name\"`?", "Comment lire la valeur de la clé `\"name\"` ?", "كيف نقرأ قيمة المفتاح `\"name\"`؟"),
         "options": ['product(name)', 'product["name"]', 'product[0]', 'product.name()'], "answer": 1,
         "explain": L("Square brackets with the key.", "Des crochets avec la clé.", "أقواس مربعة مع المفتاح.")},
        {"q": L("Which instruction deletes the key `\"stock\"`?", "Quelle instruction supprime la clé `\"stock\"` ?", "ما التعليمة التي تحذف المفتاح `\"stock\"`؟"),
         "options": ['remove product["stock"]', 'product["stock"] = 0', 'del product["stock"]', 'product.pop'], "answer": 2,
         "explain": L("`del` deletes an entry. Setting 0 only changes the value.", "`del` supprime une entrée. Mettre 0 change seulement la valeur.",
                      "`del` تحذف العنصر، أما وضع 0 فيغيّر القيمة فقط.")},
        {"q": L("`set([1, 2, 2, 3, 3, 3])` contains how many values?", "`set([1, 2, 2, 3, 3, 3])` contient combien de valeurs ?",
                "كم قيمة تحتوي `set([1, 2, 2, 3, 3, 3])`؟"),
         "options": ["6", "3", "2", "1"], "answer": 1,
         "explain": L("A set removes duplicates: {1, 2, 3}.", "Un ensemble supprime les doublons : {1, 2, 3}.", "المجموعة تحذف التكرار: {1, 2, 3}.")},
        {"q": L("How do you check if a key exists?", "Comment vérifier qu'une clé existe ?", "كيف نتحقق من وجود مفتاح؟"),
         "options": ['"price" in product', 'product.has("price")', 'exists(product, "price")', 'product == "price"'], "answer": 0,
         "explain": L("The word `in` searches among the keys.", "Le mot `in` cherche parmi les clés.", "الكلمة `in` تبحث بين المفاتيح.")},
        {"q": L("Best type to store each student's mark by name?", "Meilleur type pour stocker la note de chaque étudiant par nom ?",
                "ما أفضل نوع لتخزين علامة كل طالب حسب اسمه؟"),
         "options": L(["A dictionary", "A tuple", "A string", "A bool"], ["Un dictionnaire", "Un tuple", "Une chaîne", "Un bool"],
                      ["قاموس", "صف", "نص", "bool"]),
         "answer": 0,
         "explain": L("Name (key) → mark (value): `{\"Sara\": 15}`.", "Nom (clé) → note (valeur) : `{\"Sara\": 15}`.",
                      "الاسم (مفتاح) ← العلامة (قيمة): `{\"Sara\": 15}`.")},
    ],
}
