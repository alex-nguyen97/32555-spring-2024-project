import re
from colors.text_colors import *

class Utils:
    EMAIL_REGEX = r"^[a-z.]+@university\.com$"
    PASSWORD_REGEX = r"^[A-Z][a-zA-Z]{5,}[0-9]{3,}$"

def printErrorMessage(errorMessage): 
    print(RED + errorMessage + RESET)

def printSuccessMessage(successMessage): 
    print(GREEN + successMessage + RESET)
    
class ErrorMessageHandling:
    def printInvalidEntry():
        printErrorMessage("Invalid choice. Please select again.")
    def printFileNotFound():
        printErrorMessage("The file does not exist!")
        print(YELLOW + "Create a new file..." + RESET)
    def printUpdateStudentFailed(): 
        printErrorMessage("Update student failed. The student does not exist. Please try again!")

class SuccessMessageHandling: 
    def printUpdateStudentSuccessful(): 
        printSuccessMessage("Update student successfully")
