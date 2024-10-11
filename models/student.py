class Student:
    def __init__(self, student_id, name, email, password):
        # 6-digit unique ID (made private with _)
        self._student_id = student_id
        self._name = name               # Student's full name
        self._email = email             # Student's email
        self._password = password       # Student's password
