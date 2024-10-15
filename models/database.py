import pickle
from cli.utils.utils import ErrorMessageHandling
from cli.utils.utils import SuccessMessageHandling
class Database:
    FILE_NAME = "students.data"

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
            open(self.FILE_NAME, "wb").close()

    @staticmethod
    def write_objects_to_file(objects):
        with open(Database.FILE_NAME, "wb") as file:
            pickle.dump(objects, file)

    @staticmethod
    def read_objects_from_file():
        try:
            with open(Database.FILE_NAME, "rb") as file:
                objects = pickle.load(file)
                print(objects)
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
