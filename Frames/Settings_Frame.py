import customtkinter as ctk
'''
This frame creates a settings environment that allows the user 
to change the settings of the dashboard
'''

class SettingsFrame(ctk.CTkFrame):

    selectedTransactions = []

    def __init__(self, app, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app  # Store the app instance4

        self.grid_columnconfigure(0, weight=1)  # Ensure widgets fill the width
        self.grid_rowconfigure(0, weight=1)  # Weight for the top row
        self.grid_rowconfigure(1, weight=1)  # Weight for the middle row
        self.grid_rowconfigure(2, weight=1)  # Weight for the bottom row

        self.label = ctk.CTkLabel(self, text="Settings",font=("Arial", 24))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        # Create a BooleanVar to track the state of the checkbox
        self.darkmode_var = ctk.BooleanVar(value=True)

        self.darkmodecheckbox = ctk.CTkCheckBox(self, text="Dark Mode", variable=self.darkmode_var, command=self.darkmode)
        self.darkmodecheckbox.grid(row=1, column=0, padx=10, pady=10, sticky="n")

    def darkmode(self):
        print("Dark Mode Toggled")
        if self.darkmode_var.get():
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")