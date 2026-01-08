import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

projectname='mlproject'

list_of_file=[
    f"src/{projectname}/__init__.py",
    f"src/{projectname}/components/__init__.py",
    f"src/{projectname}/components/data_ingestion.py",
    f"src/{projectname}/components/data_transformation.py",
    f"src/{projectname}/components/model_trainer.py",
    f"src/{projectname}/components/model_monitering.py",
    f"src/{projectname}/pipelines/__init__.py",
    f"src/{projectname}/components/training_pipeline.py",
    f"src/{projectname}/components/prediction_pipeline.py",
    f"src/{projectname}/exception.py",
    f"src/{projectname}/logger.py",
    f"src/{projectname}/utils.py",
    "app.py",
    "Dockerfile",
    "requirement.txt",
    "setup.py",
    "main.py"
]

for filepath in list_of_file:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for file {filename}")
        
    if (not os.path.exists(filepath)) or(os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exist")