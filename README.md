# better-job-finder

## Background

The term Data Science is very generic and a job role can be very different with the same title, data science. Data science can be broken down into 3 roles: Data engineer, Data analyst, ML engineer. The problem with a lot of job posting websites is that the particular data science role you are looking for is filled with the noise of other roles.

## Project Goal

To create a platform that pulls jobs from multiple sources and allows you to train your own recommendation model, to find interesting jobs that you might apply too.

Features:
    - Streaming data from multiple job sites
    - Interesting/Not interesting classification data collection
    - List of recommendated jobs

## Purpose

The job recommendations from websites (e.g Linkedin) aren't tailored specifically for you and often times recommend jobs with other roles.

----------------------------------------------------------------------------------------------------

### Initial data
Inital project development will be based on the data scraped from:

- [Dataset 1](https://www.kaggle.com/jobspikr/data-scientist-job-postings-from-the-usa)
- [Dataset 2](https://www.kaggle.com/rashikrahmanpritom/data-science-job-posting-on-glassdoor)
- [Dataset 3](https://www.kaggle.com/andrewmvd/data-scientist-jobs)

Eventually data will be scraped myself, to added to the pipeline

# Tasks
1. Create rough platform website with Streamlit
2. Add functionality such as linking to data scraper,saving labeled jobs, running model on jobs
3. Optimize recommendation model
    - Dealing with disproportionate classes
    - Training on Colab
    - Finetune tokenenizer
    - Finetune classifier



# Monetization Capability
Selling user personalized dataset of job keywords, location, and job results they thought are interesting or not interesting (liked or disliked).

## How does this makes money?
Selling that data to job sites gives them another dimension of characterization for each person. This can lead to them providing better job results, that end up being applied too.