# better-job-finder
[![Python](https://img.shields.io/badge/Python-3.8-blue?style=flat&logo=Python)](https://www.python.org/downloads/release/python-380/)
[![Streamlit](https://img.shields.io/badge/Made_with-Streamlit-red?style=flat&logo=Streamlit)](https://streamlit.io)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.5-orange?style=flat&logo=Tensorflow)](https://www.tensorflow.org/api_docs)
[![Bert](https://img.shields.io/badge/Huggingface-Bert--based--uncased-yellow?style=flat)](https://huggingface.co/bert-base-uncased)
## Background

The term Data science is very generic and a job role can be very different with the same title. Data science can be broken down into 3 roles: Data engineer, Data analyst, ML engineer. The problem with a lot of job posting websites is that the particular data science role you are looking for is filled with the noise of the other roles.

## Project Goal

To create a user friendly platform that pulls jobs from multiple sources and allows you to train your own recommendation model, to find interesting jobs that you might apply too.

----------------------------------------------------------------------------------------------------
## Demo
![demo](https://user-images.githubusercontent.com/23107070/123326306-13e20900-d507-11eb-8de6-6b5467550a01.gif)

----------------------------------------------------------------------------------------------------
## Installation

Step 1: Clone Repo
```
git clone https://github.com/Taher-Dohadwala/better-job-finder.git
```

Step 2: Run setup script \
Setup directory structure, create virtual env (venv), and install dependencies
```
bash setup.sh
```

Step 3: Download initial model, place into models directory\
[Model Download](https://drive.google.com/drive/folders/1a81152GvE3FQ-pNzW8XAplCE5tDj1x6H?usp=sharing)

----------------------------------------------------------------------------------------------------
## Usage

To run Job Finder Platform app
```
streamlit run job_finder_platform.py
```

To fine-tune model with new labeled data
```
python training.py
```

----------------------------------------------------------------------------------------------------
## Initial data collection
Initial attempt to scrape data from job posting failed due scraping too much and being captcha blocked.


Project development started with data scrape and posted on Kaggle:

- [Dataset 1](https://www.kaggle.com/jobspikr/data-scientist-job-postings-from-the-usa)
- [Dataset 2](https://www.kaggle.com/rashikrahmanpritom/data-science-job-posting-on-glassdoor)
- [Dataset 3](https://www.kaggle.com/andrewmvd/data-scientist-jobs)

These datasets were explored and combined to
## Scraped data
So far Indeed is the only successfully scraped website
Will add Glassdoor, and Monster


## Monetization Capability
Selling user personalized dataset of job keywords, location, and job results they thought are interesting or not interesting (liked or disliked).

### How does this makes money?
Selling that data to job sites gives them another dimension of characterization for each person. This can lead to them providing better job results, that end up being applied too.