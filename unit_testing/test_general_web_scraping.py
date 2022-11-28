import unittest
import bs4
import sys
sys.path.append("..")

from libraries_and_configuration_files.general_web_scraping import GeneralScraper

class TestGeneralScraper(unittest.TestCase):

    def setUp(self) -> None:
        
        self.test_path = "./test_raw_data"
        self.test_start_url = "https://a-z-animals.com/animals/"
        self.test_links_selector = 'ul[class="list-unstyled row"]'
        self.test_dict_properties = {
    'Name': ('#title-header > div > div:nth-child(1) > div > h1', 'text') 
    ,'Latin Name': ('#title-header > div > div:nth-child(1) > div > p', 'text') 
    ,'Class': ('#content-wrapper > div > main > article > div.entry-content > div.row.animal-facts-box > div:nth-child(1) > dl > dd:nth-child(6)', 'text') 
    ,'Conservation status': ('a:is([href="/animals/endangered/extinct/"],[href="/animals/endangered/least-concern/"],[href="/animals/endangered/extinct-in-the-wild/"],[href="/animals/endangered/critically-endangered/"],[href="/animals/endangered/endangered/"],[href="/animals/endangered/vulnerable/"],[href="/animals/endangered/near-threatened/"],[href="/animals/endangered/data-deficient/"],[href="/animals/endangered/not-evaluated/"],[href="/animals/endangered/not-listed/"])', 'text')
    ,'Diet': ('dt:has(a[href="https://a-z-animals.com/reference/glossary/#jump-diet"]) + dd', 'text')
    #If there is an image add the image source selector here.
    #,'Image source': ('#single-animal-text > figure.wp-block-image.size-large > img, #single-animal-text > figure.wp-container-2.wp-block-gallery-1.wp-block-gallery.has-nested-images.columns-default.is-cropped > figure > img, #single-animal-text > div:nth-child(31) > figure > img, #single-animal-text > div.wp-block-image > figure > img', 'src')
    }

        self.test_web_scraper = GeneralScraper(self.test_path, self.test_start_url, self.test_links_selector, self.test_dict_properties, slice(0,1,1))


    def test_make_soup(self):

        soup = GeneralScraper.make_soup(self.test_start_url)

        self.assertIsInstance(soup, bs4.BeautifulSoup)


    def test_add_uuid_to_dick(self):

        test_dict = self.test_web_scraper.dict_properties
        GeneralScraper.add_uuid_to_dick(test_dict)

        self.assertIn("UUID", test_dict)

    def test_complete_rel_href(self):

        test_half_url = "/animals/alpaca/"
        full_url = self.test_web_scraper.complete_rel_href(test_half_url)

        
        self.assertEqual(full_url[0:len(self.test_web_scraper.site_url)],self.test_web_scraper.site_url)

    def test_make_list_of_urls_to_scrape(self):

        test_list_of_urls_to_scrape = self.test_web_scraper.make_list_of_urls_to_scrape()

        self.assertIsInstance(test_list_of_urls_to_scrape, list)

    def test_scrape_data_from_url(self):

        test_individual_url = "https://a-z-animals.com/animals/alpaca/"
        test_properties_data = self.test_web_scraper.scrape_data_from_url(test_individual_url)

        self.assertIsInstance(test_properties_data, dict)
        self.assertEqual(test_properties_data["Name"],"Alpaca")

    



if __name__ == "__main__":
    unittest.main()



        
