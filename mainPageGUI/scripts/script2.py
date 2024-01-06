import tkinter as tk

# Function to switch to Page 1
def show_page1():
    main_frame.config(bg='lightblue')  # Change background color to light blue
    main_frame.pack(side='left', fill='both', expand=True)
    sidebar_frame.pack(side='right', fill='y')
    page1_frame.pack(side='left', fill='both', expand=True)
    page2_frame.pack_forget()
    
# Function to switch to Page 2
def show_page2():
    main_frame.config(bg='lightcoral')  # Change background color to light red
    main_frame.pack(side='left', fill='both', expand=True)
    sidebar_frame.pack(side='right', fill='y')
    page1_frame.pack_forget()
    page2_frame.pack(side='left', fill='both', expand=True)

# Create the main window
root = tk.Tk()
root.title("Page Switcher")
root.geometry("600x400")

# Sidebar frame and buttons
sidebar_frame = tk.Frame(root, bg='gray', width=100)
sidebar_frame.pack(side='right', fill='y')

page1_button = tk.Button(sidebar_frame, text="Page 1", command=show_page1)
page2_button = tk.Button(sidebar_frame, text="Page 2", command=show_page2)
page1_button.pack(fill='x')
page2_button.pack(fill='x')

# Main frame
main_frame = tk.Frame(root)
main_frame.pack(side='left', fill='both', expand=True)

# Page 1 frame and widgets
page1_frame = tk.Frame(main_frame)
page1_label = tk.Label(page1_frame, text="This is Page 1")
page1_label.pack()

# Page 2 frame and widgets
page2_frame = tk.Frame(main_frame)
page2_label = tk.Label(page2_frame, text="This is Page 2")
page2_label.pack()

# Show Page 1 initially
show_page1()

root.mainloop()