# data-collection-pipeline

This repo contains the code for a semi general purpose web-scraper that runs using the library BeautifulSoup.

## Project structure:
The scripts ```data_handling.py``` and ```general_web_scraping.py``` are libraries that define classes used for general web-scraping. To scrape a specific website, an instance of the class ```GeneralScraper``` is created, which takes as input the specifications specified in a configuration file.

I have included three example web-scraping scripts, along with their configuration files. These are:
- ```specific_scraper_az_animals.py```
- ```specific_scraper_election.py```
- ```specific_scraper_imdb_250.py```

Each of these scripts is identical except for the configuration file that they import. To create a script to scrape a different website it would only be necessary to write a new configuration file, copy and paste one of these scripts and make the edit. These scripts run out of the box once the necessary requirements have been installed, and save their data as a ```.csv```.

## How it works
The scraper starts on a central URL that contains a number of links to other pages which are to be scraped. The specific selection of links can be configured in the configuration file. The scraper finds and saves the href of each of these links, then visits each one and gathers data from it.
The data to be gathered from each page can be configured in the configuration file.

## Configuration files
Since the BeautifulSoup library does not support XPath, elements to be scraped are found via their CSS selector. The configuration file must be given the CSS selectors for all data that is to be scraped. CSS selectors can be copied from a web-page using Chrome's 'inspect element' feature, but that will only give the absolute path selector. For greater precision, some knowledge of CSS selectors is required to write the configuration files. 

The parameters in the configuration file are as followed:

- ```STARTING_URL```: This is the central URL, from which the links to other pages will be gathered. For example, in ```specific_scraper_election.py``` script, this page is the BBC's a-z list of all UK constituencies: https://www.bbc.co.uk/news/politics/constituencies.
- ```LINKS_SELECTOR```: On the page of the starting URL, this is the CSS selector that will be used to gather all links. In the code it is parsed into BeautifulSoup's ```select``` method which returns a list of all elements satisfying that CSS selector. As such multiple 'containers of links' can be selected. For example, on the BBC's a-z contituency list there is a separate link container for each letter of the alphabet.
- ```LINKS_SELECTOR-SLICE```: (Optional) As mentioned above BeautifulSoup's select method returns a list so for extra precision you can input a slice object that will be applied to that list before scraping commences. In our election example, setting this to ```slice(0,1,1)``` will only scrape links from the first container, so only the constituencies beggining with the letter 'a'.
- ```DICT_PROPERTIES```: This parameter defines the data we want to scrape from each page. It is a dictionary object whose keys are the names of each of the pieces of the data we want to scrape. The values are a tuple object containing the CSS selector for the piece of data we are looking for, and a string which tells the scraper which attribute we would like to scrape from that element, for example: ```'text'``` or ```'href'```. To download an image, set the key to ```'Image Source'``` and the attribute to ```'src'```.
- ```RAW_DATA_PATH```: This parameter can be changed to change the name of the folder in which the output data is to be saved.

## Docker containerisation
The repo containers a Dockerfile that can be used to build a docker image to run these scripts. With its present configuration the resulting docker container will run indefinitely with no output. The individual scripts can then be run from within the in-container terminal. The simplest way to save the data produced by the scraper, when it is run in Docker, is to navigate to the directory where you would like to save the data and run the following command:

```docker run -v /$(pwd)/raw_data:/raw_data <docker_image_name>```

This creates a bind mount between the raw_data folder in the Docker container, and the raw_data folder created in the current directory.
This github repo has a workflow action that connects it to Dockerhub.