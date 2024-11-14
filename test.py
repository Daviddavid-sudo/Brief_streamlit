import streamlit as st
import pandas as pd
import numpy as np
import json

st.title('Create Quiz')
questions = {"questions": []}

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if 'questions' not in st.session_state:
    with open('data.json', 'r') as f:
        st.session_state.questions = json.load(f)
    st.session_state.index = 0


def click_button():
    st.session_state.clicked = True


left, middle, start, right = st.columns(4)
left_button = left.button("Add question", use_container_width=True, on_click=click_button)
middle_button = middle.button("Submit question", use_container_width=True)
start_button = start.button("Start quiz", use_container_width=True)
right_button = right.button("Next Question", use_container_width=True)

def write_to_json(filename, new_data):
    with open(filename, 'r+') as f:
        file_data = json.load(f)
        file_data["questions"].append(new_data)
        f.seek(0)
        json.dump(file_data,f)

        
def start_game():
    st.write_stream(st.session_state.questions['questions'][st.session_state.index])
    responses_dict = st.session_state.questions['questions'][st.session_state.index]
    option = []
    for x in responses_dict.values():
        for y in responses_dict.values():
            for keys in y:
                option.append(y[keys][0])

    selected_choice = st.radio(
            "Choose a reponse",
            options=option
            )

    if right_button:
        st.session_state.index +=1
        st.rerun()

if left_button and st.session_state.clicked:
    question_text = st.text_input("Enter Question")
    responses = {}

    t = st.text_area("Enter responses")

    if t is not None:
        textsplit = t.splitlines()
        for i in range(len(textsplit)):
            responses[i+1]=[textsplit[i], False]

    data = {question_text: responses}
    number = st.number_input("Correct response", step=1)
    
    if number:
        data[question_text][number][1] =  True

    if middle_button:
        write_to_json('data.json', data)
        st.session_state.clicked = False

if start_button:
    start_game()
