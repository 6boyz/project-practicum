import streamlit as st
from model import Model, MODEL_NAME
from model_example_data import CONTEXT, QUESTION

st.set_page_config(
    page_title=MODEL_NAME, initial_sidebar_state="expanded"
)
st.write(
    f"""
# 🦾 {MODEL_NAME}
Загрузите контекст вопроса и спросите модель чтобы получить ответ!
    """
)

st.text_input("Вопрос", key="question", value=QUESTION)
st.text_area("Контекст", key="context", value=CONTEXT, height=350)

if st.session_state.question and st.session_state.context:
    answer_dict = (Model._get_model()(question=st.session_state.question, context=st.session_state.context))
    st.text_input('Ответ', value=answer_dict['answer'], disabled=True)