from models.database import Database
from colors.text_colors import *
from models.student import Student


class AdminController:
    def __init__(self):
        student_loaded = Database.read_objects_from_file()
        students_objects = [
            Student.convert_to_student_class(student)
            for student in student_loaded
        ]
        self.student_list = students_objects

    def show_students_list(self):
        print(YELLOW + "Student List" + RESET)
        students = self.student_list
        if not students:
            print("     < Nothing to Display >")
            return
        for student in students:
            print(f"{student.name} :: {student.ID} --> Email: {student.email}")
        return

    def group_students_by_grade(self):
        print(YELLOW + "Grade Grouping" + RESET)
        students = self.student_list
        grade_groups = {}

        for student in students:
            grade = student.grade

            if grade not in grade_groups:
                grade_groups[grade] = []

            grade_groups[grade].append(student)

        for grade, students in grade_groups.items():
            for student in students:
                student_detail = self.print_student_details(student)
                print(f"{grade} --> {student_detail}")

    def partition_students_by_pass_fail(self):
        students = self.student_list
        pass_students = []
        fail_students = []

        for student in students:
            if student.calculate_average_mark() >= 50:
                pass_students.append(student)
            else:
                fail_students.append(student)

        fail_str = self.format_students("FAIL", fail_students)
        pass_str = self.format_students("PASS", pass_students)

        print(pass_str)
        print(fail_str)

    def format_students(self, status, students):
        formatted_students = []
        for student in students:
            student_detail = self.print_student_details(student)
            formatted_students.append(student_detail)
        return f"[{status}] --> {formatted_students}"

    def print_student_details(self, student):
        return (f"{student.name} :: ID --> {student.ID} - GRADE: {student.grade} - MARK: {student.mark:.2f}")

    def remove_student_by_id(self):
        student_id_to_remove = input("Remove by ID: ")
        students = self.student_list
        for student in students:
            if student.ID == student_id_to_remove:
                students.remove(student)
                Database.write_objects_to_file(students)
                return
        print(f"{RED}Student {student_id_to_remove} does not exist{RESET}")

    def clear_database(self):
        student_id_clear = input(
            RED + "Are you sure you want to clear the database (Y)ES/(N)O: ")
        if student_id_clear == "Y":
            Database.clear_file_data()
            print(YELLOW + "Students data cleared")
        else:
            return
