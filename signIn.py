import customtkinter as ctk
import pandas as pd

####################################
# Error could result if multiple users enter same user name
# For future improvement either only allow a username to be create if it is unique
# Or modify function to continue searching if password does not match username
####################################
def logInPressed(userNameEntry, passWordEntry, users, passwords, app, mainWindow):
    # Takes user input for username and stores in user
    user = userNameEntry.get().strip()
    print(user)
    # Takes user input for password and stores in password
    password = passWordEntry.get().strip()

    print("Username: " + user + "\nPassword: " + password)

    # Sorts through array of all entered usernames to look for a match
    for i in range(len(users)):
        if users[i] == user:
            print("User Match")
            app.grid_rowconfigure(2, weight=0)
            app.grid_rowconfigure(3, weight=0)
            app.grid_rowconfigure(4, weight=0)
            app.grid_rowconfigure(5, weight=0)
            app.grid_columnconfigure(2, weight=0)
            app.grid_columnconfigure(3, weight=0)
            app.grid_columnconfigure(4, weight=0)
            # Destroy all widgets in the current window
            # Determines if entered password matched the stored password for the entered username
            if passwords[i] == password:
                for widget in app.winfo_children():
                    widget.destroy()
                print("Logged In")
                mainWindow(app, user)
                return
            else:
                print("Incorrect Password")
    print("User not found")


def createAccountPressed(userNameEntry, passWordEntry, users, passwords):
    # Add logic to create a new account
    user = userNameEntry.get().strip()
    password = passWordEntry.get().strip()
    if user and password:
        users.append(user)
        passwords.append(password)
        print("Account created for user:", user)
    else:
        print("Username and password cannot be empty")
    
def toggle_password_visibility(passWordEntry, show_password):
    if show_password.get():
        passWordEntry.configure(show="")
    else:
        passWordEntry.configure(show="*")

def signInScreen(app, users, secretWords, mainWindow):
    app.grid_rowconfigure(0, weight=1)
    app.grid_rowconfigure(1, weight=1)
    app.grid_rowconfigure(2, weight=1)
    app.grid_rowconfigure(3, weight=1)
    app.grid_rowconfigure(4, weight=1)
    app.grid_rowconfigure(5, weight=1)
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)
    app.grid_columnconfigure(2, weight=1)
    app.grid_columnconfigure(3, weight=1)
    app.grid_columnconfigure(4, weight=1)

    # Create a rounded frame
    frame = ctk.CTkFrame(app, corner_radius=15)
    frame.grid(row=1, column=1, columnspan=3, rowspan=3, sticky="nsew", padx=0, pady=0)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_rowconfigure(2, weight=1)
    frame.grid_rowconfigure(3, weight=1)
    frame.grid_rowconfigure(4, weight=1)

    # Welcome label
    welcome_label = ctk.CTkLabel(frame, text="Welcome! Login or Create an Account", font=("Arial", 24))
    welcome_label.grid(row=0, column=0, columnspan=3, pady=0)

    # Username entry
    userNameEntry = ctk.CTkEntry(frame, placeholder_text="Username", width=300)
    userNameEntry.grid(row=1, column=1, pady=0)

    # Password entry
    passWordEntry = ctk.CTkEntry(frame, placeholder_text="Password", show="*", width=300)
    passWordEntry.grid(row=2, column=1, pady=0)

    # Show password button
    show_password = ctk.BooleanVar()
    show_password_button = ctk.CTkCheckBox(frame, text="Show Password", variable=show_password, command=lambda: toggle_password_visibility(passWordEntry, show_password))
    show_password_button.grid(row=2, column=1, padx=(550, 0), sticky="w")

    # Log in button
    logInButton = ctk.CTkButton(frame, text="Log In", command=lambda: logInPressed(userNameEntry, passWordEntry, users, secretWords, app, mainWindow), width=300)
    logInButton.grid(row=3, column=1, pady=0)

    # Create account button
    createAccountButton = ctk.CTkButton(frame, text="Create Account", command=lambda: createAccountPressed(userNameEntry, passWordEntry, users, secretWords), width=300)
    createAccountButton.grid(row=4, column=1, pady=0)
