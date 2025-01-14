import customtkinter as ctk
import seaborn as sns
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

'''
This frame creates a view transactions environment that allows the user 
to review all transactions done
'''

class StatisticsFrame(ctk.CTkFrame):
    def __init__(self, app, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app  # Store the app instance
        self.grid_columnconfigure(0, weight=1)  # Ensure widgets fill the width

        self.label = ctk.CTkLabel(self, text="Select Time Range:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.time_range_var = ctk.StringVar(value="1 Week")
        self.time_range_menu = ctk.CTkOptionMenu(self, variable=self.time_range_var, values=["1 Week", "1 Month", "1 Year"])
        self.time_range_menu.grid(row=1, column=0, padx=10, pady=10)

        self.generate_button = ctk.CTkButton(self, text="Generate Graph", command=self.generate_graph)
        self.generate_button.grid(row=2, column=0, padx=10, pady=10)

        self.canvas = None

    def generate_graph(self):
        time_range = self.time_range_var.get()
        end_date = datetime.now()
        if time_range == "1 Week":
            start_date = end_date - timedelta(weeks=1)
        elif time_range == "1 Month":
            start_date = end_date - timedelta(days=30)
        elif time_range == "1 Year":
            start_date = end_date - timedelta(days=365)

        filtered_transactions = [
            transaction for transaction in self.app.transactions.values()
            if start_date <= datetime.strptime(transaction.date, "%m/%d/%y") <= end_date
        ]

        if not filtered_transactions:
            print("No transactions found for the selected time range.")
            return

        df = pd.DataFrame([{
            "Transaction": t.transaction_text,
            "Income": float(t.income),
            "Expenses": float(t.expenses),
            "Date": datetime.strptime(t.date, "%m/%d/%y")
        } for t in filtered_transactions])

        fig, ax = plt.subplots()
        sns.lineplot(data=df, x="Date", y="Income", ax=ax, label="Income")
        sns.lineplot(data=df, x="Date", y="Expenses", ax=ax, label="Expenses")
        ax.set_title("Income and Expenses Over Time")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=3, column=0, padx=10, pady=10, sticky="nsew")