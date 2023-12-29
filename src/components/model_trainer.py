import os
import sys

from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from src.utils import save_object, evaluate_models

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
# from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.metrics import r2_score


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info('Starting model training')

            # spliting independent and dependent feature in train and test data
            x_train, y_train, x_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            # creating models dictionary to create all object
            models = {
                'Linear Regressor' : LinearRegression(), 
                'Decision Tree Regressor' : DecisionTreeRegressor(),
                'Random Forest Regressor' : RandomForestRegressor(),
                'AdaBoost Regressor' : AdaBoostRegressor(),
                'Gradient Boosting Regressor' : GradientBoostingRegressor(),
                # 'XG Boost Regressor' : XGBRegressor(),
                'CatBoosting Regressor' : CatBoostRegressor(verbose = False)
            }

            logging.info('All models Created')

            # hyperparameter turning
            parameters = {
                "Linear Regressor" : {},
                "Decision Tree Regressor": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                "Random Forest Regressor":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "AdaBoost Regressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Gradient Boosting Regressor":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                # "XG Boost Regressor":{
                #     'learning_rate':[.1,.01,.05,.001],
                #     'n_estimators': [8,16,32,64,128,256]
                # },
                "CatBoosting Regressor":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                }
            }
            
            # creating model report which is implemented in utils.py
            models_report:dict = evaluate_models(x_train, x_test, y_train, y_test, models, parameters)
            
            logging.info(f'{models_report}')
            
            # getting best model score and best model name
            max_model_score = max(list(models_report.values()))
            best_model_name = [model_name for model_name in list(models_report.keys()) if models_report[model_name] == max_model_score][0]
            best_model = models[best_model_name]

            logging.info(f'Best model is {best_model_name} with r2 score {max_model_score}')

            # keeping some threshold for model score 
            if max_model_score < 0.6:
                logging.info('No Best Model')
                raise CustomException('No best model found', sys)
            
            # training best model 
            y_pred = best_model.predict(x_test)
            r2_sco = r2_score(y_test, y_pred)
                
            # save the best model
            save_object(
                self.model_trainer_config.trained_model_file_path,
                best_model
            )

            logging.info('Best Model saved as pickle file')

            return r2_sco
        
        except Exception as e:
            raise CustomException(e, sys)