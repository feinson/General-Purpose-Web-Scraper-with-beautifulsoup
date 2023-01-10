from bs4 import BeautifulSoup
import requests

def make_soup(url: str):


            '''It takes a url as an argument, makes a request to that url, and returns a BeautifulSoup object
            with html parsing.

            Parameters
            ----------
            url
                the url of the page you want to scrape
            
            Returns
            -------
                the soup object.
            
            '''
            soup = BeautifulSoup(requests.get(url).content, "html.parser")
            return soup

soup = make_soup("https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/")

listy = soup.select('#main-content > div > div > span > table > tbody > tr')

print(listy)