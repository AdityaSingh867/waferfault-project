import os , sys
from dataclasses import dataclass
from sklearn.ensemble import (AdaBoostClassifier , GradientBoostingClassifier ,RandomForestClassifier )
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from src.exception import CustomExcption
from src.logger import logging
from src.utils import save_object , load_object , evaluate_model

@dataclass 

class ModelTrainerConfig:
    Trained_model_file_path = os.path.join("artifacts" , "model.pkl")
        

class ModelTrainer:
    def __init__(self):
        self.mode_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self , train_array , test_array):
        try:
            logging.info(f"Splitting training and testing input and target feature")

            X_train , y_train , X_test , y_test = (
                train_array[: , :-1],
                train_array[: , -1],
                test_array[: , :-1],
                test_array[: , -1]
            )

            models = {
                "Random Forest" : RandomForestClassifier(),
                "Decision Tree" : DecisionTreeClassifier(),
                "Gradient Boosting" : GradientBoostingClassifier(),
                "K-Neighbors Classifire" : KNeighborsClassifier(),
                "XGBClassifire" : XGBClassifier(),
                'AdaBoost Classifire' : AdaBoostClassifier()
            }

            logging.info(f"Extracting model config file path")

            model_report : dict = evaluate_model(X=X_train , y=y_train , models=models)

            # To get best model score from dict

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_name)
            ]

            best_model = models[best_model_name]
            
            logging.info(f"Best found model on both training and testing dataset")            
            logging.info(f"saving model at path : {self.mode_trainer_config.Trained_model_file_path}")

            save_object(
                file_path=self.mode_trainer_config.Trained_model_file_path,
                obj=best_model
            )

        
        except Exception as e:
            logging.info("Exception occured in initiate_model_trainer")
            raise CustomExcption(e , sys)