"""
This script contains the UI interface for viewing recommendation
"""
import random

import streamlit as st
from streamlit_ui.job_finder import search_result_block,search
from streamlit_ui.data_streamer import DataStreamer

import tensorflow as tf
from transformers import DistilBertTokenizerFast
from transformers import TFDistilBertForSequenceClassification


data_streamer = DataStreamer()
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')
loaded_model = TFDistilBertForSequenceClassification.from_pretrained("models/recommendation")


def search_result_block(job_title,company,location_,date,apply,description,confidence):
    """This function contains a boilerplate job posting card layout """
    
    # split into two columns
    col1, col2 = st.beta_columns(2)
    # left side contains job info
    with col1:
        st.text(job_title)
        st.text(company)
        st.text(location_)
        st.text(date)
    with col2:
        # right slide contains apply link and label selection
        link = f'[Apply]({apply})'
        st.markdown(link, unsafe_allow_html=True)
        
        # Display confidence
        st.text(f"{confidence*100:.2f}% confidence")
    
    # hides description until clicked on
    with st.beta_expander("See Description"):
        st.markdown(description)

# cache optimizes for same searches
@st.cache(show_spinner=False)
def search(position,location):
    """Takes a job position and location and returns aggregated job search results """
    data_streamer.search(position,location)
    job_titles,companies,locations,dates,applies,descriptions = data_streamer.get_data()
    return job_titles,companies,locations,dates,applies,descriptions

@st.cache(show_spinner=False)
def make_prediction(example):
    predict_input = tokenizer.encode(example,
                                 truncation=True,
                                 padding=True,
                                 return_tensors="tf")
    tf_output = loaded_model.predict(predict_input)[0]
    tf_prediction = tf.nn.softmax(tf_output, axis=1).numpy()[0]
    pred = tf.argmax(tf_prediction)
    confidence = tf_prediction[pred]
    return pred,confidence
    
def app():
    # Title of the app
    st.title('Search and view recommended jobs')
    
    # top search bar
    col1, col2 = st.beta_columns(2)
    with col1:
        position = st.text_input('Job Search', 'Data Science')
    with col2:
        location = st.text_input("Location","Chicago, IL")
    
    results = st.beta_container()
    with st.spinner("Finding Interesting Jobs..."):
        job_titles,companies,locations,dates,applies,descriptions = search(position,location)
    
    predictions = []
    confidences = []
    with st.spinner("Model Inference..."):
        for description in descriptions:
            pred,conf = make_prediction(description)
            predictions.append(pred)
            confidences.append(conf)
    no_results = True
    with results:
        st.text("Recommended Jobs Only:")
        for i,(pred,conf,job_title,company,location_,date,apply,description) in enumerate(zip(predictions,confidences,job_titles,companies,locations,dates,applies,descriptions)):
            if pred == 1 and conf > 0.5:
                search_result_block(job_title,company,location_,date,apply,description,conf)
                if no_results:
                    no_results = False
        if no_results:
            st.text("No matches with this search. Try another search")
            
            
if __name__ == '__main__':
    app()
    