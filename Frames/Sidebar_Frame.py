import customtkinter as ctk

from Frames.CreateTransaction_Frame import CreateTransactionFrame
from Frames.ViewTransactions_Frame import ViewTransactionsFrame
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
        if button_name == "Create Transaction":
            self.show_create_transaction(master) #Shows the Create transaction environment
        elif button_name == "View Transactions":
            self.show_view_transactions(master)

    def show_create_transaction(self, master): #Creates the transaction from mainwindow
        for widget in master.MainFrame.winfo_children():
            widget.destroy() #Destroys any previous widget on mainframe
        create_transaction_frame = CreateTransactionFrame(master, master.MainFrame)
        create_transaction_frame.grid(sticky="nwse")

    def show_view_transactions(self, master):
        for widget in master.MainFrame.winfo_children():
            widget.destroy()
        view_transactions_frame = ViewTransactionsFrame(master, master.MainFrame)
        view_transactions_frame.grid(sticky="nwse")

    def toggle_visibility(self):
        if self.winfo_ismapped():  # Check if the frame is visible
            self.grid_remove()  # Hide the frame
        else:
            self.grid()
            
            


        
            

        

