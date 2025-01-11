import customtkinter as ctk

#Determines if 
def logInPressed(userNameBox, passWordBox, users, passwords, app, mainWindow):    
####################################
# Error could result if multiple users enter same user name
# For future improvement either only allow a username to be create if it is unique
# Or modify function to continue searching if password does not match username
####################################

#Takes user input for username and stores in user
    user = userNameBox.get("1.10", "1.end") #The textbox indexing starts from 1 not from 0
    print(user)
#Takes user input for password and stores in password
    password = passWordBox.get("1.10", "1.end")

    print("Username: " + user + "\nPassword: " + password)

#Sorts through array of all entered usernames to look for a match
    for i in range(0, len(users)):
         if users[i] == user:
              print("User Match")

#Determines if entered password matched the stored password for the entered username
              if passwords[i] == password:
                print("Logged In")

#Reformat rows
                app.grid_rowconfigure(0, weight=0)
                app.grid_rowconfigure(1, weight=0)
                app.grid_rowconfigure(2, weight=0)
                app.grid_rowconfigure(3, weight=0)
                app.grid_rowconfigure(4, weight=0)
                app.grid_rowconfigure(5, weight=0)

#If passwords match close sign in window and open main window
                clearFrame(app)
                mainWindow(app, user)


                


#Clears all widgets from the frame
def clearFrame(app):
    for widget in app.winfo_children():
       widget.destroy()

#Adds username and password for a new account
def createAccountPressed(userNameBox, passWordBox, users, passwords):

#Takes user input for username and stores in user
    user = userNameBox.get("1.10", "1.end")
#Takes user input for password and stores in password
    password = passWordBox.get("1.10", "1.end")

#Add new username and password to temp arrays
    users.append(user)
    passwords.append(password)

#Removes username and password from textboxes
    userNameBox.delete("1.10", "1.end")
    passWordBox.delete("1.10", "1.end")
    

#Runs program
def signInScreen(app, users, secretWords, mainWindow):
    print("Running")
    fontSettings = ("Arial", 24)

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
    userNameBox = ctk.CTkTextbox(app, width=300, height=75, border_color="black", text_color="black",border_width=5, fg_color= "gray", font = fontSettings, border_spacing=20)
    userNameBox.insert("0.0", "Username: ")
    userNameBox.grid(column=3, row = 2, sticky = '')

#Password box
    passWordBox = ctk.CTkTextbox(app, width=300, height=75, border_color="black", text_color="black",border_width=5, fg_color= "gray", font = fontSettings, border_spacing=20)
    passWordBox.insert("0.0", "Password: ")
    passWordBox.grid(column=3, row = 4, sticky = '')

#Log in button
    logIn = ctk.CTkButton(app, text="Log In", command=lambda: logInPressed(userNameBox, passWordBox, users, secretWords, app, mainWindow), width=300, height=75, border_color="black", text_color="black",border_width=5, font = fontSettings)
    logIn.grid(column=1, row=2, sticky='')

#Create account button
    createAccount = ctk.CTkButton(app, text="Create Account", command=lambda: createAccountPressed(userNameBox, passWordBox, users, secretWords), width=300, height=75, border_color="black", text_color="black",border_width=5, font = fontSettings)
    createAccount.grid(column=1, row=4, sticky='')
