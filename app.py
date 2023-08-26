import streamlit as st
from models.lstm_model import train_lstm_model
from models.generator import generate_text
from tensorflow.keras.preprocessing.text import Tokenizer

def main():
    st.title('Artistic Text Generation')

    # Load dataset
    with open("data/artistic_texts.txt", "r", encoding="utf-8") as f:
        artistic_texts = f.readlines()

    # Train the LSTM model (you can optimize this to train only once)
    model = train_lstm_model(artistic_texts)

    seed_text = st.text_area("Enter your seed text here")

    if st.button("Generate"):
        if seed_text:
            tokenizer = Tokenizer()
            tokenizer.fit_on_texts(artistic_texts)
            generated_text = generate_text(model, tokenizer, seed_text, num_words=100)
            st.markdown("## Generated Artistic Text")
            st.write(generated_text, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
