import streamlit as st
import time

# Example data as test
# https://www.monster.com/job-openings/lead-data-science-analyst-riverwoods-il--1d0c6760-e0b4-45df-b8e3-edd37a7028dc
job_title = "Lead Data Science Analyst"
company = "Discover"
location_ = "Riverwoods, IL 60015"
date = "Posted: 6 days ago"
apply = "https://www.ivyexec.com/job-opening/data-scientist/chicago/illinois/usa?job_id=8313542&ref=ccmns&promo=ccmns&ccuid=31628994452"
description = """
Description

Discover. A brighter future.

With Discover, you’ll have the chance to make a difference at one of the world’s leading digital banking and payments companies. From Day 1, you’ll do meaningful work you’re passionate about, with the support and resources you need for success. We value what makes each employee unique and provide a collaborative, team-based culture that gives everyone an opportunity to shine. Be the reason millions of people find a brighter financial future, while building the future you want, here at Discover.

Job Description 
 
At Discover, be part of a culture where diversity, teamwork and collaboration reign. Join a company that is just as employee-focused as it is on its customers and is consistently awarded for both. We’re all about people, and our employees are why Discover is a great place to work. Be the reason we help millions of consumers build a brighter financial future and achieve yours along the way with a rewarding career.

Responsible for working closely with management to execute analytical initiatives. Responsible for solving business problem by leveraging techniques such as advanced data analytics, exception analysis, data visualization and Robotics Process automation.   This role will utilize data analytical technique and skills to monitor compliance risks and identify consumer harm. Creates reports and dashboards to closely monitor performance metrics and provide insights.

Responsibilities

Leads the development and implementation of advanced analytics including prescriptive analytics and machine learning algorithm & recommendation to solve business problems. Operates as a subject matter expert on statistical analysis, test and design of experiment, analysis methodology, modeling & application, and financial impact analysis.
Collaborates with cross-functional partners to understand their business needs, formulate and complete end-to-end analysis that includes data gathering, analysis, ongoing scaled deliverables and presentations. Delivers effective presentations of findings and recommendations to multiple levels of leadership, creating visual displays of quantitative information.
Establishes and maintains effective performance tracking; identify improvement opportunity, form hypothesis, proposes, designs and implements tests to drive strategy enhancement and optimization.
Manages multiple priorities, communicate business performance and project progress to management & business partners.
Develops and automates reports, iteratively build and prototype dashboards to provide insights at scale, solving for analytical needs. Facilitates implementation of work product and ensure accuracy.
Consistently follows standard work processes and documentation requirements. Recommends improvement to work processes to increase efficiency while maintaining quality of work.
Continuously improves technical and leadership skills through training and development.
Minimum Qualifications

At a minimum, here’s what we need from you:

Bachelor's Degree in Analytics, Engineering, or Statistics
4+ years of experience in Credit Risk, Fraud Risk, Marketing Analytics, Optimization, Operations Analytics, Modeling/Data Science or related.
Preferred Qualifications

If we had our say, we’d also look for:

Master's Degree in Analytics, Engineering, or Statistics
2+ years of experience in Credit Risk, Fraud Risk, Marketing Analytics, Optimization, Operations Analytics, Modeling/Data Science or related
1+ years of experience in Compliance, Risk analytics and testing.
#LI-RD1

What are you waiting for? Apply today!

The same way we treat our employees is how we treat all applicants – with respect. Discover Financial Services is an equal opportunity employer (EEO is the law). We thrive on diversity & inclusion. You will be treated fairly throughout our recruiting process and without regard to race, color, religion, sex, sexual orientation, gender identity, national origin, disability, or veteran status in consideration for a career at Discover."""

button_states = {}
# This function contains a boilerplate example of the 
def search_result_block(job_title,company,location_,date,description,block_id,idx):
    col1, col2 = st.beta_columns(2)
    with col1:
        st.text(job_title)
        st.text(company)
        st.text(location_)
        st.text(date)
    with col2:
        link = f'[Apply]({apply})'
        st.markdown(link, unsafe_allow_html=True)
        button_states[block_id]= st.radio(
        f"Label:{idx}",
        ('Interesting', 'Not Interesting'))

    with st.beta_expander("See Description"):
        st.markdown(description)
    
    
def main():
    # Title of the app
    st.title('Job Search Platform')
    
    # typical job search website UI
    col1, col2 = st.beta_columns(2)
    with col1:
        job = st.text_input('Job Search', 'Entry Level Data Science')
    with col2:
        location = st.text_input("Location","Chicago, IL")
        
    # typical job result
    
    results = st.beta_container()
    with results:
        search_result_block(job_title,company,location_,date,description,"b1",1)
        search_result_block(job_title,company,location_,date,description,"b2",2)
        search_result_block(job_title,company,location_,date,description,"b3",3)
        search_result_block(job_title,company,location_,date,description,"b4",4)
        
    st.text(f"List of labels from current selection: {button_states['b1']}, {button_states['b2']},{button_states['b3']},{button_states['b4']}")
        
if __name__ == '__main__':
    main()