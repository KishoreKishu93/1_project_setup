
import pandas as pd
import numpy as np
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

import os
import sys

class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts","raw.csv")
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")

        try:
            data = pd.read_csv(Path(os.path.join("notebooks/data","gemstone.csv")))
            logging.info("I have read the dataset as a dataframe")
            
            #Create a Artifact folder
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)), exist_ok=True)
            #Save the data file in that folder
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Saved the raw data in artifacts folder")

            logging.info("Perform train test split")
            train_data,test_data=train_test_split(data, test_size=0.25)

            #Saved Train and Test data in artifacts folder
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            logging.info("Saved Train and Test data in artifacts folder")
            logging.info("train test split completed")

        except Exception as e:
            logging.info("exception occured during the DataIngestion stage")
            raise customexception(e,sys)

    


