import tkinter as tk
import threading
import time

# Function to update GUI elements with values from secondary script
def update_gui():
    # Replace with code to update GUI elements based on shared variables
    # For example, label.config(text=shared_variable)
    label.config(text=f"Value: {shared_variable}")
    root.after(1000, update_gui)  # Update every 1 second

# Function to start a new thread for the secondary script
def start_secondary_script():
    global shared_variable
    shared_variable = 0  # Initialize shared variable

    def secondary_thread():
        global shared_variable
        while True:
            # Replace with code to update shared_variable in real-time
            shared_variable += 1
            time.sleep(1)

    secondary_thread = threading.Thread(target=secondary_thread)
    secondary_thread.daemon = True  # Thread will exit when the main script exits
    secondary_thread.start()
    update_gui()  # Start GUI update

# Create the main GUI window
root = tk.Tk()
root.title("Main Script")

# Create a label to display information from secondary script
label = tk.Label(root, text="")
label.pack()

# Create a button to start the secondary script
start_button = tk.Button(root, text="Start Secondary Script", command=start_secondary_script)
start_button.pack()

# Start the Tkinter main loop
root.mainloop()
