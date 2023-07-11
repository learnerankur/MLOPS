import sys

def error_message_detail(error,error_detail:sys):
    # execution information
    _,_,exc_tb=error_detail.exc_info() # first two info are not relevant, last info is relevant
    #print("error_detail execution info, thurd parameter value is",exc_tb)
    file_name=exc_tb.tb_frame.f_code.co_filename  # to get file name, fetching from exc_tb, search custom excpetion handling
    error_message="Error Occured in Python Script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    # constructor
    def __init__(self,error_message,error_detail:sys):
        # Inheriting from the exception
        super.__init__(error_message) 
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
    

