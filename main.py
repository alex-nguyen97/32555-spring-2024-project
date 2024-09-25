import customtkinter as ctk
from ui.login import LoginScreen
from ui.registration import RegistrationScreen
import utils.helpers as helpers


class Main():
    def __init__(self):
        self.start_program()

    def start_program(self):
        print('Here are the types of applications: ')
        print('1. CLIUniApp')
        print('2. GUIUniApp')
        while (True):
            option = int(input(
                'Please choose the type of application that you want to start (select 1 or 2, 3 is exit): '))
            if (option == 1):
                print('You have chosen the CLIUniApp!')
                return
            elif (option == 2):
                print('You have chosen the GUIUniApp!')
                self.create_container()

            elif (option == 3):
                print('Program is exiting...')
                return
            else:
                print('You have typed something wrong. Please type again!')

    def create_container(self):
        # creating a container
        ctk.set_appearance_mode("Dark")
        # Themes: "blue", "green", "dark-blue"
        ctk.set_default_color_theme("blue")
        root = ctk.CTk()
        root.geometry(helpers.SCREEN_SIZE)

        container = ctk.CTkFrame(master=root)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (LoginScreen, RegistrationScreen):
            frame = F(container, self)
            # initializing frame of that object from
            # login, register respectively with
            # for loop
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginScreen)
        root.mainloop()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    app = Main()
