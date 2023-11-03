import sys

class customexception(Exception):
    def __init__(self, error_message, error_details:sys):
       self.error_message=error_message
       _,_,exe_tb = error_details.exc_info()

       self.line_no= exe_tb.tb_lineno #Get the line no
       self.file_name = exe_tb.tb_frame.f_code.co_filename #Get the file name in which error has occured
     

    def __str__(self): #This method is the string representation of teh object
        return "Error occured in the python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.line_no, str(self.error_message))
    

if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        raise customexception(e,sys)
