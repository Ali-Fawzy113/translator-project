import streamlit as st
from deep_translator import GoogleTranslator

st.title("Translator Project 🌍")
st.markdown("Project by Ali Aboielkher")
if st.button("About"):
    st.info("مرحبا بكم في مشروع يترجم من اللغة العربية للغة الانجليزية والعكس")
option = st.selectbox(
    "Select Target Language (اختر لغة الترجمة):",
    ("Arabic (العربية)", "English (الإنجليزية)"))

target_lang = 'ar' if option == "Arabic (العربية)" else 'en'

text = st.text_input("Enter your sentences / أدخل جملتك:")

if text:
    translation = GoogleTranslator(source='auto', target=target_lang).translate(text)
    st.subheader("Translation:")
    st.success(translation)