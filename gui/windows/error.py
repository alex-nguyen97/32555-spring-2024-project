import tkinter as tk
from tkinter import ttk

class ErrorWindow:
    def __init__(self, parent, message):
        self.parent = parent
        self.parent.title("Error")
        
        # Configure the style
        self.style = ttk.Style()
        self.style.configure("Error.TLabel", foreground="red", font=("Arial", 12))
        self.style.configure("Error.TButton", background="#ffcccc", foreground="red", font=("Arial", 10, "bold"))
        
        # Frame for better organization
        self.frame = ttk.Frame(parent, style="Error.TFrame")
        self.frame.pack(padx=20, pady=10)
        
        # Error message label
        self.message_label = ttk.Label(self.frame, text=message, style="Error.TLabel")
        self.message_label.pack(pady=10)
        
        # OK button
        self.ok_button = ttk.Button(self.frame, text="OK", command=self.close_window, style="Error.TButton")
        self.ok_button.pack(pady=5)

    def close_window(self):
        self.parent.destroy()

    # Place the error window in the center of the parent window
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
    root = tk.Tk()
    app = ErrorWindow(root, "Incorrect email or password")
    app.center_window()  # Call the center_window method
    root.mainloop()

if __name__ == "__main__":
    main()
