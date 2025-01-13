from PIL import ImageTk
import customtkinter as ctk

class HeadFrame(ctk.CTkFrame):
    def __init__(self, master, img, home_command):
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
        
        # Add the logo as an image button to the nested frame
        self.logo_button = ctk.CTkButton(nested_frame, image=ctk_logo, text="", fg_color="transparent", bg_color="transparent", hover_color=nested_frame.cget("bg_color"), command=home_command)
        self.logo_button.image = ctk_logo  # Keep a reference to avoid garbage collection
        self.logo_button.grid(sticky="nwe", padx=0, pady=0)
