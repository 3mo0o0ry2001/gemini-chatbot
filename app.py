import logging
import os

import google.generativeai as genai
import streamlit as st


def _configure_logging() -> None:
    """إعداد التسجيل مع مستوى INFO بشكل افتراضي."""

    logging.basicConfig(
        level=os.getenv("APP_LOG_LEVEL", "INFO"),
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )


@st.cache_resource(show_spinner=False)
def _get_model() -> genai.GenerativeModel:
    """تهيئة نموذج Gemini 2 بعد ضبط مفتاح API بشكل آمن."""

    api_key = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        logging.error("GOOGLE_API_KEY is not set. Aborting model initialization.")
        st.error("لم يتم العثور على مفتاح Google API. يرجى إعداده قبل استخدام التطبيق.")
        st.stop()

    genai.configure(api_key=api_key)
    model_name = st.secrets.get("GEMINI_MODEL", "gemini-pro")
    logging.info("Initializing Gemini model '%s'", model_name)
    return genai.GenerativeModel(model_name)

# تصميم الواجهة
st.set_page_config(page_title="شات بوت AI", page_icon="🤖", layout="centered")
st.markdown("""
    <style>
        .chat-container {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .user-msg {
            background-color: #d1e7dd;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 5px;
        }
        .bot-msg {
            background-color: #f8d7da;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# إعداد التسجيل قبل بناء الواجهة
_configure_logging()

# واجهة Streamlit
st.title("🤖 شات بوت باستخدام Gemini 2 API")
st.write("أدخل استفسارك وسيتولى الذكاء الاصطناعي الإجابة عليه.")

# سجل المحادثة
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# إدخال المستخدم
user_input = st.text_input("💬 اكتب هنا:")

model = _get_model()


if st.button("🚀 إرسال"):
    if not user_input:
        st.warning("⚠️ الرجاء إدخال نص قبل الإرسال!")
    elif len(user_input) > 1000:
        st.warning("⚠️ النص طويل جداً. يرجى تقصيره إلى 1000 حرف كحد أقصى.")
    else:
        try:
            logging.info("Sending prompt to Gemini model (length=%s characters)", len(user_input))
            response = model.generate_content(user_input)
            reply = response.text or "عذرًا، لم أتمكن من توليد إجابة."  # ضبط رد افتراضي

            # حفظ المحادثة
            st.session_state.chat_history.append(("أنت:", user_input))
            st.session_state.chat_history.append(("🤖 شات بوت:", reply))
        except Exception as error:
            logging.exception("Gemini API request failed")
            st.error("حدث خطأ أثناء التواصل مع خدمة Gemini. يرجى المحاولة لاحقًا.")

# عرض المحادثة بتصميم محسّن خارج كتلة الزر لضمان التحديث الدائم
if st.session_state.chat_history:
    st.subheader("📝 المحادثة:")
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    for sender, message in st.session_state.chat_history:
        css_class = "user-msg" if sender == "أنت:" else "bot-msg"
        st.markdown(
            f"<div class='{css_class}'><b>{sender}</b>: {message}</div>",
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)
