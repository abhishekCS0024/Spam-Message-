import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer



ps = PorterStemmer()



from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import string

nltk.download('punkt_tab')
nltk.download('stopwords')

# Initialize the stemmer
ps = PorterStemmer()

def transform_message(message):
    message = message.lower()
    message = nltk.word_tokenize(message)
    
    y = []
    for i in message:
        if i.isalnum():
            y.append(i)
    
    message = y[:]
    y.clear()
    
    for i in message:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    message = y[:]
    y.clear()
    
    for i in message:
        y.append(ps.stem(i))
    
            
    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('Spam_message.pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    # 1. preprocess
    transformed_sms = transform_message(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.markdown("<h1 style='text-align: center; color: red;'>🚫 Spam</h1>", unsafe_allow_html=True)

    else:
        st.markdown("<h1 style='text-align: center; color: green;'>✅ Not Spam</h1>", unsafe_allow_html=True)

# import streamlit as st

# result = 1  # This is just an example; replace with your actual result

# if result == 1:
#     st.markdown("<h1 style='text-align: center; color: red;'>🚫 Spam</h1>", unsafe_allow_html=True)
# else:
#     st.markdown("<h1 style='text-align: center; color: green;'>✅ Not Spam</h1>", unsafe_allow_html=True)


# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from nltk.stem import PorterStemmer
# import string
# import pickle
# import streamlit as st

# # Ensure NLTK data is downloaded
# nltk.download('punkt_tab')
# # nltk.download('punkt')
# nltk.download('stopwords')

# # Initialize the stemmer
# ps = PorterStemmer()

# def transform_message(message):
#     message = message.lower()
#     message = nltk.word_tokenize(message)  # Use the correct function

#     y = []
#     for i in message:
#         if i.isalnum():
#             y.append(i)

#     message = y[:]
#     y.clear()

#     for i in message:
#         if i not in stopwords.words('english') and i not in string.punctuation:
#             y.append(i)

#     message = y[:]
#     y.clear()

#     for i in message:
#         y.append(ps.stem(i))

#     return " ".join(y)

# # Load model and vectorizer
# tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
# model = pickle.load(open('Spam_message.pkl', 'rb'))

# # Streamlit app
# st.title("Email/SMS Spam Classifier")
# input_sms = st.text_area("Enter the message")

# if st.button('Predict'):
#     transformed_sms = transform_message(input_sms)
#     vector_input = tfidf.fit_transform([transformed_sms]) 
#     result = model.predict(vector_input)[0]
#     if result == 1:
#         st.header("Spam")
#     else:
#         st.header("Not Spam")
