# AI Student Assistant Chatbot

## Project Overview

AI Student Assistant is an NLP-based chatbot designed to answer common student queries related to college admissions, courses, fees, internships, and placements.

## Features

- Admission-related queries
- Course and program information
- Fee-related queries
- Internship information
- Placement information
- Greeting, thanks, and goodbye responses
- Unknown-question handling

## Technologies Used

- Python
- Flask
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Logistic Regression
- HTML
- CSS
- JavaScript

## How It Works

1. User enters a question in the chatbot interface.
2. The question is converted into TF-IDF features.
3. The Logistic Regression model predicts the user's intent.
4. The chatbot selects an appropriate response.
5. If the confidence is too low, the chatbot returns an unknown-question message.

## Project Structure

AI_Student_Chatbot_Project
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── data
│   └── intents.json
│
├── static
│   └── style.css
│
└── templates
    └── index.html

## How to Run

1. Install Python.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Install the required packages:

pip install -r requirements.txt

5. Run the application:

python app.py

6. Open the following address in a web browser:

http://127.0.0.1:5000

## Testing

The chatbot was tested with questions related to:

- Admissions
- Courses
- Fees
- Internships
- Placements
- Job opportunities
- Greetings and general conversation
- Unrelated questions

## Live Demo

[Click here to view the AI Student Assistant Chatbot](https://bhumikajonnalagadda.github.io/AI-Student-Assistant-Chatbot/)

## GitHub Repository

[View the project source code on GitHub](https://github.com/Bhumikajonnalagadda/AI-Student-Assistant-Chatbot)

## Project Status

**Minor Project - Completed**
