"""Interface texts in English, French and Arabic."""
from syllabus import L

LANGS = {"fr": "Français", "en": "English", "ar": "العربية"}

AUTHOR = {
    "name": L("Dr. BADREDDINE Amina", "Dr BADREDDINE Amina", "د. بدر الدين أمينة"),
    "department": L("Department of Accounting and Financial Sciences",
                    "Département des sciences financières et de comptabilité",
                    "قسم العلوم المالية والمحاسبة"),
    "faculty": L("Faculty of Economics, Commercial and Management Sciences",
                 "Faculté des sciences économiques, commerciales et des sciences de gestion",
                 "كلية العلوم الاقتصادية والتجارية وعلوم التسيير"),
    "university": L("M'Hamed Bougara University of Boumerdes, Algeria",
                    "Université M'Hamed Bougara de Boumerdès, Algérie",
                    "جامعة امحمد بوقرة بومرداس، الجزائر"),
    "email": "badreddine.amina@yahoo.fr",
    "orcid": "https://orcid.org/0009-0008-4863-8034",
    "youtube": "https://www.youtube.com/channel/UCh2Dbga75K55XlP1bdLwS7g",
}

UI = {
    # navigation
    "nav_home": L("Home", "Accueil", "الرئيسية"),
    "nav_weeks": L("15 weeks", "15 semaines", "15 أسبوعاً"),
    "nav_syllabus": L("Syllabus", "Programme", "دليل المادة"),
    "nav_play": L("Playground", "Laboratoire", "المختبر"),
    "nav_progress": L("My progress", "Ma progression", "تقدّمي"),
    "nav_about": L("About", "À propos", "حول المنصة"),
    "brand_sub": L("Learn Python", "Apprendre Python", "تعلّم Python"),

    # home
    "hero_tag": L("Programming Basics 1 · Official programme", "Bases de la programmation 1 · Programme officiel",
                  "أساسيات البرمجة 1 · البرنامج الرسمي"),
    "hero_l1": L("Write code.", "Écris du code.", "اكتب الكود."),
    "hero_l2": L("Week by week.", "Semaine après semaine.", "أسبوعاً بعد أسبوع."),
    "hero_l3": L("Think like an economist.", "Pense en économiste.", "وفكّر كاقتصادي."),
    "hero_sub": L(
        "The 15 weeks of the ministerial programme, with lessons, code that runs in your browser, corrected exercises "
        "and quizzes. Examples come from economics, accounting and finance.",
        "Les 15 semaines du programme ministériel : cours, code exécutable dans ton navigateur, exercices corrigés "
        "et quiz. Les exemples viennent de l'économie, de la comptabilité et de la finance.",
        "الأسابيع الخمسة عشر للبرنامج الوزاري: دروس، وأكواد تعمل في متصفحك، وتمارين مصحّحة واختبارات قصيرة، "
        "بأمثلة من الاقتصاد والمحاسبة والمالية."),
    "cta_start": L("Start week 1", "Commencer la semaine 1", "ابدأ الأسبوع الأول"),
    "cta_continue": L("Continue: week {n}", "Continuer : semaine {n}", "واصل: الأسبوع {n}"),
    "cta_syllabus": L("See the programme", "Voir le programme", "اطّلع على البرنامج"),
    "stat_weeks": L("weeks", "semaines", "أسبوعاً"),
    "stat_langs": L("languages", "langues", "لغات"),
    "stat_install": L("installation", "installation", "تثبيت"),
    "next_tag": L("Your next week", "Ta prochaine semaine", "أسبوعك القادم"),
    "progress_label": L("{d} of 15 weeks completed", "{d} semaines sur 15 terminées", "{d} من 15 أسبوعاً مكتملة"),
    "journey_tag": L("Follow the programme", "Suis le programme", "اتّبع البرنامج"),
    "journey_title": L("Your 15-week journey", "Ton parcours en 15 semaines", "مسارك في 15 أسبوعاً"),
    "journey_link": L("Full syllabus", "Programme complet", "دليل المادة كاملاً"),
    "how_tag": L("How it works", "Comment ça marche", "كيف تعمل المنصة"),
    "how_title": L("One week = five steps", "Une semaine = cinq étapes", "كل أسبوع = خمس خطوات"),
    "how_steps": L(
        [("Objectives", "Know what you will be able to do."), ("Lesson", "A short, structured lesson."),
         ("Code lab", "Edit and run real Python code."), ("Exercises", "Your output is checked automatically."),
         ("Quiz", "Test yourself and follow your progress.")],
        [("Objectifs", "Sache ce que tu sauras faire."), ("Cours", "Une leçon courte et structurée."),
         ("Labo de code", "Modifie et exécute du vrai code Python."), ("Exercices", "Ta sortie est vérifiée automatiquement."),
         ("Quiz", "Teste-toi et suis ta progression.")],
        [("الأهداف", "اعرف ما ستصبح قادراً عليه."), ("الدرس", "درس قصير ومنظّم."),
         ("مختبر الكود", "عدّل ونفّذ كود Python حقيقياً."), ("التمارين", "تُصحَّح مخرجاتك تلقائياً."),
         ("الاختبار", "اختبر نفسك وتابع تقدّمك.")]),

    # premium access
    "lock_title": L("Premium content", "Contenu premium", "محتوى مدفوع"),
    "lock_text": L("Unlock all examples, exercises with automatic correction and quizzes of the 15 weeks, for one year.",
                   "Débloque tous les exemples, les exercices corrigés automatiquement et les quiz des 15 semaines, pendant un an.",
                   "افتح كل الأمثلة والتمارين المصحّحة تلقائياً والاختبارات للأسابيع الخمسة عشر، لمدة سنة."),
    "lock_has_ex": L("This week contains {n} exercises:", "Cette semaine contient {n} exercices :", "يحتوي هذا الأسبوع على {n} تمارين:"),
    "lock_has_quiz": L("This week's quiz: {n} questions with explanations.", "Le quiz de la semaine : {n} questions avec explications.",
                       "اختبار هذا الأسبوع: {n} أسئلة مع الشرح."),
    "lock_has_more_ex": L("{n} more examples to run this week.", "Encore {n} exemples à exécuter cette semaine.",
                          "{n} أمثلة أخرى للتنفيذ في هذا الأسبوع."),
    "code_label": L("Access code", "Code d'accès", "رمز الدخول"),
    "code_btn": L("Unlock", "Débloquer", "فتح المحتوى"),
    "code_ok": L("Premium access active until {d}.", "Accès premium actif jusqu'au {d}.", "الاشتراك المدفوع مفعّل حتى {d}."),
    "code_bad": L("This code is not valid. Check it and try again.", "Ce code n'est pas valide. Vérifie-le et réessaie.",
                  "هذا الرمز غير صالح. تحقّق منه وأعد المحاولة."),
    "code_expired": L("This code expired on {d}.", "Ce code a expiré le {d}.", "انتهت صلاحية هذا الرمز في {d}."),
    "how_to_buy": L("To get your access code, write to", "Pour obtenir ton code d'accès, écris à", "للحصول على رمز الدخول، راسل"),
    "premium": L("Premium", "Premium", "مدفوع"),

    # home: final project demo and offer
    "build_tag": L("What you will build", "Ce que tu vas construire", "ما ستبنيه"),
    "build_title": L("By week 15, you write programs like this one", "En semaine 15, tu écris des programmes comme celui-ci",
                     "في الأسبوع 15، ستكتب برامج مثل هذا"),
    "build_text": L("A small program that analyses a shop's monthly sales and prints a report. Press **Run**: it works right here, in your browser.",
                    "Un petit programme qui analyse les ventes mensuelles d'un magasin et affiche un rapport. Clique sur **Exécuter** : il fonctionne ici, dans ton navigateur.",
                    "برنامج صغير يحلّل المبيعات الشهرية لمتجر ويعرض تقريراً. اضغط **تشغيل**: يعمل هنا مباشرة في متصفحك."),
    "build_points": L(
        ["Lists to store the data (week 10)", "Loops to go through the months (week 7)", "Functions to compute totals and averages (week 8)",
         "Conditions to find the best and worst month (week 6)"],
        ["Des listes pour stocker les données (semaine 10)", "Des boucles pour parcourir les mois (semaine 7)",
         "Des fonctions pour calculer totaux et moyennes (semaine 8)", "Des conditions pour trouver le meilleur et le pire mois (semaine 6)"],
        ["قوائم لتخزين البيانات (الأسبوع 10)", "حلقات للمرور على الأشهر (الأسبوع 7)", "دوال لحساب المجاميع والمتوسطات (الأسبوع 8)",
         "شروط لإيجاد أفضل وأسوأ شهر (الأسبوع 6)"]),
    "offer_tag": L("Free or premium", "Gratuit ou premium", "مجاني أو مدفوع"),
    "offer_title": L("Start for free, unlock when you are ready", "Commence gratuitement, débloque quand tu es prêt",
                     "ابدأ مجاناً، وافتح المحتوى متى كنت مستعداً"),
    "free_name": L("Free", "Gratuit", "مجاني"),
    "free_list": L(["Objectives of the 15 weeks", "All the lessons", "The first example of each week", "The Python playground"],
                   ["Les objectifs des 15 semaines", "Tous les cours", "Le premier exemple de chaque semaine", "Le laboratoire Python"],
                   ["أهداف الأسابيع الخمسة عشر", "كل الدروس", "المثال الأول من كل أسبوع", "مختبر Python"]),
    "premium_list": L(["Everything in Free", "All the examples", "Exercises with automatic correction, hints and solutions",
                       "Quizzes with explanations", "Progress tracking", "1 year of access"],
                      ["Tout le contenu gratuit", "Tous les exemples", "Exercices corrigés automatiquement, indices et solutions",
                       "Quiz avec explications", "Suivi de la progression", "1 an d'accès"],
                      ["كل المحتوى المجاني", "كل الأمثلة", "تمارين مصحّحة تلقائياً مع تلميحات وحلول", "اختبارات مع الشرح",
                       "متابعة التقدّم", "سنة كاملة من الوصول"]),
    "per_year": L("1 year", "1 an", "سنة واحدة"),

    # weeks
    "week_n": L("Week {n}", "Semaine {n}", "الأسبوع {n}"),
    "available": L("Available", "Disponible", "متاح"),
    "soon": L("In preparation", "En préparation", "قيد الإعداد"),
    "done": L("Completed", "Terminée", "مكتمل"),
    "open": L("Open", "Ouvrir", "افتح"),
    "programme_box": L("Ministerial programme for this week", "Programme ministériel de la semaine", "محتوى البرنامج الوزاري لهذا الأسبوع"),
    "soon_text": L("The lesson, examples and exercises of this week are being prepared. Here is what the programme covers:",
                   "Le cours, les exemples et les exercices de cette semaine sont en préparation. Voici ce que couvre le programme :",
                   "الدرس والأمثلة والتمارين لهذا الأسبوع قيد الإعداد. هذا ما يغطيه البرنامج:"),
    "sec_objectives": L("Objectives", "Objectifs", "الأهداف"),
    "sec_lesson": L("Lesson", "Cours", "الدرس"),
    "sec_examples": L("Code lab", "Labo de code", "مختبر الكود"),
    "sec_exercises": L("Exercises", "Exercices", "التمارين"),
    "sec_quiz": L("Quiz", "Quiz", "اختبار قصير"),
    "after_week": L("By the end of this week, you will be able to:", "À la fin de cette semaine, tu seras capable de :",
                    "في نهاية هذا الأسبوع، ستكون قادراً على أن:"),
    "example": L("Example", "Exemple", "مثال"),
    "exercise": L("Exercise", "Exercice", "تمرين"),
    "task": L("Task", "Consigne", "المطلوب"),
    "hint": L("Hint", "Indice", "تلميح"),
    "solution": L("Show a possible solution", "Voir une solution possible", "عرض حل ممكن"),
    "solution_note": L("Try on your own first: you learn by making mistakes!", "Essaie d'abord seul : on apprend en se trompant !",
                       "حاول بنفسك أولاً: نتعلّم من أخطائنا!"),
    "mark_solved": L("I solved this exercise", "J'ai résolu cet exercice", "حللت هذا التمرين"),
    "prev": L("Previous week", "Semaine précédente", "الأسبوع السابق"),
    "next": L("Next week", "Semaine suivante", "الأسبوع التالي"),
    "back": L("All weeks", "Toutes les semaines", "كل الأسابيع"),
    "quiz_intro": L("Answer all the questions, then submit.", "Réponds à toutes les questions, puis valide.",
                    "أجب عن كل الأسئلة ثم اضغط إرسال."),
    "submit": L("Submit my answers", "Valider mes réponses", "إرسال الإجابات"),
    "score": L("Your score: **{s} / {n}**", "Ton score : **{s} / {n}**", "نتيجتك: **{s} / {n}**"),
    "correct": L("Correct", "Correct", "إجابة صحيحة"),
    "wrong": L("Not quite. Correct answer:", "Pas tout à fait. Bonne réponse :", "ليس تماماً. الإجابة الصحيحة:"),
    "unanswered": L("Please answer every question before submitting.", "Réponds à toutes les questions avant de valider.",
                    "يرجى الإجابة عن كل الأسئلة قبل الإرسال."),
    "great": L("Excellent work!", "Excellent travail !", "عمل ممتاز!"),
    "keep": L("Review the lesson and try again.", "Relis le cours et réessaie.", "راجع الدرس وأعد المحاولة."),
    "pass_note": L("A week counts as completed when you score at least half of the quiz.",
                   "Une semaine est terminée quand tu obtiens au moins la moitié des points du quiz.",
                   "يُعدّ الأسبوع مكتملاً عند الحصول على نصف نقاط الاختبار على الأقل."),

    # syllabus page
    "syl_title": L("Course syllabus", "Fiche de la matière", "دليل المادة التعليمية"),
    "syl_sub": L("Official programme, harmonised nationally.", "Programme officiel, harmonisé au niveau national.",
                 "البرنامج الرسمي الموحّد وطنياً."),
    "syl_id": L("Identification", "Identification", "التعرف على المادة"),
    "f_field": L("Field", "Domaine", "الميدان"), "f_branch": L("Branch", "Filière", "الفرع"),
    "f_level": L("Level", "Niveau", "المستوى"), "f_semester": L("Semester", "Semestre", "السداسي"),
    "f_unit": L("Teaching unit", "Unité d'enseignement", "وحدة التعليم"),
    "f_credits": L("Credits / coefficient", "Crédits / coefficient", "الرصيد / المعامل"),
    "f_volume": L("Weekly volume", "Volume horaire hebdomadaire", "الحجم الساعي الأسبوعي"),
    "syl_prereq": L("Prerequisites", "Prérequis", "المكتسبات"),
    "syl_goal": L("General objective", "Objectif général", "الهدف العام للمادة"),
    "syl_outcomes": L("Learning outcomes", "Objectifs d'apprentissage", "أهداف التعلم"),
    "syl_axes": L("Content of the module (axes)", "Contenu de la matière (axes)", "محتوى المادة التعليمية"),
    "syl_axis": L("Axis {n}", "Axe {n}", "المحور {n}"),
    "syl_weekly": L("Weekly programme", "Programme hebdomadaire", "البرنامج الأسبوعي"),
    "syl_eval": L("Assessment", "Évaluation", "طريقة التقييم"),
    "syl_ca": L("Continuous assessment, marked out of 20", "Contrôle continu, noté sur 20", "التقييم المستمر، على 20"),
    "syl_personal": L("Personal work", "Travail personnel", "الأعمال الشخصية المقررة للمادة"),
    "syl_exam_note": L("Final and make-up exams: dates set by the administration.",
                       "Examen final et rattrapage : dates fixées par l'administration.",
                       "امتحان نهاية السداسي والامتحان الاستدراكي: تحدّدهما الإدارة."),

    # playground
    "play_title": L("Python playground", "Laboratoire Python", "مختبر بايثون"),
    "play_text": L("A free editor to write and test any Python code. Pick a template or start from scratch.",
                   "Un éditeur libre pour écrire et tester n'importe quel code Python. Choisis un modèle ou pars de zéro.",
                   "محرّر حرّ لكتابة واختبار أيّ كود Python. اختر نموذجاً أو ابدأ من الصفر."),
    "template": L("Template", "Modèle", "النموذج"),
    "tpl_blank": L("Blank page", "Page blanche", "صفحة فارغة"),
    "tpl_hello": L("Hello", "Bonjour", "مرحباً"),
    "tpl_vat": L("VAT calculator", "Calcul de la TVA", "حساب الرسم على القيمة المضافة"),
    "tpl_input": L("Read values with input()", "Lire des valeurs avec input()", "قراءة القيم بـ input()"),

    # progress
    "progress_title": L("My progress", "Ma progression", "تقدّمي"),
    "progress_note": L("Your progress is kept while this browser tab stays open. Download it to keep a copy.",
                       "Ta progression est conservée tant que cet onglet reste ouvert. Télécharge-la pour en garder une copie.",
                       "يُحفظ تقدّمك ما دامت نافذة المتصفح مفتوحة. حمّله للاحتفاظ بنسخة."),
    "weeks_done": L("Weeks completed", "Semaines terminées", "الأسابيع المكتملة"),
    "avg_score": L("Average quiz score", "Score moyen aux quiz", "متوسط نتائج الاختبارات"),
    "ex_solved": L("Exercises solved", "Exercices résolus", "التمارين المحلولة"),
    "col_week": L("Week", "Semaine", "الأسبوع"),
    "col_quiz": L("Best quiz score", "Meilleur score", "أفضل نتيجة"),
    "col_ex": L("Exercises solved", "Exercices résolus", "التمارين المحلولة"),
    "download": L("Download my progress (CSV)", "Télécharger ma progression (CSV)", "تحميل تقدّمي (CSV)"),
    "reset_progress": L("Reset my progress", "Réinitialiser ma progression", "إعادة تعيين التقدّم"),

    # about
    "about_title": L("About the platform", "À propos de la plateforme", "حول المنصة"),
    "about_text": L(
        "**PyDZ** teaches Python step by step, through the 15 weeks of the official programme of **Programming Basics 1** "
        "(first year, semester 1, economics, commerce and management). Each week combines a lesson, code that runs in the "
        "browser, auto-checked exercises and a quiz, with examples from economics, accounting and finance. The platform is "
        "available in French, English and Arabic; the code always stays in English, as in professional practice.",
        "**PyDZ** enseigne Python pas à pas, à travers les 15 semaines du programme officiel de **Bases de la programmation 1** "
        "(première année, semestre 1, sciences économiques, commerciales et de gestion). Chaque semaine réunit un cours, du code "
        "exécutable dans le navigateur, des exercices corrigés automatiquement et un quiz, avec des exemples tirés de l'économie, "
        "de la comptabilité et de la finance. La plateforme existe en français, en anglais et en arabe ; le code reste toujours "
        "en anglais, comme dans la pratique professionnelle.",
        "تعلّم **PyDZ** لغة Python خطوة بخطوة عبر الأسابيع الخمسة عشر للبرنامج الرسمي لمقياس **أساسيات البرمجة 1** "
        "(السنة الأولى، السداسي الأول، العلوم الاقتصادية والتجارية وعلوم التسيير). يجمع كل أسبوع بين درس، وأكواد تعمل في المتصفح، "
        "وتمارين تُصحَّح تلقائياً، واختبار قصير، بأمثلة من الاقتصاد والمحاسبة والمالية. المنصة متاحة بالعربية والفرنسية والإنجليزية، "
        "ويبقى الكود دائماً بالإنجليزية كما في الممارسة المهنية."),
    "tech_title": L("How does the code run?", "Comment le code s'exécute-t-il ?", "كيف يُنفَّذ الكود؟"),
    "tech_text": L(
        "Python runs **inside your own browser** thanks to **Pyodide** (Python compiled to WebAssembly). Nothing to install, it "
        "even works on a phone. The first run downloads the interpreter (a few seconds), then the browser keeps it.",
        "Python s'exécute **dans ton propre navigateur** grâce à **Pyodide** (Python compilé en WebAssembly). Rien à installer, "
        "cela fonctionne même sur téléphone. La première exécution télécharge l'interpréteur (quelques secondes), puis le navigateur le garde.",
        "يعمل Python **داخل متصفحك** بفضل **Pyodide** (نسخة من Python مترجمة إلى WebAssembly). لا شيء للتثبيت، ويعمل حتى على الهاتف. "
        "يحمّل التشغيل الأول المفسّر (بضع ثوانٍ)، ثم يحتفظ به المتصفح."),
    "contact": L("Contact", "Contact", "التواصل"),
    "channel": L("YouTube channel", "Chaîne YouTube", "قناة YouTube"),
    "created_by": L("Created by", "Conçu par", "من إعداد"),
    "footer": L("All rights reserved", "Tous droits réservés", "جميع الحقوق محفوظة"),

    # code runner
    "run": L("Run", "Exécuter", "تشغيل"),
    "stop": L("Stop", "Arrêter", "إيقاف"),
    "reset": L("Reset", "Réinitialiser", "إعادة تعيين"),
    "copy": L("Copy", "Copier", "نسخ"),
    "copied": L("Copied!", "Copié !", "تم النسخ!"),
    "output": L("Output", "Sortie", "المخرجات"),
    "runnable": L("Runnable code", "Code exécutable", "كود قابل للتنفيذ"),
    "stdin_label": L("Program input: values read by input(), one per line",
                     "Entrées du programme : valeurs lues par input(), une par ligne",
                     "مدخلات البرنامج: القيم التي يقرؤها ⁦input()⁩، قيمة في كل سطر"),
    "first_run": L("The first run may take a few seconds to load Python.", "La première exécution peut prendre quelques secondes.",
                   "قد يستغرق التشغيل الأول بضع ثوانٍ لتحميل بايثون."),
    "loading": L("Loading the Python interpreter…", "Chargement de l'interpréteur Python…", "جارٍ تحميل مفسّر بايثون…"),
    "running": L("Running…", "Exécution…", "جارٍ التنفيذ…"),
    "done_t": L("Finished in {t} s", "Terminé en {t} s", "انتهى في {t} ثانية"),
    "stopped": L("Stopped. The interpreter will reload at the next run.", "Arrêté. L'interpréteur sera rechargé à la prochaine exécution.",
                 "تم الإيقاف. سيُعاد تحميل المفسّر في التشغيل القادم."),
    "no_output": L("(no output)", "(aucune sortie)", "(لا توجد مخرجات)"),
    "check_ok": L("Correct! Your output matches the expected result.", "Bravo ! Ta sortie correspond au résultat attendu.",
                  "أحسنت! مخرجاتك مطابقة للنتيجة المنتظرة."),
    "check_bad": L("Not yet. Expected output:", "Pas encore. Sortie attendue :", "ليس بعد. النتيجة المنتظرة:"),
    "load_fail": L("Could not load Python. Check your internet connection and try again.",
                   "Impossible de charger Python. Vérifie ta connexion Internet et réessaie.",
                   "تعذّر تحميل بايثون. تحقّق من اتصالك بالإنترنت وأعد المحاولة."),
}


def T(value, lang):
    """Text for the current language; values shared by all languages are returned unchanged."""
    if isinstance(value, dict) and set(value) == {"en", "fr", "ar"}:
        return value[lang]
    return value


def runner_texts(lang):
    keys = ["run", "stop", "reset", "copy", "copied", "output", "first_run", "loading", "running",
            "stopped", "no_output", "check_ok", "check_bad", "load_fail"]
    t = {k: UI[k][lang] for k in keys}
    t["done"] = UI["done_t"][lang]
    t["title"] = UI["runnable"][lang]
    t["stdin"] = UI["stdin_label"][lang]
    return t
