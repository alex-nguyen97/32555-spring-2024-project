from .controllers.student_controller import StudentController
from .controllers.admin_controller import AdminController
from colors.text_colors import *
from .utils.utils import ErrorMessageHandling
import os
from dotenv import load_dotenv

load_dotenv()
ENVIRONMENT = os.getenv('ENVIRONMENT')
UNIVERSITY_SYSTEM = os.getenv('UNIVERSITY_SYSTEM')
STUDENT_SYSTEM = os.getenv('STUDENT_SYSTEM')


class CLISystem:
    def __init__(self):
        self.student_controller = StudentController()
        self.admin_controller = AdminController()

    def run(self):
        print(CYAN + "Welcome to the University System" + RESET)
        while True:
            print(
                CYAN + "\nPlease select the following actions for University System: " + RESET)
            print("(A) Admin")
            print("(S) Student")
            print("(X) Exit")

            if (ENVIRONMENT == 'dev' and UNIVERSITY_SYSTEM != None):
                option = UNIVERSITY_SYSTEM
            else:
                option = input(CYAN + "Your choice: " + RESET).lower()

            if option == "a":
                self.show_admin_menu()
            elif option == "s":
                self.show_student_menu()
            elif option == "x":
                print(YELLOW + "System is Exiting...")
                print(YELLOW + "Thank you!!" + RESET)
                break
            else:
                ErrorMessageHandling.printInvalidEntry()

    def show_admin_menu(self):
        while True:
            print(
                CYAN + "\nPlease select the following actions for Admin System: " + RESET)
            print("(C) Clear Database")
            print("(G) Group Students")
            print("(P) Partition Student")
            print("(R) Remove Student")
            print("(S) Show")
            print("(X) Exit")

            option = input(CYAN + "Your choice: " + RESET).lower()

            if option == "c":
                self.admin_controller.clear_database()
            elif option == "g":
                self.admin_controller.group_students_by_grade()
            elif option == "p":
                self.admin_controller.partition_students_by_pass_fail()
            elif option == "r":
                self.admin_controller.remove_student_by_id()
            elif option == "s":
                self.admin_controller.show_students_list()
            elif option == "x":
                print(YELLOW + "Admin System is Exiting..." + RESET)
                break
            else:
                ErrorMessageHandling.printInvalidEntry()

    def show_student_menu(self):
        while True:
            print(
                CYAN + "\nPlease select the following actions for Student System: " + RESET)
            print("(L) Login")
            print("(R) Register")
            print("(X) Exit")

            if (ENVIRONMENT == 'dev' and STUDENT_SYSTEM != None):
                option = STUDENT_SYSTEM
            else:
                option = input(CYAN + "Your choice: " + RESET).lower()

            if option == "l":
                self.student_controller.login_student()
            elif option == "r":
                self.student_controller.register_student()
            elif option == "x":
                print(YELLOW + "Student System is Exiting..." + RESET)
                break
            else:
                ErrorMessageHandling.printInvalidEntry()


if __name__ == "__main__":
    cli_system = CLISystem()
    cli_system.run()
