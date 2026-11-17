"""
Official syllabus of the module "Programming Basics 1" (أساسيات البرمجة 1),
first year, semester 1, Faculty of Economics, Commercial and Management Sciences.
Weekly titles follow the ministerial programme. Arabic wording is the official one.
"""


def L(en, fr, ar):
    return {"en": en, "fr": fr, "ar": ar}


MODULE = {
    "name": L("Programming Basics 1 (Python)", "Bases de la programmation 1 (Python)", "أساسيات البرمجة 1 (Python)"),
    "field": L("Economics, Commercial and Management Sciences",
               "Sciences économiques, commerciales et sciences de gestion",
               "العلوم الاقتصادية، التجارية وعلوم التسيير"),
    "branch": L("All branches", "Toutes les filières", "كل الفروع"),
    "level": L("First year (Licence)", "Première année (Licence)", "السنة الأولى"),
    "semester": L("Semester 1", "Semestre 1", "السداسي الأول"),
    "unit": L("Methodological unit", "Unité méthodologique", "وحدة منهجية"),
    "credits": "1", "coef": "1",
    "volume": L("3 h per week: 1 h 30 lecture + 1 h 30 practical work",
                "3 h par semaine : 1 h 30 de cours + 1 h 30 de travaux pratiques",
                "3 سا أسبوعياً: 1:30 محاضرة + 1:30 أعمال تطبيقية"),
    "prereq": L(
        ["Basic use of a computer", "Basic mathematics and descriptive statistics"],
        ["Utilisation de base d'un ordinateur", "Notions de base en mathématiques et en statistique descriptive"],
        ["مبادئ أولية في التعامل مع جهاز الحاسوب وتشغيله", "مبادئ أولية في الرياضيات والإحصاء الوصفي"],
    ),
    "goal": L(
        "Enable students to understand the basic concepts of programming and apply them with Python, by developing "
        "problem-solving and algorithm-design skills, understanding basic data structures and program flow control, and "
        "moving from procedural to object-oriented programming, so that they can build simple applications and analyse "
        "data in academic and professional contexts.",
        "Permettre à l'étudiant de comprendre les concepts fondamentaux de la programmation et de les appliquer avec Python, "
        "en développant des compétences en résolution de problèmes et en conception d'algorithmes, en maîtrisant les structures "
        "de données de base et le contrôle du flux d'un programme, et en passant de la programmation procédurale à la "
        "programmation orientée objet, afin de construire des applications simples et d'analyser des données dans des "
        "contextes académiques et professionnels.",
        "تمكين الطالب من فهم المفاهيم الأساسية للبرمجة وتطبيقها باستخدام لغة Python، وذلك من خلال تطوير مهارات حل المشكلات "
        "وتصميم الخوارزميات، وفهم هياكل البيانات الأساسية، والتحكم في تدفق البرنامج، والانتقال من البرمجة الإجرائية إلى "
        "البرمجة كائنية التوجه، بما يؤهله لبناء تطبيقات بسيطة وتحليل البيانات في السياقات الأكاديمية والعملية.",
    ),
    "outcomes": L(
        ["Introduce programming concepts and Python.",
         "Develop problem-solving skills through programming.",
         "Learn to design and implement algorithms."],
        ["Présenter les concepts de la programmation et Python.",
         "Développer les compétences de résolution de problèmes par la programmation.",
         "S'initier à la conception et à la mise en œuvre d'algorithmes."],
        ["تقديم مفاهيم البرمجة وPython.",
         "تطوير مهارات حل المشكلات باستخدام البرمجة.",
         "التعرف على تصميم وتنفيذ الخوارزميات."],
    ),
    "axes": L(
        ["Introduction to programming with Python", "Writing a first simple program in Python",
         "Variables and arithmetic operations", "Working with strings", "Lists and tuples",
         "Dictionaries and sets", "Prompt engineering and its applications in programming",
         "Working with files", "Final project"],
        ["Introduction à la programmation avec Python", "Écrire un premier programme simple en Python",
         "Les variables et les opérations arithmétiques", "Manipuler les chaînes de caractères", "Les listes et les tuples",
         "Les dictionnaires et les ensembles", "L'ingénierie des prompts et ses applications en programmation",
         "La manipulation des fichiers", "Projet final"],
        ["مدخل إلى البرمجة بلغة Python", "كتابة أول برنامج بسيط بلغة Python", "المتغيرات والعمليات الحسابية عليها",
         "التعامل مع النصوص (Strings)", "القوائم (Lists) والصفوف (Tuples)", "القواميس (Dictionaries) والمجموعات (Sets)",
         "هندسة الأوامر وتطبيقاتها في البرمجة", "التعامل مع الملفات", "مشروع نهائي"],
    ),
    # (label, value): final exam 40 %, continuous assessment 60 % marked out of 20
    "assessment": [
        (L("Final exam (lecture)", "Examen final (cours)", "الامتحان (وزن المحاضرة)"), "40 %"),
        (L("Continuous assessment (practical work)", "Contrôle continu (travaux pratiques)", "الأعمال الموجهة والتطبيقية"), "60 %"),
    ],
    "ca_detail": [
        (L("Project", "Projet", "تقييم بالمشاريع"), "15"),
        (L("Attendance", "Assiduité", "المواظبة (الحضور / الغياب)"), "3"),
        (L("Participation", "Participation", "عناصر أخرى (المشاركة)"), "2"),
    ],
    "personal_work": L(
        ["Solve exercises during practical sessions", "Solve exercises given as homework", "Oral evaluation questions",
         "Interactive questions on the Moodle platform", "Attendance and interaction on Moodle",
         "Chat and forum on the Moodle e-learning platform",
         "Collect data on a phenomenon and organise it by data type",
         "Use Python to build graphical and analytical presentations of different types of data"],
        ["Résolution d'exercices pendant les séances de TP", "Exercices à faire à la maison", "Interrogations orales",
         "Questions interactives sur la plateforme Moodle", "Présence et interaction sur Moodle",
         "Discussion et forum sur la plateforme d'enseignement Moodle",
         "Collecter des données sur un phénomène et les classer selon leur type",
         "Utiliser Python pour présenter graphiquement et analyser différents types de données"],
        ["حل تمارين خلال حصص الأعمال الموجهة", "حل تمارين مقدمة على شكل واجبات منزلية", "استجواب تقييمي",
         "تقييم الأسئلة التفاعلية للطلبة عبر منصة Moodle", "الحضور والتفاعل في منصة Moodle",
         "إنشاء دردشة ومنتدى في منصة Moodle للتعليم الالكتروني", "جمع بيانات حول ظاهرة ما وتبويبها حسب نوع البيانات",
         "استخدام برنامج Python لإعداد العرض البياني والتحليلي لأنواع مختلفة من البيانات"],
    ),
}

