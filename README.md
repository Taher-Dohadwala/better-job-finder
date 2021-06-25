# better-job-finder
[![Python](https://img.shields.io/badge/Python-3.8-blue?style=flat&logo=Python)](https://www.python.org/downloads/release/python-380/)
[![Streamlit](https://img.shields.io/badge/Made_with-Streamlit-red?style=flat&logo=Streamlit)](https://streamlit.io)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.5-orange?style=flat&logo=Tensorflow)](https://www.tensorflow.org/api_docs)
[![Bert](https://img.shields.io/badge/🤗_Hugging_Face-Bert--based--uncased-yellow?style=flat)](https://huggingface.co/bert-base-uncased)

## Project Goal

Develop a bring your own model job search platform, where you can label and train your own personalized recommendation model.


----------------------------------------------------------------------------------------------------

## Background

Job titles often have different underlying roles. When looking for a job for a particular role, the job title alone cannot guarentee the job role matching what you are looking for.

For example, the serach term Data science is generic and a job role can be very different with the same title. Data science can be broken down into 3 main roles: Data engineer, Data analyst, ML engineer. The problem with job posting websites is that the particular data science role you are looking for is filled with the noise of the other roles. By having a recommendation model that is based on your own preferences can help de-noise the job search space.


----------------------------------------------------------------------------------------------------

## Demo <a name="demo"></a>
![demo](https://user-images.githubusercontent.com/23107070/123326306-13e20900-d507-11eb-8de6-6b5467550a01.gif)

----------------------------------------------------------------------------------------------------

# Table of contents
* [Installation](#installation)
* [Usage](#usage)
* [Initial data collection](#initial-data-collection)
* [Recommendation Model](#recommendation-model)
* [Data Streaming](#data-streaming)
* [Job Finder Platform](#job-finder-platform)
* [Monetization Capability](#monetization-capability)

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

Step 3: Download starter model, place into models/recommendation directory\
[Google Drive](https://drive.google.com/drive/folders/1a81152GvE3FQ-pNzW8XAplCE5tDj1x6H?usp=sharing)

----------------------------------------------------------------------------------------------------
## Usage

To run the Job Finder Platform app
```
streamlit run job_finder_platform.py
```

To fine-tune model with new labeled data
```
python training.py
```

----------------------------------------------------------------------------------------------------
## Initial data collection
First attempts to scrape data from job posting failed due scraping too much and being captcha blocked.


Project development then continued with data scraped and posted on Kaggle:

- [10000 Data Scientist Job Postings from the USA](https://www.kaggle.com/jobspikr/data-scientist-job-postings-from-the-usa)
- [Data Science Job Posting on Glassdoor](https://www.kaggle.com/rashikrahmanpritom/data-science-job-posting-on-glassdoor)
- [Data Scientist Jobs](https://www.kaggle.com/andrewmvd/data-scientist-jobs)

These 3 datasets were explored and combined to form the initial training dataset for our language model.

----------------------------------------------------------------------------------------------------

## Recommendation Model
Utilized the 🤗 Hugging Face framework for Transformers combined with TensorFlow.\
The recommendation model is the [bert-base-uncased](https://huggingface.co/bert-base-uncased) Transformer model

Using helper scripts to aid with the labeling process, manually labeled 300 job descriptions, as "Interesting" or "Not interesting".

Then transferred the training script to Google Colab and fine-tuned the Transformer model for sequence classification for 20 epochs.

----------------------------------------------------------------------------------------------------

## Data Streaming
The Job Finding platform streams job postings from multiple sources.

The DataStreamer Object utilizes the DataSource interface to allow for easily adding new data sources.

Currently only Indeed.com is scraped for job postings.
The limitations to data streaming is that random sleep between scrapes is neccesary in order to not be blocked via captcha.

----------------------------------------------------------------------------------------------------
## Job Finder Platform

Utilized Streamlit for rapid UI prototyping. The Job Finder Platform contains two pages.

The first being the manual search and label page. Users have the option to expand and read the full job description, and decide whether it was Interesting or Not interesting. At the bottom on the page is a button to save the labels which can be used to fine-tune the Transformer model in the future.


The second being the search and view only the recommended jobs. Users can enter job searches and recommendation model will return only the highest confidence jobs.

----------------------------------------------------------------------------------------------------

## Monetization Capability 
Selling user personalized dataset of job searches, location, and job results that they thought are interesting or not interesting.

### How does this makes money?
Selling that data to job sites gives them another dimension of characterization for each person. This can lead to them providing better job results, that end up being applied too.

----------------------------------------------------------------------------------------------------