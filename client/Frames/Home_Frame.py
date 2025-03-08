import customtkinter as ctk
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.dates import DateFormatter, AutoDateLocator
from datetime import datetime, timedelta

class HomeFrame(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)  # Ensure widgets fill the width
        self.grid_rowconfigure(0, weight=0)  # Weight for the top row
        self.grid_rowconfigure(1, weight=1)  # Make the body frame row expandable

        self.app = master.master
        self.num_transactions = len(self.app.transactions)
        self.news_info = "Welcome to the Home! Currently you are using PyNancial Pro Version 1.0.0 which is the latest version. Stay tuned for more updates!"

        # Create a frame to act as a border for the welcome label
        self.greeting_frame = ctk.CTkFrame(self, border_width=2, corner_radius=10, border_color="black")
        self.greeting_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.greeting_frame.grid_columnconfigure(0, weight=1)

        self.greeting = ctk.CTkLabel(self.greeting_frame, text=f"Welcome {user}!", font=("Arial", 40))
        self.greeting.grid(row=0, column=0, padx=10, pady=10)

        # Body frame
        self.body_frame = ctk.CTkFrame(self, border_width=2, corner_radius=10, border_color="black")
        self.body_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")  # Allow expansion
        self.body_frame.columnconfigure(0, weight=1)  # Allow the first column to expand horizontally
        self.body_frame.columnconfigure(1, weight=1)  # Allow the second column to expand horizontally
        self.body_frame.rowconfigure(0, weight=0)  # Static row for transactions label
        self.body_frame.rowconfigure(1, weight=1)  # Allow the weekly_report_frame row to expand

        self.transactions_label = ctk.CTkLabel(self.body_frame, text=f"Total Transactions: {self.num_transactions} ", font=("Arial", 30))
        self.transactions_label.grid(row=0, column=0, padx=10, pady=10)

        self.news_frame = ctk.CTkFrame(self.body_frame, border_width=2, corner_radius=10, border_color="black")
        self.news_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")  # Allow expansion inside body_frame
        self.news_frame.grid_columnconfigure(0, weight=1)
        self.news_frame.grid_rowconfigure(0, weight=1)

        self.weekly_report_frame = ctk.CTkScrollableFrame(self.body_frame, border_width=2, corner_radius=10, border_color="black")
        self.weekly_report_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.weekly_report_frame.grid_columnconfigure(0, weight=1)  # Expand contents horizontally
        self.weekly_report_label = ctk.CTkLabel(self.weekly_report_frame, text="Weekly Report", font=("Arial", 24))
        self.weekly_report_label.grid(row=0, column=0, padx=10, pady=10)
        self.generate_weekly_report()

        self.news = ctk.CTkLabel(self.news_frame, text=f"News: \n {self.news_info} ", font=("Arial", 24), anchor="w", wraplength=300)
        self.news.grid(row=0, column=0, padx=10, pady=10)
        
    def generate_weekly_report(self):
        end_date = datetime.now()
        start_date = end_date - timedelta(weeks=1)

        filtered_transactions = [
            transaction for transaction in self.app.transactions
            if start_date <= datetime.strptime(transaction.date, "%m/%d/%Y") <= end_date
        ]

        if not filtered_transactions:
            print("No transactions found for the past week.")
            return

        cumulative_earnings = 0
        df = pd.DataFrame([{
            "Transaction": t.getTransactionText(),
            "Cumulative Earnings": (cumulative_earnings := cumulative_earnings + (float(t.getIncome()) - float(t.getExpenses()))),
            "Date": datetime.strptime(t.getDate(), "%m/%d/%Y")
        } for t in filtered_transactions])

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=df, x="Date", y="Cumulative Earnings", ax=ax, label="Cumulative Earnings", errorbar=None)
        ax.set_title("Cumulative Earnings Over the Past Week")

        ax.xaxis.set_major_formatter(DateFormatter("%m-%d %A"))
        ax.xaxis.set_major_locator(AutoDateLocator())
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        fig.tight_layout(pad=3.0)

        canvas = FigureCanvasTkAgg(fig, master=self.weekly_report_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
