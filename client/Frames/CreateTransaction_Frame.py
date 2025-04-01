import customtkinter as ctk
from controller import save_transaction
from CTkMessagebox import CTkMessagebox as ctkm
from Frames.Transaction import Transaction
'''
This frame creates a report creation environment that allows the user
to input expenses and income to be tracked
'''

class CreateTransactionFrame(ctk.CTkFrame):
    def __init__(self, app, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app

        self.grid_columnconfigure(0, weight=1)  # Ensure widgets fill the width
        
        self.label = ctk.CTkLabel(self, text="Enter your Transaction Name:")
        self.label.grid(row=0, column=0, padx=10, pady=10)
        
        self.entry = ctk.CTkEntry(self)
        self.entry.grid(row=1, column=0, padx=10, pady=10)

        self.income_label = ctk.CTkLabel(self, text="Enter Income:")
        self.income_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.income_entry = ctk.CTkEntry(self)
        self.income_entry.grid(row=3, column=0, padx=10, pady=10)
        
        self.expense_label = ctk.CTkLabel(self, text="Enter Expenses:")
        self.expense_label.grid(row=4, column=0, padx=10, pady=10)
        
        self.expense_entry = ctk.CTkEntry(self)
        self.expense_entry.grid(row=5, column=0, padx=10, pady=10)
        
        self.date_label = ctk.CTkLabel(self, text="Enter Date of Transaction (mm/dd/yyyy):")
        self.date_label.grid(row=6, column=0, padx=10, pady=10)
        
        self.date_entry = ctk.CTkEntry(self)
        self.date_entry.grid(row=7, column=0, padx=10, pady=10)

        self.submit_button = ctk.CTkButton(self, text="Submit", command=lambda: self.submit_transaction())
        self.submit_button.grid(row=8, column=0, padx=10, pady=10)

    """This method creates a popup window that asks the user to confirm the transaction"""
    def confirmPopup(self, title, income, expenses, date):
        # Creates the popup with the transaction details and 2 buttons
        msg = ctkm(title="Confirm Transaction?", 
                   message=f"Create transaction with info\nTitle: {title}\nIncome: {income}\nExpenses: {expenses}\nDate: {date}",
                   option_1="Confirm", option_2="Cancel", icon="check")
        
        # Retrieves the button clicked by the user
        confirm = msg.get()

        # Returns if users confirms or cancels the transaction
        if confirm == "Confirm":
            print("Transaction confirmed")
            return True
        elif confirm == "Cancel":
            print("Transaction cancelled")
            return False    

    """This method submits the transaction to the server and adds it to the list of transactions"""
    def submit_transaction(self):
        title = self.entry.get()
        income = self.income_entry.get()
        expenses = self.expense_entry.get()
        date = self.date_entry.get()

        user = self.app.user
        
        print(title, income, expenses, date, user)

        # Calls to pull up the popup window
        userConfirm = self.confirmPopup(title, income, expenses, date)

        # If the user cancels the transaction it does not save
        if not userConfirm:
            return
        
        # If the user confirms the transaction it saves
        response = save_transaction(user, title, float(income), float(expenses), date)
        if response and response.status_code == 201:
            transaction_id = response.json().get('transaction_id')
            if transaction_id:
                # Adds transaction to the list
                new_transaction = Transaction(transaction_id, title, float(income), float(expenses), date)
                self.app.transactions.append(new_transaction)
                print(f"Transaction submitted: {title}, Income: {income}, Expenses: {expenses}, Date: {date}")
                ctkm(title="Transaction Submitted", message="Transaction has been submitted successfully.", icon="check")
            else:
                print("Failed to retrieve transaction ID from response.")
                ctkm(title="Transaction Failed", message="Failed to retrieve transaction ID from response.", icon="cancel")
        else:
            print(f"Failed to save transaction. Status code: {response.status_code if response else 'No response'}")
            ctkm(title="Transaction Failed", message=f"Failed to save transaction. Please try again.\n Status code: {response.status_code}", icon="cancel")