# Gemini Chatbot

Gemini Chatbot هو شات بوت مدعوم بالذكاء الاصطناعي مبني باستخدام Gemini 2 API وStreamlit. يهدف إلى توفير تجربة تفاعلية للمستخدمين من خلال الردود الذكية والدقيقة.

## التثبيت

1. تأكد من أنك قمت بتثبيت Python.
2. قم بتثبيت التبعيات عبر:
    ```bash
    pip install -r requirements.txt
    ```

3. قم بإعداد متغير البيئة `GOOGLE_API_KEY` قبل تشغيل التطبيق أو أضفه إلى ملف `/.streamlit/secrets.toml` الخاص بـ Streamlit.
   - مثال على تعيينه مؤقتًا في سطر الأوامر (لأنظمة Unix):
     ```bash
     export GOOGLE_API_KEY="your-secure-key"
     ```
   - أو أضف الملف `.streamlit/secrets.toml` بالمحتوى التالي:
     ```toml
     GOOGLE_API_KEY = "your-secure-key"
     GEMINI_MODEL = "gemini-pro"
     ```
   سيقرأ التطبيق القيمة بشكل آمن من `st.secrets` أو من متغير البيئة دون الحاجة لتضمين المفتاح داخل المستودع.

## الاستخدام

لتشغيل الشات بوت:
1. ابدأ التطبيق باستخدام Streamlit:
    ```bash
    streamlit run app.py
    ```

2. افتح المتصفح على الرابط الذي سيظهر في سطر الأوامر للوصول إلى الشات بوت.

> **ملاحظة:** يمكن التحكم في مستوى التسجيل عبر متغير البيئة `APP_LOG_LEVEL` (مثل `INFO` أو `DEBUG`) لمراقبة الأخطاء والتصرف أثناء التشغيل.

## المساهمة

إذا كنت ترغب في المساهمة في المشروع:
1. قم بعمل Fork لهذا المستودع.
2. اعمل على التعديلات في الفرع الخاص بك.
3. أرسل Pull Request مع شرح التعديلات التي أجريتها.

### التعديل مباشرةً من GitHub

إذا كنت ترغب في إجراء تعديل سريع دون استنساخ المستودع محليًا، يمكنك استعمال محرر GitHub المدمج:

1. افتح الملف المطلوب في المستودع عبر واجهة GitHub ثم اضغط على زر **Edit** (أيقونة القلم) في أعلى الملف.
2. نفّذ التغييرات داخل المحرر، ثم اكتب رسالة وصفية في خانة الالتزام.
3. اختر ما إذا كنت تريد الالتزام مباشرة على الفرع الحالي أو إنشاء فرع جديد، ثم اضغط **Commit changes** لحفظ التعديل.
4. في حال إنشائك فرعًا جديدًا، يمكنك بعد ذلك فتح Pull Request للمراجعة والدمج.

---

## English Translation

Gemini Chatbot is an AI-powered chatbot built with the Gemini 2 API and Streamlit. It aims to provide users with an interactive experience through smart, accurate responses.

## Installation

1. Make sure Python is installed.
2. Install the dependencies with:
    ```bash
    pip install -r requirements.txt
    ```
3. Set the `GOOGLE_API_KEY` environment variable before running the app or add it to Streamlit's `/.streamlit/secrets.toml` file.
   - Example of setting it temporarily in the terminal (Unix systems):
     ```bash
     export GOOGLE_API_KEY="your-secure-key"
     ```
   - Or add a `.streamlit/secrets.toml` file with the following content:
     ```toml
     GOOGLE_API_KEY = "your-secure-key"
     GEMINI_MODEL = "gemini-pro"
     ```
   The app securely reads the value from `st.secrets` or the environment variable without storing the key in the repository.

## Usage

To run the chatbot:
1. Start the app with Streamlit:
    ```bash
    streamlit run app.py
    ```
2. Open the browser at the URL shown in the terminal to access the chatbot.

> **Note:** You can control the logging level with the `APP_LOG_LEVEL` environment variable (for example, `INFO` or `DEBUG`) to monitor issues while the app is running.

## Contributing

If you want to contribute to the project:
1. Fork this repository.
2. Make your changes in your branch.
3. Submit a pull request describing the updates you made.

### Editing Directly on GitHub

If you need to make a quick change without cloning the repository locally, you can use GitHub's built-in editor:

1. Open the target file on GitHub, then click the **Edit** button (pencil icon) at the top of the file.
2. Apply your changes in the editor, and provide a descriptive commit message.
3. Choose whether to commit directly to the current branch or create a new branch, then click **Commit changes** to save.
4. If you created a new branch, open a pull request for review and merging.

<!-- Reapplied branch update -->
