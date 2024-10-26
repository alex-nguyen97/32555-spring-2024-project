import customtkinter as ctk
from datetime import datetime
from .error import ErrorWindow
from models.database import Database
import re
from cli.utils.utils import Utils
import os
from dotenv import load_dotenv
from models.student import Student

load_dotenv()
ENVIRONMENT = os.getenv('ENVIRONMENT')
STUDENT_EMAIL = os.getenv('STUDENT_EMAIL')
STUDENT_PASSWORD = os.getenv('STUDENT_PASSWORD')


class LoginWindow:
    def __init__(self, parent, navigate):
        self.parent = parent
        self.navigate = navigate
        self.parent.title("GUI Uni App")
        self.parent.geometry("600x400+500+200")

        self.setup_ui()

    def setup_ui(self):
        self.clear_content()

        # Title Label
        self.app_name_label = ctk.CTkLabel(
            self.parent, text="Student Enrolment GUI", font=ctk.CTkFont(size=16, weight="bold")
        )
        self.app_name_label.pack(pady=10)

        # Frame for entries
        self.frame = ctk.CTkFrame(self.parent)
        self.frame.pack(pady=10)

        # Email Label and Entry
        self.email_label = ctk.CTkLabel(self.frame, text="Email:")
        self.email_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.email_entry = ctk.CTkEntry(self.frame)
        self.email_entry.grid(row=0, column=1, padx=5, pady=5)

        # Password Label and Entry
        self.password_label = ctk.CTkLabel(self.frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.password_entry = ctk.CTkEntry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Login Button
        self.login_button = ctk.CTkButton(
            self.parent, text="Login", command=self.login)
        self.login_button.pack(pady=5)

        # Exit Button
        self.exit_button = ctk.CTkButton(
            self.parent, text="Exit", command=self.exit)
        self.exit_button.pack(pady=5)

    def show(self):
        # Show the window
        self.parent.deiconify()

    def login(self):
        if ENVIRONMENT == 'dev' and STUDENT_EMAIL is not None and STUDENT_PASSWORD is not None:
            email = STUDENT_EMAIL
            password = STUDENT_PASSWORD
        else:
            email = self.email_entry.get()
            password = self.password_entry.get()

        isMatchEmailFormat = re.match(Utils.EMAIL_REGEX, email)
        isMatchPasswordFormat = re.match(Utils.PASSWORD_REGEX, password)

        error_message = None
        if not isMatchEmailFormat and not isMatchEmailFormat:
            error_message = "Incorrect email and password format"
        elif not isMatchEmailFormat:
            error_message = "Incorrect email format"
        elif not isMatchPasswordFormat:
            error_message = "Incorrect password format"

        if error_message:
            self.show_error(error_message)
            return

        students = Database.read_objects_from_file()
        students_objects = [
            Student.convert_to_student_class(student)
            for student in students
        ]

        for student in students_objects:
            if student.email == email and student.password == password:
                self.clear_content()
                self.navigate('/subject-enrollment', student=student)
                return

        error_message = "Incorrect email or password"
        self.show_error(error_message)

    def exit(self):
        """Closes the application."""
        self.parent.destroy()

    def clear_content(self):
        """Clears the content of the current window."""
        for widget in self.parent.winfo_children():
            widget.destroy()

    def show_error(self, message):
        """Displays an error window."""
        error_window = ctk.CTkToplevel(self.parent)
        ErrorWindow(error_window, message)


def main():
    root = ctk.CTk()
    LoginWindow(root, navigate=None)
    root.mainloop()


if __name__ == "__main__":
    main()
