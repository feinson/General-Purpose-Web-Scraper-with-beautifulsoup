''' This configuration file should be edited based on the website that you would like to scrape. 
    These variables will be used in the general_web_scraper and data_handling code.'''

# Set the URL variable to the one you would like the scrape to start on.
STARTING_URL = 'https://www.bbc.co.uk/news/politics/constituencies'

# This should be a list of selectors that BeautifulSoup can use to find the objects containing the list of links
LINKS_SELECTOR = 'tr[class="az-table__row"]'

# A dictionary that contains the properties that you want to scrape, their selector, and the attribute to
# extract.
DICT_PROPERTIES = {
    'Name': ('//h1[@class="productName_title"]', 'text'), 
    'Starting_Price': ('//p[@data-product-price="price"]', 'text'), 
    'Flavour_Selected': ('//select[@id="athena-product-variation-dropdown-5"]//option[@selected]', 'text'), 
    'Stars': ('//span[@class="athenaProductReviews_aggregateRatingValue"]', 'text'), 
    'Product_Image':('//img[@class="athenaProductImageCarousel_image"]', 'src'), 
    'Unique_ID':('//input[@name="prodId"]', 'value') 
    }

# This is the name of the bucket that the data will be stored in.
BUCKET_NAME = 'aicoredatacollectionbucket'


# This is the path to the raw data folder.
RAW_DATA_PATH = "./raw_data"