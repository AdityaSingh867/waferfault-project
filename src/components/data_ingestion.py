import os , sys 
from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

from src.exception import CustomExcption
from src.logger import logging


@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts' , "train.csv")
    raw_data_path :str = os.path.join('artifacts' , "raw.csv")
    test_data_path : str = os.path.join('artifacts' , 'test.csv')




class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")

        try :
            df = pd.read_csv(os.path.join('notebooks' , 'wafer_23012020_041211.csv'))
            logging.info("Expored collection as DataFrame")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path) , exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False , header=True)

            train_set , test_set = train_test_split(df , test_size=0.2 , random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path , index=False , header = True) 

            test_set.to_csv(self.ingestion_config.test_data_path , index=False , header = True)

            logging.info(f"data ingested from notebooks folder {self.ingestion_config.raw_data_path}")

            logging.info("Exited initiate_data_ingestion method of DataIngestion class")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            logging.info("Exception Occured in DataIngestion")
            raise CustomExcption(e , sys)