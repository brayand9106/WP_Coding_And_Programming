import customtkinter as ctk

#Determines if 
def logInPressed(username, password, users, secretWords, app, mainWindow):    

#The textbox indexing starts from 1 not from 0
    user = username.get("1.10", "1.end")
    passcode = password.get("1.10", "1.end")
    print(user + passcode)
    for i in range(0, len(users)):
         if users[i] == user:
              print("User Match")
              if secretWords[i] == passcode:
                print("Logged In")
                clearFrame(app)
                mainWindow(app)


def clearFrame(app):
    for widget in app.winfo_children():
       widget.destroy()

def createAccountPressed(password):
      print(password.get("0.0", "end"))

#Runs program
def signInScreen(app, users, secretWords, mainWindow):
    print("Running")
    

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

#Password box
    passWord = ctk.CTkTextbox(app, width=300, height=75, border_color="black", text_color="black",border_width=5, fg_color= "gray")
    passWord.insert("0.0", "Password: ")
    passWord.grid(column=3, row = 4, sticky = '')

#Log in button
    logIn = ctk.CTkButton(app, text="Log In", command=lambda: logInPressed(userName, passWord, users, secretWords, app, mainWindow), width=300, height=75, border_color="black", text_color="black",border_width=5)
    logIn.grid(column=1, row=2, sticky='')

#Create account button
    createAccount = ctk.CTkButton(app, text="Create Account", command=lambda: createAccountPressed(passWord), width=300, height=75, border_color="black", text_color="black",border_width=5)
    createAccount.grid(column=1, row=4, sticky='')
