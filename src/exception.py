import sys
# sys is used to access the variable and functions that describe the of the running python environment.


def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info() # it will give in which file and which line error is occured
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_num = exc_tb.tb_lineno
    error_message = f'Error occured in python script name [{file_name}] line number [{line_num}] error message [{str(error)}]'
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
    

# added below code just to test file
# from src.logger import logging
# if __name__ == '__main__':
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info('Divide by Zero')
#         raise CustomException(e, sys)
