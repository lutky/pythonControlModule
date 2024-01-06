# File: app.py
# Version: 1.00
# Author: ALu
# Date: December 17, 2023
# Description: This is the main script that runs the program
#
# Usage:
# - Run this script by executing 'python app.py' in your terminal.
#
# Dependencies:
# - This script requires Python 3.7 or higher.
#
# Revision History
#	V1.00 - initial commit

# Import the required libraries
import tkinter as tk

# Function to switch to Page 2 (Loadable Scripts)
def show_page2():
    global main_frame  # Define main_frame as a global variable
    
    # Change the background color of the main frame to light red
    main_frame.config(bg='lightcoral')

    # Pack the main frame and sidebar frame
    main_frame.pack(side='left', fill='both', expand=True)

    # Forget the Page 1 frame to hide it
    page1_frame.pack_forget()

    # Pack the Page 2 frame to show it
    page2_frame.pack(side='left', fill='both', expand=True)
    
    # Set the background color for Page 2
    page2_frame.config(bg='lightblue')

    # Create a nested frame within Page 2 with a border of 20 pixels
    nested_frame = tk.Frame(page2_frame, bg='white', bd=20, relief="solid")
    nested_frame.pack(fill='both', expand=True)

    # Label within the nested frame
    nested_label = tk.Label(nested_frame, text="Frame 2 Nested Window")
    nested_label.pack()

# Function to switch to Page 1 (Main Page)
def show_page1():
    global main_frame  # Define main_frame as a global variable
    
    main_frame.config(bg='lightblue')  # Change background color to light blue
    main_frame.pack(side='left', fill='both', expand=True)
    sidebar_frame.pack(side='right', fill='y')
    page1_frame.pack(side='left', fill='both', expand=True)
    page2_frame.pack_forget()

# Function to close the application when the window is closed
def on_closing():
    root.destroy()

# Function to determine the value of the current bottom sidebar radio button selection
def on_radio_button_select():
    selected_value.set(radio_button1.get())
def on_radio_button_select():
    selected_value.set(radio_button2.get())
def on_radio_button_select():
    selected_value.set(radio_button3.get())

# Create the main window
root = tk.Tk()
root.title("LutkenhouseControl")
root.geometry("600x400")
root.protocol("WM_DELETE_WINDOW", on_closing)

# Create the bottom bar and buttons
bottom_bar = tk.Frame(root, bg="lightblue", height=30)
bottom_bar.pack(side="bottom", fill="x")

# Variable to store the selected radio button's value
selected_value = tk.StringVar()

# Create three radio buttons and add them to the radio_frame
radio_button1 = tk.Radiobutton(bottom_bar, bg= 'cyan', text="Option 1", variable=selected_value, value="Option 1", command=on_radio_button_select)
radio_button2 = tk.Radiobutton(bottom_bar, bg= 'blue', text="Option 2", variable=selected_value, value="Option 2", command=on_radio_button_select)
radio_button3 = tk.Radiobutton(bottom_bar, bg= 'blue', text="Option 3", variable=selected_value, value="Option 3", command=on_radio_button_select)

# Set a default selected value if needed
selected_value.set("Option 1")

radio_button1.pack(side=tk.LEFT, padx = 10)
radio_button2.pack(side=tk.LEFT, padx = 10)
radio_button3.pack(side=tk.LEFT, padx = 10)


# Sidebar frame and buttons
sidebar_frame = tk.Frame(root, bg='gray', width=100)
sidebar_frame.pack(side='right', fill='y')

page1_button = tk.Button(sidebar_frame, text="Page 1", command=show_page1)
page2_button = tk.Button(sidebar_frame, text="Page 2", command=show_page2)
page1_button.pack(fill='x')
page2_button.pack(fill='x')

#Create the main content area  
#content = tk.Frame(root)
#content.pack(side="top", fill="both", expand=True)

# Main frame
main_frame = tk.Frame(root, bg='green')
main_frame.pack(side='left', fill='both', expand=True)

# Page 1 frame and widgets
page1_frame = tk.Frame(main_frame)
page1_label = tk.Label(page1_frame, text="This is Page 1")
page1_label.pack()

# Page 2 frame and widgets with a background color
page2_frame = tk.Frame(main_frame, bg='lightblue')

# Show Page 1 initially
show_page1()

root.mainloop()

# Function to handle radio button selection
def on_radio_button_select():
    print("Selected option:", selected_value.get())


