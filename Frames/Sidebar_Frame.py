import customtkinter as ctk

'''
This class creates the Sidebar in order for the user to navigate through the dashboard

'''


class SideBarFrame(ctk.CTkFrame):
    def __init__(self, master, *navs):
        super().__init__(master)
        self.navList = []

        # Configure grid for vertical stretching
        self.grid_columnconfigure(0, weight=1)  # Ensure buttons fill the width
        self.grid_rowconfigure("all", weight=1)  # Equal weight for rows

        self.configure(
            border_width=1,
            border_color="#000000"
        )

        for i, nav in enumerate(navs):
            self.button = ctk.CTkButton(self, text=str(nav), command=lambda name=nav: self.onClick(name))
            self.navList.append(self.button)
            print(str(self.button))
            self.button.grid(row=i, pady=30, padx=10, sticky="ew")


    def onClick(self, button_name):
        print(f"{button_name} clicked on")

    def toggle_visibility(self):
        if self.winfo_ismapped():  # Check if the frame is visible
            self.grid_remove()  # Hide the frame
        else:
            self.grid()
            
            


        
            

        

