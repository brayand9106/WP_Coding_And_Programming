"""
This class creates the transaction object which is how Pynancial Pro 
keeps track of the user's transactions
"""

class Transaction:
    def __init__(self, id, title, income, expenses, date):
        self.id = id
        self.title = title
        self.income = income
        self.expenses = expenses
        self.date = date

    def getTransactionID(self):
        return self.id

    def getTransactionText(self):
        return self.title
    
    def getIncome(self):
        return self.income
    
    def getExpenses(self):
        return self.expenses
    
    def getDate(self):
        return self.date