import streamlit as st
import json
import os

def main_page():
    """_summary_
    """
    st.markdown('Create Quiz')
    st.sidebar.markdown('Create Quiz')


def page2():
    """_summary_
    """
    st.markdown('Quiz')
    st.sidebar.markdown('Quiz')


page_names_to_funcs = {
    "Create Quiz": main_page,
    "Try Out Quiz": page3,
}

st.title('Create Quiz')

def write_to_json(filename: str, new_data: dict[list[list]]):
    """_summary_

    Args:
        filename (str): _description_
        new_data (dict[list[list]]): _description_
    """
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump([], f)
    
    with open(filename, 'r') as f:
        try:
            file_data = json.load(f)
        except json.JSONDecodeError:
            file_data = []

    file_data.append(new_data)

    with open(filename, 'w') as f:
        json.dump(file_data, f, indent=4)

question_text = st.text_input("Enter Question")
st.write(question_text)
responses = []

t = st.text_area("Enter responses")
textsplit = t.splitlines()

for i in range(len(textsplit)):
    st.write(str(i+1) + ": "+ textsplit[i])
if t:
    for i in range(len(textsplit)):
        responses.append(textsplit[i])
    
    number = st.number_input("Correct response", step=1, max_value=len(textsplit))
    data = {"question": question_text, "responses": responses, "answer": responses[number-1]}

if st.button("Add question", use_container_width=True):
    st.write('Question added')
    write_to_json('data2.json', data)
