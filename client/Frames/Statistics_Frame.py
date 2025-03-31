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
        self.grid_columnconfigure(2, weight=1)  # Ensure widgets fill the width
        self.grid_rowconfigure(5, weight=1)  # Ensure the graph row expands

        self.label_time_range = ctk.CTkLabel(self, text="Select Time Range:")
        self.label_time_range.grid(row=0, column=1, padx=10, pady=10)

        self.time_range_var = ctk.StringVar(value="1 Week")
        self.time_range_menu = ctk.CTkOptionMenu(self, variable=self.time_range_var, values=["1 Week", "1 Month", "1 Year"])
        self.time_range_menu.grid(row=1, column=1, padx=10, pady=10)

        self.label_graph_type = ctk.CTkLabel(self, text="Select Graph Type:")
        self.label_graph_type.grid(row=2, column=1, padx=10, pady=10)

        self.graph_type_var = ctk.StringVar(value="Income/Expenses")
        self.graph_type_menu = ctk.CTkOptionMenu(self, variable=self.graph_type_var, values=["Income/Expenses", "Net Earnings", "Cumulative Earnings"], command=self.update_graph_chart_type)
        self.graph_type_menu.grid(row=3, column=1, padx=10, pady=10)

        self.graph_chart_type = ctk.StringVar(value="Line Graph")
        self.graph_chart_type_menu = ctk.CTkOptionMenu(self, variable=self.graph_chart_type, values=["Line Graph", "Pie Chart", "Double Bar Graph"])
        self.graph_chart_type_menu.grid(row=3, column=2, padx=(5,10), pady=10, sticky="w")

        self.generate_button = ctk.CTkButton(self, text="Generate Graph", command=self.generate_graph)
        self.generate_button.grid(row=4, column=1, padx=10, pady=10)

        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.canvas = None

    def update_graph_chart_type(self, selected_graph_type):
        '''Show the user which type of graph for income/expenses'''
        if selected_graph_type == "Income/Expenses":
            self.graph_chart_type_menu.configure(state="normal")
        else:
            self.graph_chart_type_menu.configure(state="disabled")

    def generate_graph(self):
        time_range = self.time_range_var.get()
        graph_type = self.graph_type_var.get()
        if graph_type == "Income/Expenses":
            graph_chart_type = self.graph_chart_type.get()
        else:
            graph_chart_type = None

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

        # Clear previous content in the scrollable_frame
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        if not filtered_transactions:
            print("No transactions found for the selected time range.")
            no_transactions_label = ctk.CTkLabel(self.scrollable_frame, text="No transactions to analyze for the given time period.", font=("Arial", 20))
            no_transactions_label.pack(expand=True)  # Center the label
            return

        if graph_type == "Income/Expenses":
            if graph_chart_type == "Pie Chart":
                self.generate_pie_chart(filtered_transactions)
                return
            elif graph_chart_type == "Double Bar Graph":
                self.generate_double_bar_graph(filtered_transactions)
                return

            df = pd.DataFrame([{
                "Transaction": t.getTransactionText(),
                "Income": t.getIncome(),
                "Expenses": t.getExpenses(),
                "Date": datetime.strptime(t.getDate(), "%m/%d/%Y")
            } for t in filtered_transactions])

            fig, ax = plt.subplots(figsize=(10, 6))
            sns.lineplot(data=df, x="Date", y="Income", ax=ax, label="Income", marker="o", errorbar=None)
            sns.lineplot(data=df, x="Date", y="Expenses", ax=ax, label="Expenses", marker="o", errorbar=None)
            ax.set_title("Income and Expenses Over Time")
        elif graph_type == "Net Earnings":
            df = pd.DataFrame([{
                "Transaction": t.getTransactionText(),
                "Net Earnings": t.getIncome() - t.getExpenses(),
                "Date": datetime.strptime(t.getDate(), "%m/%d/%Y")
            } for t in filtered_transactions])

            fig, ax = plt.subplots(figsize=(10, 6))
            sns.lineplot(data=df, x="Date", y="Net Earnings", ax=ax, label="Net Earnings", marker="o", errorbar=None)
            ax.set_title("Net Earnings Over Time")
        elif graph_type == "Cumulative Earnings":
            # Sort transactions by date
            filtered_transactions.sort(key=lambda t: datetime.strptime(t.getDate(), "%m/%d/%Y"))

            cumulative_earnings = 0
            df = pd.DataFrame([{
                "Transaction": t.getTransactionText(),
                "Cumulative Earnings": (cumulative_earnings := cumulative_earnings + (t.getIncome() - t.getExpenses())),
                "Date": datetime.strptime(t.getDate(), "%m/%d/%Y")
            } for t in filtered_transactions])

            # Group by date and keep the row with the highest cumulative earnings
            df = df.groupby("Date", as_index=False).max()

            fig, ax = plt.subplots(figsize=(10, 6))
            sns.lineplot(data=df, x="Date", y="Cumulative Earnings", ax=ax, label="Cumulative Earnings", marker="o", errorbar=None)
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


    def generate_pie_chart(self, transactions):
        """Generate a pie chart for income vs expenses."""
        total_income = sum(t.getIncome() for t in transactions)
        total_expenses = sum(t.getExpenses() for t in transactions)

        if total_income == 0 and total_expenses == 0:
            print("No data available for pie chart.")
            no_data_label = ctk.CTkLabel(self.scrollable_frame, text="No data available for pie chart.", font=("Arial", 20))
            no_data_label.pack(expand=True)
            return

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.pie([total_income, total_expenses], labels=["Income", "Expenses"], autopct="%1.1f%%", startangle=90)
        ax.set_title("Income vs Expenses")
        self.display_graph(fig)


    def generate_double_bar_graph(self, transactions):
        """Generate a double bar graph for income and expenses."""
        df = pd.DataFrame([{
            "Transaction": t.getTransactionText(),
            "Income": t.getIncome(),
            "Expenses": t.getExpenses(),
            "Date": datetime.strptime(t.getDate(), "%m/%d/%Y")
        } for t in transactions])

        if df.empty:
            print("No data available for double bar graph.")
            no_data_label = ctk.CTkLabel(self.scrollable_frame, text="No data available for double bar graph.", font=("Arial", 20))
            no_data_label.pack(expand=True)
            return
        
        df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d", errors="coerce")

        # Set the Date column as the index
        df.set_index("Date", inplace=True)

        # Plot the double bar graph
        fig, ax = plt.subplots(figsize=(10, 6))
        df[["Income", "Expenses"]].plot(kind="bar", ax=ax, width=0.8)
        # Explicitly set the x-axis ticks and labels
        ax.set_xticks(range(len(df.index)))  # Set tick positions
        ax.set_xticklabels(df.index.strftime("%Y-%m-%d"), rotation=45, ha="right")  # Format and rotate labels
        # Format the x-axis to display only the date
        ax.set_title("Income and Expenses Comparison")
        ax.set_xlabel("Date")
        ax.set_ylabel("Amount")

        # Adjust layout
        fig.tight_layout(pad=3.0)

        self.display_graph(fig)

    def display_graph(self, fig):
        """Display the generated graph in the scrollable frame."""
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(fig, master=self.scrollable_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill='both', expand=True)
