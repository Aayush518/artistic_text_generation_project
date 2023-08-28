import streamlit as st
from models.lstm_model import train_lstm_model
from models.generator import generate_text
from tensorflow.keras.preprocessing.text import Tokenizer
import random

def main():
    st.title('Artistic Text Generation')

    # Load dataset
    with open("data/artistic_texts.txt", "r", encoding="utf-8") as f:
        artistic_texts = f.readlines()

    # Train the LSTM model (you can optimize this to train only once)
    model = train_lstm_model(artistic_texts)

    seed_text = st.text_area("Enter your seed text here")

    # Additional features: text style, word count, and style suggestions
    selected_style = st.selectbox("Select Text Style", ["Elegant", "Playful", "Mysterious"])
    word_count_limit = st.number_input("Word Count Limit", min_value=10, max_value=500, value=100)

    if st.button("Generate"):
        if seed_text:
            tokenizer = Tokenizer()
            tokenizer.fit_on_texts(artistic_texts)
            generated_text = generate_text(model, tokenizer, seed_text, num_words=word_count_limit)
            st.markdown("## Generated Artistic Text")
            st.write(generated_text, unsafe_allow_html=True)

            # Generate style suggestions based on the selected style
            style_suggestions = []
            if selected_style in styles:
                style_suggestions = random.sample(styles[selected_style], 3)
            st.markdown("### Style Suggestions:")
            for suggestion in style_suggestions:
                st.write(suggestion)

if __name__ == "__main__":
    main()
