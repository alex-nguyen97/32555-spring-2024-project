import random
from models.student import Student
from models.subject import Subject
from services.file_manager import FileManager
from services.validation import validate_email, validate_password


class StudentService:
    def __init__(self):
        self.file_manager = FileManager("data/students.data")
        self.students = self.file_manager.load_students()

    def register_student(self, name, email, password):
        if not validate_email(email):
            return "Invalid email format. Must end with '@university.com'."

        if not validate_password(password):
            return "Password does not meet criteria. Must start with an uppercase letter, contain at least 5 letters, and have 3 or more digits."

        # Generate unique student ID (6 digits)
        student_id = str(random.randint(1, 999999)).zfill(6)

        # Check if email is already registered
        if any(student.email == email for student in self.students):
            return "Email is already registered."

        # Create new student
        new_student = Student(student_id, name, email, password)

        # Add to student list and save
        self.students.append(new_student)
        self.file_manager.save_students(self.students)
        return f"Student registered successfully with ID: {student_id}"

    def login_student(self, email, password):
        for student in self.students:
            if student.email == email and student.password == password:
                return student
        return None  # Invalid login credentials

    def enrol_subject(self, student):
        if len(student.enrolled_subjects) >= 4:
            return "You are already enrolled in 4 subjects."

        # Generate unique subject ID and random mark
        subject_id = str(random.randint(1, 999)).zfill(3)
        mark = random.randint(25, 100)

        # Create subject and assign grade
        new_subject = Subject(subject_id, mark)
        student.enrolled_subjects.append(new_subject)

        # Save updated student information
        self.file_manager.save_students(self.students)
        return f"Enrolled in new subject with ID: {subject_id}, Mark: {mark}, Grade: {new_subject.grade}"

    def remove_subject(self, student, subject_id):
        subject_to_remove = None
        for subject in student.enrolled_subjects:
            if subject.subject_id == subject_id:
                subject_to_remove = subject
                break

        if subject_to_remove:
            student.enrolled_subjects.remove(subject_to_remove)
            self.file_manager.save_students(self.students)
            return f"Subject {subject_id} removed successfully."
        else:
            return f"Subject {subject_id} not found in your enrolment list."

    def view_enrolled_subjects(self, student):
        if not student.enrolled_subjects:
            return "You are not enrolled in any subjects."

        subject_list = []
        for subject in student.enrolled_subjects:
            subject_list.append(f"Subject ID: {subject.subject_id}, Mark: {
                                subject.mark}, Grade: {subject.grade}")

        return "\n".join(subject_list)

    def change_password(self, student, new_password):
        if not validate_password(new_password):
            return "Password does not meet criteria. Must start with an uppercase letter, contain at least 5 letters, and have 3 or more digits."

        student.password = new_password
        self.file_manager.save_students(self.students)
        return "Password changed successfully."

    def get_student_by_email(self, email):
        for student in self.students:
            if student.email == email:
                return student
        return None
