import threading 
import customtkinter as ctk
from PIL import Image, ImageTk
import os
from controller import get_chatbot_response as chatbot_response_controller
import time

'''
This class creates a help window for the user to be able to learn how to use
Pynancial Pro

'''

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
        self.create_toggle_button("Help bot (Llama A.I.)", self.toggle_helpbot_frame)

        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.grid(row=3, column=0, padx=10, pady=10, sticky="esw")
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(1, weight=1)


        self.overview_text = ctk.CTkLabel(self.content_frame, text="", font=("Arial", 16), wraplength=400)
        self.overview_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")

        self.image_label = ctk.CTkLabel(self.content_frame, text="")
        self.image_label.grid(row=1, column=0, padx=10, pady=10, sticky="new")

        self.user_input = ctk.CTkEntry(self.content_frame, width=400)
        self.submit_button = ctk.CTkButton(self.content_frame, text="Submit Question", command=self.fetch_response)

    def create_toggle_button(self, text, command):
        button = ctk.CTkButton(self.buttons_frame, text=text, command=command)
        button.pack(padx=5, pady=5, fill='x')

    def toggle_overview(self):
        self.clear_content_frame()
        self.overview_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")
        self.image_label.grid(row=1, column=0, padx=10, pady=10, sticky="new")
        self.overview_text.configure(text="This is the main overview. Here you can find general information about the application and its features. You can also find a detailed explanation of each feature by clicking on the corresponding buttons in Help. If you have any questions or need help, please feel free to contact us. Pynancial Pro is designed to help you manage your finances more effectively and efficiently. We hope you enjoy using it!")
        self.image_label.configure(image='')  # Clear any displayed image

    def toggle_home_frame(self):
        self.clear_content_frame()
        self.overview_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")
        self.image_label.grid(row=1, column=0, padx=10, pady=10, sticky="new")
        self.overview_text.configure(text="The home display is designed to offer a simple summary of your use of Pynancial Pro. It displays the total number of transactions you have added, any features recently updated or added, and a graph displaying a summary of your transactions over the last week. From the home menu every other tab is available to for you to explore, and if you leave it, you may return to it simply by clicking the Pynancial Pro logo in the top left corner.")
        self.display_image(os.path.join(os.getcwd(), "Images", "Help_Images", "Home_image.png"))

    def toggle_createtransaction_frame(self):
        self.clear_content_frame()
        self.overview_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")
        self.image_label.grid(row=1, column=0, padx=10, pady=10, sticky="new")
        self.overview_text.configure(text="After clicking the “Create Transaction” button, on the side bar, you will be taken to a menu allowing you to add any number of transactions to Pynancial Pro. In the textbox beneath the “Enter your transaction” prompt, you may add a transaction description, we recommend that your transaction description is as descriptive as possible. Beneath the “Enter income” and “Enter expenses” prompts, include and income or expenses for your transaction to be saved for later. To track expenses over time, enter a date under the “Enter date of transaction prompt.” It is essential to make sure that the date in stored in the format mm/dd/yyyy.")
        self.display_image(os.path.join(os.getcwd(), "Images", "Help_Images", "CreateTransaction_image.png"))

    def toggle_viewtransactions_frame(self):
        self.clear_content_frame()
        self.overview_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")
        self.image_label.grid(row=1, column=0, padx=10, pady=10, sticky="new")
        self.overview_text.configure(text="The View Transactions tab will allow you to view all transactions you have added to Pynancial Pro. If you wish to remove a transaction selected the checkbox next to the desired transaction and click the delete button in the lower right corner. If you wish to order transactions for easier viewing, click the header above them. The “ID” header will sort transactions into the order initially entered, the “Report” header alphabetically by the description provided on creation, the “Income” header by income from greatest to least, the “Expenses” by expenses from greatest to least, and the date by oldest to newest. Lastly there is the search function which allows you to search for an entry by the text description, sorting matching entries to the top.")
        self.display_image(os.path.join(os.getcwd(), "Images", "Help_Images", "ViewTransactions_image.png"))    

    def toggle_statistics_frame(self):
        self.clear_content_frame()
        self.overview_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")
        self.image_label.grid(row=1, column=0, padx=10, pady=10, sticky="new")
        self.overview_text.configure(text="The statistics window provides an interface to generate a graphical summary of incomes and expenses over either a week, a month, or a year using the “Select Time Range” dropdown menu. Graphs can be further customized to include just income and expenses or net earnings or cumulative earnings from the “Select Graph Type” dropdown. After selecting your desired time frame and graph type, clicking the “Generate Graph” button to create your graphic.")
        self.display_image(os.path.join(os.getcwd(), "Images", "Help_Images", "Statistics_image.png"))

    def toggle_helpbot_frame(self):
        self.clear_content_frame()
        self.overview_text.configure(text="Please provide your query or question below, and I will assist you based on your questions.")
        self.user_input.grid(row=0, column=0, padx=10, pady=10, sticky="new")
        self.submit_button.grid(row=1, column=0, padx=10, pady=10, sticky="new")
        self.overview_text.grid(row=2, column=0, padx=10, pady=10, sticky="new")

    def display_image(self, image_path):
        image = Image.open(image_path)
        image = image.resize((600, 300), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo
    '''
    def fetch_response(self):
        user_input = self.user_input.get()
        self.overview_text.configure(text="Loading, Please wait while I fetch the response...")
        response = chatbot_response_controller(user_input)
        print(response)
        self.overview_text.configure(text=response)'
    '''
    '''
    def get_chatbot_response(self):
        threading.Thread(target=self.fetch_response, daemon=True).start()
    '''
    def fetch_response(self):
        user_input = self.user_input.get()
        self.overview_text.configure(text="Loading, Please wait while I fetch the response...")
        def chatbot_response():
            try:
                # Get the full response from the chatbot
                response = chatbot_response_controller(user_input)
                if isinstance(response, dict) and "error" in response:
                    self.overview_text.configure(text=response["error"])
                else:
                    self.typing_effect(response)  # Use the typing effect for the full response
            except Exception as e:
                self.overview_text.configure(text="An error occurred while fetching the response. Please try again later.")
                
        threading.Thread(target=chatbot_response, daemon=True).start()

    def typing_effect(self, text):
        current_text = self.overview_text.cget("text")
        for char in text:
            current_text += char
            self.overview_text.configure(text=current_text)
            self.overview_text.update_idletasks()
            time.sleep(0.03)

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.grid_forget()
