# import streamlit as st
# st.title("Hello streamlit")
# st.write("! ده اول تطبيق ليك")
print("*******************************")
# import streamlit as st
# st.title("Translator Project 🌍")
# text = st.text_input("Enter your sentences:")
# if text:
#     st.write(text)
print("*******************************")
import streamlit as st
from deep_translator import GoogleTranslator
st.title("Translator Project 🌍")
text = st.text_input("Enter your sentences:")
if text:
    translation = GoogleTranslator(source='auto', target='ar').translate(text)
    st.subheader("Translation:")
    st.success(translation)