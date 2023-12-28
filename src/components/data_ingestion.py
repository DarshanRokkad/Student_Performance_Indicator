import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass       # used to create class variable without using constructor

from src.components.data_transformation import DataTransformation


@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw_data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()    # contains all the data paths
    
    def initiate_data_ingestion(self):
        logging.info('Enter the data ingestion method')
        try:
            df = pd.read_csv('notebook\data\stud.csv')   # here we can give any other data source like MONGODB,... and read data
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)
            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)  # saving raw data

            logging.info('Train test split initiated')
            train_set, test_set = train_test_split(df, test_size = 0.2, random_state = 42)
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)   # saving train data
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)    # saving test data

            logging.info('Data ingestion completed')
            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)   # this will be used in data transformation
        
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == '__main__':
    # checking data ingestion
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    
    # checking data transformation
    data_transformation = DataTransformation()
    train_arr, test_arr, preprocessor_object_file_path = data_transformation.initiate_data_transformation(train_data_path, test_data_path)