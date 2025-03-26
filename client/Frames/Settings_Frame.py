import customtkinter as ctk
from CTkMessagebox import CTkMessagebox as ctkm
from tkinter import colorchooser
from Frames.utils import recreate_frames, logout
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
        self.grid_rowconfigure(0, weight=0)  # Weight for the top row
        self.grid_rowconfigure(1, weight=0)  # Weight for the middle row
        self.grid_rowconfigure(2, weight=0)  # Weight for the bottom row

        self.label = ctk.CTkLabel(self, text="Settings",font=("Arial", 24))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        # Create a BooleanVar to track the state of the checkbox
        self.darkmode_var = ctk.BooleanVar(value=self.app.dark_mode)

        self.darkmodecheckbox = ctk.CTkCheckBox(self, text="Dark Mode", variable=self.darkmode_var, command=self.darkmode)
        self.darkmodecheckbox.grid(row=1, column=0, padx=10, pady=10, sticky="n")

        self.themebutton = ctk.CTkButton(self, text="Change Theme", command=self.change_theme_popup)
        self.themebutton.grid(row=2, column=0, padx=10, pady=10, sticky="n")

        self.colorbutton = ctk.CTkButton(self, text="Change Color", command=lambda: self.apply_color(colorchooser.askcolor()[1]))
        self.colorbutton.grid(row=3, column=0, padx=10, pady=10, sticky="n")

        self.logoutbutton = ctk.CTkButton(self, text="Logout", command=lambda: logout(self.app))
        self.logoutbutton.grid(row=0, column=1, padx=10, pady=10, sticky="ne")

    def darkmode(self):
        print("Dark Mode Toggled")
        if self.darkmode_var.get():
            ctk.set_appearance_mode("Dark")
            self.app.dark_mode = True
        else:
            ctk.set_appearance_mode("Light")
            self.app.dark_mode = False

    def change_theme(self, msg_option):
        print("Theme Changed")
        ctk.set_default_color_theme(msg_option)
        recreate_frames(self.app)

    def change_theme_popup(self):
        msg = ctkm(title="Change Theme", message="Select theme", option_1="blue", option_2="green", option_3="dark-blue", icon="info")
        self.change_theme(msg.get())

    def apply_color(self, color_code):
        # Recursively apply the selected color to all CTkButton widgets
        def apply_color_recursive(widget):
            if isinstance(widget, ctk.CTkButton):
                widget.configure(fg_color=color_code, hover_color=color_code, border_color=color_code)
            for child in widget.winfo_children():
                apply_color_recursive(child)

        apply_color_recursive(self.app)