import customtkinter as ctk
import tkinter.messagebox
import utils.helpers as helpers


class LoginScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        # self.root = root
        # self.root.title("Login Screen")
        super().__init__(parent)
        self.build_ui()

    def build_ui(self):
        # Configure the window

        # # Create a frame for the login form
        # self.frame = ctk.CTkFrame(master=self.root)
        # self.frame.pack(pady=50, padx=50, fill="both", expand=True)

        # Add a label for the login title
        self.label = ctk.CTkLabel(
            self, text="Please Login", font=helpers.HEADING)
        self.label.pack(pady=20)

        # Add the username entry field
        self.username_label = ctk.CTkLabel(self, text="Username")
        self.username_label.pack(pady=10)
        self.username_entry = ctk.CTkEntry(
            self, placeholder_text="Enter your username")
        self.username_entry.pack(pady=10)

        # Add the password entry field
        self.password_label = ctk.CTkLabel(self, text="Password")
        self.password_label.pack(pady=10)
        self.password_entry = ctk.CTkEntry(
            self, placeholder_text="Enter your password", show="*")
        self.password_entry.pack(pady=10)

        # Add a login button
        self.login_button = ctk.CTkButton(
            master=self, text="Login", command=self.check_login)
        self.login_button.pack(pady=20)

        # Add a register button
        self.login_button = ctk.CTkButton(
            self, text="Don't have account? Please register!", command=self.navigate_register)
        self.login_button.pack(pady=20)

    def check_login(self):
        # Get username and password from entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if username and password match predefined values
        if username == "admin" and password == "password":
            tkinter.messagebox.showinfo(
                "Login Success", "You have successfully logged in!")
        else:
            tkinter.messagebox.showerror(
                "Login Failed", "Invalid username or password")

    def navigate_register(self):
        print("go to register page")
