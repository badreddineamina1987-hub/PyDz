"""
WEEK 13 · Prompt engineering and its applications in programming  (level: very easy)
Programme: using AI tools to generate applied code.
"""
from syllabus import L

WEEK = {
    "objectives": L(
        [
            "**Explain** what a prompt is.",
            "**Write** a clear prompt with 5 parts: role, task, data, constraints, format.",
            "**Ask** an AI assistant to generate, explain or correct Python code.",
            "**Test** the code given by the AI before trusting it.",
            "**Use** AI honestly and safely.",
        ],
        [
            "**Expliquer** ce qu'est un prompt.",
            "**Écrire** un prompt clair en 5 parties : rôle, tâche, données, contraintes, format.",
            "**Demander** à un assistant IA de générer, expliquer ou corriger du code Python.",
            "**Tester** le code donné par l'IA avant de lui faire confiance.",
            "**Utiliser** l'IA de façon honnête et prudente.",
        ],
        [
            "**يشرح** ما هو الأمر الموجّه (prompt).",
            "**يكتب** أمراً واضحاً من 5 أجزاء: الدور، المهمة، البيانات، القيود، الشكل.",
            "**يطلب** من مساعد ذكاء اصطناعي توليد كود Python أو شرحه أو تصحيحه.",
            "**يختبر** الكود الذي يقدّمه الذكاء الاصطناعي قبل الوثوق به.",
            "**يستعمل** الذكاء الاصطناعي بنزاهة وحذر.",
        ],
    ),

    "lesson": L(
r'''
### 1. AI assistants and prompts
Tools like **ChatGPT**, **Claude**, **Gemini** or **Copilot** can write Python code for you.
A **prompt** is the **message** (the question or instruction) you write to the AI.
👉 **A clear prompt = a better answer.**

### 2. Bad prompt, good prompt
❌ *"Python code for a loan"*

✅ *"You are a Python teacher for economics students. Write a short Python program that computes the monthly payment of a loan. Data: amount 1 000 000 DZD, yearly rate 6 %, duration 5 years. Use only variables and the formula, no library. Add a comment on each line and display the result rounded to 2 decimals."*

### 3. The 5 parts of a good prompt
| Part | Question | Example |
|---|---|---|
| **Role** | Who should the AI be? | "You are a Python teacher" |
| **Task** | What must it do? | "Write a program that computes…" |
| **Data** | With which values? | "amount 1 000 000 DZD, rate 6 %" |
| **Constraints** | What limits? | "no library, beginner level" |
| **Format** | How to present it? | "comments on each line, rounded result" |

### 4. Useful prompts for a student
- **Generate:** "Write a Python function that computes the VAT of a price."
- **Explain:** "Explain this code line by line, simply: …"
- **Correct:** "My code gives this error: … Here is the code: … What is wrong?"
- **Improve:** "Make this code clearer and add comments."
- **Practise:** "Give me 3 easy exercises on Python loops with economic examples."

### 5. Always test the AI's code
The AI can make **mistakes**, even when it sounds very sure.
1. **Read** the code: do you understand each line?
2. **Run** it.
3. **Check** with a case you know by heart. Example: the average of 10 and 20 must be 15.
4. If it is wrong, **say it** to the AI and ask again.

### 6. Rules of good use
- 🔒 Never give **personal or confidential data** (names, passwords, real company accounts).
- 🎓 The AI helps you **learn**; it does not do your exam. Say when you used it.
- 🧠 If you cannot explain the code, you have not learned it yet.

> **Remember:** good prompt → test → understand → improve.
''',
r'''
### 1. Les assistants IA et les prompts
Des outils comme **ChatGPT**, **Claude**, **Gemini** ou **Copilot** peuvent écrire du code Python pour toi.
Un **prompt** est le **message** (la question ou la consigne) que tu écris à l'IA.
👉 **Un prompt clair = une meilleure réponse.**

### 2. Mauvais prompt, bon prompt
❌ *« Code Python pour un prêt »*

✅ *« Tu es un professeur de Python pour des étudiants en économie. Écris un court programme Python qui calcule la mensualité d'un prêt. Données : montant 1 000 000 DA, taux annuel 6 %, durée 5 ans. Utilise seulement des variables et la formule, sans bibliothèque. Ajoute un commentaire sur chaque ligne et affiche le résultat arrondi à 2 décimales. »*

### 3. Les 5 parties d'un bon prompt
| Partie | Question | Exemple |
|---|---|---|
| **Rôle** | Qui doit être l'IA ? | « Tu es un professeur de Python » |
| **Tâche** | Que doit-elle faire ? | « Écris un programme qui calcule… » |
| **Données** | Avec quelles valeurs ? | « montant 1 000 000 DA, taux 6 % » |
| **Contraintes** | Quelles limites ? | « sans bibliothèque, niveau débutant » |
| **Format** | Comment présenter ? | « commentaires sur chaque ligne, résultat arrondi » |

### 4. Des prompts utiles pour un étudiant
- **Générer :** « Écris une fonction Python qui calcule la TVA d'un prix. »
- **Expliquer :** « Explique ce code ligne par ligne, simplement : … »
- **Corriger :** « Mon code donne cette erreur : … Voici le code : … Qu'est-ce qui ne va pas ? »
- **Améliorer :** « Rends ce code plus clair et ajoute des commentaires. »
- **S'entraîner :** « Donne-moi 3 exercices faciles sur les boucles Python avec des exemples économiques. »

### 5. Toujours tester le code de l'IA
L'IA peut se **tromper**, même quand elle a l'air très sûre d'elle.
1. **Lis** le code : comprends-tu chaque ligne ?
2. **Exécute-le**.
3. **Vérifie** avec un cas que tu connais par cœur. Exemple : la moyenne de 10 et 20 doit être 15.
4. Si c'est faux, **dis-le** à l'IA et redemande.

### 6. Règles de bon usage
- 🔒 Ne donne jamais de **données personnelles ou confidentielles** (noms, mots de passe, vrais comptes d'une entreprise).
- 🎓 L'IA t'aide à **apprendre** ; elle ne passe pas ton examen. Dis quand tu l'as utilisée.
- 🧠 Si tu ne sais pas expliquer le code, tu ne l'as pas encore appris.

> **À retenir :** bon prompt → tester → comprendre → améliorer.
''',
r'''
### 1. مساعدات الذكاء الاصطناعي والأوامر الموجّهة
أدوات مثل **ChatGPT** و**Claude** و**Gemini** و**Copilot** يمكنها كتابة كود Python لك.
**الأمر الموجّه (prompt)** هو **الرسالة** (السؤال أو التعليمة) التي تكتبها للذكاء الاصطناعي.
👉 **أمر واضح = إجابة أفضل.**

### 2. أمر سيئ وأمر جيد
❌ *«كود Python لقرض»*

✅ *«أنت أستاذ Python لطلبة الاقتصاد. اكتب برنامج Python قصيراً يحسب القسط الشهري لقرض. البيانات: المبلغ 1000000 دج، المعدل السنوي 6 %، المدة 5 سنوات. استعمل المتغيرات والصيغة فقط دون مكتبات. أضف تعليقاً على كل سطر واعرض النتيجة مقرّبة إلى رقمين بعد الفاصلة.»*

### 3. الأجزاء الخمسة للأمر الجيد
| الجزء | السؤال | مثال |
|---|---|---|
| **الدور** | من يجب أن يكون الذكاء الاصطناعي؟ | «أنت أستاذ Python» |
| **المهمة** | ماذا يجب أن يفعل؟ | «اكتب برنامجاً يحسب…» |
| **البيانات** | بأي قيم؟ | «المبلغ 1000000 دج، المعدل 6 %» |
| **القيود** | ما الحدود؟ | «دون مكتبات، مستوى مبتدئ» |
| **الشكل** | كيف يُعرض؟ | «تعليق على كل سطر، نتيجة مقرّبة» |

### 4. أوامر مفيدة للطالب
- **التوليد:** «اكتب دالة Python تحسب الرسم على القيمة المضافة لسعر.»
- **الشرح:** «اشرح هذا الكود سطراً بسطر وببساطة: …»
- **التصحيح:** «الكود يعطي هذا الخطأ: … هذا هو الكود: … ما المشكلة؟»
- **التحسين:** «اجعل هذا الكود أوضح وأضف تعليقات.»
- **التدرّب:** «أعطني 3 تمارين سهلة على حلقات Python بأمثلة اقتصادية.»

### 5. اختبر دائماً كود الذكاء الاصطناعي
قد **يخطئ** الذكاء الاصطناعي حتى عندما يبدو واثقاً جداً.
1. **اقرأ** الكود: هل تفهم كل سطر؟
2. **نفّذه**.
3. **تحقّق** بحالة تعرف نتيجتها. مثال: معدل 10 و20 يجب أن يكون 15.
4. إذا كان خاطئاً، **أخبر** الذكاء الاصطناعي واطلب من جديد.

### 6. قواعد الاستعمال الجيد
- 🔒 لا تعطِ أبداً **بيانات شخصية أو سرية** (أسماء، كلمات سر، حسابات حقيقية لمؤسسة).
- 🎓 الذكاء الاصطناعي يساعدك على **التعلّم** ولا يجتاز امتحانك بدلاً منك. صرّح عندما تستعمله.
- 🧠 إذا لم تستطع شرح الكود، فأنت لم تتعلّمه بعد.

> **تذكّر:** أمر جيد ← اختبار ← فهم ← تحسين.
'''),

    "examples": [
        {
            "title": L("Code generated from a good prompt", "Code généré à partir d'un bon prompt", "كود مولَّد من أمر جيد"),
            "explain": L("This is the kind of answer given to the good prompt of the lesson (monthly payment of a loan). Run it, then change the duration.",
                         "Voici le type de réponse donnée au bon prompt du cours (mensualité d'un prêt). Exécute-le, puis change la durée.",
                         "هذا نوع الإجابة على الأمر الجيد في الدرس (القسط الشهري لقرض). نفّذه ثم غيّر المدة."),
            "code": '''# Monthly payment of a loan
amount = 1000000          # borrowed amount (DZD)
yearly_rate = 0.06        # 6 % per year
years = 5                 # duration

r = yearly_rate / 12      # monthly rate
n = years * 12            # number of months

payment = amount * r / (1 - (1 + r) ** -n)
print("Monthly payment:", round(payment, 2), "DZD")
print("Total paid:", round(payment * n, 2), "DZD")
''',
        },
        {
            "title": L("Test the AI's code with a known case", "Tester le code de l'IA avec un cas connu", "اختبر كود الذكاء الاصطناعي بحالة معروفة"),
            "explain": L("The AI wrote this function. We test it with values whose answer we know: is it right?",
                         "L'IA a écrit cette fonction. On la teste avec des valeurs dont on connaît la réponse : est-elle juste ?",
                         "كتب الذكاء الاصطناعي هذه الدالة. نختبرها بقيم نعرف نتيجتها: هل هي صحيحة؟"),
            "code": '''# Function written by an AI
def growth_rate(old, new):
    return (new - old) / old * 100

# Tests with cases we know
print(growth_rate(100, 110))    # must be 10.0
print(growth_rate(200, 100))    # must be -50.0
print(growth_rate(50, 50))      # must be 0.0
''',
        },
        {
            "title": L("When the AI is wrong", "Quand l'IA se trompe", "عندما يخطئ الذكاء الاصطناعي"),
            "explain": L("This AI code looks fine, but the test shows a mistake: the average of 10, 20 and 30 should be 20. Find the error and fix it.",
                         "Ce code de l'IA a l'air correct, mais le test montre une erreur : la moyenne de 10, 20 et 30 devrait être 20. Trouve l'erreur et corrige-la.",
                         "يبدو كود الذكاء الاصطناعي هذا سليماً، لكن الاختبار يكشف خطأً: معدل 10 و20 و30 يجب أن يكون 20. اكتشف الخطأ وصحّحه."),
            "code": '''# Code written by an AI
def average(values):
    return sum(values) / 2

print(average([10, 20, 30]))    # must be 20.0
''',
        },
    ],

    "exercises": [
        {
            "title": L("Fix the AI's average", "Corrige la moyenne de l'IA", "صحّح معدل الذكاء الاصطناعي"),
            "task": L("The AI divides by 2 instead of by the number of values. Fix the function so `average([10, 20, 30])` displays `20.0`.",
                      "L'IA divise par 2 au lieu du nombre de valeurs. Corrige la fonction pour que `average([10, 20, 30])` affiche `20.0`.",
                      "يقسم الذكاء الاصطناعي على 2 بدل عدد القيم. صحّح الدالة حتى تعرض `average([10, 20, 30])` القيمة `20.0`."),
            "starter": "def average(values):\n    return sum(values) / 2\n\nprint(average([10, 20, 30]))\n",
            "expected": "20.0",
            "hint": L("Divide by `len(values)`.", "Divise par `len(values)`.", "اقسم على `len(values)`."),
            "solution": "def average(values):\n    return sum(values) / len(values)\n\nprint(average([10, 20, 30]))\n",
        },
        {
            "title": L("The AI forgot the VAT", "L'IA a oublié la TVA", "نسي الذكاء الاصطناعي الرسم"),
            "task": L("The prompt asked for the price **including 19 % VAT**, but the AI returns the price without VAT. Fix it so the program displays `5950.0`.",
                      "Le prompt demandait le prix **TTC (TVA 19 %)**, mais l'IA renvoie le prix hors taxe. Corrige pour que le programme affiche `5950.0`.",
                      "طلب الأمر السعر **بالرسم (19 %)**، لكن الذكاء الاصطناعي أرجع السعر دون رسم. صحّح حتى يعرض البرنامج `5950.0`."),
            "starter": "def price_ttc(quantity, unit_price):\n    return quantity * unit_price\n\nprint(price_ttc(2, 2500))\n",
            "expected": "5950.0",
            "hint": L("Multiply the result by `1.19`.", "Multiplie le résultat par `1.19`.", "اضرب النتيجة في `1.19`."),
            "solution": "def price_ttc(quantity, unit_price):\n    return quantity * unit_price * 1.19\n\nprint(price_ttc(2, 2500))\n",
        },
        {
            "title": L("A name error", "Une erreur de nom", "خطأ في الاسم"),
            "task": L("Run the AI's code: there is a `NameError`. Fix the name so it displays the profit `30000`.",
                      "Exécute le code de l'IA : il y a une `NameError`. Corrige le nom pour qu'il affiche le bénéfice `30000`.",
                      "نفّذ كود الذكاء الاصطناعي: هناك خطأ `NameError`. صحّح الاسم حتى يعرض الربح `30000`."),
            "starter": "revenue = 120000\ncosts = 90000\nprofit = revenue - cost\nprint(profit)\n",
            "expected": "30000",
            "hint": L("The variable is called `costs`, with an s.", "La variable s'appelle `costs`, avec un s.", "اسم المتغير `costs` بحرف s."),
            "solution": "revenue = 120000\ncosts = 90000\nprofit = revenue - costs\nprint(profit)\n",
        },
    ],

    "quiz": [
        {"q": L("What is a prompt?", "Qu'est-ce qu'un prompt ?", "ما هو الأمر الموجّه (prompt)؟"),
         "options": L(["The message you write to the AI", "A Python error", "A type of variable", "A library"],
                      ["Le message que tu écris à l'IA", "Une erreur Python", "Un type de variable", "Une bibliothèque"],
                      ["الرسالة التي تكتبها للذكاء الاصطناعي", "خطأ في Python", "نوع من المتغيرات", "مكتبة"]),
         "answer": 0,
         "explain": L("The prompt is your question or instruction.", "Le prompt est ta question ou ta consigne.", "الأمر هو سؤالك أو تعليمتك.")},
        {"q": L("Which prompt is the best?", "Quel prompt est le meilleur ?", "أي أمر هو الأفضل؟"),
         "options": L(["\"VAT code\"", "\"Python\"",
                       "\"Write a Python function that returns a price with 19 % VAT, with comments, beginner level\"", "\"Help me\""],
                      ["« Code TVA »", "« Python »",
                       "« Écris une fonction Python qui renvoie un prix avec 19 % de TVA, avec commentaires, niveau débutant »", "« Aide-moi »"],
                      ["«كود الرسم»", "«Python»", "«اكتب دالة Python تُرجع السعر مع رسم 19 %، مع تعليقات، بمستوى مبتدئ»", "«ساعدني»"]),
         "answer": 2,
         "explain": L("It gives the task, the data, the constraints and the format.", "Il donne la tâche, les données, les contraintes et le format.",
                      "يحدّد المهمة والبيانات والقيود والشكل.")},
        {"q": L("The AI gives you code. What do you do first?", "L'IA te donne du code. Que fais-tu d'abord ?",
                "أعطاك الذكاء الاصطناعي كوداً. ماذا تفعل أولاً؟"),
         "options": L(["Copy it into the exam", "Read, run and test it", "Trust it: AI is never wrong", "Delete it"],
                      ["Le copier dans l'examen", "Le lire, l'exécuter et le tester", "Lui faire confiance : l'IA ne se trompe jamais", "Le supprimer"],
                      ["أنسخه في الامتحان", "أقرؤه وأنفّذه وأختبره", "أثق به: الذكاء الاصطناعي لا يخطئ", "أحذفه"]),
         "answer": 1,
         "explain": L("AI can be wrong. Always test with a case you know.", "L'IA peut se tromper. Teste toujours avec un cas connu.",
                      "قد يخطئ الذكاء الاصطناعي. اختبر دائماً بحالة معروفة.")},
        {"q": L("Which information must you NOT give to an AI?", "Quelle information ne faut-il PAS donner à une IA ?",
                "ما المعلومة التي يجب ألا تعطيها للذكاء الاصطناعي؟"),
         "options": L(["The error message of your code", "The password of your bank account", "The formula of VAT", "An example of data you invented"],
                      ["Le message d'erreur de ton code", "Le mot de passe de ton compte bancaire", "La formule de la TVA", "Un exemple de données inventées"],
                      ["رسالة الخطأ في الكود", "كلمة سر حسابك البنكي", "صيغة الرسم على القيمة المضافة", "مثال لبيانات مخترعة"]),
         "answer": 1,
         "explain": L("Never share personal or confidential data.", "Ne partage jamais de données personnelles ou confidentielles.",
                      "لا تشارك أبداً بيانات شخصية أو سرية.")},
        {"q": L("In a prompt, \"no library, beginner level\" is…", "Dans un prompt, « sans bibliothèque, niveau débutant » est…",
                "في الأمر الموجّه، «دون مكتبات، مستوى مبتدئ» هو…"),
         "options": L(["the role", "the data", "a constraint", "the format"], ["le rôle", "les données", "une contrainte", "le format"],
                      ["الدور", "البيانات", "قيد", "الشكل"]),
         "answer": 2,
         "explain": L("It limits what the AI can use.", "Cela limite ce que l'IA peut utiliser.", "إنه يحدّ مما يستعمله الذكاء الاصطناعي.")},
        {"q": L("To test an average function, which case is useful?", "Pour tester une fonction de moyenne, quel cas est utile ?",
                "لاختبار دالة معدل، ما الحالة المفيدة؟"),
         "options": L(["average([10, 20]) must give 15", "Run it once without looking", "Ask a friend to guess", "No test is needed"],
                      ["average([10, 20]) doit donner 15", "L'exécuter une fois sans regarder", "Demander à un ami de deviner", "Aucun test n'est nécessaire"],
                      ["average([10, 20]) يجب أن تعطي 15", "تنفيذها مرة دون النظر", "الطلب من صديق أن يخمّن", "لا حاجة لأي اختبار"]),
         "answer": 0,
         "explain": L("A case whose answer you know shows if the code is right.", "Un cas dont tu connais la réponse montre si le code est juste.",
                      "حالة تعرف نتيجتها تبيّن إن كان الكود صحيحاً.")},
    ],
}
