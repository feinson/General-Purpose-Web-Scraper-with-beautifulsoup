import os
from pydantic import validate_arguments
import json
import requests


class DataHandler:

    def __init__(self, raw_data_path: str):
        
        self.raw_data_path = raw_data_path
        

    def create_raw_data_folder(self):
        
        '''It creates the raw_data folder in the specified path
        '''
        
        try:
            os.mkdir(self.raw_data_path)
        except FileExistsError:
            pass


    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def save_data_as_json(self, complete_data: dict):

         with open(f"{self.raw_data_path}/complete_data.json", 'w') as all_data:
            json.dump(complete_data, all_data, indent=4)

    #@validate_arguments(config=dict(arbitrary_types_allowed=True))
    def save_data_as_csv(self, complete_data: dict):

           complete_data.to_csv(f"{self.raw_data_path}/complete_data.csv")

    @validate_arguments
    def save_image_if_possible(self, properties_data: dict):

        try:
            img_source_url = properties_data.pop("Image source") #It should fail here and nowhere else

            image_folder = f"{self.raw_data_path}/images"
            try:
                os.mkdir(image_folder)
            except FileExistsError:
                pass

            try:

                unique_id = properties_data["UUID"]
                img_content = requests.get(img_source_url).content
                
                with open(f"{image_folder}/{unique_id}.jpg", "wb") as f:
                    f.write(img_content)

            except:
                print("No image was found to save.")
        except:
            pass
    

