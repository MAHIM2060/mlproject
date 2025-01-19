import sys
from src.mlproject.logger import logging
def error_message_detail(error, error_detail: sys):
    """
    Function to capture and return error details, including the file name, 
    line number, and error message.
    """
    _, _,exc_tb = error_detail.exc_info()  # Get the traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  # File where the error occurred
    line_number = exc_tb.tb_lineno  # Line number where the error occurred
    error_message = f"Error occurred in script: {file_name} at line: {line_number}, error message: {str(error)}"
    return error_message
class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details)

    def __str__(self):
        return self.error_message