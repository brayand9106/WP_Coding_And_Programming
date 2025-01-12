import customtkinter as ctk

class HelpFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.HelpFrame()

    def HelpFrame(self):
        fontSettings = ("Arial", 24)
        greeting = ctk.CTkTextbox(self, height=40, font=fontSettings, fg_color="gray", border_color="black", text_color="black",border_width=5, border_spacing=20)
        greeting.insert("1.0", "Welcome to the Help Page!")
        greeting.grid(column=0, row=0, padx=30, pady=30, sticky='ew')
        greeting.configure(state= "disabled")

        reportsGuide = ctk.CTkTextbox(self, font=fontSettings, fg_color="gray", border_color="black", text_color="black",border_width=5, border_spacing=20, wrap = "word")
        reportsGuide.insert("1.0", "The transactions system is designed to keep track of all expenses and income, or account debits and credits. To create a transaction, click on the Create Transaction button on the left side of the screen. You will be prompted to enter a transaction type, income, expenses, and the date of the transaction. Once you have entered all the information, click the submit button to submit the transaction.")
        reportsGuide.grid(column=0, row=1, padx=30, pady=30, sticky='ew')
        reportsGuide.configure(state= "disabled")
        # Configure the grid to expand the textbox
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)