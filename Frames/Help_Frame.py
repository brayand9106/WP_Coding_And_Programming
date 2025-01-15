import customtkinter as ctk
from PIL import Image, ImageTk

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

        self.image_label = ctk.CTkLabel(self)
        self.image_label.grid(row=4, column=0, padx=10, pady=10, sticky="new")

    def create_toggle_button(self, text, command):
        button = ctk.CTkButton(self.buttons_frame, text=text, command=command)
        button.pack(padx=5, pady=5, fill='x')

    def toggle_overview(self):
        self.overview_text.configure(text="This is the main overview. Here you can find general information about the application and its features.")
        self.image_label.configure(image='')  # Clear any displayed image

    def toggle_home_frame(self):
        self.overview_text.configure(text="The home display is designed to offer a simple summary of your use of Pynancial Pro. It displays the total number of transactions you have added, any features recently updated or added, and a graph displaying a summary of your transactions over the last week. From the home menu every other tab is available to for you to explore, and if you leave it, you may return to it simply by clicking the Pynancial Pro logo in the top left corner.")
        self.display_image("../Images/Help_Images/Home_image.png")

    def toggle_createtransaction_frame(self):
        self.overview_text.configure(text="After clicking the “Create Transaction” button, on the side bar, you will be taken to a menu allowing you to add any number of transactions to Pynancial Pro. In the textbox beneath the “Enter your transaction” prompt, you may add a transaction description, we recommend that your transaction description is as descriptive as possible. Beneath the “Enter income” and “Enter expenses” prompts, include and income or expenses for your transaction to be saved for later. To track expenses over time, enter a date under the “Enter date of transaction prompt.” It is essential to make sure that the date in stored in the format mm/dd/yyyy.")
        self.display_image("../Images/Help_Images/CreateTransaction_image.png")

    def toggle_viewtransactions_frame(self):
        self.overview_text.configure(text="This is the View Transactions Frame. Here you can view all your transactions and filter them based on various criteria.")
        self.display_image("../Images/Help_Images/ViewTransactions_image.png")
    

    def toggle_statistics_frame(self):
        self.overview_text.configure(text="This is the Statistics Frame. Here you can generate and view various graphs based on your transactions.")
        self.display_image("../Images/Help_Images/Statistics_image.png")

    def display_image(self, image_path):
        image = Image.open(image_path)
        image = image.resize((400, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo
