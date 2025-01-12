import customtkinter as ctk

'''
This frame creates a view transactions environment that allows the user
to review all transactions done
'''

class ViewTransactionsFrame(ctk.CTkFrame):
    def __init__(self, app, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app  # Store the app instance

        self.grid_columnconfigure(0, weight=1)  # Ensure widgets fill the width
        self.grid_rowconfigure(1, weight=1)  # Ensure the listbox expands

        self.label = ctk.CTkLabel(self, text="View Transactions")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.filter_entry = ctk.CTkEntry(self, placeholder_text="Filter transactions")
        self.filter_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.filter_button = ctk.CTkButton(self, text="Filter", command=self.filter_transactions)
        self.filter_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.update_button = ctk.CTkButton(self, text="Update", command=self.update_transaction)
        self.update_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.delete_button = ctk.CTkButton(self, text="Delete", command=self.delete_transaction)
        self.delete_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        self.create_table_headers()
        self.load_transactions()

    def create_table_headers(self):
        headers = ["ID", "Report", "Income", "Expenses", "Date"]
        for col, header in enumerate(headers):
            label = ctk.CTkLabel(self.scrollable_frame, text_color="black", text=header, font=("Arial", 12, "bold"), fg_color="lightgrey", corner_radius=5)
            label.grid(row=0, column=col, padx=5, pady=5, sticky="ew")
            self.scrollable_frame.grid_columnconfigure(col, weight=1)

    def load_transactions(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.create_table_headers()
        for row, (transaction_id, transaction) in enumerate(self.app.transactions.items(), start=1):
            label_id = ctk.CTkLabel(self.scrollable_frame, text=str(transaction_id))
            label_id.grid(row=row, column=0, padx=5, pady=5, sticky="ew")

            label_report = ctk.CTkLabel(self.scrollable_frame, text=transaction.transaction_text)
            label_report.grid(row=row, column=1, padx=5, pady=5, sticky="ew")

            label_income = ctk.CTkLabel(self.scrollable_frame, text=str(transaction.income))
            label_income.grid(row=row, column=2, padx=5, pady=5, sticky="ew")

            label_expenses = ctk.CTkLabel(self.scrollable_frame, text=str(transaction.expenses))
            label_expenses.grid(row=row, column=3, padx=5, pady=5, sticky="ew")

            label_date = ctk.CTkLabel(self.scrollable_frame, text=transaction.date)
            label_date.grid(row=row, column=4, padx=5, pady=5, sticky="ew")

    def filter_transactions(self):
        filter_text = self.filter_entry.get()
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.create_table_headers()
        for row, (transaction_id, transaction) in enumerate(self.app.transactions.items(), start=1):
            if filter_text.lower() in str(transaction).lower():
                label_id = ctk.CTkLabel(self.scrollable_frame, text=str(transaction_id))
                label_id.grid(row=row, column=0, padx=5, pady=5, sticky="ew")

                label_report = ctk.CTkLabel(self.scrollable_frame, text=transaction.transaction_text)
                label_report.grid(row=row, column=1, padx=5, pady=5, sticky="ew")

                label_income = ctk.CTkLabel(self.scrollable_frame, text=str(transaction.income))
                label_income.grid(row=row, column=2, padx=5, pady=5, sticky="ew")

                label_expenses = ctk.CTkLabel(self.scrollable_frame, text=str(transaction.expenses))
                label_expenses.grid(row=row, column=3, padx=5, pady=5, sticky="ew")

                label_date = ctk.CTkLabel(self.scrollable_frame, text=transaction.date)
                label_date.grid(row=row, column=4, padx=5, pady=5, sticky="ew")

    def update_transaction(self):
        selected_index = self.scrollable_frame.curselection()
        if selected_index:
            transaction_id = int(self.scrollable_frame.get(selected_index).split(",")[0].split(":")[1].strip())
            # Implement the update functionality here
            print(f"Update transaction with ID: {transaction_id}")

    def delete_transaction(self):
        selected_index = self.scrollable_frame.curselection()
        if selected_index:
            transaction_id = int(self.scrollable_frame.get(selected_index).split(",")[0].split(":")[1].strip())
            del self.app.transactions[transaction_id]
            self.load_transactions()
            print(f"Deleted transaction with ID: {transaction_id}")