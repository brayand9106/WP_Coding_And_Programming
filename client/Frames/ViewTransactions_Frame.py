import customtkinter as ctk
from controller import delete_transaction as delete_transaction_in_db, load_transactions as load_transactions_from_db
from Frames.Transaction import Transaction
'''
This frame creates a view transactions environment that allows the user
to review all transactions done
'''

class ViewTransactionsFrame(ctk.CTkFrame):

    selectedTransactions = []

    def __init__(self, app, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app  # Store the app instance

        self.grid_columnconfigure(0, weight=1)  # Ensure widgets fill the width
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)  # Ensure the listbox expands

        self.label = ctk.CTkLabel(self, text="View Transactions", font=("Arial", 34))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.search_label = ctk.CTkLabel(self, text="Search", font=("Arial", 12, "bold"))
        self.search_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.filter_entry = ctk.CTkEntry(self, placeholder_text="Search transactions")
        self.filter_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.filter_entry.bind("<KeyRelease>", self.real_time_search)

        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.update_button = ctk.CTkButton(self, text="Refresh", command=self.load_transactions)
        self.update_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.delete_button = ctk.CTkButton(self, text="Delete", command=self.delete_transaction)
        self.delete_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        self.create_table_headers()
        self.load_transactions()

    def create_table_headers(self):
        headers = ["ID", "Report", "Income", "Expenses", "Date"]
        for col, header in enumerate(headers):
            label = ctk.CTkButton(self.scrollable_frame, text_color="black", text=header, font=("Arial", 12, "bold"), fg_color="lightgrey", corner_radius=5, command=lambda text=header: self.filter_transactions(text))
            label.grid(row=0, column=col, padx=5, pady=5, sticky="ew")
            self.scrollable_frame.grid_columnconfigure(col, weight=1)

    def selectTransactions(self, transaction_id, state):
        if state.get():
            self.selectedTransactions.append(transaction_id)
            print(self.selectedTransactions)
        else:
            self.selectedTransactions.remove(transaction_id)
            print(self.selectedTransactions)

    def load_transactions(self, transactions=None):
        if transactions is None:
            transactions = self.app.transactions

        # Clear existing rows except headers
        for widget in self.scrollable_frame.winfo_children():
            if widget.grid_info()['row'] > 0:
                widget.destroy()

        for row, transaction in enumerate(transactions, start=1):
            state = ctk.BooleanVar(value=False)
            selectTransactionBox = ctk.CTkCheckBox(
                self.scrollable_frame,
                text="                          " + str(transaction.getTransactionID()),
                variable=state,
                onvalue=True,
                offvalue=False,
                command=lambda transaction_id=transaction.getTransactionID(), state=state: self.selectTransactions(transaction_id, state)
            )
            selectTransactionBox.grid(row=row, column=0, padx=20, pady=5, sticky="ew")

            label_report = ctk.CTkLabel(self.scrollable_frame, text=transaction.title, width=150)
            label_report.grid(row=row, column=1, padx=5, pady=5, sticky="ew")

            label_income = ctk.CTkLabel(self.scrollable_frame, text=str(transaction.income), width=100)
            label_income.grid(row=row, column=2, padx=5, pady=5, sticky="ew")

            label_expenses = ctk.CTkLabel(self.scrollable_frame, text=str(transaction.expenses), width=100)
            label_expenses.grid(row=row, column=3, padx=5, pady=5, sticky="ew")

            label_date = ctk.CTkLabel(self.scrollable_frame, text=transaction.date, width=100)
            label_date.grid(row=row, column=4, padx=5, pady=5, sticky="ew")

        self.scrollable_frame._parent_canvas.yview_moveto(0)  # Moves the scrollbar back to the top  # Scroll to the top

    def filter_transactions(self, button_name):
        if button_name == "ID":
            print("Filter by ID")
            sorted_transactions = sorted(self.app.transactions, key=lambda item: item.id)
        elif button_name == "Report":
            print("Filter by Report")
            sorted_transactions = sorted(self.app.transactions, key=lambda item: item.title.lower())
        elif button_name == "Income":
            print("Filter by Income")
            sorted_transactions = sorted(self.app.transactions, key=lambda item: item.income, reverse=True)
        elif button_name == "Expenses":
            print("Filter by Expenses")
            sorted_transactions = sorted(self.app.transactions, key=lambda item: item.expenses, reverse=True)
        elif button_name == "Date":
            print("Filter by Date")
            sorted_transactions = sorted(self.app.transactions, key=lambda item: item.date)
        else:
            print("Unable to filter transactions")

        self.load_transactions(sorted_transactions)

    def real_time_search(self, event):
        term = self.filter_entry.get().lower()
        print(f"Real-time search: {term}")
        if term == "":
            self.load_transactions()
        else:
            filtered_transactions = [transaction for transaction in self.app.transactions if term in transaction.title.lower()]
            self.load_transactions(filtered_transactions)

    def update_transaction(self):
        selected_index = self.scrollable_frame.curselection()
        if selected_index:
            transaction_id = int(self.scrollable_frame.get(selected_index).split(",")[0].split(":")[1].strip())
            # Implement the update functionality here
            print(f"Update transaction with ID: {transaction_id}")

    def delete_transaction(self):
        deleted_transaction_ids = []
        for transaction in self.app.transactions:
            if transaction.id in self.selectedTransactions:
                delete_transaction_in_db(transaction.id)
                deleted_transaction_ids.append(transaction.id)
        # Reload transactions from the database
        transactions_data = load_transactions_from_db(self.app.user)
        self.app.transactions = [Transaction(**data) for data in transactions_data]
        self.load_transactions()
        if deleted_transaction_ids:
            print(f"Deleted transactions with IDs: {', '.join(map(str, deleted_transaction_ids))}")
        else:
            print("No transactions were selected for deletion.")