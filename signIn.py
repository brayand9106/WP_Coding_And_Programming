import customtkinter as ctk
from Frames.Sidebar_Frame import SideBarFrame
from Frames.ToggleButton_Frame import ToggleButtonFrame

#Feedback for login and create account pressed
def logInPressed():
    print("Log In Attempt")

def createAccountPressed():
      print("Create Account Attempt")

#Runs program
if __name__ == "__main__":
    app = ctk.CTk()
    app.title("FinanceTBD")
    app.geometry("1200x700")

#Set up columns
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)
    app.grid_columnconfigure(2, weight=1)
    app.grid_columnconfigure(3, weight=1)
    app.grid_columnconfigure(4, weight=1)

#Set up rows
    app.grid_rowconfigure(0, weight=0)
    app.grid_rowconfigure(1, weight=1)
    app.grid_rowconfigure(2, weight=1)
    app.grid_rowconfigure(3, weight=0)
    app.grid_rowconfigure(4, weight=1)
    app.grid_rowconfigure(5, weight=1)

#Username box
    userName = ctk.CTkTextbox(app, width=300, height=75, border_color="black", text_color="black",border_width=5, fg_color= "gray")
    userName.insert("0.0", "Username: ")
    userName.grid(column=3, row = 2, sticky = '')

# Get username (Work In Progress)
#    user = userName.get("0.0", "end")

#Password box
    passWord = ctk.CTkTextbox(app, width=300, height=75, border_color="black", text_color="black",border_width=5, fg_color= "gray")
    passWord.insert("0.0", "Password: ")
    passWord.grid(column=3, row = 4, sticky = '')

#Log in button
    logIn = ctk.CTkButton(app, text="Log In", command=logInPressed, width=300, height=75, border_color="black", text_color="black",border_width=5)
    logIn.grid(column=1, row=2, sticky='')
    
#Create account button
    createAccount = ctk.CTkButton(app, text="Create Account", command=createAccountPressed, width=300, height=75, border_color="black", text_color="black",border_width=5)
    createAccount.grid(column=1, row=4, sticky='')




    app.mainloop()