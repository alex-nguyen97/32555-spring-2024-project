import pickle

class Database:
    FILE_NAME = "students.data"

    @staticmethod
    def check_file_existence():
        try:
            with open(Database.FILE_NAME, "rb"):
                pass
            return True
        except FileNotFoundError:
            return False

    @staticmethod
    def create_file_if_not_exists():
        if not Database.check_file_existence():
            open(Database.FILE_NAME, "wb").close()

    @staticmethod
    def write_objects_to_file(objects):
        with open(Database.FILE_NAME, "wb") as file:
            pickle.dump(objects, file)
        # print("Objects written to file.")

    @staticmethod
    def read_objects_from_file():
        try:
            with open(Database.FILE_NAME, "rb") as file:
                objects = pickle.load(file)
            # print("Objects read from file.")
            return objects
        except (EOFError, FileNotFoundError):
            return []

    @staticmethod
    def clear_file_data():
        open(Database.FILE_NAME, "w").close()
        #print("File data cleared.")

    @staticmethod
    def update_student(student):
        students = Database.read_objects_from_file()
        for i, s in enumerate(students):
            if s.email == student.email:
                students[i] = student
                Database.write_objects_to_file(students)
                return True
        return False
