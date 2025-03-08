import customtkinter as ctk
import seaborn as sns
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, AutoDateLocator
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
        self.grid_rowconfigure(5, weight=1)  # Ensure the graph row expands

        self.label_time_range = ctk.CTkLabel(self, text="Select Time Range:")
        self.label_time_range.grid(row=0, column=0, padx=10, pady=10)

        self.time_range_var = ctk.StringVar(value="1 Week")
        self.time_range_menu = ctk.CTkOptionMenu(self, variable=self.time_range_var, values=["1 Week", "1 Month", "1 Year"])
        self.time_range_menu.grid(row=1, column=0, padx=10, pady=10)

        self.label_graph_type = ctk.CTkLabel(self, text="Select Graph Type:")
        self.label_graph_type.grid(row=2, column=0, padx=10, pady=10)

        self.graph_type_var = ctk.StringVar(value="Income/Expenses")
        self.graph_type_menu = ctk.CTkOptionMenu(self, variable=self.graph_type_var, values=["Income/Expenses", "Net Earnings", "Cumulative Earnings"])
        self.graph_type_menu.grid(row=3, column=0, padx=10, pady=10)

        self.generate_button = ctk.CTkButton(self, text="Generate Graph", command=self.generate_graph)
        self.generate_button.grid(row=4, column=0, padx=10, pady=10)

        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

        self.canvas = None

    def generate_graph(self):
        time_range = self.time_range_var.get()
        graph_type = self.graph_type_var.get()
        end_date = datetime.now()
        if time_range == "1 Week":
            start_date = end_date - timedelta(weeks=1)
        elif time_range == "1 Month":
            start_date = end_date - timedelta(days=30)
        elif time_range == "1 Year":
            start_date = end_date - timedelta(days=365)

        filtered_transactions = [
            transaction for transaction in self.app.transactions
            if start_date <= datetime.strptime(transaction.date, "%m/%d/%Y") <= end_date
        ]

        if not filtered_transactions:
            print("No transactions found for the selected time range.")
            return

        if graph_type == "Income/Expenses":
            df = pd.DataFrame([{
                "Transaction": t.getTransactionText(),
                "Income": t.getIncome(),
                "Expenses": t.getExpenses(),
                "Date": datetime.strptime(t.getDate(), "%m/%d/%Y")
            } for t in filtered_transactions])

            fig, ax = plt.subplots(figsize=(10, 6))
            sns.lineplot(data=df, x="Date", y="Income", ax=ax, label="Income", errorbar=None)
            sns.lineplot(data=df, x="Date", y="Expenses", ax=ax, label="Expenses", errorbar=None)
            ax.set_title("Income and Expenses Over Time")
        elif graph_type == "Net Earnings":
            df = pd.DataFrame([{
                "Transaction": t.getTransactionText(),
                "Net Earnings": t.getIncome() - t.getExpenses(),
                "Date": datetime.strptime(t.getDate(), "%m/%d/%Y")
            } for t in filtered_transactions])

            fig, ax = plt.subplots(figsize=(10, 6))
            sns.lineplot(data=df, x="Date", y="Net Earnings", ax=ax, label="Net Earnings", errorbar=None)
            ax.set_title("Net Earnings Over Time")
        elif graph_type == "Cumulative Earnings":
            cumulative_earnings = 0
            df = pd.DataFrame([{
                "Transaction": t.getTransactionText(),
                "Cumulative Earnings": (cumulative_earnings := cumulative_earnings + (t.getIncome() - t.getExpenses())),
                "Date": datetime.strptime(t.getDate(), "%m/%d/%Y")
            } for t in filtered_transactions])

            fig, ax = plt.subplots(figsize=(10, 6))
            sns.lineplot(data=df, x="Date", y="Cumulative Earnings", ax=ax, label="Cumulative Earnings", errorbar=None)
            ax.set_title("Cumulative Earnings Over Time")
        
        if time_range == "1 Week":
            ax.xaxis.set_major_formatter(DateFormatter("%m-%d %A"))

        ax.xaxis.set_major_locator(AutoDateLocator())
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        fig.tight_layout(pad=3.0)

        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(fig, master=self.scrollable_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill='both', expand=True)