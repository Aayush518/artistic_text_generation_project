from flask import Flask, render_template, request
from models.lstm_model import train_lstm_model
from models.generator import generate_text
from tensorflow.keras.preprocessing.text import Tokenizer

app = Flask(__name__)

# Global variables to store user settings
selected_style = None
word_count_limit = 100

@app.route('/', methods=['GET', 'POST'])
def index():
    global selected_style, word_count_limit

    # Load dataset
    with open("data/artistic_texts.txt", "r", encoding="utf-8") as f:
        artistic_texts = f.readlines()

    # Train the LSTM model (you can optimize this to train only once)
    model = train_lstm_model(artistic_texts)

    generated_text = ""

    if request.method == 'POST':
        seed_text = request.form['seed_text']
        if seed_text:
            tokenizer = Tokenizer()
            tokenizer.fit_on_texts(artistic_texts)
            generated_text = generate_text(model, tokenizer, seed_text, num_words=word_count_limit)

    return render_template('index.html', generated_text=generated_text)

if __name__ == "__main__":
    app.run(debug=True)
