import customtkinter
import tkinter.messagebox

# Set the appearance mode and color theme for CustomTkinter
customtkinter.set_appearance_mode("Dark")  # Modes: "System", "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"


class LoginApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure the window
        self.title("Login Screen")
        self.geometry("1000x500")

        # Create a frame for the login form
        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.pack(pady=50, padx=50, fill="both", expand=True)

        # Add a label for the login title
        self.label = customtkinter.CTkLabel(master=self.frame, text="Please Login", font=("Arial", 20))
        self.label.pack(pady=20)

        # Add the username entry field
        self.username_label = customtkinter.CTkLabel(master=self.frame, text="Username")
        self.username_label.pack(pady=10)
        self.username_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter your username")
        self.username_entry.pack(pady=10)

        # Add the password entry field
        self.password_label = customtkinter.CTkLabel(master=self.frame, text="Password")
        self.password_label.pack(pady=10)
        self.password_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter your password", show="*")
        self.password_entry.pack(pady=10)

        # Add a login button
        self.login_button = customtkinter.CTkButton(master=self.frame, text="Login", command=self.check_login)
        self.login_button.pack(pady=20)

    def check_login(self):
        # Get username and password from entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if username and password match predefined values
        if username == "admin" and password == "password":
            tkinter.messagebox.showinfo("Login Success", "You have successfully logged in!")
        else:
            tkinter.messagebox.showerror("Login Failed", "Invalid username or password")


if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
