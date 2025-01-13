import customtkinter as ctk
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
            label = ctk.CTkButton(self.scrollable_frame, text_color="black", text=header, font=("Arial", 12, "bold"), fg_color="lightgrey", corner_radius=5, command = lambda text = header : self.filter_transactions(text))
            label.grid(row=0, column=col, padx=5, pady=5, sticky="ew")
            self.scrollable_frame.grid_columnconfigure(col, weight=1)
    
    def selectTransactions(self, transaction_id, state):
        if state.get():
            self.selectedTransactions.append(transaction_id - 1 )
            print(self.selectedTransactions)
        else:
            self.selectedTransactions.remove(transaction_id - 1)
            print(self.selectedTransactions)

    def load_transactions(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.create_table_headers()
    
        for row, (transaction_id, transaction) in enumerate(self.app.transactions.items(), start=1):
            state = ctk.BooleanVar(value = False)
            selectTransactionBox = ctk.CTkCheckBox(self.scrollable_frame, text= "                          " + str(row),
                                                   variable = state, onvalue = True, offvalue = False,
                                                   command = lambda row=row, state=state : self.selectTransactions(row, state)
                                                   )
            selectTransactionBox.grid(row=row, column=0, padx=20, pady=5, sticky="ew")


            label_report = ctk.CTkLabel(self.scrollable_frame, text=self.app.transactions[transaction_id][1])
            label_report.grid(row=row, column=1, padx=5, pady=5, sticky="ew")

            label_income = ctk.CTkLabel(self.scrollable_frame, text=str(self.app.transactions[transaction_id][2]))
            label_income.grid(row=row, column=2, padx=5, pady=5, sticky="ew")

            label_expenses = ctk.CTkLabel(self.scrollable_frame, text=str(self.app.transactions[transaction_id][3]))
            label_expenses.grid(row=row, column=3, padx=5, pady=5, sticky="ew")

            label_date = ctk.CTkLabel(self.scrollable_frame, text=self.app.transactions[transaction_id][4])
            label_date.grid(row=row, column=4, padx=5, pady=5, sticky="ew")

    def filter_transactions(self, button_name):
        if button_name == "ID":
            print("Filter by ID")
            for i in range(len(self.app.transactions)):
                for j in range(1, (len(self.app.transactions)) - i - 1):
                    if self.app.transactions[j][0] > self.app.transactions[j+1][0]:
                        self.app.transactions[j], self.app.transactions[j + 1] = self.app.transactions[j + 1], self.app.transactions[j]
                        print("Swtiching " + str(self.app.transactions[j]) + " with " + str(self.app.transactions[j + 1]))
            self.app.save()
        elif button_name == "Report":
            print("Filter by Report")
        elif button_name == "Income":
            print("Filter by Income")
        elif button_name == "Expenses":
            print("Filter by Expenses")
        elif button_name == "Date":
            print("Filter by Date")
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.create_table_headers()
        for row, (transaction_id, transaction) in enumerate(self.app.transactions.items(), start=1):
            
            state = ctk.BooleanVar(value = False)
            selectTransactionBox = ctk.CTkCheckBox(self.scrollable_frame, text= "                          " + str(row),
                                                   variable = state, onvalue = True, offvalue = False,
                                                   command = lambda row=row, state=state : self.selectTransactions(row, state)
                                                   )
            selectTransactionBox.grid(row=row, column=0, padx=20, pady=5, sticky="ew")

            label_report = ctk.CTkLabel(self.scrollable_frame, text=self.app.transactions[transaction_id][1])
            label_report.grid(row=row, column=1, padx=5, pady=5, sticky="ew")

            label_income = ctk.CTkLabel(self.scrollable_frame, text=str(self.app.transactions[transaction_id][2]))
            label_income.grid(row=row, column=2, padx=5, pady=5, sticky="ew")

            label_expenses = ctk.CTkLabel(self.scrollable_frame, text=str(self.app.transactions[transaction_id][3]))
            label_expenses.grid(row=row, column=3, padx=5, pady=5, sticky="ew")

            label_date = ctk.CTkLabel(self.scrollable_frame, text=self.app.transactions[transaction_id][4])
            label_date.grid(row=row, column=4, padx=5, pady=5, sticky="ew")

    def update_transaction(self):
        selected_index = self.scrollable_frame.curselection()
        if selected_index:
            transaction_id = int(self.scrollable_frame.get(selected_index).split(",")[0].split(":")[1].strip())
            # Implement the update functionality here
            print(f"Update transaction with ID: {transaction_id}")

    def delete_transaction(self):
            for x in range(len(self.selectedTransactions)):
                transaction_id = self.selectedTransactions.pop(0)
                del self.app.transactions[transaction_id]
                print(self.app.transactions)
            self.load_transactions()
            print(f"Deleted transaction with ID: {transaction_id}")
            self.app.save()