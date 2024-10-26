import customtkinter as ctk
from .windows.login import LoginWindow
from .windows.subject_enrollment import SubjectEnrollmentWindow


class GUIUniApp:
    def __init__(self):
        # Initialize the main window with customtkinter
        self.root = ctk.CTk()
        self.root.title("Student Application GUI")

        # Customize the appearance (optional)
        # Modes: "System" (default), "Dark", "Light"
        ctk.set_appearance_mode("System")
        # Themes: "blue" (default), "green", "dark-blue"
        ctk.set_default_color_theme("blue")

    def run(self):
        # Create the login window and display it
        self.login_window = LoginWindow(self.root, self.navigate)
        # Run the main event loop
        self.root.mainloop()

    def navigate(self, route, **kwargs):
        """Navigates between different application routes."""
        routes = {
            '/login': self.goto_login,
            '/subject-enrollment': self.goto_subject_enrollment,
        }

        function_to_execute = routes.get(route)

        if function_to_execute:
            function_to_execute(**kwargs)
        else:
            print("Route not found")

    def goto_login(self):
        """Navigates to the login window."""
        self.clear_content()
        LoginWindow(self.root, self.navigate).show()

    def goto_subject_enrollment(self, **kwargs):
        """Navigates to the subject enrollment window."""
        self.clear_content()
        SubjectEnrollmentWindow(self.root, self.navigate,
                                kwargs['student']).show()

    def clear_content(self):
        """Clears the main window's content before loading a new view."""
        for widget in self.root.winfo_children():
            widget.destroy()


def main():
    gui_app = GUIUniApp()
    gui_app.run()


if __name__ == "__main__":
    main()
