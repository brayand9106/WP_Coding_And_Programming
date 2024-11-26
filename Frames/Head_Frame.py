import customtkinter as ctk

class HeadFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure(0, weight=1)  # Ensure buttons fill the width
        self.grid_rowconfigure("all", weight=1)  # Equal weight for rows
