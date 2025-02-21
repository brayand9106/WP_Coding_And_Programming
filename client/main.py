#####NOTE: Make sure to run "python main.py" to run the program using a virtual env#####
#####NOTE: if program still doesnt work, go to activate file in your venv to add export TCL_LIBRARY="C:\Users\Braya\AppData\Local\Programs\Python\Python313\tcl\tcl8.6" to fix tlc error#####

import customtkinter as ctk
from Frames.Head_Frame import HeadFrame
from Frames.Sidebar_Frame import SideBarFrame
from Frames.ToggleButton_Frame import ToggleButtonFrame
from PIL import Image
import os
import pandas as pd
import customtkinter as ctk
from Frames.Head_Frame import HeadFrame
from Frames.Sidebar_Frame import SideBarFrame
from Frames.ToggleButton_Frame import ToggleButtonFrame
from Frames.SignIn_Frame import SignInFrame
from Frames.Home_Frame import HomeFrame
from controller import load_transactions



#Prepares logo for future use
logo_image_path = os.path.join(os.getcwd(), "Images", "LogoPynancial2.png")
print(logo_image_path)
logo = Image.open(logo_image_path).resize((200, 100))


#Opens main window
def mainWindow(app, user):

    # Initialize transactions attribute to use the transactions saved in excel
    app.transactions = load_transactions(user)
    if not app.transactions:
        print("No transactions found for user.")
        app.transactions = {}

    print(app.transactions)
    app.num_transactions = len(app.transactions)
    
    app.grid_columnconfigure(1, weight=0)
    app.grid_rowconfigure(1, weight=0)  # Larger weight for the main content row
    app.grid_rowconfigure(0, weight=0)
    app.grid_columnconfigure(0, weight=0)

#Creates the header using logo
    Head = HeadFrame(app, logo, go_home)
    Head.grid(row=0, column=0, columnspan=3, sticky="new")

    app.grid_columnconfigure(1, weight=10000)
    app.grid_rowconfigure(1, weight=0)
    
#Creates sidebar using sidebarframe file
    Sidebar = SideBarFrame(app, "Create Transaction", "View Transactions", "Statistics", "Settings", "Help")
    Sidebar.grid(row=1, column=0, sticky="nsw")
    # Configure Sidebar to expand vertically
    app.grid_rowconfigure(1, weight=1)

#Creates open and close button
    Togglebutton = ToggleButtonFrame(app, Sidebar)
    Togglebutton.grid(row=1, column=1, sticky="nw")
 
#Creates the main frame
    app.MainFrame = ctk.CTkFrame(app)
    app.MainFrame.grid(row=1, column=1, sticky="nwse")
# Configure MainFrame to expand
    app.MainFrame.grid_columnconfigure(0, weight=1)
    app.MainFrame.grid_rowconfigure(0, weight=1)
    home = HomeFrame(app.MainFrame, user)
    app.user = user
    home.grid(sticky="nsew")

    Togglebutton.lift()

if (__name__ == "__main__"):
    print("Main Executed")

    ctk.set_default_color_theme("green")

#Creates app window and names it
    app = ctk.CTk()
    app.title("PyNancial Pro")
    app.geometry("1200x700")

    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    def go_home():
        for widget in app.MainFrame.winfo_children():
            widget.destroy()
        home_frame = HomeFrame(app.MainFrame, app.user)
        home_frame.grid(sticky="nsew")

#Calls sign in screen
    signInFrame = SignInFrame(app, mainWindow)
    signInFrame.grid(row=0, column=0, sticky="nsew")

    app.mainloop()
