from functools import cache
import streamlit as st
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

MODEL_NAME = "deepset/roberta-base-squad2"

class Model:
    @staticmethod
    @cache
    @st.cache(allow_output_mutation=True)
    def _get_model(model_name=MODEL_NAME):
        model = AutoModelForQuestionAnswering.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
        return nlp

    @staticmethod
    def get_prediction(question: str, context: str):
        if not question or not context: return
        return Model._get_model()({
            'question': question,
            'context' : context
        })