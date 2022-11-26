import requests
from bs4 import BeautifulSoup
from pydantic import validate_arguments
from urllib.parse import urlparse

class GeneralScraper:

    @validate_arguments
    @staticmethod
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


    @validate_arguments
    def __init__(self, URL: str, links_selector: str):

        self.site_url = f"https://{urlparse(URL).hostname}"
        self.soup = GeneralScraper.make_soup(URL)
        self.links_selector = links_selector

    @validate_arguments
    def complete_rel_href(self, half_url: str):

        if half_url[0:len(self.site_url)] != self.site_url:
            half_url = f"{self.site_url}{half_url}"

        return half_url
    
    def make_list_of_urls_to_scrape(self):

        list_of_urls_to_scrape = []
        for item in self.soup.select(self.links_selector):
            list_of_urls_to_scrape.extend([self.complete_rel_href(container.get('href')) for container in item.find_all("a", href=True)])

        return list_of_urls_to_scrape

    @validate_arguments
    def scrape_data_from_link(self, url: str, properties_dict: dict):


        soup = GeneralScraper.make_soup(url)
        properties_data = {}

        for property in properties_dict:
            selector = properties_dict[property][0]
            result_container = soup.select_one(selector)

            if properties_data[property][1] == 'text':
                result = result_container.get_text()
            else:
                result = result_container.get(properties_data[property][1])

            properties_data[property] = result

        return properties_data




            
