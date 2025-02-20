import customtkinter as ctk
from controller import save_transaction

'''
This frame creates a report creation environment that allows the user
to input expenses and income to be tracked
'''
################################################################
class Transaction():
    def __init__(self, id, transaction_text, income, expenses, date):
        self.id = id
        self.transaction_text = transaction_text
        self.income = income
        self.expenses = expenses
        self.date = date

    def getTransactionText(self):
        return self.transaction_text
    
    def getIncome(self):
        return self.income
    
    def getExpenses(self):
        return self.expenses
    
    def getDate(self):
        return self.date    
################################################################


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
        
        
    def submit_transaction(self):

        title = self.entry.get()
        income = self.income_entry.get()
        expenses = self.expense_entry.get()
        date = self.date_entry.get()

        user = self.app.user
        
        print(title, income, expenses, date, user)

        status_code = save_transaction(user, title, float(income), float(expenses), date)
        if status_code == 201:
            # Adds transaction to corresponding location in the dictionary
            self.app.transactions[self.app.num_transactions + 1] = {
                0: self.app.num_transactions + 1, 
                1: title, 
                2: float(income), 
                3: float(expenses), 
                4: date
            }
            print(self.app.transactions)
            self.app.num_transactions = len(self.app.transactions)
            print(f"Transaction submitted: {title}, Income: {income}, Expenses: {expenses}, Date: {date}")
        else:
            print(f"Failed to save transaction. Status code: {status_code}")