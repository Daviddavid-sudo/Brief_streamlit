import streamlit as st
import json
import time

st.sidebar.markdown("Page 2")
st.title('Quiz')

if 'questions' not in st.session_state:
    with open('data.json', 'r') as f:
        st.session_state.questions = json.load(f)
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.finished = False

if not st.session_state.finished:
    question_text = st.session_state.questions[st.session_state.index]["question"]
    responses_text = st.session_state.questions[st.session_state.index]["responses"]
    answer = st.session_state.questions[st.session_state.index]["answer"]
    st.write(question_text)
    selected_choice = st.radio(
            "Choose a reponse",
            options=responses_text
            )

    if st.button("Next Question", use_container_width=True):
        if answer == selected_choice:
            st.session_state.index +=1
            st.session_state.score +=1
            if st.session_state.index == len(st.session_state.questions):
                st.write('Quiz finished click next question to see results')
                st.session_state.finished = True
            else:
                st.rerun()
        else:
            st.session_state.index +=1
            if st.session_state.index == len(st.session_state.questions):
                st.write('Quiz finished click next question to see results')
                st.session_state.finished = True
            else:
                st.rerun()

else:
    st.title('Results')
    score =  "Questions correctly answered: " + str(st.session_state.score) + "/" + str(st.session_state.index)
    st.write(score)
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.finished = False
    if st.button("Try Again", use_container_width=True):
        st.rerun()