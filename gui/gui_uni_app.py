import tkinter as tk
from tkinter import ttk
from .windows.login import LoginWindow
from .windows.subject_enrollment import SubjectEnrollmentWindow

class GUIUniApp:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        #self.root.title("Student Application GUI")
        
        # Hide subject menu window initially
        # self.subject_menu_window = None
        
    def run(self):
        # C/D login window
        self.login_window = LoginWindow(self.root, self.navigate)
        # Run the main event loop
        self.root.mainloop()

    def navigate(self, route, **kwargs):
        routes = {
            '/login': self.goto_login,
            '/subject-enrollment': self.goto_subject_enrollment,
        }
        
        function_to_execute = routes.get(route)
        
        if function_to_execute:
            function_to_execute(**kwargs)
        else:
            print("Route not found")

    # Call the show method to display windows
    def goto_login(self):
        LoginWindow(self.root, self.navigate).show()

    def goto_subject_enrollment(self, **kwargs):
        SubjectEnrollmentWindow(self.root, self.navigate, kwargs['student']).show()

def main():
    gui_app = GUIUniApp()
    gui_app.run()

if __name__ == "__main__":
    main()
