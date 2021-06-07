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
    - Apply link --- STILL NEED
    - Job Description
"""
class DataSource_Indeed():
    
    def __init__(self):
        self.base_url = 'https://www.indeed.com/jobs?q={}&l={}'
        self.data = {}
        self.search_url = ""
        self.soup = None
        
        self.titles = []
        self.companies = []
        self.locations = []
        self.dates = []
        self.descriptions = []
    
    def search(self,position,location):
        """Sets job search url, and page, by converting keywords and location into the needed format for Monster search url structure"""
        position = position.replace(" ","+")
        location = location.replace(" ", "+")
        self.search_url = self.base_url.format(position,location)

    def get_info(self):
        
        # request for job search results
        page = requests.get(self.search_url)
        self.soup = BeautifulSoup(page.content,"html.parser")
        
        # Info for individual job posting
        cards = self.soup.find_all("div","jobsearch-SerpJobCard")
        for card in cards:
            self.titles.append(card.h2.a.get("title"))
            self.companies.append(card.find('span', 'company').text.strip())
            self.locations.append(card.find('div', 'recJobLoc').get('data-rc-loc'))
            self.dates.append(card.find('span', 'date').text)
        # get full description
            time.sleep(5)
            jobURL = "http://indeed.com" + card.h2.a.get('href')
            job_response = requests.get(jobURL)
            job_soup = BeautifulSoup(job_response.text,"html.parser")
            job_description_tag = job_soup.find('div',{'id':'jobDescriptionText'})
            job_description = job_description_tag.text if job_description_tag else "N/A"
            self.descriptions.append(job_description)
    
    def save_to_csv(self,filename):
        d = {"Title":self.titles,"Company":self.companies,"Location":self.locations,"Date":self.dates,"Description":self.descriptions}
        df = pd.DataFrame(data=d)
        df.to_csv(filename)

# class DataStreamer():
    
#     def __init__(self):
#         self.count = 0

if __name__=='__main__':
    # m = DataSource_Indeed()
    # m.search("Data Science","Seattle")
    # m.get_info()
    # m.save_to_csv("example_indeed_scrape.csv")
    # print("DATA SCRAPED, AND SAVED")
    print("indeed is almost finished")

    