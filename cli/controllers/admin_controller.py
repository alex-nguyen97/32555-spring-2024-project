from models.database import Database
from ..views.admin_view import AdminView
from colors.text_colors import *
from models.student import Student
from tabulate import tabulate

class AdminController:
    def __init__(self):
        self.view = AdminView()
        student_loaded = Database.read_objects_from_file()
        students_objects = [
            Student.convert_to_student_class(student)
            for student in student_loaded
        ]
        self.student_list = students_objects

    def print_student_details(self, students):
        table_data = [[student.name, student.ID, student.email,
                       student.mark] for student in students]
        headers = ["Name", "ID", "Email", "Mark"]
        print(tabulate(table_data, headers, tablefmt="fancy_grid"))

    def show_students_list(self):
        print(YELLOW + "Student List" + RESET)
        students = self.student_list
        if not students:
            print("< Nothing to Display >")
            return
        else:
            self.print_student_details(students)

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
            print(f"\n{CYAN}Grade: {grade}{RESET}")
            self.print_student_details(students)

    def partition_students_by_pass_fail(self):
        students = self.student_list
        pass_students = []
        fail_students = []

        for student in students:
            if student.calculate_average_mark() >= 50:
                pass_students.append(student)
            else:
                fail_students.append(student)

        pass_table = [[student.name, student.ID, student.email,
                       student.mark] for student in pass_students]
        fail_table = [[student.name, student.ID, student.email,
                       student.mark] for student in fail_students]
        headers = ["Name", "ID", "Email", "Mark"]

        print(f"\n{GREEN}[PASS] Students{RESET}")
        if pass_table:
            print(tabulate(pass_table, headers, tablefmt="fancy_grid"))
        else:
            print("< No Pass Students >")

        print(f"\n{RED}[FAIL] Students{RESET}")
        if fail_table:
            print(tabulate(fail_table, headers, tablefmt="fancy_grid"))
        else:
            print("< No Fail Students >")

    def remove_student_by_id(self):
        student_id_to_remove = input("Enter Student ID to Remove: ")
        students = self.student_list
        student_found = False
        for student in students:
            if student.ID == student_id_to_remove:
                # Confirm deletion
                confirmation = input(f"Are you sure you want to remove student {student.name} (ID: {student.ID})? (Y)ES/(N)O: ").lower()
                if confirmation == 'y':
                    students.remove(student)
                    Database.write_objects_to_file(
                        [student.to_dict() for student in students])
                    print(
                        GREEN + f"Student {student_id_to_remove} removed successfully." + RESET)
                else:
                    print(YELLOW + "Student removal canceled." + RESET)
                student_found = True
                break

        if not student_found:
            print(
                RED + f"Student with ID {student_id_to_remove} does not exist." + RESET)

    def clear_database(self):
        confirmation = input(
            RED + "Are you sure you want to clear the database? (Y)ES/(N)O: ").lower()
        if confirmation == "y":
            Database.clear_file_data()
            print(YELLOW + "Students data cleared." + RESET)
        else:
            print(YELLOW + "Database clearing canceled." + RESET)
