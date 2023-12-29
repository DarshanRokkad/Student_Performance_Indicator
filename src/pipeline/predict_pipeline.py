import sys
import pandas as pd

from src.exception import CustomException
from src.logger import logging
from src.utils import load_object


class CustomData:
    def __init__(
            self, 
            gender:str,
            race_ethnicity:str,
            parental_level_of_education:str,
            lunch:str,
            test_preparation_course:str,
            reading_score:int,
            writing_score:int
        ):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dic = {
                'gender' : [self.gender],
                'race_ethnicity' : [self.race_ethnicity],
                'parental_level_of_education' : [self.parental_level_of_education],
                'lunch' : [self.lunch],
                'test_preparation_course' : [self.test_preparation_course],
                'reading_score' : [self.reading_score],
                'writing_score' : [self.writing_score],
            }
            
            df = pd.DataFrame(custom_data_input_dic)
            
            logging.info('Converted input data into DataFrame')

            return df
        
        except Exception as e:
            raise CustomException(e, sys)


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try: 
            logging.info('Prediction started')

            preproessor_path = 'artifacts/preprocessor.pkl'
            preprocessor = load_object(preproessor_path)
            model_path = 'artifacts/model.pkl'
            model = load_object(model_path)

            logging.info('loaded preprocessor and model object')

            scaled_data = preprocessor.transform(features)

            logging.info(f'Scaled input data')

            pred = model.predict(scaled_data)

            logging.info(f'Predicted output and output is {pred}')

            return pred
        
        except Exception as e:
            raise CustomException(e, sys)