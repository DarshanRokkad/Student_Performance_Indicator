import os
import sys
from src.logger import logging
from src.exception import CustomException

import numpy as np
import pandas as pd
import dill         # used to pickle the model or preprocessors
from sklearn.metrics import r2_score


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok = True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
        
        logging.info('object saved successfully')
    
    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(x_train, x_test, y_train, y_test, models):
    try:

        logging.info('Model evaluation starts')
        
        report = {}    

        for i in range(len(list(models))):
            # model creation
            regressor = list(models.values())[i]
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