import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email Spam Classifier Made by Rabi Subedi Chettri")

input_sms = st.text_area("Enter a message")

if st.button('Check'):

    # preprocess
    transformed_sms = transform_text(input_sms)
    # vectorized
    vector_input = tfidf.transform([transformed_sms]).toarray()

    # predict
    result = model.predict(vector_input)[0]
    # Display
    if result == 1:
        st.header("The message is Spam")
    else:
        st.header("The message is not Spam")
