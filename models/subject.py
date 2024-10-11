import random

class Subject:
    def __init__(self, ID):
        self.ID = ID
        self.mark = self.generate_mark()
        self.grade = self.determine_grade()

    def generate_mark(self):
        return random.randint(25, 100)

    def determine_grade(self):
        if self.mark >= 85:
            return "HD"
        elif self.mark >= 75:
            return "D"
        elif self.mark >= 65:
            return "C"
        elif self.mark >= 50:
            return "P"
        else:
            return "Z"
