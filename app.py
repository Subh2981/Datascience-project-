from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_transformation import DataTransformationconfig,DataTransformation
from src.mlproject.components.data_ingestion import DataIngestion,DataIngestionConfig

if __name__=="__main__":
    logging.info("The Execution has started")
    
    try:
        
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_path,test_path=data_ingestion.initialte_data_ingestion()
        #data_transformation_config=DataTransformationconfig()
        data_transformation=DataTransformation()
        data_transformation.initiate_data_transformation(train_path,test_path)
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
        