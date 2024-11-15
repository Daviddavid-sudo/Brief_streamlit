import streamlit as st
import json
import time

st.sidebar.markdown("Page 3")
st.title('History')

if 'questions' not in st.session_state:
    with open('data.json', 'r') as f:
        st.session_state.questions = json.load(f)
    st.session_state.score = 0
    st.session_state.finished = False

if not st.session_state.finished:
    questions = st.session_state.questions
    for i in range(len(questions)):
        line = f"Question {i+1}: {questions[i]["question"]}"
        st.write(line)
        for response in questions[i]["responses"]:
            st.write(response)