import customtkinter as ctk


class ErrorWindow:
    def __init__(self, parent, message):
        self.parent = parent
        self.parent.title("Error")

        self.frame = ctk.CTkFrame(
            parent, corner_radius=10, fg_color=parent.cget("bg"))
        self.frame.pack(padx=20, pady=10)

        # Error message label
        self.message_label = ctk.CTkLabel(
            self.frame, text=message, text_color="red", font=("Arial", 12))
        self.message_label.pack(pady=10)

        # OK button
        self.ok_button = ctk.CTkButton(
            self.frame, text="OK", command=self.close_window)
        self.ok_button.pack(pady=5)

        # Center the window
        self.parent.after(self.center_window)

    def close_window(self):
        self.parent.destroy()

    def center_window(self):
        # Get the window's width and height
        window_width = self.frame.winfo_reqwidth()
        window_height = self.frame.winfo_reqheight()

        # Get the parent's width and height
        parent_width = self.parent.winfo_width()
        parent_height = self.parent.winfo_height()

        # Calculate the position to center the window
        position_top = int(parent_height / 2 - window_height / 2)
        position_right = int(parent_width / 2 - window_width / 2)

        # Set the new position
        self.parent.geometry("+{}+{}".format(position_right, position_top))


def main():
    root = ctk.CTk()  # Use CustomTkinter for the root window
    ErrorWindow(root, "Incorrect email or password")
    root.mainloop()


if __name__ == "__main__":
    main()
