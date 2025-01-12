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

#Creates the header using logo
    Head = HeadFrame(app, logo)
    Head.grid(columnspan=2, sticky="ew")

    app.grid_columnconfigure(1, weight=10000)
    app.grid_rowconfigure(1, weight=1)
    
#Creates sidebar using sidebarframe file
    Sidebar = SideBarFrame(app, "Create Transaction", "View Transactions", "Statistics", "Settings", "TBD3")
    Sidebar.grid(row=1, column=0, sticky="nsw")

#Creates open and close button
    Togglebutton = ToggleButtonFrame(app, Sidebar)
    Togglebutton.grid(row=1, column=1, sticky="nw")
 
    ###############Add main frame here####################
    app.MainFrame = HomeFrame(app, user)
    app.MainFrame.grid(row=1, column=1, sticky="nwse")

    Togglebutton.lift()
    


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

    app.transactions = {}
    app.num_transactions = 0

#Creates sign in screen header
    app.grid_columnconfigure(0, weight=1)
    Head = HeadFrame(app, logo)
    Head.grid(columnspan=5, sticky="ew")

#Calls sign in screen
    signIn.signInScreen(app, users, passwords, mainWindow)

    

    app.mainloop()
