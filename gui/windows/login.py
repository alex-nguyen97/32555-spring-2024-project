import tkinter as tk
from tkinter import ttk
import logging
from datetime import datetime
from .error import ErrorWindow
from models.database import Database
import re
from cli.utils.utils import Utils

class LoginWindow:
    def __init__(self, parent, navigate):
        self.parent = parent
        self.navigate = navigate
        self.parent.title("GUI Uni App")
        self.parent.geometry("600x400-500-200")  # Set window size
        #self.parent.configure(bg='#607b8d') # Set background color
        self.clear_content()
        # Add a label for the app name
        self.app_name_label = ttk.Label(parent, text="Student Enrolment GUI", font=("Arial", 16, "bold"))
        self.app_name_label.pack(pady=10)

        # Create a frame for better organization
        self.frame = ttk.Frame(parent)
        self.frame.pack(pady=10)

        # Email label and entry
        self.email_label = ttk.Label(self.frame, text="Email:")
        self.email_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.email_entry = ttk.Entry(self.frame)
        self.email_entry.grid(row=0, column=1, padx=5, pady=5)

        # Password label and entry
        self.password_label = ttk.Label(self.frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.password_entry = ttk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Login and Exit buttons
        self.login_button = ttk.Button(parent, text="Login", command=self.login)
        self.login_button.pack(pady=5)

        self.exit_button = ttk.Button(parent, text="Exit", command=self.exit)
        self.exit_button.pack(pady=5)

    def login(self): # Validation for the login process
        # Set up logging
        logging.basicConfig(filename='log.txt', level=logging.INFO, 
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        # Log the login attempt
        logging.info('Login attempt made with email: %s', self.email_entry.get())

        # if not re.match(Utils.EMAIL_REGEX, self.email_entry.get()) or not re.match(Utils.PASSWORD_REGEX, self.password_entry.get()):
        #     error_message = "Incorrect email or password format"
        #     self.show_error(error_message)
        #     logging.info('Login attempt unsuccessful: %s', error_message)
        #     return      # After displaying error message

        students = Database.read_objects_from_file() # Read students from database file
        for student in students:
            if student.email == self.email_entry.get() and student.password == self.password_entry.get():
                self.clear_content()
                self.navigate('/subject-enrollment', student=student)
                logging.info('Login attempt successful') # Log successful login attempt
                return

        error_message = "Incorrect email or password"
        self.show_error(error_message)
        logging.info('Login attempt unsuccessful: %s', error_message) # Log unsuccessful login attempt

    def exit(self):
        # Close the window
        self.parent.destroy()

    # Create Basewindow class for show, hide and clear_content methods?
    def show(self):
        # Show the subject menu window
        self.parent.deiconify()

    def hide(self):
        # Hide the login window
        self.parent.withdraw()

    def clear_content(self):
        # Clear the content of the login window
        for widget in self.parent.winfo_children():
            widget.destroy()

    def show_error(self, message):
        # Show an error window with the relevant message
        error_window = tk.Toplevel(self.parent)
        ErrorWindow(error_window, message)

def main():
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
