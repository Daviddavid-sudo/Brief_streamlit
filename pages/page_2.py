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
    st.write_stream(st.session_state.questions['questions'][st.session_state.index])
    responses_dict = st.session_state.questions['questions'][st.session_state.index].values()
    results = []
    correct = []
    answer = False

    for response in responses_dict:
        for x in response:
            results.append(x[0])
            if x[1]:
                correct.append(x[0])

    selected_choice = st.radio(
            "Choose a reponse",
            options=results
            )

    answer = selected_choice in correct

    if st.button("Next Question", use_container_width=True):
        if answer:
            st.session_state.index +=1
            st.session_state.score +=1
            if st.session_state.index == len(st.session_state.questions['questions']):
                st.write('Quiz finished click next question to see results')
                st.session_state.finished = True
            else:
                st.rerun()
        else:
            st.session_state.index +=1
            if st.session_state.index == len(st.session_state.questions['questions']):
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