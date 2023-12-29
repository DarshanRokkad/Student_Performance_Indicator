import os
import sys
from src.logger import logging
from src.exception import CustomException

import numpy as np
import pandas as pd
import dill         # used to pickle the model or preprocessors
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok = True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
        
        logging.info('object saved successfully')
    
    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(x_train, x_test, y_train, y_test, models, params):
    try:

        logging.info('Model evaluation starts')
        
        report = {}            

        for i in range(len(list(models))):
            # model creation
            regressor = list(models.values())[i]

            # adding hyperparameter tuning
            param = params[list(models.keys())[i]]
            grid_cv = GridSearchCV(estimator = regressor, param_grid = param, cv = 5)
            grid_cv.fit(x_train, y_train)
            regressor.set_params(**grid_cv.best_params_)

            # model training
            regressor.fit(x_train, y_train)
            
            # prediction 
            y_pred = regressor.predict(x_test)

            # model score
            r2 = r2_score(y_test, y_pred)

            # adding score to report 
            report[list(models.keys())[i]] = r2

        logging.info('Model evaluation complete')
        
        return report
    
    except Exception as e:
        CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            obj = dill.load(file_obj)
            logging.info('object loaded')            
            return obj
        
    except Exception as e:
        raise CustomException(e, sys)