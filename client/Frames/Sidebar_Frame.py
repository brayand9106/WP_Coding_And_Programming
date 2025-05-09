import customtkinter as ctk

from Frames.CreateTransaction_Frame import CreateTransactionFrame
from Frames.ViewTransactions_Frame import ViewTransactionsFrame
from Frames.Help_Frame import HelpFrame
from Frames.Statistics_Frame import StatisticsFrame
from Frames.Settings_Frame import SettingsFrame
'''
This class creates the Sidebar in order for the user to navigate through the dashboard

'''


class SideBarFrame(ctk.CTkFrame):
    def __init__(self, master, *navs):
        super().__init__(master)
        self.navList = []
        self.app = master

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
            self.button.grid(row=i, pady=30, padx=10, sticky="ew")

    """This method binds sidebar buttons to the functions that are called when clicked"""
    def onClick(self, button_name, master):
        print(f"{button_name} clicked on")
        if button_name == "Create Transaction":
            self.show_create_transaction(master) #Shows the Create transaction environment
        elif button_name == "View Transactions":
            self.show_view_transactions(master)
        elif button_name == "Help":
            self.show_help(master) #Shows the Help environment
        elif button_name == "Statistics":
            self.show_statistics(master) #Shows the Statistics environment
        elif button_name == "Settings":
            self.show_settings(master) #Shows the Settings environment
        

    """This method displays the help window from sidebar button destroys previous"""
    def show_help(self, master):
        for widget in master.MainFrame.winfo_children():
            widget.destroy()
        help_frame = HelpFrame(master.MainFrame)
        help_frame.grid(sticky="nwse")

    """This method displays the create transaction window from sidebar button destroys previous"""
    def show_create_transaction(self, master): #Creates the transaction from mainwindow
        for widget in master.MainFrame.winfo_children():
            widget.destroy() #Destroys any previous widget on mainframe
        create_transaction_frame = CreateTransactionFrame(master, master.MainFrame)
        create_transaction_frame.grid(sticky="nwse")

    """This method displays the view transactions window from sidebar button destroys previous"""
    def show_view_transactions(self, master):
        for widget in master.MainFrame.winfo_children():
            widget.destroy()
        view_transactions_frame = ViewTransactionsFrame(master, master.MainFrame)
        view_transactions_frame.grid(sticky="nwse")

    """This method displays the settings window from sidebar button destroys previous"""
    def show_settings(self, master):
        for widget in master.MainFrame.winfo_children():
            widget.destroy()
        settings_frame = SettingsFrame(master, master.MainFrame)
        settings_frame.grid(sticky="nwse")

    """This method displays the statistics window from sidebar button destroys previous"""
    def show_statistics(self, master):
        for widget in master.MainFrame.winfo_children():
            widget.destroy()
        statistics_frame = StatisticsFrame(master, master.MainFrame)
        statistics_frame.grid(sticky="nwse")

    """This method is used to toggle the visibility of the sidebar"""
    def toggle_visibility(self):
        if self.winfo_ismapped():  # Check if the frame is visible
            self.grid_remove()  # Hide the frame
        else:
            self.grid()
            
            


        
            

        

