import sys
class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_detail:sys):
        _, _, exc_tb=error_detail.exc_info()
        self.error_message=error_message
        self.line_number=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return (
            f"Error occurred in script: [{self.file_name}] "
            f"at line number: [{self.line_number}] "
            f"error message: [{self.error_message}]"
        )
