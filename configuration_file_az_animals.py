''' This configuration file should be edited based on the website that you would like to scrape. 
    These variables will be used in the general_web_scraper and data_handling code.'''

# Set the URL variable to the one you would like the scrape to start on.
STARTING_URL = 'https://a-z-animals.com/animals/'

# This should be a list of selectors that BeautifulSoup can use to find the objects containing the list of links
LINKS_SELECTOR = 'ul[class="list-unstyled row"]'
LINKS_SELECTOR_SLICE = slice(0,1,1) # OPTIONAL: The BeautifulSoup select function returns a list. We can select a slice of that list if we want. If not comment this out.


# A dictionary that contains the properties that you want to scrape, their selector, and the attribute to
# extract. Because BeautifulSoup doesn't support Xpath, we have to use CSS selectors which is a bit of a nightmare. For some sites it should be easier.
DICT_PROPERTIES = {
    'Name': ('#title-header > div > div:nth-child(1) > div > h1', 'text') 
    ,'Latin Name': ('#title-header > div > div:nth-child(1) > div > p', 'text') 
    ,'Class': ('#content-wrapper > div > main > article > div.entry-content > div.row.animal-facts-box > div:nth-child(1) > dl > dd:nth-child(6)', 'text') 
    ,'Conservation status': ('a[href="/animals/endangered/extinct/"], a[href="/animals/endangered/least-concern/"], a[href="/animals/endangered/extinct-in-the-wild/"], a[href="/animals/endangered/critically-endangered/"], a[href="/animals/endangered/endangered/"], a[href="/animals/endangered/vulnerable/"], a[href="/animals/endangered/near-threatened/"], a[href="/animals/endangered/data-deficient/"], a[href="/animals/endangered/not-evaluated/"], a[href="/animals/endangered/not-listed/"]', 'text')
    #If there is an image add the image source selector here.
    #,'Image source': ('#single-animal-text > figure.wp-block-image.size-large > img, #single-animal-text > figure.wp-container-2.wp-block-gallery-1.wp-block-gallery.has-nested-images.columns-default.is-cropped > figure > img, #single-animal-text > div:nth-child(31) > figure > img, #single-animal-text > div.wp-block-image > figure > img', 'src')
    }

    # 

# This is the name of the bucket that the data will be stored in.
BUCKET_NAME = 'aicoredatacollectionbucket'


# This is the path to the raw data folder.
RAW_DATA_PATH = "./raw_data"