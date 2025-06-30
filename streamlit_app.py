# streamlit_app.py

import streamlit as st
from markov_model import MarkovChain


st.title("🧠 Text Generator with Markov Chains")

uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
order = st.slider("Order of Markov Chain (n)", 1, 5, 2)
length = st.slider("Length of generated text", 10, 200, 50)

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    generator = MarkovChain(order=order)

    generator.train(text)
    st.success("Model trained!")

    if st.button("Generate"):
        output = generator.generate(length=length)
        st.text_area("Generated Text", value=output, height=300)
