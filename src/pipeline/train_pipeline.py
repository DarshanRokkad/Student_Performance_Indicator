import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

logging.info('Training pipeline started')

data_ingestion = DataIngestion()
train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

data_transformation = DataTransformation()
train_arr, test_arr = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

model_trainer = ModelTrainer()
model_trainer.initiate_model_training(train_arr, test_arr)

logging.info('Training pipeline completed')