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

    """Returns the transaction ID"""
    def getTransactionID(self):
        return self.id

    """Returns the transaction title"""
    def getTransactionText(self):
        return self.title
    
    """Returns the transaction income"""
    def getIncome(self):
        return self.income
    
    """Returns the transaction expenses"""
    def getExpenses(self):
        return self.expenses
    
    """Returns the transaction date"""
    def getDate(self):
        return self.date