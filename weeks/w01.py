"""
WEEK 1 · Introduction to programming with Python
Programme: what programming is · why Python matters in economics ·
the working environment (VS Code, Jupyter Notebook) · installing Python and running the editor.
"""
from syllabus import L

WEEK = {
    "objectives": L(
        [
            "**Define** programming, a program and a programming language, with everyday examples.",
            "**Distinguish** low-level from high-level languages, and a compiler from an interpreter.",
            "**Explain** why Python is widely used in economics, accounting and finance.",
            "**Recognise** the main working environments (IDE): VS Code and Jupyter Notebook.",
            "**Install** Python, open an editor and run a first line of code.",
        ],
        [
            "**Définir** la programmation, un programme et un langage de programmation, avec des exemples du quotidien.",
            "**Distinguer** les langages de bas niveau et de haut niveau, ainsi qu'un compilateur d'un interpréteur.",
            "**Expliquer** pourquoi Python est très utilisé en économie, en comptabilité et en finance.",
            "**Reconnaître** les principaux environnements de travail (IDE) : VS Code et Jupyter Notebook.",
            "**Installer** Python, ouvrir un éditeur et exécuter une première ligne de code.",
        ],
        [
            "**يعرّف** البرمجة والبرنامج ولغة البرمجة، مع أمثلة من الحياة اليومية.",
            "**يميّز** بين اللغات منخفضة المستوى وعالية المستوى، وبين المترجم (Compiler) والمفسّر (Interpreter).",
            "**يشرح** أسباب الاستخدام الواسع للغة Python في الاقتصاد والمحاسبة والمالية.",
            "**يتعرّف** على أهم بيئات العمل (IDE): VS Code وJupyter Notebook.",
            "**يثبّت** Python ويفتح محرراً وينفّذ أول سطر من الكود.",
        ],
    ),

    # ------------------------------------------------------------------ LESSON
    "lesson": L(
r'''
### 1. What is programming?
A computer is very fast but it has no initiative: it does **exactly** what it is told, nothing more and nothing less.

- **Programming** is the activity of writing precise instructions so that a computer solves a problem or performs a task.
- A **program** is the ordered set of these instructions. The text we write is called the **code** (or *source code*).
- A **programming language** is the vocabulary and the grammar used to write these instructions: Python, R, Java, C…

> **Analogy:** a cooking recipe is a "program" for a cook. The ingredients are the **data**, the steps are the **instructions**, and the dish is the **result**. If one step is vague or missing, the dish fails: the same is true for a program.

### 2. From human language to machine language
A processor only understands **machine language** (sequences of 0 and 1). We therefore write in a language that humans can read, and a tool translates it.

| Level | Description | Examples |
|---|---|---|
| Low level | Close to the machine, hard to read | Machine code, Assembly |
| High level | Close to human language, easy to read | **Python**, R, Java, C++ |

Two ways to translate a high-level program:
- **Compiler:** translates the whole program once, then the result is executed (C, C++).
- **Interpreter:** reads and executes the program **line by line** (**Python**). If line 3 contains an error, lines 1 and 2 have already run.

### 3. Python in a few words
- Created in **1991** by the Dutch programmer **Guido van Rossum**.
- **Free and open source**: anyone can install it, at home or at work.
- **Readable**: its syntax is close to English, which makes it ideal for beginners.
- **Rich libraries** (ready-made tools): pandas, NumPy, Matplotlib, Statsmodels, scikit-learn…
- One of the most used languages in the world for **data analysis** and **artificial intelligence**.

### 4. Why does Python matter in economics?
Economists, accountants and financial analysts work with **data**: prices, sales, GDP, exchange rates, balance sheets, surveys. Python lets them process this data **quickly, without errors and in a reproducible way**.

| Task | With a calculator or by hand | With Python |
|---|---|---|
| Compute the VAT of 5 000 invoices | Hours, risk of mistakes | One line, a few seconds |
| Average, median, standard deviation of a series | Long calculations | `mean()`, `median()`, `std()` |
| Draw the evolution of inflation | Manual drawing | A chart in three lines |
| Update the same report every month | Redo everything | Re-run the program |

Typical uses:
- **Economics:** statistics, econometrics (regressions), forecasting, simulation of economic models.
- **Accounting:** automating Excel reports, checking and reconciling statements, cleaning large ledgers.
- **Finance:** returns, interest and loan schedules, portfolio and risk analysis.
- **Artificial intelligence:** prediction and classification (studied in *Programming Basics 2*).

### 5. The working environment (IDE)
An **IDE** (*Integrated Development Environment*) is a program that gathers everything needed to code: an **editor** with colours and suggestions, a button to **run** the code, and tools to **find errors**.

**Visual Studio Code (VS Code)**
- Free, light and very popular editor (Microsoft).
- With the **Python extension**, it colours the code, suggests corrections and runs a file with ▶.
- Ideal for complete programs saved as `.py` files.

**Jupyter Notebook**
- An interactive **notebook** that opens in the web browser.
- The code is written in **cells**; each cell is run separately and its result appears just below it.
- You can mix code, text and charts: perfect for **data analysis** and for revising a course.

Other environments: **IDLE** (simple editor installed with Python), **Google Colab** (Jupyter online, with a Google account) and **this platform**, where Python runs directly in your browser.

### 6. Installing Python and running the editor
**Step 1: install Python**
1. Go to **python.org/downloads** and download the latest version for your system.
2. **Windows:** in the first window, tick ✅ **"Add python.exe to PATH"**, then click **Install Now**.
3. Check: open the *Command Prompt* (`cmd`) and type:
```
python --version
```
The answer looks like `Python 3.13.0`. On macOS or Linux, type `python3 --version`.

**Step 2: install and configure VS Code**
1. Download it from **code.visualstudio.com** and install it.
2. Open the **Extensions** menu (four squares icon), search for **Python** (publisher: Microsoft) and click **Install**.
3. *File → New File*, save it as `hello.py`, write `print("Hello, Python!")` and press ▶ (*Run Python File*).

**Step 3: install and launch Jupyter Notebook**
1. In the command prompt, type:
```
pip install notebook
```
2. Launch it with:
```
jupyter notebook
```
3. The browser opens: choose *New → Python 3*, type a line in a cell and press **Shift + Enter**.

> **Tip:** the **Anaconda** distribution installs Python, Jupyter and the data-analysis libraries all at once. **No computer?** Use this platform or Google Colab on a phone.

### Summary
Programming means giving a computer precise instructions. Python is a free, readable, interpreted language, very widely used in economics, accounting and finance. We write it in an IDE such as **VS Code** (programs) or **Jupyter Notebook** (interactive analysis). Next week: **algorithms**, the method used to design a program before writing it.
''',
r'''
### 1. Qu'est-ce que la programmation ?
Un ordinateur est très rapide mais n'a aucune initiative : il fait **exactement** ce qu'on lui demande, ni plus ni moins.

- La **programmation** est l'activité qui consiste à écrire des instructions précises pour qu'un ordinateur résolve un problème ou réalise une tâche.
- Un **programme** est l'ensemble ordonné de ces instructions. Le texte que l'on écrit s'appelle le **code** (ou *code source*).
- Un **langage de programmation** est le vocabulaire et la grammaire utilisés pour écrire ces instructions : Python, R, Java, C…

> **Analogie :** une recette de cuisine est un « programme » pour le cuisinier. Les ingrédients sont les **données**, les étapes sont les **instructions** et le plat est le **résultat**. Si une étape est floue ou manquante, le plat est raté : c'est pareil pour un programme.

### 2. Du langage humain au langage machine
Un processeur ne comprend que le **langage machine** (des suites de 0 et de 1). On écrit donc dans un langage lisible par l'humain, puis un outil le traduit.

| Niveau | Description | Exemples |
|---|---|---|
| Bas niveau | Proche de la machine, difficile à lire | Code machine, Assembleur |
| Haut niveau | Proche du langage humain, facile à lire | **Python**, R, Java, C++ |

Deux façons de traduire un programme de haut niveau :
- **Compilateur :** traduit tout le programme en une fois, puis le résultat est exécuté (C, C++).
- **Interpréteur :** lit et exécute le programme **ligne par ligne** (**Python**). Si la ligne 3 contient une erreur, les lignes 1 et 2 ont déjà été exécutées.

### 3. Python en quelques mots
- Créé en **1991** par le programmeur néerlandais **Guido van Rossum**.
- **Gratuit et open source** : tout le monde peut l'installer, chez soi ou au travail.
- **Lisible** : sa syntaxe est proche de l'anglais, ce qui le rend idéal pour débuter.
- **Riches bibliothèques** (outils prêts à l'emploi) : pandas, NumPy, Matplotlib, Statsmodels, scikit-learn…
- L'un des langages les plus utilisés au monde pour l'**analyse de données** et l'**intelligence artificielle**.

### 4. Pourquoi Python est-il important en économie ?
Économistes, comptables et analystes financiers travaillent avec des **données** : prix, ventes, PIB, taux de change, bilans, enquêtes. Python permet de traiter ces données **rapidement, sans erreur et de façon reproductible**.

| Tâche | À la calculatrice ou à la main | Avec Python |
|---|---|---|
| Calculer la TVA de 5 000 factures | Des heures, risque d'erreurs | Une ligne, quelques secondes |
| Moyenne, médiane, écart-type d'une série | Calculs longs | `mean()`, `median()`, `std()` |
| Tracer l'évolution de l'inflation | Dessin manuel | Un graphique en trois lignes |
| Mettre à jour le même rapport chaque mois | Tout refaire | Relancer le programme |

Usages typiques :
- **Économie :** statistiques, économétrie (régressions), prévision, simulation de modèles économiques.
- **Comptabilité :** automatiser les rapports Excel, contrôler et rapprocher les relevés, nettoyer de gros journaux comptables.
- **Finance :** rendements, intérêts et tableaux d'amortissement, analyse de portefeuille et de risque.
- **Intelligence artificielle :** prévision et classification (étudiées en *Bases de la programmation 2*).

### 5. L'environnement de travail (IDE)
Un **IDE** (*environnement de développement intégré*) est un logiciel qui réunit tout le nécessaire pour coder : un **éditeur** avec couleurs et suggestions, un bouton pour **exécuter** le code et des outils pour **trouver les erreurs**.

**Visual Studio Code (VS Code)**
- Éditeur gratuit, léger et très populaire (Microsoft).
- Avec l'**extension Python**, il colore le code, propose des corrections et exécute un fichier avec ▶.
- Idéal pour des programmes complets enregistrés en fichiers `.py`.

**Jupyter Notebook**
- Un **carnet** interactif qui s'ouvre dans le navigateur web.
- Le code s'écrit dans des **cellules** ; chaque cellule s'exécute séparément et son résultat s'affiche juste en dessous.
- On peut mélanger code, texte et graphiques : parfait pour l'**analyse de données** et pour réviser un cours.

Autres environnements : **IDLE** (éditeur simple installé avec Python), **Google Colab** (Jupyter en ligne, avec un compte Google) et **cette plateforme**, où Python s'exécute directement dans ton navigateur.

### 6. Installer Python et lancer l'éditeur
**Étape 1 : installer Python**
1. Va sur **python.org/downloads** et télécharge la dernière version pour ton système.
2. **Windows :** dans la première fenêtre, coche ✅ **« Add python.exe to PATH »**, puis clique sur **Install Now**.
3. Vérifie : ouvre l'*invite de commandes* (`cmd`) et tape :
```
python --version
```
La réponse ressemble à `Python 3.13.0`. Sous macOS ou Linux, tape `python3 --version`.

**Étape 2 : installer et configurer VS Code**
1. Télécharge-le sur **code.visualstudio.com** et installe-le.
2. Ouvre le menu **Extensions** (icône à quatre carrés), cherche **Python** (éditeur : Microsoft) et clique sur **Install**.
3. *File → New File*, enregistre le fichier sous `hello.py`, écris `print("Hello, Python!")` et clique sur ▶ (*Run Python File*).

**Étape 3 : installer et lancer Jupyter Notebook**
1. Dans l'invite de commandes, tape :
```
pip install notebook
```
2. Lance-le avec :
```
jupyter notebook
```
3. Le navigateur s'ouvre : choisis *New → Python 3*, tape une ligne dans une cellule et appuie sur **Maj + Entrée**.

> **Astuce :** la distribution **Anaconda** installe en une fois Python, Jupyter et les bibliothèques d'analyse de données. **Pas d'ordinateur ?** Utilise cette plateforme ou Google Colab sur un téléphone.

### À retenir
Programmer, c'est donner à un ordinateur des instructions précises. Python est un langage gratuit, lisible et interprété, très utilisé en économie, en comptabilité et en finance. On l'écrit dans un IDE comme **VS Code** (programmes) ou **Jupyter Notebook** (analyse interactive). La semaine prochaine : les **algorithmes**, la méthode pour concevoir un programme avant de l'écrire.
''',
r'''
### 1. ما هي البرمجة؟
الحاسوب سريع جداً لكنه لا يملك أي مبادرة: ينفّذ **بالضبط** ما نطلبه منه، لا أكثر ولا أقل.

- **البرمجة** هي كتابة تعليمات دقيقة ليحلّ الحاسوب مشكلة أو ينجز مهمة.
- **البرنامج** هو مجموعة مرتّبة من هذه التعليمات. والنص الذي نكتبه يسمّى **الكود** (أو *الشيفرة المصدرية*).
- **لغة البرمجة** هي المفردات والقواعد التي نكتب بها هذه التعليمات: Python، R، Java، C…

> **تشبيه:** وصفة الطبخ هي «برنامج» للطبّاخ. المكوّنات هي **البيانات**، والخطوات هي **التعليمات**، والطبق هو **النتيجة**. إذا كانت خطوة غامضة أو ناقصة فسد الطبق، وكذلك البرنامج.

### 2. من لغة الإنسان إلى لغة الآلة
المعالج لا يفهم إلا **لغة الآلة** (سلاسل من 0 و1). لذلك نكتب بلغة يقرؤها الإنسان، ثم تقوم أداة بترجمتها.

| المستوى | الوصف | أمثلة |
|---|---|---|
| منخفض المستوى | قريب من الآلة، صعب القراءة | لغة الآلة، Assembly |
| عالي المستوى | قريب من لغة الإنسان، سهل القراءة | **Python**، R، Java، C++ |

طريقتان لترجمة برنامج عالي المستوى:
- **المترجم (Compiler):** يترجم البرنامج كاملاً دفعة واحدة، ثم تُنفَّذ النتيجة (C، C++).
- **المفسّر (Interpreter):** يقرأ البرنامج وينفّذه **سطراً بسطر** (**Python**). إذا كان في السطر 3 خطأ، فإن السطرين 1 و2 قد نُفّذا قبله.

### 3. Python في سطور
- أنشأها المبرمج الهولندي **Guido van Rossum** سنة **1991**.
- **مجانية ومفتوحة المصدر**: يمكن لأي شخص تثبيتها في البيت أو العمل.
- **سهلة القراءة**: قواعدها قريبة من اللغة الإنجليزية، مما يجعلها مثالية للمبتدئين.
- **مكتبات غنية** (أدوات جاهزة): pandas، NumPy، Matplotlib، Statsmodels، scikit-learn…
- من أكثر اللغات استخداماً في العالم في **تحليل البيانات** و**الذكاء الاصطناعي**.

### 4. أهمية Python في الاقتصاد
يعمل الاقتصاديون والمحاسبون والمحلّلون الماليون على **البيانات**: الأسعار، المبيعات، الناتج المحلي الإجمالي، أسعار الصرف، الميزانيات، الاستبيانات. وتسمح Python بمعالجة هذه البيانات **بسرعة ودون أخطاء وبطريقة قابلة لإعادة الإنتاج**.

| المهمة | بالآلة الحاسبة أو يدوياً | باستخدام Python |
|---|---|---|
| حساب الرسم على القيمة المضافة لـ 5000 فاتورة | ساعات، مع خطر الأخطاء | سطر واحد، بضع ثوانٍ |
| المتوسط والوسيط والانحراف المعياري لسلسلة | حسابات طويلة | `mean()`، `median()`، `std()` |
| رسم تطوّر التضخم | رسم يدوي | منحنى في ثلاثة أسطر |
| تحديث التقرير نفسه كل شهر | إعادة كل شيء | إعادة تشغيل البرنامج |

استخدامات نموذجية:
- **الاقتصاد:** الإحصاء، الاقتصاد القياسي (الانحدار)، التنبؤ، محاكاة النماذج الاقتصادية.
- **المحاسبة:** أتمتة تقارير Excel، مراقبة الكشوف ومطابقتها، تنظيف دفاتر محاسبية كبيرة.
- **المالية:** العوائد، الفوائد وجداول اهتلاك القروض، تحليل المحافظ والمخاطر.
- **الذكاء الاصطناعي:** التنبؤ والتصنيف (يُدرَس في *أساسيات البرمجة 2*).

### 5. بيئة العمل (IDE)
**بيئة التطوير المتكاملة (IDE)** برنامج يجمع كل ما نحتاجه للبرمجة: **محرّر** بألوان واقتراحات، وزرّ **لتنفيذ** الكود، وأدوات **لاكتشاف الأخطاء**.

**Visual Studio Code (VS Code)**
- محرّر مجاني وخفيف وواسع الانتشار (من Microsoft).
- مع **إضافة Python** يلوّن الكود ويقترح التصحيحات وينفّذ الملف بالزر ▶.
- مثالي للبرامج الكاملة المحفوظة في ملفات `.py`.

**Jupyter Notebook**
- **دفتر** تفاعلي يُفتح في متصفح الويب.
- يُكتب الكود في **خلايا**، وتُنفَّذ كل خلية على حدة وتظهر نتيجتها تحتها مباشرة.
- يمكن الجمع بين الكود والنص والمنحنيات: مثالي **لتحليل البيانات** ولمراجعة الدروس.

بيئات أخرى: **IDLE** (محرّر بسيط يأتي مع Python)، و**Google Colab** (Jupyter عبر الإنترنت بحساب Google)، و**هذه المنصة** التي يعمل فيها Python مباشرة داخل متصفحك.

### 6. تثبيت Python وتشغيل المحرّر
**الخطوة 1: تثبيت Python**
1. ادخل إلى **python.org/downloads** وحمّل آخر نسخة لنظام تشغيلك.
2. **في Windows:** في النافذة الأولى ضع علامة ✅ على **«Add python.exe to PATH»** ثم اضغط **Install Now**.
3. للتحقق: افتح *موجّه الأوامر* (`cmd`) واكتب:
```
python --version
```
يظهر جواب مثل `Python 3.13.0`. في macOS أو Linux اكتب `python3 --version`.

**الخطوة 2: تثبيت VS Code وإعداده**
1. حمّله من **code.visualstudio.com** وثبّته.
2. افتح قائمة **Extensions** (أيقونة المربعات الأربعة)، وابحث عن **Python** (الناشر: Microsoft) واضغط **Install**.
3. *File → New File*، احفظ الملف باسم `hello.py`، واكتب `print("Hello, Python!")` ثم اضغط ▶ (*Run Python File*).

**الخطوة 3: تثبيت Jupyter Notebook وتشغيله**
1. في موجّه الأوامر اكتب:
```
pip install notebook
```
2. شغّله بالأمر:
```
jupyter notebook
```
3. يُفتح المتصفح: اختر *New → Python 3*، واكتب سطراً في خلية ثم اضغط **Shift + Enter**.

> **نصيحة:** توزيعة **Anaconda** تثبّت Python وJupyter ومكتبات تحليل البيانات دفعة واحدة. **لا تملك حاسوباً؟** استخدم هذه المنصة أو Google Colab على الهاتف.

### الخلاصة
البرمجة هي إعطاء الحاسوب تعليمات دقيقة. Python لغة مجانية وسهلة القراءة ومفسَّرة، واسعة الاستخدام في الاقتصاد والمحاسبة والمالية. نكتبها في بيئة تطوير مثل **VS Code** (للبرامج) أو **Jupyter Notebook** (للتحليل التفاعلي). في الأسبوع القادم: **الخوارزميات**، أي طريقة تصميم البرنامج قبل كتابته.
'''),

    # ---------------------------------------------------------------- EXAMPLES
    "examples": [
        {
            "title": L("Python answers you", "Python te répond", "Python تجيبك"),
            "explain": L(
                "`print()` displays a message. The `sys` module tells us which version of Python is running. Press **Run**, then change the message and run again.",
                "`print()` affiche un message. Le module `sys` indique la version de Python utilisée. Clique sur **Exécuter**, puis modifie le message et relance.",
                "تعرض الدالة `print()` رسالة على الشاشة، ويخبرنا الموديول `sys` بنسخة Python المستعملة. اضغط **تشغيل**، ثم غيّر الرسالة وأعد التشغيل."),
            "code": '''# My very first lines of Python
print("Hello, Python!")
print("Bonjour, Python !")
print("مرحباً، Python!")

import sys
print("Python version:", sys.version.split()[0])
''',
        },
        {
            "title": L("Python as an economist's calculator", "Python, la calculatrice de l'économiste", "Python آلة حاسبة للاقتصادي"),
            "explain": L(
                "Three quick calculations an economics student meets every day. You do not need to understand every symbol yet: we will study them in weeks 4 and 5.",
                "Trois calculs rapides qu'un étudiant en économie rencontre tous les jours. Pas besoin de tout comprendre maintenant : nous les étudierons aux semaines 4 et 5.",
                "ثلاثة حسابات سريعة يصادفها طالب الاقتصاد يومياً. لا داعي لفهم كل الرموز الآن، سندرسها في الأسبوعين 4 و5."),
            "code": '''# 1) Growth rate of sales between two years
sales_2024 = 1_250_000
sales_2025 = 1_400_000
print("Growth rate (%):", (sales_2025 - sales_2024) / sales_2024 * 100)

# 2) Price including VAT (19 %)
print("Price incl. VAT (DZD):", 2500 * 1.19)

# 3) Average of three exam marks
print("Average:", (12 + 15 + 9) / 3)
''',
        },
        {
            "title": L("An interpreter works line by line", "Un interpréteur travaille ligne par ligne", "المفسّر يعمل سطراً بسطر"),
            "explain": L(
                "Line 3 contains a spelling mistake (`pritn`). Run the code: the first two lines are executed, then Python stops and shows an error message. Correct the mistake and run again.",
                "La ligne 3 contient une faute de frappe (`pritn`). Exécute le code : les deux premières lignes s'exécutent, puis Python s'arrête et affiche un message d'erreur. Corrige la faute et relance.",
                "في السطر 3 خطأ إملائي (`pritn`). نفّذ الكود: يُنفَّذ السطران الأولان ثم يتوقف Python ويعرض رسالة خطأ. صحّح الخطأ وأعد التشغيل."),
            "error_ok": True,   # the error is the point of this example
            "code": '''print("Line 1: executed")
print("Line 2: executed")
pritn("Line 3: is there a problem?")
print("Line 4: will I be executed?")
''',
        },
    ],

    # --------------------------------------------------------------- EXERCISES
    "exercises": [
        {
            "title": L("My first message", "Mon premier message", "رسالتي الأولى"),
            "task": L(
                "Write a program that displays exactly: `I am learning Python!`",
                "Écris un programme qui affiche exactement : `I am learning Python!`",
                "اكتب برنامجاً يعرض بالضبط: `I am learning Python!`"),
            "starter": "# Write your code below\n",
            "expected": "I am learning Python!",
            "hint": L("Use `print()` and put the text between quotes.", "Utilise `print()` et mets le texte entre guillemets.",
                      "استخدم `print()` وضع النص بين علامتي تنصيص."),
            "solution": 'print("I am learning Python!")\n',
        },
        {
            "title": L("Module identity card", "Fiche d'identité du module", "بطاقة تعريف المقياس"),
            "task": L(
                "Display these three lines, in this order:\n```\nModule: Programming Basics 1\nLanguage: Python\nSemester: 1\n```",
                "Affiche ces trois lignes, dans cet ordre :\n```\nModule: Programming Basics 1\nLanguage: Python\nSemester: 1\n```",
                "اعرض الأسطر الثلاثة التالية بهذا الترتيب:\n```\nModule: Programming Basics 1\nLanguage: Python\nSemester: 1\n```"),
            "starter": "# One print() per line\n",
            "expected": "Module: Programming Basics 1\nLanguage: Python\nSemester: 1",
            "hint": L("Write three `print()` instructions, one under the other.", "Écris trois instructions `print()`, l'une sous l'autre.",
                      "اكتب ثلاث تعليمات `print()` الواحدة تحت الأخرى."),
            "solution": 'print("Module: Programming Basics 1")\nprint("Language: Python")\nprint("Semester: 1")\n',
        },
        {
            "title": L("A firm's turnover", "Le chiffre d'affaires d'une entreprise", "رقم أعمال مؤسسة"),
            "task": L(
                "A firm sold **1 200** units at **350 DZD** each. Display its turnover (the number only).",
                "Une entreprise a vendu **1 200** unités à **350 DA** l'unité. Affiche son chiffre d'affaires (le nombre seulement).",
                "باعت مؤسسة **1200** وحدة بسعر **350 دج** للوحدة. اعرض رقم أعمالها (الرقم فقط)."),
            "starter": "# turnover = quantity * unit price\n",
            "expected": "420000",
            "hint": L("In Python, multiplication is written `*`: `print(1200 * 350)`.",
                      "En Python, la multiplication s'écrit `*` : `print(1200 * 350)`.",
                      "في Python يُكتب الضرب بالرمز `*`: `print(1200 * 350)`."),
            "solution": "print(1200 * 350)\n",
        },
    ],

    # -------------------------------------------------------------------- QUIZ
    "quiz": [
        {
            "q": L("What is a program?", "Qu'est-ce qu'un programme ?", "ما هو البرنامج؟"),
            "options": L(
                ["A piece of computer hardware", "An ordered set of instructions that a computer executes", "A type of internet connection", "A spreadsheet file"],
                ["Un composant matériel de l'ordinateur", "Un ensemble ordonné d'instructions exécutées par l'ordinateur", "Un type de connexion Internet", "Un fichier de tableur"],
                ["قطعة من مكوّنات الحاسوب", "مجموعة مرتّبة من التعليمات ينفّذها الحاسوب", "نوع من الاتصال بالإنترنت", "ملف جدول بيانات"]),
            "answer": 1,
            "explain": L("A program is written in a programming language and executed by the computer.",
                         "Un programme est écrit dans un langage de programmation et exécuté par l'ordinateur.",
                         "يُكتب البرنامج بلغة برمجة وينفّذه الحاسوب."),
        },
        {
            "q": L("How is Python code executed?", "Comment le code Python est-il exécuté ?", "كيف يُنفَّذ كود Python؟"),
            "options": L(
                ["By an interpreter, line by line", "By a compiler only, all at once", "It runs without any translation", "By the keyboard"],
                ["Par un interpréteur, ligne par ligne", "Uniquement par un compilateur, en une fois", "Il s'exécute sans aucune traduction", "Par le clavier"],
                ["بواسطة مفسّر، سطراً بسطر", "بواسطة مترجم فقط، دفعة واحدة", "يُنفَّذ دون أي ترجمة", "بواسطة لوحة المفاتيح"]),
            "answer": 0,
            "explain": L("Python is an interpreted language: an error on line 3 does not prevent lines 1 and 2 from running.",
                         "Python est un langage interprété : une erreur à la ligne 3 n'empêche pas les lignes 1 et 2 de s'exécuter.",
                         "Python لغة مفسَّرة: الخطأ في السطر 3 لا يمنع تنفيذ السطرين 1 و2."),
        },
        {
            "q": L("Which of these tools is an IDE?", "Lequel de ces outils est un IDE ?", "أيّ من هذه الأدوات بيئة تطوير (IDE)؟"),
            "options": L(["Microsoft Word", "Google Chrome", "Visual Studio Code", "Windows Explorer"],
                         ["Microsoft Word", "Google Chrome", "Visual Studio Code", "L'Explorateur Windows"],
                         ["Microsoft Word", "Google Chrome", "Visual Studio Code", "مستكشف Windows"]),
            "answer": 2,
            "explain": L("VS Code gathers an editor, a run button and error-finding tools.",
                         "VS Code réunit un éditeur, un bouton d'exécution et des outils pour trouver les erreurs.",
                         "يجمع VS Code بين محرّر وزرّ للتنفيذ وأدوات لاكتشاف الأخطاء."),
        },
        {
            "q": L("In Jupyter Notebook, how do you run a cell?", "Dans Jupyter Notebook, comment exécute-t-on une cellule ?",
                   "في Jupyter Notebook، كيف تُنفَّذ الخلية؟"),
            "options": L(["Ctrl + S", "Shift + Enter", "Alt + F4", "Ctrl + P"], ["Ctrl + S", "Maj + Entrée", "Alt + F4", "Ctrl + P"],
                         ["Ctrl + S", "Shift + Enter", "Alt + F4", "Ctrl + P"]),
            "answer": 1,
            "explain": L("Shift + Enter runs the cell and moves to the next one.", "Maj + Entrée exécute la cellule et passe à la suivante.",
                         "Shift + Enter ينفّذ الخلية وينتقل إلى الخلية الموالية."),
        },
        {
            "q": L("When installing Python on Windows, which option must be ticked?",
                   "Lors de l'installation de Python sous Windows, quelle option faut-il cocher ?",
                   "عند تثبيت Python في Windows، ما الخيار الذي يجب تحديده؟"),
            "options": L(["Add python.exe to PATH", "Install Microsoft Office", "Disable the antivirus", "Restart in safe mode"],
                         ["Add python.exe to PATH", "Installer Microsoft Office", "Désactiver l'antivirus", "Redémarrer en mode sans échec"],
                         ["Add python.exe to PATH", "تثبيت Microsoft Office", "تعطيل مضاد الفيروسات", "إعادة التشغيل في الوضع الآمن"]),
            "answer": 0,
            "explain": L("This option lets you type `python` in any command prompt.",
                         "Cette option permet de taper `python` dans n'importe quelle invite de commandes.",
                         "يسمح هذا الخيار بكتابة `python` في أي موجّه أوامر."),
        },
        {
            "q": L("Which command checks the installed version of Python?", "Quelle commande vérifie la version de Python installée ?",
                   "ما الأمر الذي يتحقّق من نسخة Python المثبّتة؟"),
            "options": ["pip install notebook", "jupyter notebook", "print(version)", "python --version"],
            "answer": 3,
            "explain": L("`pip install notebook` installs Jupyter and `jupyter notebook` launches it.",
                         "`pip install notebook` installe Jupyter et `jupyter notebook` le lance.",
                         "`pip install notebook` يثبّت Jupyter و`jupyter notebook` يشغّله."),
        },
        {
            "q": L("Why is Python useful to an accountant or an economist?", "Pourquoi Python est-il utile à un comptable ou à un économiste ?",
                   "لماذا تفيد Python المحاسب أو الاقتصادي؟"),
            "options": L(
                ["It replaces the need to understand economics", "It processes large amounts of data quickly and reproducibly",
                 "It only works for video games", "It is only used to build websites"],
                ["Elle dispense de comprendre l'économie", "Elle traite de grandes quantités de données rapidement et de façon reproductible",
                 "Elle ne sert qu'aux jeux vidéo", "Elle sert uniquement à créer des sites web"],
                ["تغني عن فهم الاقتصاد", "تعالج كميات كبيرة من البيانات بسرعة وبطريقة قابلة لإعادة الإنتاج",
                 "لا تصلح إلا لألعاب الفيديو", "تُستعمل فقط لإنشاء مواقع الويب"]),
            "answer": 1,
            "explain": L("Python automates calculations and reports; the economic reasoning remains yours.",
                         "Python automatise les calculs et les rapports ; le raisonnement économique reste le tien.",
                         "تؤتمت Python الحسابات والتقارير، أما التحليل الاقتصادي فيبقى من عملك أنت."),
        },
    ],
}
