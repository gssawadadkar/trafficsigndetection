import sys

class AppException(Exception):
    def __init__(self, error_message):
        """
        Custom exception class to store error details.

        Args:
            error_message (str): The error message.
        """
        super().__init__(error_message)
        self.error_message = error_message

    def error_message_detail(self):
        """
        Generates a detailed error message with file name and line number.

        Returns:
            str: Detailed error message.
        """
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"Error occurred in file '{file_name}', line {line_number}: {self.error_message}"


# # Example usage
# try:
#     # Some code that might raise an exception
#     x = 1 / 0
# except ZeroDivisionError as e:
#     app_exception = AppException("Cannot divide by zero")
#     error_message = app_exception.error_message_detail()
#     print(error_message)

