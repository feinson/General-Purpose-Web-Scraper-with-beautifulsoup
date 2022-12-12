''' This configuration file should be edited based on the website that you would like to scrape. 
    These variables will be used in the general_web_scraper and data_handling code.'''

# Set the URL variable to the one you would like the scrape to start on.
STARTING_URL = 'https://www.bbc.co.uk/news/politics/constituencies'

# This should be a list of selectors that BeautifulSoup can use to find the objects containing the list of links
LINKS_SELECTOR = 'table[class="az-table"]'
#LINKS_SELECTOR_SLICE = slice(0,1,1) # OPTIONAL: The BeautifulSoup select function returns a list. We can select a slice of that list if we want. If not comment this out.


# A dictionary that contains the properties that you want to scrape, their selector, and the attribute to
# extract. Because BeautifulSoup doesn't support Xpath, we have to use CSS selectors which is a bit of a nightmare. For some sites it should be easier.
DICT_PROPERTIES = {
    'Constituency': ('#constituency_title > div > h1', 'text') 
    ,'Result': ('p[class="ge2019-constituency-result-headline__text"]', 'text') 
    ,'Winning Party': ('#constituency_result_table2019 > div > ol > li:nth-child(1) > div > div > span[class="ge2019-constituency-result__party-name"]', 'text')
    ,'Second Party': ('#constituency_result_table2019 > div > ol > li:nth-child(2) > div > div > span[class="ge2019-constituency-result__party-name"]', 'text')
    ,'MP': ('#constituency_result_table2019 > div > ol > li:nth-child(1) > div.ge2019-constituency-result__row > div.ge2019-constituency-result__candidate > span', 'text')
    ,'Votes for winning party': ('#constituency_result_table2019 > div > ol > li:nth-child(1) > div.ge2019-constituency-result__details > ul > li:nth-child(1) > span > span.ge2019-constituency-result__details-value', 'text')
    #If there is an image add the image source selector here.
    #,'Image source': ('#single-animal-text > figure.wp-block-image.size-large > img, #single-animal-text > figure.wp-container-2.wp-block-gallery-1.wp-block-gallery.has-nested-images.columns-default.is-cropped > figure > img, #single-animal-text > div:nth-child(31) > figure > img, #single-animal-text > div.wp-block-image > figure > img', 'src')
    }

    # 



# This is the path to the raw data folder.
RAW_DATA_PATH = "./raw_data"