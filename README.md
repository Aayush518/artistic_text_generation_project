# Artistic Text Generation Project

This project demonstrates the generation of artistic text using LSTM-based language modeling. The project includes a Flask web app and a Streamlit app that allow users to input a seed text and generate creative and artistic text based on the provided seed.

## Features

- Generate artistic text using LSTM-based language modeling.
- User-friendly web interfaces using Flask and Streamlit.
- User input for seed text to influence the generated text.
- Styling and formatting for an enhanced user experience.

## Folder Structure

The project is organized as follows:

```
artistic_text_generation_project/
│
├── data/
│   └── artistic_texts.txt
│
├── models/
│   ├── lstm_model.py
│   └── generator.py
│
├── requirements.txt
├── README.md
├── main.py (Flask app)
├── app.py (Streamlit app)
├── static/
│   ├── style.css
│
└── templates/
    ├── index.html
```

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Aayush518/artistic_text_generation_project.git
   ```

2. Navigate to the project directory:

   ```bash
   cd artistic_text_generation_project
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Flask App

1. Run the Flask app:

   ```bash
   python main.py
   ```

2. Access the app in your web browser at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Streamlit App

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Access the app in your web browser at: [http://localhost:8501](http://localhost:8501)

## Enhancements

This is a basic example of an artistic text generation project. We can further enhance the project by adding features like:
- Improved UI and styling.
- User authentication and saved text generation history.
- Multiple text sources and styles for generation.
- Deployment to a web hosting platform for public access.

