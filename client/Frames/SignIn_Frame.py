import customtkinter as ctk
import pandas as pd

class SignInFrame(ctk.CTkFrame):
    def __init__(self, master, users, mainWindow):
        super().__init__(master)
        self.users = users
        self.mainWindow = mainWindow

        # Ensure SignInFrame expands
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create a rounded frame inside SignInFrame
        self.frame = ctk.CTkFrame(self, corner_radius=15)
        self.frame.grid(row=0, column=0, sticky="nsew", padx=250, pady=100)

        # Configure self.frame to expand fully
        self.frame.grid_columnconfigure(0, weight=10)

        # Welcome label
        self.welcome_label = ctk.CTkLabel(self.frame, text="Welcome! Login or Create an Account", font=("Arial", 24))
        self.welcome_label.grid(row=0, column=0, columnspan=3, pady=(40, 20))  # Increased top padding

                # Username entry (Very slightly moved left)
        self.userNameEntry = ctk.CTkEntry(self.frame, placeholder_text="Username", width=300)
        self.userNameEntry.grid(row=1, column=1, pady=(10, 10), padx=(8, 0), sticky="w")

        # Password entry (Very slightly moved left)
        self.passWordEntry = ctk.CTkEntry(self.frame, placeholder_text="Password", show="*", width=300)
        self.passWordEntry.grid(row=2, column=1, pady=(10, 10), padx=(8, 0), sticky="w")

        # Error Label (Aligned with inputs)
        self.error_label = ctk.CTkLabel(self.frame, text="", font=("Arial", 16), text_color="red", height=1)
        self.error_label.grid(row=3, column=1, pady=(5, 5), padx=(8, 0), sticky="w")

        # Show password checkbox (Right beside password entry with no spacing)
        self.show_password = ctk.BooleanVar()
        self.show_password_button = ctk.CTkCheckBox(self.frame, text="Show Password", variable=self.show_password, command=self.toggle_password_visibility)
        self.show_password_button.grid(row=2, column=2, padx=(0, 80), pady=(10, 10), sticky="w")  # No spacing between password entry and checkbox

        # Log in button (Very slightly moved left)
        self.logInButton = ctk.CTkButton(self.frame, text="Log In", command=self.logInPressed, width=300)
        self.logInButton.grid(row=4, column=1, pady=(0, 10), padx=(8, 0), sticky="w")

        # Create account button (Very slightly moved left)
        self.createAccountButton = ctk.CTkButton(self.frame, text="Create Account", command=self.createAccountPressed, width=300)
        self.createAccountButton.grid(row=5, column=1, pady=(10, 40), padx=(8, 0), sticky="w")


    def toggle_password_visibility(self):
        if self.show_password.get():
            self.passWordEntry.configure(show="")
        else:
            self.passWordEntry.configure(show="*")

    def logInPressed(self):
        username = self.userNameEntry.get().strip()
        password = self.passWordEntry.get().strip()

        # Example validation logic
        if not username or not password:
            self.error_label.configure(text="Username and password cannot be empty")
            return

        # Example user validation logic
        if username in self.users and self.users[username]["Passwords"] == password:
            for widget in self.master.winfo_children():
                widget.destroy()
            self.mainWindow(self.master, username)
        else:
            self.error_label.configure(text="Invalid username or password")

    def createAccountPressed(self):
        username = self.userNameEntry.get().strip()
        password = self.passWordEntry.get().strip()
        if username and password:
            self.users[username] = {"Passwords": password}
            users_df = pd.DataFrame.from_dict(self.users, orient="index")
            users_df.reset_index(inplace=True)
            users_df.rename(columns={"index": "UserNames"}, inplace=True)
            users_df.set_index("UserNames", inplace=True)
            users_df.to_excel("Users.xlsx")
            pd.DataFrame().to_excel(f"{username}.xlsx")
            self.error_label.configure(text="Account created successfully", text_color="green")
        else:
            self.error_label.configure(text="Username and password cannot be empty", text_color="red")