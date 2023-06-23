import os , sys
import pandas as pd
import numpy as np
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from src.logger import logging 
from src.exception import CustomExcption

def save_object(file_path , obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path , exist_ok=True)

        with open(file_path , 'wb') as file_obj:
            dill.dump(obj , file_obj)

    except Exception as e:
        logging.info("Exception occured in save_obj")
        raise CustomExcption(e , sys)
    
def load_object(file_path):
    try:
        with open(file_path , 'rb') as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        logging.info("Exception occured in load_object")
        raise CustomExcption(e , sys)
    

def evaluate_model(X , y , models):
    try:
        X_train , X_test , y_train , y_test = train_test_split(
            X , y , test_size=0.2 , random_state=42)
        
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i] 

            model.fit(X_train , y_train)

            # Prediction

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train , y_train_pred)

            test_model_score = r2_score(y_test , y_test_pred)

            report[list(models.keys())[i]] = test_model_score

            return report
        
    except Exception as e:
        logging.info("Exception occured in evaluate model")
        raise CustomExcption(e , sys)