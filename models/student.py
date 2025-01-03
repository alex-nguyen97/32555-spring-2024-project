import random
from models.database import Database
from colors.text_colors import *
from models.subject import Subject
from cli.utils.utils import Utils
import re
from tabulate import tabulate


class Student:
    def __init__(self, name, email, password, ID=None, subjects=None, mark=0.0, grade="P"):
        if ID is None:
            self.ID = self.generate_ID()
        else:
            self.ID = ID

        if subjects is None:
            self.subjects = []
        else:
            self.subjects = [
                Subject(subject["ID"], subject["mark"], subject["grade"])
                for subject in subjects
            ]

        self.name = name
        self.email = email
        self.password = password
        self.mark = mark
        self.grade = grade

    def generate_ID(self):
        return str(random.randint(1, 999999)).zfill(6)

    def enrol_subject(self):
        if len(self.subjects) < 4:
            subject = Subject(random.randint(100, 999))
            print(YELLOW + "Enrolling in Subject-" + str(subject.ID) + RESET)
            self.subjects.append(subject)
            print(YELLOW + "You are now enrolled in " +
                  str(len(self.subjects)) + " out of 4 subjects" + RESET)
            # Recalculate marks and grades . . .
            self.mark = sum(
                subject.mark for subject in self.subjects) / len(self.subjects)
            if self.mark >= 50:
                self.grade = "P"
            else:
                self.grade = "F"
            Database.update_student(self)
        else:
            print(RED + "Students are allowed to enroll in 4 subjects only" + RESET)

    def enrol_subject_ui(self):
        if len(self.subjects) < 4:
            subject = Subject(random.randint(100, 999))
            self.subjects.append(subject)
            # Recalculate marks and grades . . .
            self.mark = sum(
                subject.mark for subject in self.subjects) / len(self.subjects)
            if self.mark >= 50:
                self.grade = "P"
            else:
                self.grade = "F"
            Database.update_student(self)
            return True
        else:
            return False

    def drop_subject(self):
        subject_id_to_drop = input("Remove subject by ID: ")
        for subject in self.subjects:
            if str(subject.ID) == subject_id_to_drop:
                self.subjects.remove(subject)
                print(YELLOW + "Dropping Subject " +
                      subject_id_to_drop + RESET)
                print(YELLOW + "You are now enrolled in " +
                      str(len(self.subjects)) + " out of 4 subjects" + RESET)
                # Recalculate marks and grades . . .
                self.mark = sum(
                    subject.mark for subject in self.subjects) / len(self.subjects)
                if self.mark >= 50:
                    self.grade = "P"
                else:
                    self.grade = "F"
                Database.update_student(self)
                return
        print(RED + "Subject not found." + RESET)

    def drop_subject_ui(self, id):
        for subject in self.subjects:
            if str(subject.ID) == id:
                self.subjects.remove(subject)
                # Recalculate marks and grades . . .
                self.mark = sum(
                    subject.mark for subject in self.subjects) / len(self.subjects)
                if self.mark >= 50:
                    self.grade = "P"
                else:
                    self.grade = "F"
                Database.update_student(self)
                return

    def change_password(self):
        print(YELLOW + "Updating Password" + RESET)
        new_password = input("New Password: ")
        while (True):
            confirm_password = input("Confirm Password: ")
            if new_password == confirm_password:
                if re.match(Utils.PASSWORD_REGEX, confirm_password):
                    self.password = new_password
                    Database.update_student(self)
                    return
                else:
                    print(RED + "Incorrect password format" + RESET)
            else:

                print(RED + "Password does not match - try again" + RESET)

    def calculate_average_mark(self):
        if not self.subjects:
            return 0
        total_marks = sum(subject.mark for subject in self.subjects)
        return total_marks / len(self.subjects)

    def determine_pass_or_fail(self):
        return self.calculate_average_mark() >= 50

    def show_enrolled_subjects(self):
        subjects = self.subjects
        if not subjects:
            print(RED + "No subjects enrolled." + RESET)
        else:
            table_data = [[subject.ID, subject.mark, subject.grade]
                          for subject in subjects]
            headers = ["Subject ID", "Mark", "Grade"]
            print(tabulate(table_data, headers, tablefmt="fancy_grid"))

    def to_dict(self):
        subject_list = []
        if self.subjects is not None:
            for subject in self.subjects:
                subject_dict = {
                    "ID": subject.ID,
                    "mark": subject.mark,
                    "grade": subject.grade,
                }
                subject_list.append(subject_dict)

        return {
            "ID": self.ID,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "subjects": subject_list,
            "mark": self.mark,
            "grade": self.grade
        }

    @staticmethod
    def convert_to_student_class(student):
        return Student(
            student["name"],
            student["email"],
            student["password"],
            student.get("ID"),
            student.get("subjects", []),
            student.get("mark", 0.0),
            student.get("grade", "Z")
        )
