"""
Run this script to see the UI interface for viewing jobs, labeling, and seeing recommendations

Usage: streamlit run recommendation_platform.py
"""

import streamlit as st
import time
from data_streamer import DataStreamer


button_states = {}
data_streamer = DataStreamer()


def search_result_block(job_title,company,location_,date,apply,description,block_id):
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
        button_states[block_id]= st.selectbox(
        "Label",
        ('Unread','Interesting', 'Not Interesting'),
        key=block_id)
    
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

    
def main():
    # Title of the app
    st.title('Job Search Platform')
    
    # typical job search website UI
    col1, col2 = st.beta_columns(2)
    with col1:
        position = st.text_input('Job Search', 'Data Science')
    with col2:
        location = st.text_input("Location","Chicago, IL")

    # typical job result
    results = st.beta_container()
    with st.spinner("Getting Jobs..."):
        job_titles,companies,locations,dates,applies,descriptions = search(position,location)
    
    with results:
        for i, (job_title,company,location_,date,apply,description) in enumerate(zip(job_titles,companies,locations,dates,applies,descriptions)):
            search_result_block(job_title,company,location_,date,apply,description,f"b{i}")
    
    # st.text(f"List of labels from current selection: {button_states['b1']}, {button_states['b2']},{button_states['b3']},{button_states['b4']}")
            
if __name__ == '__main__':
    main()