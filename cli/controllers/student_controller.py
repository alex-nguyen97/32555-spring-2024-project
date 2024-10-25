from models.student import Student
from models.subject import Subject
from models.database import Database
from ..views.student_view import StudentView
from colors.text_colors import *
import re
import random
from ..utils.utils import Utils
import os
from dotenv import load_dotenv
from ..utils.utils import ErrorMessageHandling

load_dotenv()
ENVIRONMENT = os.getenv('ENVIRONMENT')
STUDENT_EMAIL = os.getenv('STUDENT_EMAIL')
STUDENT_PASSWORD = os.getenv('STUDENT_PASSWORD')
STUDENT_EMAIL_REGISTER = os.getenv('STUDENT_EMAIL_REGISTER')
STUDENT_PASSWORD_REGISTER = os.getenv('STUDENT_PASSWORD_REGISTER')
STUDENT_NAME_REGISTER = os.getenv('STUDENT_NAME_REGISTER')


class StudentController:
    def __init__(self):
        self.view = StudentView()
        student_loaded = Database.read_objects_from_file()
        students_objects = [
            Student(student["name"],
                    student["email"],
                    student["password"],
                    student["ID"],
                    student["subjects"],
                    student["mark"],
                    student["grade"])
            for student in student_loaded
        ]
        self.student_list = students_objects

    def register_student(self):
        print(GREEN + "Student Sign Up" + RESET)
        while True:
            # Collect email and password
            if (ENVIRONMENT == 'dev' and STUDENT_EMAIL_REGISTER != None and STUDENT_PASSWORD_REGISTER != None):
                email = STUDENT_EMAIL_REGISTER
                password = STUDENT_PASSWORD_REGISTER
            else:
                email = input("Email: ")
                password = input("Password: ")

            # Validate email and password
            if not re.match(Utils.EMAIL_REGEX, email) or not re.match(Utils.PASSWORD_REGEX, password):
                print(RED + "Incorrect email or password format." + RESET)
            else:
                print(YELLOW + "Email and password formats acceptable." + RESET)
                # Check if email exists already
                student_name = self.check_student_exists_by_email(email)
                if student_name is not None:
                    print(f"{RED}Student {student_name} already exists{RESET}")
                else:
                    break

        # Collect name
        name = input("Name: ")

        # Create a new student object
        student = Student(name, email, password)

        # Save student to database
        if self.student_list is None:
            self.student_list = []

        self.student_list.append(student)
        print(YELLOW + "Enrolling Student " + name + RESET)
        students_dict = [student.to_dict() for student in self.student_list]
        Database.write_objects_to_file(students_dict)

    def login_student(self):
        print(GREEN + "Student Sign In" + RESET)
        while True:
            # Collect email and password
            if ENVIRONMENT == 'dev' and STUDENT_EMAIL is not None and STUDENT_PASSWORD is not None:
                email = STUDENT_EMAIL
                password = STUDENT_PASSWORD
            else:
                email = input("Email: ")
                password = input("Password: ")

            # Validate email and password
            if not re.match(Utils.EMAIL_REGEX, email) or not re.match(Utils.PASSWORD_REGEX, password):
                print(RED + "Incorrect email or password format." + RESET)
            else:
                print(YELLOW + "Email and password formats acceptable." + RESET)
                break

        for student in self.student_list:
            if student.email == email and student.password == password:
                # If found, display login success message
                self.student_course_menu(student)
                return student

        # If not found, display error message
        self.view.display_error(RED + "Student does not exist" + RESET)
        return None

    def check_student_exists_by_email(self, email):
        # Check if student exists in the database
        for student in self.student_list:
            if student.email == email:
                # If found, return the student's name
                return student.name
        # If not found, return None
        return None

    # After login . . .
    def student_course_menu(self, student):
        while True:
            print(
                CYAN + "\nPlease select the following actions for Student Course Menu: " + RESET)
            print("(C) Change: Change the password.")
            print(
                "(E) Enrol: Enrol in a subject. A student can enrol in a maximum of four (4) subjects.")
            print("(R) Remove: Remove a subject from the enrolment list.")
            print("(S) Show All Students: Shows the enrolled subjects with their marks and grades.")
            print("(X) Exit")

            option = input(CYAN + "Your choice: " + RESET).lower()

            if option == "c":
                student.change_password()
            elif option == "e":
                if len(student.subjects) >= 4:
                    print(RED + "You have already enrolled in the maximum of 4 subjects." + RESET)
                else:
                    subject = Subject(random.randint(100, 999))
                    student.enrol_subject(subject)
                    print(GREEN + "Enrolled in a new subject successfully." + RESET)
            elif option == "r":
                student.drop_subject()
            elif option == "s":
                student.show_enrolled_subjects()
            elif option == "x":
                break
            else:
                ErrorMessageHandling.printInvalidEntry()
