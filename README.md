# data-collection-pipeline

This repo contains the code for a general purpose web-scraper. This is managed by the scripts data_handling.py and general_web_scraping.py.
There is an example of a specific web-scraper that scrapes the website az-animals by calling the configuration file.

The web-scraper runs using the BeautifulSoup library, which makes it faster than Selenium based web-scrapers.

This README will be massively improved very soon! 




For Docker
Once built, you can run the docker image using the command:

docker run -v /$(pwd)/raw_data:/raw_data second_attempt

in order to get the data out of the web-scraper. Once the container is running, the individual scripts can be run from the in-container command line. 