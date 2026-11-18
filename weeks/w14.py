"""
WEEK 14 · Working with files  (level: very easy)
Programme: opening, reading and writing text files · saving and reading economic data.
"""
from syllabus import L

WEEK = {
    "objectives": L(
        [
            "**Explain** why we save data in a file.",
            "**Open** a file with `open()` and the modes `w`, `a`, `r`.",
            "**Write** in a file and **read** it again.",
            "**Use** `with`, which closes the file automatically.",
            "**Save** and **read** simple economic data (one value per line, CSV).",
        ],
        [
            "**Expliquer** pourquoi on enregistre des données dans un fichier.",
            "**Ouvrir** un fichier avec `open()` et les modes `w`, `a`, `r`.",
            "**Écrire** dans un fichier et le **relire**.",
            "**Utiliser** `with`, qui ferme le fichier automatiquement.",
            "**Enregistrer** et **lire** des données économiques simples (une valeur par ligne, CSV).",
        ],
        [
            "**يشرح** سبب حفظ البيانات في ملف.",
            "**يفتح** ملفاً بـ `open()` والأنماط `w` و`a` و`r`.",
            "**يكتب** في ملف ثم **يقرؤه** من جديد.",
            "**يستعمل** `with` التي تغلق الملف تلقائياً.",
            "**يحفظ** و**يقرأ** بيانات اقتصادية بسيطة (قيمة في كل سطر، CSV).",
        ],
    ),

    "lesson": L(
r'''
### 1. Why files?
When the program stops, the variables **disappear**. A **file** keeps the data: we can open it tomorrow, send it, or open it in Excel.

### 2. Opening a file: the 3 modes
```python
open("sales.txt", "w")
```
| Mode | Meaning | Careful |
|---|---|---|
| `"w"` | **write** | creates the file, or **erases** the old content |
| `"a"` | **add** (append) | writes at the end, keeps the old content |
| `"r"` | **read** | the file must exist |

### 3. Writing with `with`
```python
with open("sales.txt", "w") as f:
    f.write("Sales: 5000\n")
    f.write("Costs: 3200\n")
```
- `f` is the name we give to the open file.
- `\n` means **new line**.
- `write()` writes only **text**: use `str(5000)` for a number.
- `with` **closes** the file automatically at the end. 👍

### 4. Reading
```python
with open("sales.txt", "r") as f:
    content = f.read()
print(content)
```
Reading **line by line**:
```python
with open("sales.txt", "r") as f:
    for line in f:
        print(line.strip())     # strip() removes the \n
```

### 5. Adding without erasing
```python
with open("sales.txt", "a") as f:
    f.write("Profit: 1800\n")
```

### 6. Economic data: the CSV format
**CSV** = values separated by **commas**. Excel opens it directly.
```
month,sales
Jan,182000
Feb,165500
```
Reading and computing the total:
```python
total = 0
with open("sales.csv", "r") as f:
    next(f)                         # skip the header line
    for line in f:
        month, amount = line.strip().split(",")
        total = total + int(amount)
print(total)
```
💡 What we read from a file is **text**: `int()` or `float()` turns it into a number.

> **Remember:** `w` erases, `a` adds, `r` reads, and `with` closes the file for you.
''',
r'''
### 1. Pourquoi des fichiers ?
Quand le programme s'arrête, les variables **disparaissent**. Un **fichier** garde les données : on peut l'ouvrir demain, l'envoyer, ou l'ouvrir dans Excel.

### 2. Ouvrir un fichier : les 3 modes
```python
open("sales.txt", "w")
```
| Mode | Signification | Attention |
|---|---|---|
| `"w"` | **écrire** | crée le fichier, ou **efface** l'ancien contenu |
| `"a"` | **ajouter** (append) | écrit à la fin, garde l'ancien contenu |
| `"r"` | **lire** | le fichier doit exister |

### 3. Écrire avec `with`
```python
with open("sales.txt", "w") as f:
    f.write("Sales: 5000\n")
    f.write("Costs: 3200\n")
```
- `f` est le nom qu'on donne au fichier ouvert.
- `\n` veut dire **retour à la ligne**.
- `write()` n'écrit que du **texte** : utilise `str(5000)` pour un nombre.
- `with` **ferme** le fichier automatiquement à la fin. 👍

### 4. Lire
```python
with open("sales.txt", "r") as f:
    content = f.read()
print(content)
```
Lire **ligne par ligne** :
```python
with open("sales.txt", "r") as f:
    for line in f:
        print(line.strip())     # strip() enlève le \n
```

### 5. Ajouter sans effacer
```python
with open("sales.txt", "a") as f:
    f.write("Profit: 1800\n")
```

### 6. Données économiques : le format CSV
**CSV** = des valeurs séparées par des **virgules**. Excel l'ouvre directement.
```
month,sales
Jan,182000
Feb,165500
```
Lire et calculer le total :
```python
total = 0
with open("sales.csv", "r") as f:
    next(f)                         # sauter la ligne d'en-tête
    for line in f:
        month, amount = line.strip().split(",")
        total = total + int(amount)
print(total)
```
💡 Ce qu'on lit dans un fichier est du **texte** : `int()` ou `float()` le transforme en nombre.

> **À retenir :** `w` efface, `a` ajoute, `r` lit, et `with` ferme le fichier pour toi.
''',
r'''
### 1. لماذا الملفات؟
عندما يتوقف البرنامج **تختفي** المتغيرات. أما **الملف** فيحفظ البيانات: يمكن فتحه غداً أو إرساله أو فتحه في Excel.

### 2. فتح ملف: الأنماط الثلاثة
```python
open("sales.txt", "w")
```
| النمط | المعنى | انتبه |
|---|---|---|
| `"w"` | **كتابة** | ينشئ الملف، أو **يمسح** المحتوى القديم |
| `"a"` | **إضافة** | يكتب في النهاية ويحتفظ بالمحتوى القديم |
| `"r"` | **قراءة** | يجب أن يكون الملف موجوداً |

### 3. الكتابة باستعمال `with`
```python
with open("sales.txt", "w") as f:
    f.write("Sales: 5000\n")
    f.write("Costs: 3200\n")
```
- `f` هو الاسم الذي نعطيه للملف المفتوح.
- `\n` تعني **سطراً جديداً**.
- `write()` تكتب **نصوصاً** فقط: استعمل `str(5000)` للعدد.
- `with` **تغلق** الملف تلقائياً في النهاية. 👍

### 4. القراءة
```python
with open("sales.txt", "r") as f:
    content = f.read()
print(content)
```
القراءة **سطراً بسطر**:
```python
with open("sales.txt", "r") as f:
    for line in f:
        print(line.strip())     # strip() removes the \n
```

### 5. الإضافة دون مسح
```python
with open("sales.txt", "a") as f:
    f.write("Profit: 1800\n")
```

### 6. البيانات الاقتصادية: صيغة CSV
**CSV** = قيم مفصولة **بفواصل**، ويفتحها Excel مباشرة.
```
month,sales
Jan,182000
Feb,165500
```
القراءة وحساب المجموع:
```python
total = 0
with open("sales.csv", "r") as f:
    next(f)                         # skip the header line
    for line in f:
        month, amount = line.strip().split(",")
        total = total + int(amount)
print(total)
```
💡 ما نقرؤه من الملف هو **نص**: `int()` أو `float()` تحوّله إلى عدد.

> **تذكّر:** `w` تمسح، و`a` تضيف، و`r` تقرأ، و`with` تغلق الملف بدلاً منك.
'''),

    "examples": [
        {
            "title": L("Write, then read", "Écrire, puis lire", "اكتب ثم اقرأ"),
            "explain": L("We create a small report in a file, then we read it back.",
                         "On crée un petit rapport dans un fichier, puis on le relit.",
                         "ننشئ تقريراً صغيراً في ملف ثم نقرؤه من جديد."),
            "code": '''with open("report.txt", "w") as f:
    f.write("Sales: 5000\\n")
    f.write("Costs: 3200\\n")

with open("report.txt", "r") as f:
    print(f.read())
''',
        },
        {
            "title": L("Add without erasing", "Ajouter sans effacer", "الإضافة دون مسح"),
            "explain": L("Mode `a` adds a line each day. Then we count the lines.",
                         "Le mode `a` ajoute une ligne chaque jour. Ensuite on compte les lignes.",
                         "النمط `a` يضيف سطراً كل يوم، ثم نعدّ الأسطر."),
            "code": '''with open("journal.txt", "w") as f:
    f.write("Day 1: 3200 DZD\\n")

with open("journal.txt", "a") as f:
    f.write("Day 2: 4100 DZD\\n")
    f.write("Day 3: 2800 DZD\\n")

with open("journal.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    print(line.strip())
print("Number of days:", len(lines))
''',
        },
        {
            "title": L("A CSV file of sales", "Un fichier CSV de ventes", "ملف CSV للمبيعات"),
            "explain": L("We save the monthly sales in CSV (Excel can open it), then we read it and compute the total and the average.",
                         "On enregistre les ventes mensuelles en CSV (Excel peut l'ouvrir), puis on le lit et on calcule le total et la moyenne.",
                         "نحفظ المبيعات الشهرية بصيغة CSV (يفتحها Excel)، ثم نقرؤها ونحسب المجموع والمتوسط."),
            "code": '''months = ["Jan", "Feb", "Mar"]
sales = [182000, 165500, 210300]

with open("sales.csv", "w") as f:
    f.write("month,sales\\n")
    for i in range(len(months)):
        f.write(months[i] + "," + str(sales[i]) + "\\n")

total = 0
count = 0
with open("sales.csv", "r") as f:
    next(f)                              # skip the header
    for line in f:
        month, amount = line.strip().split(",")
        total = total + int(amount)
        count = count + 1

print("Total:", total)
print("Average:", round(total / count, 2))
''',
        },
    ],

    "exercises": [
        {
            "title": L("Save and read a line", "Enregistrer et lire une ligne", "احفظ سطراً واقرأه"),
            "task": L("Write `Sales: 5000` in the file `data.txt`, then read the file and display its content.",
                      "Écris `Sales: 5000` dans le fichier `data.txt`, puis lis le fichier et affiche son contenu.",
                      "اكتب `Sales: 5000` في الملف `data.txt` ثم اقرأ الملف واعرض محتواه."),
            "starter": 'with open("data.txt", "w") as f:\n    # write the line here\n\nwith open("data.txt", "r") as f:\n    print(f.read())\n',
            "expected": "Sales: 5000",
            "hint": L('`f.write("Sales: 5000")`', '`f.write("Sales: 5000")`', '`f.write("Sales: 5000")`'),
            "solution": 'with open("data.txt", "w") as f:\n    f.write("Sales: 5000")\n\nwith open("data.txt", "r") as f:\n    print(f.read())\n',
        },
        {
            "title": L("Count the lines", "Compte les lignes", "عدّ الأسطر"),
            "task": L("The program writes 2 lines. **Add** a third line `Mar 210300` with mode `a`, then the program displays the number of lines: `3`.",
                      "Le programme écrit 2 lignes. **Ajoute** une troisième ligne `Mar 210300` avec le mode `a` ; le programme affiche alors le nombre de lignes : `3`.",
                      "يكتب البرنامج سطرين. **أضف** سطراً ثالثاً `Mar 210300` بالنمط `a`، فيعرض البرنامج عدد الأسطر: `3`."),
            "starter": 'with open("sales.txt", "w") as f:\n    f.write("Jan 182000\\n")\n    f.write("Feb 165500\\n")\n\n# add the third line here with mode "a"\n\nwith open("sales.txt", "r") as f:\n    print(len(f.readlines()))\n',
            "expected": "3",
            "hint": L('`with open("sales.txt", "a") as f:` then `f.write("Mar 210300\\n")`',
                      '`with open("sales.txt", "a") as f:` puis `f.write("Mar 210300\\n")`',
                      '`with open("sales.txt", "a") as f:` ثم `f.write("Mar 210300\\n")`'),
            "solution": 'with open("sales.txt", "w") as f:\n    f.write("Jan 182000\\n")\n    f.write("Feb 165500\\n")\n\nwith open("sales.txt", "a") as f:\n    f.write("Mar 210300\\n")\n\nwith open("sales.txt", "r") as f:\n    print(len(f.readlines()))\n',
        },
        {
            "title": L("Total from a CSV", "Total d'un CSV", "مجموع من ملف CSV"),
            "task": L("The CSV file is ready. Complete the loop to add each amount to `total`, then display the total.",
                      "Le fichier CSV est prêt. Complète la boucle pour ajouter chaque montant à `total`, puis affiche le total.",
                      "ملف CSV جاهز. أكمل الحلقة لإضافة كل مبلغ إلى `total` ثم اعرض المجموع."),
            "starter": 'with open("costs.csv", "w") as f:\n    f.write("item,amount\\nrent,45000\\nsalaries,120000\\nenergy,15000\\n")\n\ntotal = 0\nwith open("costs.csv", "r") as f:\n    next(f)\n    for line in f:\n        item, amount = line.strip().split(",")\n        # add amount to total (it is a text!)\n\nprint(total)\n',
            "expected": "180000",
            "hint": L("`total = total + int(amount)`", "`total = total + int(amount)`", "`total = total + int(amount)`"),
            "solution": 'with open("costs.csv", "w") as f:\n    f.write("item,amount\\nrent,45000\\nsalaries,120000\\nenergy,15000\\n")\n\ntotal = 0\nwith open("costs.csv", "r") as f:\n    next(f)\n    for line in f:\n        item, amount = line.strip().split(",")\n        total = total + int(amount)\n\nprint(total)\n',
        },
    ],

    "quiz": [
        {"q": L("Which mode erases the old content of a file?", "Quel mode efface l'ancien contenu d'un fichier ?", "ما النمط الذي يمسح المحتوى القديم للملف؟"),
         "options": ['"r"', '"a"', '"w"', '"x"'], "answer": 2,
         "explain": L('`"w"` writes from zero.', '`"w"` écrit à partir de zéro.', '`"w"` يكتب من الصفر.')},
        {"q": L("Which mode adds at the end without erasing?", "Quel mode ajoute à la fin sans effacer ?", "ما النمط الذي يضيف في النهاية دون مسح؟"),
         "options": ['"a"', '"w"', '"r"', '"e"'], "answer": 0,
         "explain": L('`"a"` = append.', '`"a"` = append (ajouter).', '`"a"` = append (إضافة).')},
        {"q": L("What does `with` do for us?", "Que fait `with` pour nous ?", "ماذا تفعل `with` لنا؟"),
         "options": L(["It deletes the file", "It sorts the lines", "It closes the file automatically", "It prints the file"],
                      ["Elle supprime le fichier", "Elle trie les lignes", "Elle ferme le fichier automatiquement", "Elle affiche le fichier"],
                      ["تحذف الملف", "ترتّب الأسطر", "تغلق الملف تلقائياً", "تعرض الملف"]),
         "answer": 2,
         "explain": L("No need to call `close()`.", "Pas besoin d'appeler `close()`.", "لا حاجة لاستدعاء `close()`.")},
        {"q": L("What does `\\n` mean in a text?", "Que veut dire `\\n` dans un texte ?", "ماذا تعني `\\n` في النص؟"),
         "options": L(["Number", "New line", "Nothing", "End of the file"], ["Nombre", "Retour à la ligne", "Rien", "Fin du fichier"],
                      ["عدد", "سطر جديد", "لا شيء", "نهاية الملف"]),
         "answer": 1,
         "explain": L("It goes to the next line.", "Elle passe à la ligne suivante.", "تنتقل إلى السطر الموالي.")},
        {"q": L("We read `\"45000\"` from a file. How do we add it to a number?", "On lit `\"45000\"` dans un fichier. Comment l'ajouter à un nombre ?",
                "قرأنا `\"45000\"` من ملف. كيف نضيفه إلى عدد؟"),
         "options": ['total + "45000"', 'total + int("45000")', 'total + text("45000")', 'total & "45000"'], "answer": 1,
         "explain": L("A file gives text: `int()` turns it into a number.", "Un fichier donne du texte : `int()` le transforme en nombre.",
                      "الملف يعطي نصاً: `int()` تحوّله إلى عدد.")},
        {"q": L("In a CSV file, values are separated by…", "Dans un fichier CSV, les valeurs sont séparées par…", "في ملف CSV، تُفصل القيم بـ…"),
         "options": L(["stars", "brackets", "nothing", "commas"], ["des étoiles", "des parenthèses", "rien", "des virgules"],
                      ["نجوم", "أقواس", "لا شيء", "فواصل"]),
         "answer": 3,
         "explain": L("CSV = Comma-Separated Values.", "CSV = Comma-Separated Values (valeurs séparées par des virgules).",
                      "CSV = Comma-Separated Values (قيم مفصولة بفواصل).")},
    ],
}
