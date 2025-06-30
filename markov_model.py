import streamlit as st
from markov_model import MarkovChain

st.set_page_config(page_title="Markov Chain Text Generator", page_icon="🧠", layout="centered")

# Set custom dark theme background and styling
st.markdown("""
    <style>
        body {
            background-color: #111;
            color: #eee;
        }
        .stApp {
            background-color: #111;
        }
        .stTextInput, .stSlider, .stFileUploader, .stButton > button {
            background-color: #222 !important;
            color: #eee !important;
            border-radius: 0.5rem;
        }
        .stButton > button:hover {
            background-color: #333 !important;
        }
        h1, h2, h3, h4, h5, h6, p {
            color: #eee !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Markov Chain Text Generator")
st.markdown("""
Upload a `.txt` file, choose the order of the Markov Chain, and generate your own custom text!
""")

uploaded_file = st.file_uploader("📄 Upload a text file", type="txt")

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
elif st.button("Use Sample Text"):
    with open("data/sample.txt", "r", encoding="utf-8") as f:
        text = f.read()
else:
    text = None

order = st.slider("🔢 Order of Markov Chain (n)", min_value=1, max_value=5, value=2)
length = st.slider("✍️ Length of Generated Text (in words)", min_value=10, max_value=200, value=50)

generate = st.button("✨ Generate Text")

if generate and text:
    model = MarkovChain(order)
    model.train(text)
    output = model.generate(length)
    st.subheader("📜 Generated Text")
    st.write(output)

st.markdown("""
---
Made with ❤️ using [Streamlit](https://streamlit.io)
""")
