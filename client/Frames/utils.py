from Frames.SignIn_Frame import SignInFrame

"""
This file contains utility functions which affect the entirety of the application
and its frames
"""

def recreate_frames(app):
    # Destroy existing frames if they exist
    for widget in app.winfo_children():
        widget.destroy()

    # Recreate the frames
    from main import mainWindow
    mainWindow(app, app.user)

def logout(app):
    # Clear user-specific data
    app.user = None
    app.transactions = []
    app.num_transactions = 0

    from main import mainWindow
    # Redirect to login screen
    for widget in app.winfo_children():
        widget.destroy()

    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(1, weight=0)
    app.grid_columnconfigure(1, weight=0)
    
    signInFrame = SignInFrame(app, mainWindow)
    signInFrame.grid(row=0, column=0, sticky="nsew")