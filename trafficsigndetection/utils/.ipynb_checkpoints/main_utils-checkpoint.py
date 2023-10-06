import os.path
import sys
import yaml
import base64

# Custom exception class
from trafficsigndetection.exception import AppException

# Custom logger
from trafficsigndetection.logger import logging

def read_yaml_file(file_path: str) -> dict:
    """
    Read a YAML file and return its content as a dictionary.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        dict: Content of the YAML file as a dictionary.

    Raises:
        AppException: If there's an error reading the YAML file.
    """
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("Read YAML file successfully")
            return yaml.safe_load(yaml_file)

    except Exception as e:
        # Raise a custom exception with the original exception
        raise AppException("Error reading YAML file", sys) from e


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Write content to a YAML file.

    Args:
        file_path (str): Path to the YAML file.
        content (object): Content to be written (dictionary, list, etc.).
        replace (bool, optional): Whether to replace the existing file. Defaults to False.

    Raises:
        AppException: If there's an error writing to the YAML file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logging.info("Successfully wrote YAML file")

    except Exception as e:
        # Raise a custom exception with the original exception
        raise AppException("Error writing YAML file", sys) from e


def decodeImage(imgstring, fileName):
    """
    Decode a base64-encoded image string and save it to a file.

    Args:
        imgstring (str): Base64-encoded image string.
        fileName (str): Name of the file to save the image.

    Returns:
        None
    """
    imgdata = base64.b64decode(imgstring)
    with open("./data/" + fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    """
    Encode an image into base64.

    Args:
        croppedImagePath (str): Path to the image file.

    Returns:
        str: Base64-encoded image string.
    """
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
