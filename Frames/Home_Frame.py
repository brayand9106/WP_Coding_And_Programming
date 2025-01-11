import customtkinter as ctk

class HomeFrame(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master)
        self.displayHome(user)


    def displayHome(self, user):
        fontSettings = ("Arial", 24)
        greeting = ctk.CTkTextbox(self, width=300, height=50, border_color="black", text_color="black",border_width=5, fg_color= "gray", border_spacing=20, font = fontSettings)
        greeting.insert("0.0", "Welcome " + user + "!")
        greeting.grid(row=1, column=1, padx=30, pady=30, sticky = 'w')