from models.student import Student
from models.subject import Subject
from models.database import Database
from ..views.student_view import StudentView
from colors.text_colors import *
import re
import random
from ..utils.utils import Utils


class StudentController:
    def __init__(self):
        self.view = StudentView()
        student_loaded= Database.read_objects_from_file()
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
            email = input("Email: ")
            password = input("Password: ")

            # Validate email and password
            # if not re.match(Utils.EMAIL_REGEX, email) or not re.match(Utils.PASSWORD_REGEX, password):
            if(False):
                print(RED + "Incorrect email or password format." + RESET)
            else:
                print(YELLOW + "Email and password formats acceptable." + RESET)
                # Check if email exists already . . .
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
        # Ensure that students is not None
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
            email = input("Email: ")
            password = input("Password: ")

            # Validate email and password
            # if not re.match(Utils.EMAIL_REGEX, email) or not re.match(Utils.PASSWORD_REGEX, password):
            if(False):
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
            choice = input(CYAN + "Student Course Menu (c/e/r/s/x): " + RESET)
            if choice == "c":
                student.change_password()
            elif choice == "e":
                subject = Subject(random.randint(100, 999))
                #print(YELLOW + "Enrolling in Subject-" + str(subject.ID) + RESET)
                student.enrol_subject(subject)
            elif choice == "r":
                student.drop_subject()
            elif choice == "s":
                student.show_enrolled_subjects()
            elif choice == "x":
                break
            else:
                print("Invalid choice. Please try again.")