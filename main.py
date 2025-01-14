#####NOTE: Make sure to run "python main.py" to run the program using a virtual env#####
#####NOTE: if program still doesnt work, go to activate file in your venv to add export TCL_LIBRARY="C:\Users\Braya\AppData\Local\Programs\Python\Python313\tcl\tcl8.6" to fix tlc error#####

import customtkinter as ctk
from Frames.Head_Frame import HeadFrame
from Frames.Sidebar_Frame import SideBarFrame
from Frames.ToggleButton_Frame import ToggleButtonFrame
from PIL import Image
import os
import signIn
import pandas as pd
import customtkinter as ctk
from Frames.Head_Frame import HeadFrame
from Frames.Sidebar_Frame import SideBarFrame
from Frames.ToggleButton_Frame import ToggleButtonFrame
from Frames.Home_Frame import HomeFrame



#Prepares logo for future use
logo_image_path = os.path.join(os.getcwd(), "Images", "LogoPynancial2.png")
logo = Image.open(logo_image_path).resize((200, 100))


#Opens main window
def mainWindow(app, user):

    # Initialize transactions attribute to use the transactions saved in excel
    app.transactions = loadTransactions(user)
    print(app.transactions)

    app.num_transactions = len(app.transactions)
    
#Used to save after every added transaction
    app.save = lambda : saveTransactions(user, app.transactions)
    
#Creates the header using logo
    Head = HeadFrame(app, logo, go_home)
    Head.grid(columnspan=2, sticky="ew")

    app.grid_columnconfigure(1, weight=10000)
    app.grid_rowconfigure(1, weight=1)
    
#Creates sidebar using sidebarframe file
    Sidebar = SideBarFrame(app, "Create Transaction", "View Transactions", "Statistics", "Settings", "Help")
    Sidebar.grid(row=1, column=0, sticky="nsw")

#Creates open and close button
    Togglebutton = ToggleButtonFrame(app, Sidebar)
    Togglebutton.grid(row=1, column=1, sticky="nw")
 
#Creates the main frame
    app.MainFrame = HomeFrame(app, user)
    app.MainFrame.grid(row=1, column=1, sticky="nwse")

    Togglebutton.lift()
    
#Saves transactions to excel file
def saveTransactions(user, data):    
    print("Saving data")

#Takes dictionary and converts it to a dataframe
    savedData = pd.DataFrame.from_dict(data, orient = 'index')
    print(savedData)

#Save dataframe to excel file
    savedData.to_excel(excel_writer = user + ".xlsx")

#Loads transactions from excel file
def loadTransactions(user):

#Creates a dataframe from excel file
    savedData = pd.read_excel(user + ".xlsx")
    print("Loading saved data")
    print(savedData)

#Converts dataframe to dictionary
    return savedData.to_dict(orient = 'index')


######Temp arrays for storing test usernames and passwords
users = ["TestUser"]
passwords = ["Password"]
#########


if (__name__ == "__main__"):
    print("Main Executed")

    ctk.set_default_color_theme("green")

#Creates app window and names it
    app = ctk.CTk()
    app.title("PyNancial Pro")
    app.geometry("1200x700")

    def go_home():
        for widget in app.MainFrame.winfo_children():
            widget.destroy()
        home_frame = HomeFrame(app.MainFrame, "TestUser")
        home_frame.grid(sticky="nsew")

#Creates sign in screen header
    app.grid_columnconfigure(0, weight=1)
    Head = HeadFrame(app, logo, go_home)
    Head.grid(columnspan=5, sticky="ew")

#Calls sign in screen
    signIn.signInScreen(app, users, passwords, mainWindow)

    

    app.mainloop()
