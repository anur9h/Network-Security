import sys
from networksecurity.logging.logger import logger

class NetworksecurityError(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occured in script: [{self.file_name}] at line number: [{self.lineno}] error message: [{self.error_message}]"


if __name__ == '__main__':
    try:
        logger.info('Logging started')  # ✅ Correct usage
        result = 10 / 0
        logger.info(f'Result: {result}')

    except Exception as e:
        raise NetworksecurityError(e, sys)
