import customtkinter as ctk
from PIL import Image, ImageTk
import os

class HelpFrame(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_rowconfigure(0, weight=1)  # Weight for the top row
        self.grid_columnconfigure(0, weight=1)
        
        self.help_label = ctk.CTkLabel(self, text="Help", font=("Arial", 24))
        self.help_label.grid(row=0, column=0, padx=10, pady=10, sticky="new")


        self.buttons_frame = ctk.CTkFrame(self)
        self.buttons_frame.grid(row=2, column=0, padx=10, pady=10, sticky="new")

        self.create_toggle_button("Overview", self.toggle_overview)
        self.create_toggle_button("Home Window", self.toggle_home_frame)
        self.create_toggle_button("Create Transaction Window", self.toggle_createtransaction_frame)
        self.create_toggle_button("View Transactions Window", self.toggle_viewtransactions_frame)
        self.create_toggle_button("Statistics Window", self.toggle_statistics_frame)

        self.overview_text = ctk.CTkLabel(self, text="", font=("Arial", 16), wraplength=400)
        self.overview_text.grid(row=3, column=0, padx=10, pady=10, sticky="new")

        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.grid(row=4, column=0, padx=10, pady=10, sticky="new")

    def create_toggle_button(self, text, command):
        button = ctk.CTkButton(self.buttons_frame, text=text, command=command)
        button.pack(padx=5, pady=5, fill='x')

    def toggle_overview(self):
        self.overview_text.configure(text="This is the main overview. Here you can find general information about the application and its features. You can also find a detailed explanation of each feature by clicking on the corresponding buttons in Help. If you have any questions or need help, please feel free to contact us. Pynancial Pro is designed to help you manage your finances more effectively and efficiently. We hope you enjoy using it!")
        self.image_label.configure(image='')  # Clear any displayed image

    def toggle_home_frame(self):
        self.overview_text.configure(text="The home display is designed to offer a simple summary of your use of Pynancial Pro. It displays the total number of transactions you have added, any features recently updated or added, and a graph displaying a summary of your transactions over the last week. From the home menu every other tab is available to for you to explore, and if you leave it, you may return to it simply by clicking the Pynancial Pro logo in the top left corner.")
        self.display_image(os.path.join(os.getcwd(), "Images", "Help_Images", "Home_image.png"))

    def toggle_createtransaction_frame(self):
        self.overview_text.configure(text="After clicking the “Create Transaction” button, on the side bar, you will be taken to a menu allowing you to add any number of transactions to Pynancial Pro. In the textbox beneath the “Enter your transaction” prompt, you may add a transaction description, we recommend that your transaction description is as descriptive as possible. Beneath the “Enter income” and “Enter expenses” prompts, include and income or expenses for your transaction to be saved for later. To track expenses over time, enter a date under the “Enter date of transaction prompt.” It is essential to make sure that the date in stored in the format mm/dd/yyyy.")
        self.display_image(os.path.join(os.getcwd(), "Images", "Help_Images", "CreateTransaction_image.png"))

    def toggle_viewtransactions_frame(self):
        self.overview_text.configure(text="The View Transactions tab will allow you to view all transactions you have added to Pynancial Pro. If you wish to remove a transaction selected the checkbox next to the desired transaction and click the delete button in the lower right corner. If you wish to order transactions for easier viewing, click the header above them. The “ID” header will sort transactions into the order initially entered, the “Report” header alphabetically by the description provided on creation, the “Income” header by income from greatest to least, the “Expenses” by expenses from greatest to least, and the date by oldest to newest. Lastly there is the search function which allows you to search for an entry by the text description, sorting matching entries to the top.")
        self.display_image(os.path.join(os.getcwd(), "Images", "Help_Images", "ViewTransactions_image.png"))
    

    def toggle_statistics_frame(self):
        self.overview_text.configure(text="The statistics window provides an interface to generate a graphical summary of incomes and expenses over either a week, a month, or a year using the “Select Time Range” dropdown menu. Graphs can be further customized to include just income and expenses or net earnings or cumulative earnings from the “Select Graph Type” dropdown. After selecting your desired time frame and graph type, clicking the “Generate Graph” button to create your graphic.")
        self.display_image(os.path.join(os.getcwd(), "Images", "Help_Images", "Statistics_image.png"))

    def display_image(self, image_path):
        image = Image.open(image_path)
        image = image.resize((600, 300), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo
