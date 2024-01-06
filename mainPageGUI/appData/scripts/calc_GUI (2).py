import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("400x300")  # Set the window size

# Create the sidebar
sidebar = tk.Frame(root, bg="lightgray", width=100)
sidebar.pack(side="left", fill="y")

# Create the content area
content = tk.Frame(root)
content.pack(side="top", fill="both", expand=True)

# Create the bottom bar
bottom_bar = tk.Frame(root, bg="lightblue", height=30)
bottom_bar.pack(side="bottom", fill="x")

# Add widgets to the sidebar, content area, and bottom bar as needed

# Start the tkinter main loop
root.mainloop()
