import requests
from bs4 import BeautifulSoup

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
class DataSource_Monster():
    
    def __init__(self):
        self.base_url = "https://www.monster.com/jobs/search/"
        self.data = {}
        self.keywords = None
        self.location = None
        self.search_url = f"{self.base_url}?q=&where="
        self.soup = None
    
    def set_page(self,keywords,location):
        """Sets job search url, and page, by converting keywords and location into the needed format for Monster search url structure"""
        self.keywords = keywords.replace(" ","+")
        self.location = location.replace(" ", "")
        self.search_url = f"{self.base_url}?q={self.keywords}&where={self.location}"
        page = requests.get(self.search_url)
        print(page)
        self.soup = BeautifulSoup(page.content,"html.parser")


    def get_info(self):
        job_elems = self.soup.find_all('section', class_='card-content')
        for job_elem in job_elems:
            title_elem = job_elem.find('h2', class_='title')
            company_elem = job_elem.find('div', class_='company')
            location_elem = job_elem.find('div', class_='location')
            if None in (title_elem, company_elem, location_elem):
                continue
            print(title_elem.text.strip())
            print(company_elem.text.strip())
            print(location_elem.text.strip())
            print()
        
 

# class DataStreamer():
    
#     def __init__(self):
#         self.count = 0

if __name__=='__main__':
    m = DataSource_Monster()
    m.set_page("Data Science","Seattle")
    print(m.search_url)
    m.get_info()
    