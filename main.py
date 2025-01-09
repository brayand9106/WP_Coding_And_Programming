#####NOTE: Make sure to run "python main.py" to run the program using a virtual env#####
#####NOTE: if program still doesnt work, go to activate file in your venv to add export TCL_LIBRARY="C:\Users\Braya\AppData\Local\Programs\Python\Python313\tcl\tcl8.6" to fix tlc error#####

from PIL import Image
import os
import signIn

logo_image_path = os.path.join(os.getcwd(), "Images", "LogoPynancial2.png")
logo = Image.open(logo_image_path).resize((200, 100))


def mainWindow(app):

    Head = HeadFrame(app, logo)
    Head.grid(columnspan=2, sticky="ew")

    app.grid_columnconfigure(1, weight=10000)
    app.grid_rowconfigure(1, weight=1)

    Sidebar = SideBarFrame(app, "Statistics", "Settings", "TBD", "TBD2", "TBD3")
    Sidebar.grid(row=1, column=0, sticky="nsw")

    Togglebutton = ToggleButtonFrame(app, Sidebar)
    Togglebutton.grid(row=1, column=1, sticky="nw")

    ###############Add main frame here####################
    

import customtkinter as ctk
from Frames.Head_Frame import HeadFrame
from Frames.Sidebar_Frame import SideBarFrame
from Frames.ToggleButton_Frame import ToggleButtonFrame

users = ["Norman", "Todd", "Howard"]
passwords = ["1234", "Beagle", "abc"]

if (__name__ == "__main__"):
    print("Main Executed")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.title("PyNancial Pro")
    app.geometry("1200x700")

    app.grid_columnconfigure(0, weight=1)

    Head = HeadFrame(app, logo)
    Head.grid(columnspan=5, sticky="ew")

    signIn.signInScreen(app, users, passwords, mainWindow)

    

    


    app.mainloop()
