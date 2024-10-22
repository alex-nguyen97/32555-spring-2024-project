import json
from cli.utils.utils import ErrorMessageHandling
from cli.utils.utils import SuccessMessageHandling


class Database:
    FILE_NAME = "students.json"

    def __init__(self):
        self.create_file_if_not_exists()

    def check_file_exist(self):
        try:
            with open(self.FILE_NAME, "rb"):
                pass
            return True
        except FileNotFoundError:
            ErrorMessageHandling.printFileNotFound()
            return False

    def create_file_if_not_exists(self):
        if not self.check_file_exist():
            with open(self.FILE_NAME, "w") as file:
                json.dump([], file)

    @staticmethod
    def write_objects_to_file(objects):
        with open(Database.FILE_NAME, "w") as file:
            json.dump(objects, file, indent=4)

    @staticmethod
    def read_objects_from_file():
        try:
            with open(Database.FILE_NAME, "r") as file:
                objects = json.load(file)
            return objects
        except (EOFError, FileNotFoundError):
            return []

    @staticmethod
    def clear_file_data():
        open(Database.FILE_NAME, "w").close()

    @staticmethod
    def update_student(student):
        students = Database.read_objects_from_file()
        for i, s in enumerate(students):
            if s.email == student.email:
                students[i] = student
                Database.write_objects_to_file(students)
                SuccessMessageHandling.printUpdateStudentSuccessful()
                return True
        ErrorMessageHandling.printUpdateStudentFailed()
        return False
