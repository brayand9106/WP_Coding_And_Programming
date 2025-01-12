import customtkinter as ctk

'''
This frame creates a view transactions environment that allows the user
to review all transactions done
'''

class ViewTransactionsFrame(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)  # Ensure widgets fill the width