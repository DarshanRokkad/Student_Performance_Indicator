# data transformation is used to do feature engineering
import os
import sys
from src.exception import CustomException
from src.logger import logging

import numpy as np
import pandas as pd 
from sklearn.impute import SimpleImputer            # for handling missing values
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline               # to create pipeline for numerical and categorical features
from sklearn.compose import ColumnTransformer       # to combine both numerical and categorical pipeline
from dataclasses import dataclass
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_object_file_path = os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation 
        '''
        try:
            logging.info('Data transformation started')

            # create list of numerical and categorical features 
            numerical_features = [
                'reading_score', 
                'writing_score'
                ]
            categorical_features = [
                'gender', 
                'race_ethnicity', 
                'parental_level_of_education', 
                'lunch', 
                'test_preparation_course'
                ]
            
            logging.info(f'Numerical features: {numerical_features}')
            logging.info(f'Categorical features: {categorical_features}')
            
            # creating pipeline for numerical and categorical columns
            numerical_pipeline = Pipeline(
                steps = [
                    ('step 1 : median imputation', SimpleImputer(strategy = 'median')),
                    ('step 2 : standard scaling', StandardScaler())
                ]
            )
            categorical_pipeline = Pipeline(
                steps = [
                    ('step 1 : mode imputation', SimpleImputer(strategy = 'most_frequent')),
                    ('step 2 : one hot encoding', OneHotEncoder())
                ]
            )

            # combining the pipeline using column transformers
            preprocessor = ColumnTransformer(
                [
                    ('numerical pipeline', numerical_pipeline, numerical_features),
                    ('categorical pipeline', categorical_pipeline, categorical_features)
                ]
            )

            logging.info('Completed preprocessor column transformer object')

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)
    
    def initiate_data_transformation(self, train_data_path, test_data_path):
        try:
            logging.info('Data transformation initiated')

            # reading training and testing data
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)

            logging.info('Sucessfully read train and test data')

            # separating independent and dependent feature in both train and test dataframe
            output_feature = 'math_score'
            input_feature_train_df = train_df.drop(columns = [output_feature], axis = 1)
            output_feature_train_df = train_df[output_feature]
            input_feature_test_df = test_df.drop(columns = [output_feature], axis = 1)
            output_feature_test_df = test_df[output_feature]

            logging.info('Obtaining preprocessing data transformer object and applying on training and testing dataframe')

            # applying preprocessing on our data
            preprocesser_object = self.get_data_transformer_object()
            input_feature_train_arr = preprocesser_object.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocesser_object.transform(input_feature_test_df)
            train_arr = np.c_[input_feature_train_arr, np.array(output_feature_train_df)]           # concatinate data transformed training feature with output feature 
            test_arr = np.c_[input_feature_test_arr, np.array(output_feature_test_df)]

            logging.info('Completed preprocessing on training and test data')
            
            # save_object is implemented in utils.py can be used to pickle the object
            save_object(                
                file_path = self.data_transformation_config.preprocessor_object_file_path,
                obj = preprocesser_object
            )

            logging.info('Saved preprocessor object')

            return (train_arr, test_arr, self.data_transformation_config.preprocessor_object_file_path)         # this is further used to train model


        except Exception as e:
            raise CustomException(e, sys)
