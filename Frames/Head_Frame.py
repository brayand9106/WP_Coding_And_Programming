from PIL import ImageTk


import customtkinter as ctk

class HeadFrame(ctk.CTkFrame):
    def __init__(self, master, img):
        super().__init__(master)
        
        self.configure(
            border_width=1,
            border_color="#000000"
        )
        self.grid_columnconfigure(0, weight=0)  # Ensure buttons fill the width
        self.grid_rowconfigure("all", weight=0)  # Equal weight for rows

        # Load the image
        ctk_logo = ImageTk.PhotoImage(img)

        # Create a nested frame
        nested_frame = ctk.CTkFrame(self, fg_color="transparent", bg_color="transparent")
        nested_frame.grid(sticky="w", padx=2, pady=2)
        # Add the logo to the nested frame
        self.logo = ctk.CTkLabel(nested_frame, image=ctk_logo, text="", fg_color="transparent", bg_color="transparent")
        self.logo.image = ctk_logo  # Keep a reference to avoid garbage collection
        self.logo.grid(sticky="nwe", padx=0, pady=0)
