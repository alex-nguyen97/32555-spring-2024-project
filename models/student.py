import random 
from models.database import Database
from colors.text_colors import *
from models.subject import Subject
from cli.utils.utils import Utils
import re


class Student:
    def __init__(self, name, email, password):
        self.ID = self.generate_ID()
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []
        self.mark = 0.0
        self.grade = "P"

    def generate_ID(self):
        return str(random.randint(1, 999999)).zfill(6)

    def enrol_subject(self, subject):
        if len(self.subjects) < 4:
            print(YELLOW + "Enrolling in Subject-" + str(subject.ID) + RESET)
            self.subjects.append(subject)
            print(YELLOW + "You are now enrolled in " + str(len(self.subjects)) + " out of 4 subjects" + RESET)
            # Recalculate marks and grades . . .
            self.mark = sum(subject.mark for subject in self.subjects) / len(self.subjects)
            if self.mark >= 50:
                self.grade = "P"
            else:
                self.grade = "F"
            Database.update_student(self)
        else:
            print(RED + "Students are allowed to enroll in 4 subjects only" + RESET)

    def enrol_subject_ui(self):
        subject = Subject(random.randint(100, 999))
        if len(self.subjects) < 4:
            self.subjects.append(subject)
            # Recalculate marks and grades . . .
            self.mark = sum(subject.mark for subject in self.subjects) / len(self.subjects)
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
                print(YELLOW + "Dropping Subject " + subject_id_to_drop + RESET)
                print(YELLOW + "You are now enrolled in " + str(len(self.subjects)) + " out of 4 subjects" + RESET)
                # Recalculate marks and grades . . .
                self.mark = sum(subject.mark for subject in self.subjects) / len(self.subjects)
                if self.mark >= 50:
                    self.grade = "P"
                else:
                    self.grade = "F"
                Database.update_student(self)
                return
        print("Subject not found.")

    def drop_subject_ui(self, id):
        for subject in self.subjects:
            if str(subject.ID) == id:
                self.subjects.remove(subject)
                # Recalculate marks and grades . . .
                self.mark = sum(subject.mark for subject in self.subjects) / len(self.subjects)
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
        if self.subjects:
            print("Enrolled Subjects:")
            for subject in self.subjects:
                print(f"[ Subject:: {subject.ID} -- mark = {subject.mark} -- grade = {subject.grade} ]")
        else:
            print(YELLOW + "Showing 0 subjects.")

    # def get_enrolled_subjects(self):
    #     enrolled_subjects = []
    #     if self.subjects:
    #         for subject in self.subjects:
    #             enrolled_subjects.append(subject)
    #     return enrolled_subjects
