import logging
import os # required for the creation of files and folder
from datetime import datetime

# Construct the log file name using the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Construct the path to the log file in a 'log' directory (you can specify your path here)
log_path = os.path.join(os.getcwd(), "log", LOG_FILE)

# Ensure the directory structure for the log file exists
os.makedirs(os.path.dirname(log_path), exist_ok=True)

# Set the log file path
LOG_FILE_PATH = log_path

# Configure the logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Test the logging
logging.info("This is a test log message.")

