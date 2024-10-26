import customtkinter as ctk
from models.database import Database
from .error import ErrorWindow


class SubjectEnrollmentWindow:
    def __init__(self, parent, navigate, student):
        self.parent = parent
        self.navigate = navigate
        self.student = student
        self.parent.title("Subject Enrollment")

        # Main frame setup
        self.frame = ctk.CTkFrame(parent, corner_radius=10)
        self.frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        # Frame for subjects
        self.subjects_frame = ctk.CTkFrame(self.frame)
        self.subjects_frame.pack(
            side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=20, pady=10)

        # Subject list with delete buttons
        self.subject_labels = []
        for idx, subject in enumerate(self.student.subjects):
            self.create_subject_frame(idx, subject)

        # Frame for action buttons
        buttons_frame = ctk.CTkFrame(self.frame)
        buttons_frame.pack(side=ctk.RIGHT, padx=10, pady=10)

        # Enrollment button
        self.enroll_button = ctk.CTkButton(
            buttons_frame, text="Enroll", command=self.enroll)
        self.enroll_button.pack(anchor=ctk.E, padx=5, pady=10)

        # Logout button
        self.logout_button = ctk.CTkButton(
            buttons_frame, text="Logout", command=self.logout)
        self.logout_button.pack(anchor=ctk.E, padx=5, pady=5)

        # Hide window initially
        self.hide()

    def create_subject_frame(self, idx, subject):
        subject_frame = ctk.CTkFrame(
            self.subjects_frame, corner_radius=5, fg_color="#ffffff")
        subject_frame.grid(row=idx, column=0, sticky="ew", padx=5, pady=5)
        subject_frame.grid_columnconfigure(0, weight=1)
        # Label for each subject
        subject_info = f"Subject ID: {subject.ID} - Mark: {subject.mark}"
        subject_label = ctk.CTkLabel(
            subject_frame, text=subject_info, anchor="w")
        subject_label.grid(row=0, column=0, sticky="w", padx=10)

        # Delete button for each subject
        delete_button = ctk.CTkButton(
            subject_frame, text="Delete", width=50, command=lambda s=subject: self.delete_subject(s))
        delete_button.grid(row=0, column=1, sticky="e")
        self.subject_labels.append((subject_label, delete_button))

    def delete_subject(self, subject):
        # Remove subject from list and update UI
        if subject in self.student.subjects:
            self.student.subjects.remove(subject)
            Database.update_student(self.student)
            self.update_subject_list()

    def update_subject_list(self):
        # Clear current list and recreate it with updated data
        for widget in self.subjects_frame.winfo_children():
            widget.destroy()

        self.subject_labels.clear()

        for idx, subject in enumerate(self.student.subjects):
            self.create_subject_frame(idx, subject)

    def enroll(self):
        # Handle subject enrollment
        if self.student.enrol_subject_ui():
            self.update_subject_list()
        else:
            self.show_error(
                "Students are allowed to enroll in 4 subjects only")

    def logout(self):
        # Handle logout action
        self.clear_content()
        self.navigate("/login")

    def clear_content(self):
        # Clear window content
        for widget in self.frame.winfo_children():
            widget.destroy()

    def show(self):
        # Show the window
        self.parent.deiconify()

    def hide(self):
        # Hide the window
        self.parent.withdraw()

    def show_error(self, message):
        # Display error window with message
        error_window = ctk.CTkToplevel(self.parent)
        ErrorWindow(error_window, message)


def main():
    root = ctk.CTk()
    # Placeholder for navigate and student
    app = SubjectEnrollmentWindow(root, lambda route: None, student=None)
    root.mainloop()


if __name__ == "__main__":
    main()
