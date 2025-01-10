import customtkinter as ctk

'''
This frame creates a report creation environment that allows the user
to input expenses and income to be tracked
'''

class CreateReportFrame(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)  # Ensure widgets fill the width
        
        self.label = ctk.CTkLabel(self, text="Enter your report:")
        self.label.grid(row=0, column=0, padx=10, pady=10)
        
        self.entry = ctk.CTkEntry(self)
        self.entry.grid(row=1, column=0, padx=10, pady=10)

        self.income_label = ctk.CTkLabel(self, text="Enter income:")
        self.income_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.income_entry = ctk.CTkEntry(self)
        self.income_entry.grid(row=3, column=0, padx=10, pady=10)
        
        self.expense_label = ctk.CTkLabel(self, text="Enter expenses:")
        self.expense_label.grid(row=4, column=0, padx=10, pady=10)
        
        self.expense_entry = ctk.CTkEntry(self)
        self.expense_entry.grid(row=5, column=0, padx=10, pady=10)
        
        self.date_label = ctk.CTkLabel(self, text="Enter date of transaction:")
        self.date_label.grid(row=6, column=0, padx=10, pady=10)
        
        self.date_entry = ctk.CTkEntry(self)
        self.date_entry.grid(row=7, column=0, padx=10, pady=10)

        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit_report)
        self.submit_button.grid(row=8, column=0, padx=10, pady=10)
        
        
    def submit_report(self):
        report_text = self.entry.get()
        income = self.income_entry.get()
        expenses = self.expense_entry.get()
        date = self.date_entry.get()
        print(f"Report submitted: {report_text}, Income: {income}, Expenses: {expenses}, Date: {date}")