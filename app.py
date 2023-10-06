from trafficsigndetection.logger import logging
from trafficsigndetection.exception import AppException
import sys
# Example usage
try:
    # Some code that might raise an exception
    x = 1 / "s"
except ZeroDivisionError as e:
    app_exception = AppException("Cannot divide by zero")
    error_message = app_exception.error_message_detail()
    print(error_message)