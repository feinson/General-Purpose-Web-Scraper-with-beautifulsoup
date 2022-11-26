import requests
from bs4 import BeautifulSoup
from general_web_scraping import GeneralScraper
import configuration_file_az_animals


class AnimalScraper(GeneralScraper):

    def __init__(self):
        self.url = configuration_file_az_animals.STARTING_URL
        self.links_selector = configuration_file_az_animals.LINKS_SELECTOR


