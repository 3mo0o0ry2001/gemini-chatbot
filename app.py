import streamlit as st
import google.generativeai as genai
import os

# إعداد مفتاح API
API_KEY = "AIzaSyCJ84POOpG7QnwKYfherP-JlbHHEFdVICk"  # استبدلها بمفتاحك الحقيقي
os.environ["GOOGLE_API_KEY"] = API_KEY
genai.configure(api_key=API_KEY)

# تهيئة نموذج Gemini 2
model = genai.GenerativeModel("gemini-pro")

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

# واجهة Streamlit
st.title("🤖 شات بوت باستخدام Gemini 2 API")
st.write("أدخل استفسارك وسيتولى الذكاء الاصطناعي الإجابة عليه.")

# سجل المحادثة
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# إدخال المستخدم
user_input = st.text_input("💬 اكتب هنا:")

if st.button("🚀 إرسال"):
    if user_input:
        try:
            response = model.generate_content(user_input)
            reply = response.text
            
            # حفظ المحادثة
            st.session_state.chat_history.append(("أنت:", user_input))
            st.session_state.chat_history.append(("🤖 شات بوت:", reply))
            
            # عرض المحادثة بتصميم محسّن
            st.subheader("📝 المحادثة:")
            st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
            for sender, message in st.session_state.chat_history:
                css_class = "user-msg" if sender == "أنت:" else "bot-msg"
                st.markdown(f"<div class='{css_class}'><b>{sender}</b>: {message}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"حدث خطأ: {e}")
    else:
        st.warning("⚠️ الرجاء إدخال نص قبل الإرسال!")
