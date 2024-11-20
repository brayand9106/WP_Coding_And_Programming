#####NOTE: Make sure to run "python main.py" to run the program using a virtual env#####
#####NOTE: if program still doesnt work, go to activate file in your venv to add export TCL_LIBRARY="C:\Users\Braya\AppData\Local\Programs\Python\Python313\tcl\tcl8.6" to fix tlc error#####

import customtkinter as ctk
from Frames.Sidebar_Frame import SideBarFrame
from Frames.ToggleButton_Frame import ToggleButtonFrame

if __name__ == "__main__":
    print("Main Executed")

    app = ctk.CTk()
    app.title("FinanceTBD")
    app.geometry("1200x700")

    app.grid_columnconfigure(0, weight=0)
    app.grid_rowconfigure(0, weight=1)

    Sidebar = SideBarFrame(app, "Statistics", "Settings", "TBD", "TBD2", "TBD3")
    Sidebar.grid(row=0, column=0, sticky="nsw")

    Togglebutton = ToggleButtonFrame(app, Sidebar)
    Togglebutton.grid(column=1, row=0, sticky="nw")


    app.mainloop()
