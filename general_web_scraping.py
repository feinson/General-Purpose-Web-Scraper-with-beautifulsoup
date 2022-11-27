import requests
from bs4 import BeautifulSoup
from pydantic import validate_arguments
from urllib.parse import urlparse
import uuid

from data_handling import DataHandler

class GeneralScraper(DataHandler):

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
    def __init__(self, raw_data_path: str, URL: str, links_selector: str, dict_properties: dict, links_selector_slice = None):

        super().__init__(raw_data_path)
        self.site_url = f"https://{urlparse(URL).hostname}"
        self.soup = GeneralScraper.make_soup(URL)
        self.links_selector = links_selector
        self.dict_properties = dict_properties

        self.links_selector_slice = links_selector_slice


    @validate_arguments
    @staticmethod
    def add_uuid_to_dick(properties_data: dict):
        properties_data["UUID"] = str(uuid.uuid4())

    @validate_arguments
    def complete_rel_href(self, half_url: str):

        if half_url[0:len(self.site_url)] != self.site_url:
            half_url = f"{self.site_url}{half_url}"

        return half_url
    
    def make_list_of_urls_to_scrape(self):

        list_of_urls_to_scrape = []

        url_containers = self.soup.select(self.links_selector)
        if self.links_selector_slice != None:
            url_containers = url_containers[self.links_selector_slice]

        for item in url_containers:
            list_of_urls_to_scrape.extend([self.complete_rel_href(container.get('href')) for container in item.find_all("a", href=True)])

        return list_of_urls_to_scrape

    @validate_arguments
    def scrape_data_from_url(self, url: str):


        soup = GeneralScraper.make_soup(url)
        properties_data = {}

        for property in self.dict_properties:
            try:
                selector = self.dict_properties[property][0]
                result_container = soup.select_one(selector)

                if self.dict_properties[property][1] == 'text':
                    result = result_container.get_text()
                else:
                    result = result_container.get(self.dict_properties[property][1])
                
            except:
                result = "Not found"
                print(f"'{property}' could not be found.")
                
            properties_data[property] = result

        properties_data["Page URL"] = url

        # print(properties_data["Name"])
        return properties_data




            
