
"""
Run this script to see the UI for both search,viewing,labeling jobs and viewing recommended jobs

Usage:
streamlit run job_finder_platform.py
"""
import job_finder
import recommendation
import streamlit as st

PAGES = {
    "Manual":job_finder,
    "Recommendation":recommendation
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()