"""
WEEK 15 · Final project  (level: very easy)
Programme: combining the concepts · a program that analyses financial or economic data · presenting the project.
"""
from syllabus import L

WEEK = {
    "objectives": L(
        [
            "**Choose** a small economic or financial problem and its data.",
            "**Plan** the program with an algorithm before coding.",
            "**Combine** variables, lists, dictionaries, loops, conditions, functions and files.",
            "**Test** the program step by step.",
            "**Present** the project clearly in a few minutes.",
        ],
        [
            "**Choisir** un petit problème économique ou financier et ses données.",
            "**Planifier** le programme avec un algorithme avant de coder.",
            "**Combiner** variables, listes, dictionnaires, boucles, conditions, fonctions et fichiers.",
            "**Tester** le programme étape par étape.",
            "**Présenter** le projet clairement en quelques minutes.",
        ],
        [
            "**يختار** مسألة اقتصادية أو مالية صغيرة وبياناتها.",
            "**يخطّط** للبرنامج بخوارزمية قبل كتابة الكود.",
            "**يجمع** بين المتغيرات والقوائم والقواميس والحلقات والشروط والدوال والملفات.",
            "**يختبر** البرنامج خطوة بخطوة.",
            "**يعرض** المشروع بوضوح في بضع دقائق.",
        ],
    ),

    "lesson": L(
r'''
### 1. The goal
You will write **one complete program** that analyses economic or financial data and prints a clear report. It uses everything you learned this semester.

### 2. Project ideas
| Idea | Data | What the program shows |
|---|---|---|
| Sales of a shop | sales per month | total, average, best and worst month, growth |
| Household budget | income and expenses per category | total spent, savings, biggest expense |
| Student marks | marks per subject | average, mention, subjects to improve |
| Inflation | yearly inflation rates | average, highest year, years above 5 % |
| Loan simulator | amount, rate, duration | monthly payment, total cost, interest |

### 3. The 5 steps
1. **Understand** the problem: what is the input? what output do I want?
2. **Write the algorithm** in simple words (week 2).
3. **Code step by step**: write a small part, run it, check it, then continue.
4. **Test** with values you can check by hand.
5. **Present**: show the problem, the code, and the result.

### 4. A good structure for your program
```python
# 1. DATA
months = ["Jan", "Feb", "Mar"]
sales = [182000, 165500, 210300]

# 2. FUNCTIONS
def average(values):
    return sum(values) / len(values)

# 3. CALCULATIONS
total = sum(sales)

# 4. REPORT
print("Total:", total)

# 5. SAVE (file)
with open("report.txt", "w") as f:
    f.write("Total: " + str(total))
```

### 5. Checklist before presenting
- ✅ The program runs **without errors**.
- ✅ The variable names are **clear** (`total_sales`, not `x`).
- ✅ There are **comments** that explain the steps.
- ✅ The results are **checked** by hand on a small example.
- ✅ The report is **easy to read** (titles, units like DZD or %).

### 6. Presenting in 5 minutes
1. **The problem** (1 min): "I analyse the sales of a shop over 6 months."
2. **The data** (1 min): where they come from, what they contain.
3. **The code** (2 min): the main steps, not every line.
4. **The result** (1 min): what we learn. Example: "May is the best month; sales grew by 24 %."

> **Remember:** small steps, test often, explain simply.
''',
r'''
### 1. L'objectif
Tu vas écrire **un programme complet** qui analyse des données économiques ou financières et affiche un rapport clair. Il utilise tout ce que tu as appris ce semestre.

### 2. Idées de projets
| Idée | Données | Ce que montre le programme |
|---|---|---|
| Ventes d'un magasin | ventes par mois | total, moyenne, meilleur et pire mois, croissance |
| Budget d'un ménage | revenus et dépenses par catégorie | total dépensé, épargne, plus grosse dépense |
| Notes d'un étudiant | notes par matière | moyenne, mention, matières à améliorer |
| Inflation | taux d'inflation annuels | moyenne, année la plus haute, années au-dessus de 5 % |
| Simulateur de prêt | montant, taux, durée | mensualité, coût total, intérêts |

### 3. Les 5 étapes
1. **Comprendre** le problème : quelle est l'entrée ? quelle sortie je veux ?
2. **Écrire l'algorithme** avec des mots simples (semaine 2).
3. **Coder étape par étape** : écris une petite partie, exécute, vérifie, puis continue.
4. **Tester** avec des valeurs que tu peux vérifier à la main.
5. **Présenter** : montre le problème, le code et le résultat.

### 4. Une bonne structure pour ton programme
```python
# 1. DONNÉES
months = ["Jan", "Feb", "Mar"]
sales = [182000, 165500, 210300]

# 2. FONCTIONS
def average(values):
    return sum(values) / len(values)

# 3. CALCULS
total = sum(sales)

# 4. RAPPORT
print("Total:", total)

# 5. ENREGISTRER (fichier)
with open("report.txt", "w") as f:
    f.write("Total: " + str(total))
```

### 5. Liste de vérification avant de présenter
- ✅ Le programme s'exécute **sans erreur**.
- ✅ Les noms de variables sont **clairs** (`total_sales`, pas `x`).
- ✅ Il y a des **commentaires** qui expliquent les étapes.
- ✅ Les résultats sont **vérifiés** à la main sur un petit exemple.
- ✅ Le rapport est **facile à lire** (titres, unités comme DZD ou %).

### 6. Présenter en 5 minutes
1. **Le problème** (1 min) : « J'analyse les ventes d'un magasin sur 6 mois. »
2. **Les données** (1 min) : d'où elles viennent, ce qu'elles contiennent.
3. **Le code** (2 min) : les grandes étapes, pas chaque ligne.
4. **Le résultat** (1 min) : ce qu'on apprend. Exemple : « Mai est le meilleur mois ; les ventes ont augmenté de 24 %. »

> **À retenir :** petites étapes, tester souvent, expliquer simplement.
''',
r'''
### 1. الهدف
ستكتب **برنامجاً كاملاً** يحلّل بيانات اقتصادية أو مالية ويعرض تقريراً واضحاً، ويستعمل كل ما تعلّمته في هذا السداسي.

### 2. أفكار للمشاريع
| الفكرة | البيانات | ما يعرضه البرنامج |
|---|---|---|
| مبيعات متجر | المبيعات حسب الشهر | المجموع، المتوسط، أفضل وأسوأ شهر، النمو |
| ميزانية أسرة | المداخيل والمصاريف حسب الفئة | مجموع المصاريف، الادخار، أكبر مصروف |
| علامات طالب | العلامات حسب المادة | المعدل، التقدير، المواد التي يجب تحسينها |
| التضخم | معدلات التضخم السنوية | المتوسط، أعلى سنة، السنوات فوق 5 % |
| محاكي قرض | المبلغ، المعدل، المدة | القسط الشهري، التكلفة الكلية، الفوائد |

### 3. الخطوات الخمس
1. **افهم** المسألة: ما المدخلات؟ وما المخرجات التي أريدها؟
2. **اكتب الخوارزمية** بكلمات بسيطة (الأسبوع 2).
3. **اكتب الكود خطوة بخطوة**: اكتب جزءاً صغيراً، نفّذه، تحقّق منه، ثم واصل.
4. **اختبر** بقيم يمكنك التحقق منها يدوياً.
5. **اعرض**: قدّم المسألة والكود والنتيجة.

### 4. هيكل جيد لبرنامجك
```python
# 1. DATA
months = ["Jan", "Feb", "Mar"]
sales = [182000, 165500, 210300]

# 2. FUNCTIONS
def average(values):
    return sum(values) / len(values)

# 3. CALCULATIONS
total = sum(sales)

# 4. REPORT
print("Total:", total)

# 5. SAVE (file)
with open("report.txt", "w") as f:
    f.write("Total: " + str(total))
```

### 5. قائمة التحقق قبل العرض
- ✅ البرنامج يعمل **دون أخطاء**.
- ✅ أسماء المتغيرات **واضحة** (`total_sales` وليس `x`).
- ✅ توجد **تعليقات** تشرح الخطوات.
- ✅ النتائج **متحقَّق منها** يدوياً على مثال صغير.
- ✅ التقرير **سهل القراءة** (عناوين، ووحدات مثل DZD أو %).

### 6. العرض في 5 دقائق
1. **المسألة** (دقيقة): «أحلّل مبيعات متجر خلال 6 أشهر.»
2. **البيانات** (دقيقة): من أين جاءت وماذا تحتوي.
3. **الكود** (دقيقتان): الخطوات الكبرى وليس كل سطر.
4. **النتيجة** (دقيقة): ماذا نستنتج. مثال: «ماي هو أفضل شهر، والمبيعات نمت بـ 24 %.»

> **تذكّر:** خطوات صغيرة، اختبار متكرر، وشرح بسيط.
'''),

    "examples": [
        {
            "title": L("Complete project: sales of a shop", "Projet complet : ventes d'un magasin", "مشروع كامل: مبيعات متجر"),
            "explain": L("Data, functions, loop, condition, report and file: everything in one program. Change the data with your own figures.",
                         "Données, fonctions, boucle, condition, rapport et fichier : tout dans un seul programme. Remplace les données par tes propres chiffres.",
                         "بيانات ودوال وحلقة وشرط وتقرير وملف: كل شيء في برنامج واحد. عوّض البيانات بأرقامك الخاصة."),
            "code": '''# 1. DATA
sales = {"Jan": 182000, "Feb": 165500, "Mar": 210300,
         "Apr": 198750, "May": 240100, "Jun": 226400}

# 2. FUNCTIONS
def average(values):
    return sum(values) / len(values)

def growth(first, last):
    return (last - first) / first * 100

# 3. CALCULATIONS
values = list(sales.values())
total = sum(values)
best_month = ""
best_value = 0
for month, value in sales.items():
    if value > best_value:
        best_month = month
        best_value = value

# 4. REPORT
print("=== SALES REPORT ===")
for month, value in sales.items():
    print(month, ":", value, "DZD")
print("Total:", total, "DZD")
print("Average:", round(average(values), 2), "DZD")
print("Best month:", best_month)
print("Growth:", round(growth(values[0], values[-1]), 1), "%")

# 5. SAVE
with open("report.txt", "w") as f:
    f.write("Total: " + str(total) + "\\n")
    f.write("Best month: " + best_month + "\\n")
print("Report saved in report.txt")
''',
        },
        {
            "title": L("Project idea: household budget", "Idée de projet : budget d'un ménage", "فكرة مشروع: ميزانية أسرة"),
            "explain": L("Income, expenses by category, savings and the biggest expense.",
                         "Revenus, dépenses par catégorie, épargne et plus grosse dépense.",
                         "المداخيل والمصاريف حسب الفئة والادخار وأكبر مصروف."),
            "code": '''income = 90000
expenses = {"food": 32000, "rent": 25000, "transport": 8000,
            "energy": 6000, "other": 7000}

spent = sum(expenses.values())
savings = income - spent

print("Income:", income, "DZD")
print("Spent:", spent, "DZD")
print("Savings:", savings, "DZD", f"({savings / income * 100:.1f} %)")

biggest = ""
for category, amount in expenses.items():
    if biggest == "" or amount > expenses[biggest]:
        biggest = category
print("Biggest expense:", biggest)

if savings < 0:
    print("Warning: the budget is in deficit!")
''',
        },
        {
            "title": L("Project idea: inflation analysis", "Idée de projet : analyse de l'inflation", "فكرة مشروع: تحليل التضخم"),
            "explain": L("Yearly inflation rates (example values). Average, highest year and years above 5 %.",
                         "Taux d'inflation annuels (valeurs d'exemple). Moyenne, année la plus haute et années au-dessus de 5 %.",
                         "معدلات التضخم السنوية (قيم للتوضيح). المتوسط وأعلى سنة والسنوات فوق 5 %."),
            "code": '''years = [2019, 2020, 2021, 2022, 2023]
inflation = [2.0, 2.4, 7.2, 9.3, 9.3]     # example values (%)

print("Average:", round(sum(inflation) / len(inflation), 2), "%")

highest = max(inflation)
print("Highest:", highest, "% in", years[inflation.index(highest)])

print("Years above 5 %:")
for i in range(len(years)):
    if inflation[i] > 5:
        print(" -", years[i], ":", inflation[i], "%")
''',
        },
    ],

    "exercises": [
        {
            "title": L("Step 1: total and average", "Étape 1 : total et moyenne", "الخطوة 1: المجموع والمتوسط"),
            "task": L("Display the total and the average of the sales (rounded to 2 decimals) with **one** `print()`.",
                      "Affiche le total et la moyenne des ventes (arrondie à 2 décimales) avec **un seul** `print()`.",
                      "اعرض مجموع المبيعات ومتوسطها (مقرّباً إلى رقمين بعد الفاصلة) بـ `print()` **واحدة**."),
            "starter": "sales = [182000, 165500, 210300, 198750, 240100, 226400]\n\ntotal = \naverage = \nprint(total, round(average, 2))\n",
            "expected": "1223050 203841.67",
            "hint": L("`total = sum(sales)` and `average = total / len(sales)`", "`total = sum(sales)` et `average = total / len(sales)`",
                      "`total = sum(sales)` و`average = total / len(sales)`"),
            "solution": "sales = [182000, 165500, 210300, 198750, 240100, 226400]\n\ntotal = sum(sales)\naverage = total / len(sales)\nprint(total, round(average, 2))\n",
        },
        {
            "title": L("Step 2: the best month", "Étape 2 : le meilleur mois", "الخطوة 2: أفضل شهر"),
            "task": L("Complete the loop to find the month with the highest sales, then display it.",
                      "Complète la boucle pour trouver le mois avec les ventes les plus élevées, puis affiche-le.",
                      "أكمل الحلقة لإيجاد الشهر الذي حقّق أعلى مبيعات ثم اعرضه."),
            "starter": 'sales = {"Jan": 182000, "Feb": 165500, "Mar": 210300,\n         "Apr": 198750, "May": 240100, "Jun": 226400}\n\nbest_month = ""\nbest_value = 0\nfor month, value in sales.items():\n    if value > best_value:\n        # keep this month and this value\n\nprint(best_month)\n',
            "expected": "May",
            "hint": L("Inside the `if`: `best_month = month` and `best_value = value`", "Dans le `if` : `best_month = month` et `best_value = value`",
                      "داخل `if`: `best_month = month` و`best_value = value`"),
            "solution": 'sales = {"Jan": 182000, "Feb": 165500, "Mar": 210300,\n         "Apr": 198750, "May": 240100, "Jun": 226400}\n\nbest_month = ""\nbest_value = 0\nfor month, value in sales.items():\n    if value > best_value:\n        best_month = month\n        best_value = value\n\nprint(best_month)\n',
        },
        {
            "title": L("Step 3: save the report", "Étape 3 : enregistrer le rapport", "الخطوة 3: حفظ التقرير"),
            "task": L("Write the two report lines in `report.txt`, then read the file and display it. Expected:\n```\nTotal: 1223050\nBest month: May\n```",
                      "Écris les deux lignes du rapport dans `report.txt`, puis lis le fichier et affiche-le. Attendu :\n```\nTotal: 1223050\nBest month: May\n```",
                      "اكتب سطري التقرير في `report.txt` ثم اقرأ الملف واعرضه. المنتظر:\n```\nTotal: 1223050\nBest month: May\n```"),
            "starter": 'total = 1223050\nbest_month = "May"\n\nwith open("report.txt", "w") as f:\n    # write the 2 lines (do not forget \\n)\n\nwith open("report.txt", "r") as f:\n    print(f.read())\n',
            "expected": "Total: 1223050\nBest month: May",
            "hint": L('`f.write("Total: " + str(total) + "\\n")` then the same for the month.',
                      '`f.write("Total: " + str(total) + "\\n")` puis la même chose pour le mois.',
                      '`f.write("Total: " + str(total) + "\\n")` ثم الشيء نفسه للشهر.'),
            "solution": 'total = 1223050\nbest_month = "May"\n\nwith open("report.txt", "w") as f:\n    f.write("Total: " + str(total) + "\\n")\n    f.write("Best month: " + best_month + "\\n")\n\nwith open("report.txt", "r") as f:\n    print(f.read())\n',
        },
    ],

    "quiz": [
        {"q": L("What should you do before coding the project?", "Que faut-il faire avant de coder le projet ?", "ماذا يجب أن تفعل قبل كتابة كود المشروع؟"),
         "options": L(["Write the algorithm", "Choose the colours", "Print the code", "Nothing"],
                      ["Écrire l'algorithme", "Choisir les couleurs", "Imprimer le code", "Rien"],
                      ["كتابة الخوارزمية", "اختيار الألوان", "طباعة الكود", "لا شيء"]),
         "answer": 0,
         "explain": L("Think first (algorithm), then code.", "Réfléchir d'abord (algorithme), puis coder.", "نفكّر أولاً (الخوارزمية) ثم نكتب الكود.")},
        {"q": L("What is the best way to write the code?", "Quelle est la meilleure façon d'écrire le code ?", "ما أفضل طريقة لكتابة الكود؟"),
         "options": L(["Everything at once, then run", "Step by step, running after each part", "Copy a friend's code", "Without testing"],
                      ["Tout d'un coup, puis exécuter", "Étape par étape, en exécutant après chaque partie", "Copier le code d'un ami", "Sans tester"],
                      ["كل شيء دفعة واحدة ثم التنفيذ", "خطوة بخطوة مع التنفيذ بعد كل جزء", "نسخ كود صديق", "دون اختبار"]),
         "answer": 1,
         "explain": L("Small steps make errors easy to find.", "Les petites étapes rendent les erreurs faciles à trouver.",
                      "الخطوات الصغيرة تسهّل اكتشاف الأخطاء.")},
        {"q": L("Which variable name is the clearest?", "Quel nom de variable est le plus clair ?", "أي اسم متغير هو الأوضح؟"),
         "options": ["x", "a1", "total_sales", "t"], "answer": 2,
         "explain": L("A clear name explains itself.", "Un nom clair s'explique tout seul.", "الاسم الواضح يشرح نفسه.")},
        {"q": L("Which type fits \"sales per month\" with the month name?", "Quel type convient pour « ventes par mois » avec le nom du mois ?",
                "ما النوع المناسب لـ «المبيعات حسب الشهر» مع اسم الشهر؟"),
         "options": L(["A dictionary", "A bool", "A single int", "A comment"], ["Un dictionnaire", "Un bool", "Un seul int", "Un commentaire"],
                      ["قاموس", "bool", "عدد صحيح واحد", "تعليق"]),
         "answer": 0,
         "explain": L("Month (key) → sales (value).", "Mois (clé) → ventes (valeur).", "الشهر (مفتاح) ← المبيعات (قيمة).")},
        {"q": L("How do you check that a result is right?", "Comment vérifier qu'un résultat est juste ?", "كيف نتحقق من صحة نتيجة؟"),
         "options": L(["Compare with a small example computed by hand", "Trust the computer", "Run it twice", "Ask nobody"],
                      ["Comparer avec un petit exemple calculé à la main", "Faire confiance à l'ordinateur", "L'exécuter deux fois", "Ne demander à personne"],
                      ["المقارنة بمثال صغير محسوب يدوياً", "الثقة في الحاسوب", "تنفيذه مرتين", "عدم سؤال أحد"]),
         "answer": 0,
         "explain": L("A hand-checked case catches mistakes.", "Un cas vérifié à la main repère les erreurs.", "حالة متحقَّق منها يدوياً تكشف الأخطاء.")},
        {"q": L("In the presentation, what matters most?", "Dans la présentation, qu'est-ce qui compte le plus ?", "ما الأهم في العرض؟"),
         "options": L(["Reading every line of code", "The problem, the main steps and the result", "Talking as long as possible", "Showing only the code"],
                      ["Lire chaque ligne de code", "Le problème, les grandes étapes et le résultat", "Parler le plus longtemps possible", "Montrer seulement le code"],
                      ["قراءة كل سطر من الكود", "المسألة والخطوات الكبرى والنتيجة", "الكلام أطول وقت ممكن", "عرض الكود فقط"]),
         "answer": 1,
         "explain": L("Explain simply what you did and what you found.", "Explique simplement ce que tu as fait et ce que tu as trouvé.",
                      "اشرح ببساطة ما فعلته وما توصّلت إليه.")},
    ],
}