# token = the small piece of code shown on the week card; tone = card colour
WEEKS = [
    {"n": 1, "token": ">>>", "tone": "blue",
     "title": L("Introduction to programming with Python", "Introduction à la programmation avec Python", "مدخل إلى البرمجة بلغة Python"),
     "points": L(
         ["What programming is", "Why Python matters in economics", "The working environment (IDE): VS Code and Jupyter Notebook", "Installing Python and running the editor"],
         ["Définition de la programmation", "L'importance de Python en économie", "L'environnement de travail (IDE) : VS Code et Jupyter Notebook", "Installer Python et lancer l'éditeur"],
         ["تعريف علم البرمجة", "أهمية Python في الاقتصاد", "التعرف على بيئة العمل (IDE) مثل VS Code وJupyter Notebook", "تثبيت Python وتشغيل المحرر"])},
    {"n": 2, "token": "1→2→3", "tone": "orange",
     "title": L("Introduction to algorithms", "Introduction aux algorithmes", "مدخل للخوارزميات"),
     "points": L([], [], [])},
    {"n": 3, "token": "print()", "tone": "blue",
     "title": L("Writing a first simple program in Python", "Écrire un premier programme simple en Python", "كتابة أول برنامج بسيط بلغة Python"),
     "points": L(
         ['The "Hello, World!" program', "Syntax basics", "Running the program and fixing simple errors"],
         ['Le programme « Hello, World! »', "Les bases de la syntaxe", "Exécuter le programme et corriger les erreurs simples"],
         ['برنامج "Hello, World!"', "أساسيات تركيب الجمل (syntax)", "تشغيل البرنامج وتصحيح الأخطاء البسيطة"])},
    {"n": 4, "token": "x = 19", "tone": "orange",
     "title": L("Variables and data types", "Les variables et les types de données", "المتغيرات وأنواع البيانات"),
     "points": L(
         ["Data types (int, float, str, bool)", "Defining variables and naming rules", "Simple programs using variables and data types"],
         ["Les types de données (int, float, str, bool)", "Définir des variables et règles de nommage", "Programmes simples utilisant variables et types"],
         ["أنواع البيانات (int, float, str, bool)", "تعريف المتغيرات وقواعد التسمية", "كتابة برامج بسيطة تستخدم المتغيرات وأنواع البيانات"])},
    {"n": 5, "token": "a % b", "tone": "blue",
     "title": L("Arithmetic operations and mathematical functions", "Opérations arithmétiques et fonctions mathématiques", "العمليات الحسابية والدوال الرياضية"),
     "points": L(
         ["Arithmetic operations (+, -, *, /, %)", "The math library and mathematical functions", "Solving simple economic problems"],
         ["Les opérations arithmétiques (+, -, *, /, %)", "La bibliothèque math et les fonctions mathématiques", "Résoudre des problèmes économiques simples"],
         ["العمليات الحسابية (+, -, *, /, %)", "مكتبة math والدوال الرياضية", "تطبيقات لحل مسائل اقتصادية بسيطة"])},
    {"n": 6, "token": "if / else", "tone": "orange",
     "title": L("Program flow control: conditional statements", "Contrôle du flux : les instructions conditionnelles", "التحكم في تدفق البرنامج: جمل الشرط"),
     "points": L(
         ["if, else, elif", "Logical operators (and, or, not)", "Practical exercises on conditions"],
         ["if, else, elif", "Les opérateurs logiques (and, or, not)", "Exercices pratiques sur les conditions"],
         ["if، else، elif", "العوامل المنطقية (and, or, not)", "تمارين تطبيقية على الشروط"])},
    {"n": 7, "token": "for i in", "tone": "blue",
     "title": L("Loops", "Les boucles", "الحلقات التكرارية (Loops)"),
     "points": L(
         ["for and while loops", "Controlling loops (break, continue)", "Practical uses such as computing averages"],
         ["Les boucles for et while", "Contrôler les boucles (break, continue)", "Applications pratiques comme le calcul de moyennes"],
         ["حلقات for وwhile", "التحكم في الحلقات (break, continue)", "تطبيقات عملية مثل حساب المتوسطات"])},
    {"n": 8, "token": "def f():", "tone": "orange",
     "title": L("Functions", "Les fonctions", "الدوال (Functions)"),
     "points": L(
         ["Defining and using functions", "Passing parameters and return values", "Building functions for recurring problems"],
         ["Définir et utiliser des fonctions", "Paramètres et valeurs de retour", "Construire des fonctions pour des problèmes récurrents"],
         ["تعريف الدوال واستخدامها", "تمرير المعاملات والقيم الراجعة", "بناء دوال لحل مشاكل متكررة"])},
    {"n": 9, "token": '"abc"', "tone": "blue",
     "title": L("Working with strings", "Manipuler les chaînes de caractères", "التعامل مع النصوص (Strings)"),
     "points": L(
         ["What strings are and how to manipulate them", "Basic string functions (slice, upper, lower)", "Exercises on analysing text data"],
         ["Définition des chaînes et leur manipulation", "Fonctions de base (slice, upper, lower)", "Exercices d'analyse de données textuelles"],
         ["تعريف النصوص وطرق التلاعب بها", "دوال النصوص الأساسية (slice, upper, lower)", "تمارين على تحليل بيانات نصية"])},
    {"n": 10, "token": "[ , ]", "tone": "orange",
     "title": L("Lists and tuples", "Les listes et les tuples", "القوائم (Lists) والصفوف (Tuples)"),
     "points": L(
         ["Defining lists and tuples", "Operations on lists and iteration", "Storing economic data"],
         ["Définir des listes et des tuples", "Opérations sur les listes et parcours", "Stocker des données économiques"],
         ["تعريف القوائم والصفوف", "العمليات على القوائم والتكرار", "تطبيقات لتخزين البيانات الاقتصادية"])},
    {"n": 11, "token": "{ k: v }", "tone": "blue",
     "title": L("Dictionaries and sets", "Les dictionnaires et les ensembles", "القواميس (Dictionaries) والمجموعات (Sets)"),
     "points": L(
         ["The concept of dictionaries and sets", "Adding, deleting and searching in dictionaries", "Using dictionaries to represent related data"],
         ["Notion de dictionnaire et d'ensemble", "Ajouter, supprimer, rechercher dans un dictionnaire", "Représenter des données liées avec des dictionnaires"],
         ["مفهوم القواميس والمجموعات", "إضافة، حذف، بحث في القواميس", "استخدام القواميس في تمثيل بيانات مرتبطة"])},
    {"n": 12, "token": "class", "tone": "orange",
     "title": L("Object-oriented programming (OOP)", "La programmation orientée objet (POO)", "البرمجة كائنية التوجه (OOP)"),
     "points": L(
         ["Classes and objects", "Attributes and methods of a class", "Applied example: a financial company model"],
         ["Les classes et les objets", "Attributs et méthodes d'une classe", "Exemple appliqué : modèle d'une entreprise financière"],
         ["الفئات (Classes) والكائنات (Objects)", "خصائص وطرق الفئة", "مثال تطبيقي: نموذج شركة مالية"])},
    {"n": 13, "token": "AI → code", "tone": "blue",
     "title": L("Prompt engineering and its applications in programming", "L'ingénierie des prompts et ses applications en programmation", "هندسة الأوامر وتطبيقاتها في البرمجة"),
     "points": L(
         ["Using AI tools to generate applied code"],
         ["Utiliser les outils d'intelligence artificielle pour générer du code appliqué"],
         ["الاستعانة بأدوات الذكاء الاصطناعي لتوليد أكواد تطبيقية"])},
    {"n": 14, "token": "open()", "tone": "orange",
     "title": L("Working with files", "La manipulation des fichiers", "التعامل مع الملفات"),
     "points": L(
         ["Opening, reading and writing text files", "Practical work: saving and reading economic data"],
         ["Ouvrir, lire et écrire des fichiers texte", "Application : enregistrer et lire des données économiques"],
         ["فتح، قراءة وكتابة الملفات النصية", "تطبيق عملي على حفظ وقراءة بيانات اقتصادية"])},
    {"n": 15, "token": "project.py", "tone": "blue",
     "title": L("Final project", "Projet final", "مشروع نهائي"),
     "points": L(
         ["Combining the programming concepts", "Writing a program that analyses financial or economic data", "Presenting and discussing the project"],
         ["Intégrer les notions de programmation", "Écrire un programme qui analyse des données financières ou économiques", "Présenter et discuter le projet"],
         ["دمج مفاهيم البرمجة", "كتابة برنامج يحلل بيانات مالية أو اقتصادية", "عرض المشروع ومناقشته مع الطلاب"])},
]
