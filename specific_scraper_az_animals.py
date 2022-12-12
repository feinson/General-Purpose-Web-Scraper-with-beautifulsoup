from libraries_and_configuration_files.general_web_scraping import GeneralScraper
import pandas as pd

# Change the configuration file to specify what is to be scraped.
import libraries_and_configuration_files.configuration_file_az_animals as config

starting_url = config.STARTING_URL
links_selector = config.LINKS_SELECTOR
dict_properties = config.DICT_PROPERTIES
raw_data_path = config.RAW_DATA_PATH

try:                                                    
    links_selector_slice = config.LINKS_SELECTOR_SLICE #If, in the config file, we chose to only scrape from a slice of the list of selected objects. This is applied here.
except:
    links_selector_slice = None
    pass

if __name__ == "__main__":

    specific_scraper = GeneralScraper(raw_data_path, starting_url, links_selector, dict_properties, links_selector_slice)


    specific_scraper.create_raw_data_folder()
    list_of_urls = specific_scraper.make_list_of_urls_to_scrape()
    list_of_results_dicts = []

    for url in list_of_urls:

        results_dict = specific_scraper.scrape_data_from_url(url)
        GeneralScraper.add_uuid_to_dick(results_dict)
        specific_scraper.save_image_if_possible(results_dict)
        print(results_dict, flush=True)

        list_of_results_dicts.append(results_dict)

    complete_data = pd.DataFrame(list_of_results_dicts)
    specific_scraper.save_dataframe_as_csv(complete_data)
    

    