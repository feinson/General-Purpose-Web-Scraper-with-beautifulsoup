''' This configuration file should be edited based on the website that you would like to scrape. 
    These variables will be used in the general_web_scraper and data_handling code.'''

# Set the URL variable to the one you would like the scrape to start on.
STARTING_URL = 'https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/'

# This should be a list of selectors that BeautifulSoup can use to find the objects containing the list of links
LINKS_SELECTOR = '#main-content > div > div > span > table > tbody > tr'
#LINKS_SELECTOR_SLICE = slice(0,1,1) # OPTIONAL: The BeautifulSoup select function returns a list. We can select a slice of that list if we want. If not comment this out.


# A dictionary that contains the properties that you want to scrape, their selector, and the attribute to
# extract. Because BeautifulSoup doesn't support Xpath, we have to use CSS selectors which is a bit of a nightmare. For some sites it should be easier.
DICT_PROPERTIES = {
    'Course Name': ('#main-title > h1', 'text') 
    ,'Entrance Requirements': ('td:has(img[src="//www.ox.ac.uk/sites/files/oxford/media_wysiwyg/edit-pencil-icon-70.png"]) + td + td, td:has(img[src="https://www.ox.ac.uk/sites/files/oxford/media_wysiwyg/edit-pencil-icon-70.png"]) + td + td', 'text') 

    #If there is an image add the image source selector here. The attribute to download must be set to 'src'.
    #,'Image source': ('img[class="ipc-image"]', 'src')
    }

    # 



# This is the path to the raw data folder.
RAW_DATA_PATH = "./raw_data"