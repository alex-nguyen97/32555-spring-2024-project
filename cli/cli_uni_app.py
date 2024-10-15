from .controllers.student_controller import StudentController
from .controllers.admin_controller import AdminController
from .views.student_view import StudentView
from .views.admin_view import AdminView
from colors.text_colors import *
from .utils.utils import ErrorMessageHandling

class CLISystem:
    def __init__(self):
        self.student_view = StudentView()
        self.admin_view = AdminView()
        self.student_controller = StudentController()
        self.admin_controller = AdminController()

    def run(self):
        print(CYAN + "Welcome to the University System" + RESET)
        while True:
            print(CYAN + "\nPlease select the following actions for University System: " + RESET)
            print("(A) Admin")
            print("(S) Student")
            print("(X) Exit")
            choice = input(CYAN + "Your choice: " + RESET).lower()

            if choice == "a":
                self.show_admin_menu()
            elif choice == "s":
                self.show_student_menu()
            elif choice == "x":
                print(YELLOW + "System is Exiting...")
                print(YELLOW + "Thank you!!" + RESET)
                break
            else:
                ErrorMessageHandling.printInvalidEntry()

    def show_admin_menu(self):
        while True:
            print(CYAN + "\nPlease select the following actions for Admin System: " + RESET)
            print("(C) Clear Database")
            print("(G) Group Students")
            print("(P) Partition Student")
            print("(R) Remove Student")
            print("(S) Show")
            print("(X) Exit")
            choice = input(CYAN + "Your choice: " + RESET).lower()
            if choice == "c":
                self.admin_controller.clear_database()
            elif choice == "g":
                self.admin_controller.group_students_by_grade()
            elif choice == "p":
                self.admin_controller.partition_students_by_pass_fail()
            elif choice == "r":
                self.admin_controller.remove_student_by_id()
            elif choice == "s":
                self.admin_controller.show_students_list()
            elif choice == "x":
                print(YELLOW + "Admin System is Exiting..." + RESET)
                break
            else:
                ErrorMessageHandling.printInvalidEntry()

    def show_student_menu(self):
        while True:
            print(CYAN + "\n Please select the following actions for Student System: " + RESET)
            print("(L) Login")
            print("(R) Register")
            print("(X) Exit")
            choice = input(CYAN + "Your choice: " + RESET).lower()
            if choice == "l":
                self.student_controller.login_student()
            elif choice == "r":
                self.student_controller.register_student()
            elif choice == "x":
                print(YELLOW + "Student System is Exiting..." + RESET)
                break
            else:
                ErrorMessageHandling.printInvalidEntry()

if __name__ == "__main__":
    cli_system = CLISystem()
    cli_system.run()
