#####NOTE: Make sure to run "python main.py" to run the program using a virtual env#####
#####NOTE: if program still doesnt work, go to activate file in your venv to add export TCL_LIBRARY="C:\Users\Braya\AppData\Local\Programs\Python\Python313\tcl\tcl8.6" to fix tlc error#####

import customtkinter as ctk

if __name__ == "__main__":
    print("Main Executed")

    app = ctk.CTk()
    app.title("FinanceTBD")
    app.geometry("1200x700")


    app.mainloop()
