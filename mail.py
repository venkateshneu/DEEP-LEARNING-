import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    words = nltk.word_tokenize(text)
    words = [word for word in words if word.isalnum() and word not in stop_words and word not in string.punctuation]
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    return " ".join(words)

tfidf = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("mnb.pkl", "rb"))

st.title("Mail Classifier 📧")

input_text = st.text_area("Enter the text of the email:", height=200)

if st.button("Predict"):
    with st.spinner("Predicting..."):
        transformed_mail = preprocess_text(input_text)
        vector = tfidf.transform([transformed_mail])
        prediction = model.predict(vector)[0]
        if prediction == 1:
            st.success("The email is predicted to be spam.")
        else:
            st.success("The email is predicted to be not spam.")
