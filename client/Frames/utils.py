def recreate_frames(app):
    # Destroy existing frames if they exist
    for widget in app.winfo_children():
        widget.destroy()

    # Recreate the frames
    from main import mainWindow
    mainWindow(app, app.user)