''' This configuration file should be edited based on the website that you would like to scrape. 
    These variables will be used in the general_web_scraper and data_handling code.'''

# Set the URL variable to the one you would like the scrape to start on.
STARTING_URL = 'https://www.imdb.com/chart/top/'

# This should be a list of selectors that BeautifulSoup can use to find the objects containing the list of links
LINKS_SELECTOR = 'td[class="titleColumn"]'
#LINKS_SELECTOR_SLICE = slice(0,1,1) # OPTIONAL: The BeautifulSoup select function returns a list. We can select a slice of that list if we want. If not comment this out.


# A dictionary that contains the properties that you want to scrape, their selector, and the attribute to
# extract. Because BeautifulSoup doesn't support Xpath, we have to use CSS selectors which is a bit of a nightmare. For some sites it should be easier.
DICT_PROPERTIES = {
    'Film name': ('#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-80d4314-0.fjPRnj > div.sc-80d4314-1.fbQftq > h1', 'text') 
    ,'Year': ('#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-80d4314-0.fjPRnj > div.sc-80d4314-1.fbQftq > div > ul > li:nth-child(1) > a', 'text') 
    ,'Director': ('#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-7643a8e3-2.ebKPVC > div.sc-7643a8e3-10.itwFpV > div.sc-7643a8e3-4.iAthmE > div.sc-fa02f843-0.fjLeDR > ul > li:nth-child(1) > div > ul > li > a', 'text')
    ,'Certificate': ('#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-80d4314-0.fjPRnj > div.sc-80d4314-1.fbQftq > div > ul > li:nth-child(2) > a', 'text')
    ,'Duration': ('#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-80d4314-0.fjPRnj > div.sc-80d4314-1.fbQftq > div > ul > li:nth-child(3)', 'text')
    ,'IMDB Rating': ('#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-80d4314-0.fjPRnj > div.sc-db8c1937-0.eGmDjE.sc-80d4314-3.iBtAhY > div > div:nth-child(1) > a > div > div > div.sc-7ab21ed2-0.fAePGh > div.sc-7ab21ed2-2.kYEdvH > span.sc-7ab21ed2-1.jGRxWM', 'text')
    ,'Reviews page link': ('#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-80d4314-0.fjPRnj > div.sc-db8c1937-0.eGmDjE.sc-80d4314-3.iBtAhY > div > div:nth-child(1) > a', 'href')
    #If there is an image add the image source selector here. The attribute to download must be set to 'src'.
    ,'Image source': ('img[class="ipc-image"]', 'src')
    }

    # 

# This is the name of the bucket that the data will be stored in.
BUCKET_NAME = 'aicoredatacollectionbucket'


# This is the path to the raw data folder.
RAW_DATA_PATH = "./raw_data"