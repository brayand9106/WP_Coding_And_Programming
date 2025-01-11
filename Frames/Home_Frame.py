import customtkinter as ctk
import tkinter as tk

class HomeFrame(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master)
        self.displayHome(user)

    def displayHome(self, user):
        fontSettings = ("Arial", 24)
        greeting = tk.Text(self, width=40, height=2, borderwidth=5, relief="solid", font=fontSettings, bg="gray")
        greeting.insert("1.0", "Welcome " + user + "!")
        greeting.tag_configure("center", justify='center')
        greeting.tag_add("center", "1.0", "end")
        greeting.configure(state="disabled")  # Make the Text widget read-only

        # Create a frame to center the Text widget vertically
        container = ctk.CTkFrame(self)
        container.grid(row=0, column=0, sticky='nsew')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Place the Text widget inside the container
        greeting.grid(in_=container, padx=30, pady=30, sticky='nsew')

        # Configure the HomeFrame to expand and center the container
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)