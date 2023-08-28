from flask import Flask, render_template, request
from models.lstm_model import train_lstm_model
from models.generator import generate_text
from tensorflow.keras.preprocessing.text import Tokenizer
import random

app = Flask(__name__)

# Global variables to store user settings
selected_style = None
word_count_limit = 100

# Additional styles for text generation
styles = {
    "Elegant": ["beautiful", "graceful", "refined"],
    "Playful": ["fun", "joyful", "lively"],
    "Mysterious": ["enigmatic", "intriguing", "cryptic"]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    global selected_style, word_count_limit

    # Load dataset
    with open("data/artistic_texts.txt", "r", encoding="utf-8") as f:
        artistic_texts = f.readlines()

    # Train the LSTM model (you can optimize this to train only once)
    model = train_lstm_model(artistic_texts)

    generated_text = ""
    style_suggestions = []

    if request.method == 'POST':
        seed_text = request.form['seed_text']

        # Handle the 'style' field
        selected_style = request.form.get('style')
        if selected_style and selected_style in styles:
            style_suggestions = random.sample(styles[selected_style], 3)

        # Handle the 'word_count' field
        word_count_limit = request.form.get('word_count', 100)
        if word_count_limit:
            word_count_limit = int(word_count_limit)

        if seed_text:
            tokenizer = Tokenizer()
            tokenizer.fit_on_texts(artistic_texts)
            generated_text = generate_text(model, tokenizer, seed_text, num_words=word_count_limit)

    return render_template('index.html', generated_text=generated_text, style_suggestions=style_suggestions)

if __name__ == "__main__":
    app.run(debug=True)
