# Quiz Creation App

A web application built with Streamlit that allows users to create quizzes and save questions in a JSON file. Users can input questions, multiple-choice responses, and mark the correct answer for each question.

## Features

- **Create Quiz**: Add new questions with multiple-choice responses.
- **Try Out Quiz**: Try out the quiz and see your results at the end.

## Prerequisites
- Python 3.7 or higher
- Streamlit 1.40.1
- pydantic 2.9.2

## Setup Instructions

1. **Clone this repository** (or save your code file if this is a personal project).
2. **Install required packages**:
   ```bash
   pip install streamlit
   ```
   
## Running the Application

1. Start the Streamlit app by running:
   ```bash
   streamlit run main.py
   ```
2. Open the provided local URL in your browser (e.g., `http://localhost:8501`) to access the app.

## Usage

### Create a Quiz Question

1. **Enter Question**: Type in the quiz question.
2. **Enter Responses**: Add possible responses in the text area, one per line.
3. **Select Correct Response**: Specify which response is correct by entering the correct response’s line number.
4. **Add Question**: Click the “Add question” button to save the question and responses to `data.json`.

The `data.json` file will be updated with each new question in the following structure:

```json
{
    "questions": [
        {
            "question": "Sample question?",
            "responses": [
                ["Response 1", false],
                ["Response 2", true]
            ]
        }
    ]
}
```

### App Pages

- **Create Quiz**: For adding new questions to the quiz.
- **Try Out Quiz**: A quiz-taking interface.

## Code Structure

- **`write_to_json` function**: Handles reading from and writing to the `data.json` file, appending each new question.
- **Main Page**: Allows users to add questions and responses interactively.
- **Secondary Page (Quiz)**: Placeholder for trying out quizzes (feature in development).

## Future Improvements

- **Add Themes**: Allows for more specfic domaine questions.
- **Scalability**: The next step will be to expand our data base, instead of storing a json into a file. We shall store multiple jsons in multiple files, which are organized by theme. As well as, choosing which questionnaire we would like to add to, since we are limited with just one json.
