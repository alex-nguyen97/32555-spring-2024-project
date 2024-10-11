from .controllers.student_controller import StudentController
from .controllers.admin_controller import AdminController
from .views.student_view import StudentView
from .views.admin_view import AdminView
from colors.text_colors import *
from .utils.utils import Utils

class CLISystem:
    def __init__(self):
        self.student_view = StudentView()
        self.admin_view = AdminView()
        self.student_controller = StudentController()
        self.admin_controller = AdminController()

    def run(self):
        while True:
            choice = input(CYAN + "University System: (A)dmin, (S)tudent, or X: " + RESET)

            if choice.lower() == "a":
                self.handle_admin_menu()
            elif choice.lower() == "s":
                self.handle_student_menu()
            elif choice.lower() == "x":
                print(YELLOW + "Thank you" + RESET)
                break
            else:
                Utils.printInvalidEntry()

    def handle_admin_menu(self):
        while True:
            choice = input(CYAN + "\nAdmin System (c/g/p/r/s/x): " + RESET)
            if choice.lower() == "c":
                self.admin_controller.clear_database()
            elif choice.lower() == "g":
                self.admin_controller.group_students_by_grade()
            elif choice.lower() == "p":
                self.admin_controller.partition_students_by_pass_fail()
            elif choice.lower() == "r":
                self.admin_controller.remove_student_by_id()
            elif choice.lower() == "s":
                self.admin_controller.show_students_list()
            elif choice.lower() == "x":
                break
            else:
                print(RED + "Invalid choice. Please select again." + RESET)

    def handle_student_menu(self):
        while True:
            choice = input(CYAN + "Student Stytem (l/r/x): " + RESET)

            if choice.lower() == "l":
                self.student_controller.login_student()
            elif choice.lower() == "r":
                self.student_controller.register_student()
            elif choice.lower() == "x":
                break
            else:
                Utils.printInvalidEntry()

if __name__ == "__main__":
    cli_system = CLISystem()
    cli_system.run()
