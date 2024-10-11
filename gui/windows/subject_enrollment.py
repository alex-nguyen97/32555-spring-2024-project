import tkinter as tk
from tkinter import ttk
from models.database import Database
from .error import ErrorWindow

class SubjectEnrollmentWindow:
    def __init__(self, parent, navigate, student):
        self.parent = parent
        self.navigate = navigate
        self.student = student
        self.parent.title("Subject Enrollment")

        # Create a frame for better organization
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Create a frame for subjects
        self.subjects_frame = ttk.Frame(self.frame, padding=20)
        self.subjects_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create subject list with delete buttons
        self.subject_list = []
        self.subject_labels = []
        for idx, subject in enumerate(self.student.subjects):
            subject_frame = ttk.Frame(self.subjects_frame, padding=(5, 2))
            subject_frame.grid(row=idx, column=0, sticky="ew")
            
            # Create and position a label for each subject
            subject_info = f" Subject ID: {subject.ID} - Mark: {subject.mark}"
            subject_label = ttk.Label(subject_frame, text=subject_info, anchor="w")
            subject_label.grid(row=0, column=0, sticky="w")

            # Create a delete button for each subject
            delete_button = ttk.Button(subject_frame, text="Delete", command=lambda s=subject: self.delete_subject(s))
            delete_button.grid(row=0, column=1, sticky="e")
            # Add new subject label and delete button to the list
            self.subject_labels.append((subject_label, delete_button))

        # Create a frame for buttons
        buttons_frame = ttk.Frame(self.frame)
        buttons_frame.pack(side=tk.RIGHT)

        # Enrollment button
        self.enroll_button = ttk.Button(buttons_frame, text="Enroll", command=self.enroll)
        self.enroll_button.pack(anchor=tk.E, padx=5, pady=10)

        # Logout button
        self.logout_button = ttk.Button(buttons_frame, text="Logout", command=self.logout)
        self.logout_button.pack(anchor=tk.E, padx=5, pady=5)

        # Change password button
        # self.change_password_button = ttk.Button(buttons_frame, text="Change Password", command=self.change_password)
        # self.change_password_button.pack(anchor=tk.E, padx=5, pady=5)
        
        # Initially hide the window
        self.hide()

    def delete_subject(self, subject):
        # Remove the subject from the list and update the UI
        if subject in self.student.subjects:
            self.student.subjects.remove(subject)
            Database.update_student(self.student)
            self.update_subject_list()

    def update_subject_list(self):
        # Get the initial height of the subjects frame
        initial_height = self.subjects_frame.winfo_reqheight()

        # Clear the current subject list and re-create it with updated data
        for subject_label, delete_button in self.subject_labels:
            subject_label.destroy()
            delete_button.destroy()
        self.subject_labels.clear()

        for idx, subject in enumerate(self.student.subjects):
            subject_frame = ttk.Frame(self.subjects_frame, padding=(5, 2))
            subject_frame.grid(row=idx, column=0, sticky="ew")
            subject_info = f"Subject ID: {subject.ID} - Mark: {subject.mark}"
            subject_label = ttk.Label(subject_frame, text=subject_info, anchor="w")
            subject_label.grid(row=0, column=0, sticky="w")
            delete_button = ttk.Button(subject_frame, text="Delete", command=lambda s=subject: self.delete_subject(s))
            delete_button.grid(row=0, column=1, sticky="e")
            self.subject_labels.append((subject_label, delete_button))

        # Adjust the height of the subjects frame to maintain the initial height
        self.subjects_frame.grid_propagate(False)
        self.subjects_frame.config(height=initial_height)



    def enroll(self):
        c = self.student.enrol_subject_ui()
        if c:
            self.update_subject_list()
        else:
            error_message = "Students are allowed to enroll in 4 subjects only"
            self.show_error(error_message)

    def logout(self):
        # Handle logout action
        self.clear_content()
        self.navigate("/login")

    def change_password(self):
        # Handle change password action
        pass

    def clear_content(self):
        # Clear the content of the window
        for widget in self.frame.winfo_children():
            widget.destroy()

    def show(self):
        # Show the window
        self.parent.deiconify()

    def hide(self):
        # Hide the window
        self.parent.withdraw()

    def show_error(self, message):
        # Show an error window with the provided message
        error_window = tk.Toplevel(self.parent)
        ErrorWindow(error_window, message)

def main():
    root = tk.Tk()
    app = SubjectEnrollmentWindow(root, lambda route: None)  # Placeholder lambda function for navigate
    root.mainloop()

if __name__ == "__main__":
    main()
