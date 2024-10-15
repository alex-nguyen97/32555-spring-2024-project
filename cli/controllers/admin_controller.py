from models.database import Database
from ..views.admin_view import AdminView
from colors.text_colors import *

class AdminController:
    def __init__(self):
        self.view = AdminView()

    def show_students_list(self):
        print(YELLOW + "Student List" + RESET)
        students = Database.read_objects_from_file()
        if not students:
            print("     < Nothing to Display >")
            return
        for student in students:
            print(f"{student.name} :: {student.ID} --> Email: {student.email}")
        return

    def group_students_by_grade(self):
        print(YELLOW + "Grade Grouping" + RESET)
        students = Database.read_objects_from_file()
        grade_groups = {}

        for student in students:
            grade = student.grade
            
            if grade not in grade_groups:
                grade_groups[grade] = []

            grade_groups[grade].append(student)

        for grade, students in grade_groups.items():
            for student in students:
                print(f"{grade} --> [{student.name} :: {student.ID} --> Grade: {student.grade} - Mark: {student.mark}]")

    def partition_students_by_pass_fail(self):
        students = Database.read_objects_from_file()
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
            formatted_students.append(f"{student.name} :: ID --> {student.ID} - GRADE: {student.grade} - MARK: {student.mark:.2f}")
        return f"[{status}] --> {formatted_students}"

    def remove_student_by_id(self):
        student_id_to_remove = input("Remove by ID: ")
        students = Database.read_objects_from_file()
        for student in students:
            if student.ID == student_id_to_remove:
                students.remove(student)
                print(f"{YELLOW}Removing Student {student_id_to_remove} account.{RESET}")
                Database.write_objects_to_file(students)
                return
        print(f"{RED}Student {student_id_to_remove} does not exist{RESET}")

    def clear_database(self):
        student_id_clear = input(RED + "Are you sure you want to clear the database (Y)ES/(N)O: ")
        if student_id_clear == "Y":
            Database.clear_file_data()
            self.view.display_message(YELLOW + "Students data cleared")
        else :
            return