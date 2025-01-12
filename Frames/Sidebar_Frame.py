import customtkinter as ctk

from Frames.CreateReport_Frame import CreateReportFrame
from Frames.Help_Frame import HelpFrame

'''
This class creates the Sidebar in order for the user to navigate through the dashboard

'''


class SideBarFrame(ctk.CTkFrame):
    def __init__(self, master, *navs):
        super().__init__(master)
        self.navList = []
        self.master = master

        # Configure grid for vertical stretching
        self.grid_columnconfigure(0, weight=1)  # Ensure buttons fill the width
        self.grid_rowconfigure("all", weight=1)  # Equal weight for rows

        self.configure(
            border_width=1,
            border_color="#000000"
        )

        for i, nav in enumerate(navs):
            self.button = ctk.CTkButton(self, text=str(nav), command=lambda name=nav: self.onClick(name, master))
            self.navList.append(self.button)
            print(str(self.button))
            self.button.grid(row=i, pady=30, padx=10, sticky="ew")


    def onClick(self, button_name, master):
        print(f"{button_name} clicked on")
        if button_name == "New Transaction":
            self.show_create_report(master) #Shows the Create Report environment

        if button_name == "Help":
            self.show_help(master) #Shows the Help environment

    def show_help(self, master):
        for widget in master.MainFrame.winfo_children():
            widget.destroy()
        help_frame = HelpFrame(master.MainFrame)
        help_frame.grid(sticky="nwse")

    def show_create_report(self, master): #Creates the report from mainwindow
        for widget in master.MainFrame.winfo_children():
            widget.destroy() #Destroys any previous widget on mainframe
        create_report_frame = CreateReportFrame(master.MainFrame)
        create_report_frame.grid(sticky="nwse")

    def toggle_visibility(self):
        if self.winfo_ismapped():  # Check if the frame is visible
            self.grid_remove()  # Hide the frame
        else:
            self.grid()
            
            


        
            

        

