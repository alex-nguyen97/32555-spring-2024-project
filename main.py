import sys
from cli.cli_uni_app import CLISystem
from gui.gui_uni_app import GUIUniApp
from models.database import Database
from colors.text_colors import *
from cli.utils.utils import ErrorMessageHandling
from dotenv import load_dotenv
import os

load_dotenv()
ENVIRONMENT = os.getenv('ENVIRONMENT')
TYPE_OF_APPLICATION = os.getenv('TYPE_OF_APPLICATION')


def start_program():
    print(CYAN + 'Here are the types of applications: ' + RESET)
    print('(1) CLIUniApp')
    print('(2) GUIUniApp')
    print("(X) Exit")
    while (True):
        if (ENVIRONMENT == 'dev'):
            option = TYPE_OF_APPLICATION
        else:
            option = input(
                CYAN + 'Please choose the type of application that you want to start: ' + RESET)

        if (option == '1'):
            print(YELLOW + 'You have chosen the CLIUniApp!' + RESET)
            cli_app = CLISystem()
            cli_app.run()
            return
        elif (option == '2'):
            print(YELLOW + 'You have chosen the GUIUniApp!' + RESET)
            gui_app = GUIUniApp()
            gui_app.run()
            return
        elif (option == 'X'):
            print('Program is exiting...')
            return
        else:
            ErrorMessageHandling.printInvalidEntry()


def main():
    Database()
    start_program()


if __name__ == "__main__":
    main()
