import os
from pydantic import validate_arguments
import json


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
    def save_data_to_folder(self, complete_data: dict):

         with open(self.raw_data_path + '/data.json', 'w') as all_data:
            json.dump(complete_data, all_data, indent=4)   


    def save_image(self):

        try:
            os.mkdir(self.raw_data_path + '/images')
        except FileExistsError:
            pass
    

