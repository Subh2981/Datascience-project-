import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import os
from src.mlproject.utils import save_object

@dataclass
class DataTransformationconfig:
    preprocessor_obj_file_path=os.path.join('atifacts','preprocessor.pkl')
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationconfig()
        
    def get_data_transformation_objecct(self):
        try:
            numeric=['reading_score', 'writing_score']
            category=['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch',
                        'test_preparation_course']
            num_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy='median')),
                ('scalar',StandardScaler())
            ])
            cat_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy='most_frequent')),
                ("onehotencoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
            ])
            logging.info(f"categorical columns: {category}")
            logging.info(f"Numerical columns: {numeric}")
            
            preprocessor=ColumnTransformer([
            ("num_pipeline",num_pipeline,numeric),
            ('category_pipeline',cat_pipeline,category)
            ])
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info("Reading the train and test file")
            
            preprocessing_obj=self.get_data_transformation_objecct()
            
            target_column_name='math_score'
            numeric=['reading_score', 'writing_score']
            
            input_fetures_train=train_df.drop(columns=[target_column_name],axis=1)
            target_fetures_train=train_df[target_column_name]
            
            input_fetures_test=test_df.drop(columns=[target_column_name],axis=1)
            target_fetures_test=test_df[target_column_name]
            
            logging.info("Appplying preprocessing on training and testing data")
            
            input_fetures_train_arr=preprocessing_obj.fit_transform(input_fetures_train)
            input_fetures_test_arr=preprocessing_obj.transform(input_fetures_test)
            
            train_arr=np.c_[input_fetures_train_arr,np.array(target_fetures_train)]
            test_arr=np.c_[input_fetures_test_arr,np.array(target_fetures_test)]
            
            logging.info(F"Saved preproceinng")
            
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(sys,e)