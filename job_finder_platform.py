
"""
Run this script to launch the main app.
Functionality:
1) Search jobs and mark as interesting or not interesting
2) Save labeled data
3) View recommended jobs

Usage:
streamlit run job_finder_platform.py
"""
from streamlit_ui import job_finder
from streamlit_ui  import recommendation
import streamlit as st

PAGES = {
    "Manual":job_finder,
    "Recommendation":recommendation
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()