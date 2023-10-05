import os
from pathlib import Path # used to detect the type of operating system and manage path accordingly
import logging # for to show every log after executing every code snipet

# logging.basicConfig(level=logging.INFO,format="[%(asctime)s]:%(massages)s") # it will show time of execution and massages
logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

project_name="trafficsigndetection" # it is a root folder and it contains all config and required files
list_of_files=[
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/constant/config_entity.py",
    f"{project_name}/constant/artifacts_entity.py",
    f"{project_name}/exception/__init__.py",   # for custom exception
    f"{project_name}/logger/__init__.py", # custom log
    f"{project_name}/pipeline/__init__.py", # training pipeline
    f"{project_name}/constant/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "test.txt"
]
# github should not be empty so keep git file and used for cicd pipeline and tracking the updation after creating main.yaml we will replace it with it
# data folder is for to store the image which is upload by user for testing
#  f"{project_name}/__init__.py" it act as local package to access all files which are in project directory
# f"{project_name}/components/__init__.py" create components folder and act as package for this __init__.py file is created

for filepath in list_of_files:  # Iterate through the list of file paths
    filepath = Path(filepath)  # Convert the file path to a Path object
    
    # Split the file path into directory and filename
    filedir, filename = os.path.split(filepath)
    
    # Check if the directory is not an empty string
    if filedir != "":
        # Create the directory if it doesn't exist
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    # Check if the file doesn't exist or is empty
    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        # Create an empty file
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filename}")

    else:
        logging.info(f"{filename} is allready created.")