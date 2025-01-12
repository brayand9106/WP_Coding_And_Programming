import customtkinter as ctk
import tkinter as tk

class HomeFrame(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master)
        self.displayHome(user)

    def displayHome(self, user):
        fontSettings = ("Arial", 24)
        greeting = tk.Text(self, width=40, height=2, borderwidth=5, relief="solid", font=fontSettings, bg = "gray")
        greeting.insert("1.0", "Welcome " + user + "!")
        greeting.tag_configure("center", justify='center')
        greeting.tag_add("center", "1.0", "end")
        greeting.configure(state="disabled")  # Make the Text widget read-only
        self.columnconfigure(0, weight=1)
        greeting.grid(columnspan=3, padx=30, pady=30, sticky='ew')