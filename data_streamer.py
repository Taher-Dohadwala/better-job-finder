"""
This script contains all the data source objects that are responsible for scraping data from job posting websites.
As well as a data manager class that is used to aggregate all the data source objects.
"""

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

"""
DataSource_
These classes are responsible for scraping job posts from job websites.
Scraped Information:
    - Job Title
    - Company
    - Location
    - Posted date
    - Apply link
    - Job Description
"""
class DataSource_Indeed():
    """
    This class scrapes data from Indeed
    """
    def __init__(self):
        # Based url template for indeed
        self.base_url = 'https://www.indeed.com/jobs?q={}&l={}&sort=date&start={}'
        self.search_url = ""
        self.soup = None
        self.delay = 0.1
        self.titles = []
        self.companies = []
        self.locations = []
        self.dates = []
        self.applies = []
        self.descriptions = []
        self.page = 0
    
    def set_search(self,position,location):
        """Sets job search url, and page, by converting keywords and location into the needed format for Monster search url structure"""
        position = position.replace(" ","+")
        location = location.replace(" ", "+")
        self.search_url = self.base_url.format(position,location,self.page)

    def get_info(self):
        """Scrapes data from indeed """
        page = requests.get(self.search_url)
        self.soup = BeautifulSoup(page.content,"html.parser")
        
        # Info for individual job posting
        cards = self.soup.find_all("div","jobsearch-SerpJobCard")
        for card in cards:
            self.titles.append(card.h2.a.get("title"))
            self.companies.append(card.find('span', 'company').text.strip())
            self.locations.append(card.find('div', 'recJobLoc').get('data-rc-loc'))
            self.dates.append(card.find('span', 'date').text)

            # Get full description
            time.sleep(self.delay)
            jobURL = "http://indeed.com" + card.h2.a.get('href')
            job_response = requests.get(jobURL)
            self.applies.append(jobURL)
            job_soup = BeautifulSoup(job_response.text,"html.parser")
            job_description_tag = job_soup.find('div',{'id':'jobDescriptionText'})
            job_description = job_description_tag.text if job_description_tag else "N/A"
            self.descriptions.append(job_description)
            
    def get_data(self):
        """Returns scraped data """
        return self.titles,self.companies,self.locations,self.dates,self.applies,self.descriptions
    
    def save_to_csv(self,filename):
        """Saves data to csv """
        d = {"Title":self.titles,"Company":self.companies,"Location":self.locations,
             "Date":self.dates,"Apply":self.applies,"Description":self.descriptions}
        df = pd.DataFrame(data=d)
        df.to_csv(filename)

class DataStreamer():
    """This clas manages all DataSource_ classes and is used in recommendation_platform"""
    def __init__(self):
        self.indeed = DataSource_Indeed()
    
    def search(self, position, location):
        """Scrapes data from all DataSource_ classes managed in DataStreamer"""
        self.indeed.set_search(position,location)
        self.indeed.get_info()
    
    def get_data(self):
        """Gets data from all sources """
        job_titles,companies,locations,dates,applies,descriptions = self.indeed.get_data()
        return job_titles,companies,locations,dates,applies,descriptions
    
    def save_to_csv(self,filename):
        """Save data to csv"""
        self.indeed.save_to_csv(filename)
 