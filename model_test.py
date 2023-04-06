from model import Model
from model_example_data import CONTEXT

def test_model_1():
    prediction = Model.get_prediction(context=CONTEXT, question='Who has a experience in sales?') 
    assert prediction['answer'] == "Emily"

def test_model_2():
    prediction = Model.get_prediction(context=CONTEXT, question='Who has a STG Architects award?') 
    assert prediction['answer'] == "Maria"

def test_model_3():
    prediction = Model.get_prediction(context=CONTEXT, question='Who speak Italian or Thai?') 
    assert prediction['answer'] == "Maria"

def test_model_4():
    prediction = Model.get_prediction(context=CONTEXT, question='Who has experience of designing and developing?') 
    assert prediction['answer'] == "Maria"

def test_model_5():
    prediction = Model.get_prediction(context=CONTEXT, question='Who has  experience of sales?') 
    assert prediction['answer'] == "Emily"

def test_model_6():
    prediction = Model.get_prediction(context=CONTEXT, question='What Maria doing when not working?') 
    assert prediction['answer'] == "hiking, skiing and diving"