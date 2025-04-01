import customtkinter as ctk

'''
This frame creates a toggle button that when clicked it toggles the 
visibility of the sidebar frame
'''

class ToggleButtonFrame(ctk.CTkFrame):
    def __init__(self, master, target_frame):
        super().__init__(master)
        self.target = target_frame

        self.button = ctk.CTkButton(self, text="<", width=25, command=self.onClick)
        self.button.grid(sticky="nw")

    """This method toggles the visibility of the sidebar frame"""
    def onClick(self):
        self.target.toggle_visibility()
        if self.button.cget("text") == "<":
            self.button.configure(text=">")
        else:
            self.button.configure(text="<")


