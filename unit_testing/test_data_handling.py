import unittest
import os
import sys
sys.path.append("..")
import shutil
import pandas as pd

from libraries_and_configuration_files.data_handling import DataHandler


class TestDataHandler(unittest.TestCase):

    def setUp(self) -> None:

        self.test_path = "./test_raw_data"
        self.test_handler = DataHandler(self.test_path)
        self.test_properties_data = { 
            "Name" : "test_name",
            "UUID" : "bs4", 
            "Age" :"old", 
            "Image source" : "https://a-z-animals.com/media/alpalca-3.jpg"
            }

    def test_create_raw_data_folder(self):

            self.test_handler.create_raw_data_folder()

            self.assertTrue(os.path.exists(f"./test_raw_data"))

            os.rmdir(f"./test_raw_data")

    def test_save_data_as_json(self):

        self.test_handler.create_raw_data_folder()
        self.test_handler.save_data_as_json(self.test_properties_data)

        self.assertTrue(os.path.exists(f"{self.test_path}/complete_data.json"))

        shutil.rmtree(f"{self.test_path}")


    def test_save_dataframe_as_csv(self):

        self.test_handler.create_raw_data_folder()
        test_pandas_dataframe = pd.DataFrame(self.test_properties_data, self.test_properties_data)
        self.test_handler.save_dataframe_as_csv(test_pandas_dataframe)

        self.assertTrue(os.path.exists(f"{self.test_path}/complete_data.csv"))

        shutil.rmtree(f"{self.test_path}")


    def test_save_image_if_possible(self):

        self.test_handler.create_raw_data_folder()
        self.test_handler.save_image_if_possible(self.test_properties_data)

        uuid = self.test_properties_data["UUID"]
        self.assertTrue(os.path.exists(f"{self.test_path}/Images"))
        self.assertTrue(os.path.exists(f"{self.test_path}/Images/{uuid}.jpg"))

        shutil.rmtree(f"{self.test_path}")


if __name__ == "__main__":
    unittest.main()