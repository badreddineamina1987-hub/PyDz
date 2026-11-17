"""
WEEK 2 · Introduction to algorithms  (level: very easy)
"""
from syllabus import L

WEEK = {
    "objectives": L(
        [
            "**Say** what an algorithm is, in simple words.",
            "**Find** the input, the processing and the output of a problem.",
            "**Write** a short algorithm with the words START, READ, CALCULATE, DISPLAY, END.",
            "**Recognise** the 4 shapes of a flowchart.",
            "**Turn** a small algorithm into Python code.",
        ],
        [
            "**Dire** ce qu'est un algorithme, avec des mots simples.",
            "**Trouver** l'entrée, le traitement et la sortie d'un problème.",
            "**Écrire** un petit algorithme avec les mots DÉBUT, LIRE, CALCULER, AFFICHER, FIN.",
            "**Reconnaître** les 4 formes d'un organigramme.",
            "**Transformer** un petit algorithme en code Python.",
        ],
        [
            "**يقول** ما هي الخوارزمية بكلمات بسيطة.",
            "**يحدّد** المدخلات والمعالجة والمخرجات في مسألة.",
            "**يكتب** خوارزمية قصيرة بالكلمات: بداية، اقرأ، احسب، اعرض، نهاية.",
            "**يتعرّف** على الأشكال الأربعة للمخطط الانسيابي.",
            "**يحوّل** خوارزمية صغيرة إلى كود Python.",
        ],
    ),

    # ------------------------------------------------------------------ LESSON
    "lesson": L(
r'''
### 1. What is an algorithm?
An **algorithm** is a list of **steps**, in the **right order**, to solve a problem.

You already use algorithms every day! Example: **making tea** ☕
1. Boil water.
2. Put the tea in the cup.
3. Pour the hot water.
4. Add sugar.
5. Drink.

If you change the order (drink before pouring the water…), it does not work. **The order is important.**

### 2. Three parts: input → processing → output
Every algorithm has 3 parts:

| Part | Question | Example: average of 2 marks |
|---|---|---|
| **Input** | What do I have? | mark 1 = 12, mark 2 = 16 |
| **Processing** | What do I calculate? | (12 + 16) / 2 |
| **Output** | What do I show? | 14 |

### 3. Writing an algorithm
We write it with simple key words:
```
START
    READ mark1, mark2
    CALCULATE average = (mark1 + mark2) / 2
    DISPLAY average
END
```
This text is not Python yet. It is just a **plan**, like a recipe.

### 4. Taking a decision
Sometimes the algorithm must **choose**. Example: does the student pass?
```
START
    READ mark
    IF mark >= 10 THEN
        DISPLAY "Pass"
    ELSE
        DISPLAY "Fail"
END
```

### 5. Repeating
Sometimes we do the **same step several times**. Example: count from 1 to 5.
```
START
    REPEAT for n from 1 to 5
        DISPLAY n
END
```

### 6. The flowchart: an algorithm as a drawing
| Shape | Meaning |
|---|---|
| ⬭ Oval | START / END |
| ▱ Parallelogram | READ / DISPLAY (input and output) |
| ▭ Rectangle | CALCULATE (processing) |
| ◇ Diamond | IF (a question: yes or no?) |

The shapes are joined by **arrows** that show the order.

### 7. From the algorithm to Python
| Algorithm | Python |
|---|---|
| `READ mark` | `mark = 12` |
| `CALCULATE average = …` | `average = (12 + 16) / 2` |
| `DISPLAY average` | `print(average)` |
| `IF … THEN … ELSE` | `if … :` … `else:` |

> **Remember:** first think (algorithm), then write the code (Python).
''',
r'''
### 1. Qu'est-ce qu'un algorithme ?
Un **algorithme** est une liste d'**étapes**, dans le **bon ordre**, pour résoudre un problème.

Tu utilises déjà des algorithmes tous les jours ! Exemple : **préparer un thé** ☕
1. Faire bouillir l'eau.
2. Mettre le thé dans la tasse.
3. Verser l'eau chaude.
4. Ajouter le sucre.
5. Boire.

Si tu changes l'ordre (boire avant de verser l'eau…), ça ne marche pas. **L'ordre est important.**

### 2. Trois parties : entrée → traitement → sortie
Chaque algorithme a 3 parties :

| Partie | Question | Exemple : moyenne de 2 notes |
|---|---|---|
| **Entrée** | Qu'est-ce que j'ai ? | note 1 = 12, note 2 = 16 |
| **Traitement** | Qu'est-ce que je calcule ? | (12 + 16) / 2 |
| **Sortie** | Qu'est-ce que j'affiche ? | 14 |

### 3. Écrire un algorithme
On l'écrit avec des mots simples :
```
DÉBUT
    LIRE note1, note2
    CALCULER moyenne = (note1 + note2) / 2
    AFFICHER moyenne
FIN
```
Ce texte n'est pas encore du Python. C'est juste un **plan**, comme une recette.

### 4. Prendre une décision
Parfois, l'algorithme doit **choisir**. Exemple : l'étudiant est-il admis ?
```
DÉBUT
    LIRE note
    SI note >= 10 ALORS
        AFFICHER "Admis"
    SINON
        AFFICHER "Ajourné"
FIN
```

### 5. Répéter
Parfois, on fait **la même étape plusieurs fois**. Exemple : compter de 1 à 5.
```
DÉBUT
    RÉPÉTER pour n de 1 à 5
        AFFICHER n
FIN
```

### 6. L'organigramme : un algorithme en dessin
| Forme | Signification |
|---|---|
| ⬭ Ovale | DÉBUT / FIN |
| ▱ Parallélogramme | LIRE / AFFICHER (entrée et sortie) |
| ▭ Rectangle | CALCULER (traitement) |
| ◇ Losange | SI (une question : oui ou non ?) |

Les formes sont reliées par des **flèches** qui montrent l'ordre.

### 7. De l'algorithme à Python
| Algorithme | Python |
|---|---|
| `LIRE note` | `mark = 12` |
| `CALCULER moyenne = …` | `average = (12 + 16) / 2` |
| `AFFICHER moyenne` | `print(average)` |
| `SI … ALORS … SINON` | `if … :` … `else:` |

> **À retenir :** d'abord on réfléchit (algorithme), ensuite on écrit le code (Python).
''',
r'''
### 1. ما هي الخوارزمية؟
**الخوارزمية** هي قائمة من **الخطوات** مرتّبة **بالترتيب الصحيح** لحل مشكلة.

أنت تستعمل الخوارزميات كل يوم! مثال: **تحضير الشاي** ☕
1. اغلِ الماء.
2. ضع الشاي في الكوب.
3. اسكب الماء الساخن.
4. أضف السكر.
5. اشرب.

إذا غيّرت الترتيب (تشرب قبل سكب الماء…) فلن ينجح الأمر. **الترتيب مهم.**

### 2. ثلاثة أجزاء: مدخلات ← معالجة ← مخرجات
لكل خوارزمية 3 أجزاء:

| الجزء | السؤال | مثال: معدل علامتين |
|---|---|---|
| **المدخلات** | ماذا لديّ؟ | العلامة 1 = 12، العلامة 2 = 16 |
| **المعالجة** | ماذا أحسب؟ | (12 + 16) / 2 |
| **المخرجات** | ماذا أعرض؟ | 14 |

### 3. كتابة خوارزمية
نكتبها بكلمات بسيطة:
```
بداية
    اقرأ علامة1، علامة2
    احسب المعدل = (علامة1 + علامة2) / 2
    اعرض المعدل
نهاية
```
هذا النص ليس كود Python بعد، بل هو **مخطط** فقط، مثل وصفة الطبخ.

### 4. اتخاذ قرار
أحياناً يجب على الخوارزمية أن **تختار**. مثال: هل نجح الطالب؟
```
بداية
    اقرأ العلامة
    إذا كانت العلامة >= 10 فإن
        اعرض "ناجح"
    وإلا
        اعرض "راسب"
نهاية
```

### 5. التكرار
أحياناً نعيد **الخطوة نفسها عدة مرات**. مثال: العدّ من 1 إلى 5.
```
بداية
    كرّر من أجل n من 1 إلى 5
        اعرض n
نهاية
```

### 6. المخطط الانسيابي: الخوارزمية في شكل رسم
| الشكل | المعنى |
|---|---|
| ⬭ شكل بيضوي | بداية / نهاية |
| ▱ متوازي أضلاع | اقرأ / اعرض (المدخلات والمخرجات) |
| ▭ مستطيل | احسب (المعالجة) |
| ◇ معيّن | إذا (سؤال: نعم أم لا؟) |

تُربط الأشكال **بأسهم** تبيّن الترتيب.

### 7. من الخوارزمية إلى Python
| الخوارزمية | Python |
|---|---|
| اقرأ العلامة | `mark = 12` |
| احسب المعدل = … | `average = (12 + 16) / 2` |
| اعرض المعدل | `print(average)` |
| إذا … فإن … وإلا | `if … :` … `else:` |

> **تذكّر:** نفكّر أولاً (الخوارزمية)، ثم نكتب الكود (Python).
'''),

    # ---------------------------------------------------------------- EXAMPLES
    "examples": [
        {
            "title": L("Average of two marks", "Moyenne de deux notes", "معدل علامتين"),
            "explain": L(
                "Each step of the algorithm is one line of Python. Change the marks and press **Run** again.",
                "Chaque étape de l'algorithme devient une ligne de Python. Change les notes et clique de nouveau sur **Exécuter**.",
                "كل خطوة من الخوارزمية أصبحت سطراً في Python. غيّر العلامات ثم اضغط **تشغيل** من جديد."),
            "code": '''# READ
mark1 = 12
mark2 = 16

# CALCULATE
average = (mark1 + mark2) / 2

# DISPLAY
print("Average:", average)
''',
        },
        {
            "title": L("Pass or fail?", "Admis ou ajourné ?", "ناجح أم راسب؟"),
            "explain": L(
                "The algorithm takes a decision. Try `mark = 8`, then `mark = 15`.",
                "L'algorithme prend une décision. Essaie `mark = 8`, puis `mark = 15`.",
                "الخوارزمية تتخذ قراراً. جرّب `mark = 8` ثم `mark = 15`."),
            "code": '''# READ
mark = 8

# IF ... THEN ... ELSE
if mark >= 10:
    print("Pass")
else:
    print("Fail")
''',
        },
        {
            "title": L("Repeating: count from 1 to 5", "Répéter : compter de 1 à 5", "التكرار: العدّ من 1 إلى 5"),
            "explain": L(
                "The same step (display n) is repeated 5 times. Change 6 into 11 to count to 10.",
                "La même étape (afficher n) est répétée 5 fois. Remplace 6 par 11 pour compter jusqu'à 10.",
                "الخطوة نفسها (اعرض n) تتكرر 5 مرات. غيّر 6 إلى 11 للعدّ حتى 10."),
            "code": '''# REPEAT for n from 1 to 5
for n in range(1, 6):
    print(n)
''',
        },
    ],

    # --------------------------------------------------------------- EXERCISES
    "exercises": [
        {
            "title": L("The profit of a shop", "Le bénéfice d'un magasin", "ربح متجر"),
            "task": L(
                "A shop earned **50000** DZD and spent **32000** DZD. Display the profit (the number only).\n\nAlgorithm: profit = earnings − costs.",
                "Un magasin a gagné **50000** DA et dépensé **32000** DA. Affiche le bénéfice (le nombre seulement).\n\nAlgorithme : bénéfice = recettes − dépenses.",
                "ربح متجر **50000** دج وأنفق **32000** دج. اعرض الربح (الرقم فقط).\n\nالخوارزمية: الربح = المداخيل − المصاريف."),
            "starter": "earnings = 50000\ncosts = 32000\n\n# CALCULATE the profit, then DISPLAY it\n",
            "expected": "18000",
            "hint": L("`profit = earnings - costs` then `print(profit)`", "`profit = earnings - costs` puis `print(profit)`",
                      "`profit = earnings - costs` ثم `print(profit)`"),
            "solution": "earnings = 50000\ncosts = 32000\n\nprofit = earnings - costs\nprint(profit)\n",
        },
        {
            "title": L("Average of three marks", "Moyenne de trois notes", "معدل ثلاث علامات"),
            "task": L(
                "The marks are **10**, **14** and **12**. Display the average.",
                "Les notes sont **10**, **14** et **12**. Affiche la moyenne.",
                "العلامات هي **10** و**14** و**12**. اعرض المعدل."),
            "starter": "mark1 = 10\nmark2 = 14\nmark3 = 12\n\n# CALCULATE the average, then DISPLAY it\n",
            "expected": "12.0",
            "hint": L("Add the 3 marks, then divide by 3. Do not forget the brackets: `(a + b + c) / 3`.",
                      "Additionne les 3 notes, puis divise par 3. N'oublie pas les parenthèses : `(a + b + c) / 3`.",
                      "اجمع العلامات الثلاث ثم اقسم على 3. لا تنسَ الأقواس: `(a + b + c) / 3`."),
            "solution": "mark1 = 10\nmark2 = 14\nmark3 = 12\n\naverage = (mark1 + mark2 + mark3) / 3\nprint(average)\n",
        },
        {
            "title": L("Complete the decision", "Complète la décision", "أكمل القرار"),
            "task": L(
                "Replace the dots so that the program displays `Pass` when the mark is 10 or more, and `Fail` otherwise. With `mark = 13`, it must display `Pass`.",
                "Remplace les points pour que le programme affiche `Pass` si la note est de 10 ou plus, et `Fail` sinon. Avec `mark = 13`, il doit afficher `Pass`.",
                "عوّض النقاط حتى يعرض البرنامج `Pass` إذا كانت العلامة 10 أو أكثر، و`Fail` في غير ذلك. مع `mark = 13` يجب أن يعرض `Pass`."),
            "starter": 'mark = 13\n\nif mark >= ...:\n    print("...")\nelse:\n    print("...")\n',
            "expected": "Pass",
            "hint": L("The limit is 10. The first message is `Pass`, the second is `Fail`.",
                      "La limite est 10. Le premier message est `Pass`, le second `Fail`.",
                      "الحدّ هو 10. الرسالة الأولى `Pass` والثانية `Fail`."),
            "solution": 'mark = 13\n\nif mark >= 10:\n    print("Pass")\nelse:\n    print("Fail")\n',
        },
    ],

    # -------------------------------------------------------------------- QUIZ
    "quiz": [
        {
            "q": L("What is an algorithm?", "Qu'est-ce qu'un algorithme ?", "ما هي الخوارزمية؟"),
            "options": L(
                ["A computer brand", "Steps in the right order to solve a problem", "A type of number", "A website"],
                ["Une marque d'ordinateur", "Des étapes dans le bon ordre pour résoudre un problème", "Un type de nombre", "Un site web"],
                ["علامة تجارية لحاسوب", "خطوات مرتّبة بالترتيب الصحيح لحل مشكلة", "نوع من الأعداد", "موقع إنترنت"]),
            "answer": 1,
            "explain": L("Like a recipe: steps in the right order.", "Comme une recette : des étapes dans le bon ordre.",
                         "مثل وصفة الطبخ: خطوات بالترتيب الصحيح."),
        },
        {
            "q": L("In 'average of two marks', what is the input?", "Dans « moyenne de deux notes », quelle est l'entrée ?",
                   "في «معدل علامتين»، ما هي المدخلات؟"),
            "options": L(["The two marks", "The average", "The division", "The screen"],
                         ["Les deux notes", "La moyenne", "La division", "L'écran"],
                         ["العلامتان", "المعدل", "القسمة", "الشاشة"]),
            "answer": 0,
            "explain": L("The input is what we have at the start: the two marks.", "L'entrée, c'est ce qu'on a au départ : les deux notes.",
                         "المدخلات هي ما لدينا في البداية: العلامتان."),
        },
        {
            "q": L("In 'average of two marks', what is the output?", "Dans « moyenne de deux notes », quelle est la sortie ?",
                   "في «معدل علامتين»، ما هي المخرجات؟"),
            "options": L(["The two marks", "The keyboard", "The average", "The number 2"],
                         ["Les deux notes", "Le clavier", "La moyenne", "Le nombre 2"],
                         ["العلامتان", "لوحة المفاتيح", "المعدل", "العدد 2"]),
            "answer": 2,
            "explain": L("The output is the result we display.", "La sortie, c'est le résultat qu'on affiche.",
                         "المخرجات هي النتيجة التي نعرضها."),
        },
        {
            "q": L("In a flowchart, which shape is used for a question (yes or no)?",
                   "Dans un organigramme, quelle forme sert pour une question (oui ou non) ?",
                   "في المخطط الانسيابي، ما الشكل المستعمل للسؤال (نعم أم لا)؟"),
            "options": L(["Oval", "Rectangle", "Parallelogram", "Diamond"],
                         ["Ovale", "Rectangle", "Parallélogramme", "Losange"],
                         ["شكل بيضوي", "مستطيل", "متوازي أضلاع", "معيّن"]),
            "answer": 3,
            "explain": L("The diamond ◇ is for decisions (IF).", "Le losange ◇ sert aux décisions (SI).",
                         "المعيّن ◇ يُستعمل للقرارات (إذا)."),
        },
        {
            "q": L("Which Python instruction means DISPLAY?", "Quelle instruction Python veut dire AFFICHER ?",
                   "ما هي تعليمة Python التي تعني اعرض؟"),
            "options": ["if", "print()", "for", "="],
            "answer": 1,
            "explain": L("`print()` displays a result on the screen.", "`print()` affiche un résultat à l'écran.",
                         "`print()` تعرض النتيجة على الشاشة."),
        },
        {
            "q": L("Why is the order of the steps important?", "Pourquoi l'ordre des étapes est-il important ?",
                   "لماذا ترتيب الخطوات مهم؟"),
            "options": L(
                ["It is not important", "Because a wrong order gives a wrong result", "To make the code longer", "Because Python likes it"],
                ["Il n'est pas important", "Parce qu'un mauvais ordre donne un mauvais résultat", "Pour rendre le code plus long", "Parce que Python aime ça"],
                ["ليس مهماً", "لأن الترتيب الخاطئ يعطي نتيجة خاطئة", "لجعل الكود أطول", "لأن Python تحب ذلك"]),
            "answer": 1,
            "explain": L("You cannot calculate the average before reading the marks!", "On ne peut pas calculer la moyenne avant de lire les notes !",
                         "لا يمكن حساب المعدل قبل قراءة العلامات!"),
        },
    ],
}
