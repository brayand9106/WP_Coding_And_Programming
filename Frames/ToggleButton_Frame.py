import customtkinter as ctk

'''
This frame creates a toggle button that when clicked it toggles the 
visibility of the sidebar frame
'''

class ToggleButtonFrame(ctk.CTkFrame):
    def __init__(self, master, target_frame):
        super().__init__(master)
        self.button = ctk.CTkButton(self, text="<", width=25, command=lambda frame=target_frame: onClick(frame))
        self.button.grid(sticky="nw")

        def onClick(target_frame):
            target_frame.toggle_visibility(target_frame)


