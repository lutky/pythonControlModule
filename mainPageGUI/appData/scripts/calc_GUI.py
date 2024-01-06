import tkinter as tk

def button_click(number):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current + str(number))

def button_clear():
    entry_display.delete(0, tk.END)

def button_add():
    first_number = entry_display.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = float(first_number)
    entry_display.delete(0, tk.END)

def button_subtract():
    first_number = entry_display.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = float(first_number)
    entry_display.delete(0, tk.END)

def button_multiply():
    first_number = entry_display.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = float(first_number)
    entry_display.delete(0, tk.END)

def button_divide():
    first_number = entry_display.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = float(first_number)
    entry_display.delete(0, tk.END)

def button_equal():
    second_number = entry_display.get()
    entry_display.delete(0, tk.END)
    if math_operation == "addition":
        entry_display.insert(tk.END, f_num + float(second_number))
    elif math_operation == "subtraction":
        entry_display.insert(tk.END, f_num - float(second_number))
    elif math_operation == "multiplication":
        entry_display.insert(tk.END, f_num * float(second_number))
    elif math_operation == "division":
        try:
            entry_display.insert(tk.END, f_num / float(second_number))
        except ZeroDivisionError:
            entry_display.insert(tk.END, "Error: Division by zero")

# Handle the window closure event
def on_closing():
    # Clean up any resources or perform any necessary actions
    window.destroy()  # Destroy the window to exit the application

# Create the main window
window = tk.Tk()
window.title("Calculator Application")
window.configure(bg="#434343")

# Create the display entry field
entry_display = tk.Entry(window, width=20, font=("Arial", 16))
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create number buttons
button_1 = tk.Button(window, text="1", padx=20, pady=10, command=lambda: button_click(1), bg="#A9A9A9")
button_2 = tk.Button(window, text="2", padx=20, pady=10, command=lambda: button_click(2), bg="#A9A9A9")
button_3 = tk.Button(window, text="3", padx=20, pady=10, command=lambda: button_click(3), bg="#A9A9A9")
button_4 = tk.Button(window, text="4", padx=20, pady=10, command=lambda: button_click(4), bg="#A9A9A9")
button_5 = tk.Button(window, text="5", padx=20, pady=10, command=lambda: button_click(5), bg="#A9A9A9")
button_6 = tk.Button(window, text="6", padx=20, pady=10, command=lambda: button_click(6), bg="#A9A9A9")
button_7 = tk.Button(window, text="7", padx=20, pady=10, command=lambda: button_click(7), bg="#A9A9A9")
button_8 = tk.Button(window, text="8", padx=20, pady=10, command=lambda: button_click(8), bg="#A9A9A9")
button_9 = tk.Button(window, text="9", padx=20, pady=10, command=lambda: button_click(9), bg="#A9A9A9")
button_0 = tk.Button(window, text="0", padx=20, pady=10, command=lambda: button_click(0), bg="#A9A9A9")

# Create operator buttons
button_add = tk.Button(window, text="+", padx=20, pady=10, command=button_add, bg="#FF0000")
button_subtract = tk.Button(window, text="-", padx=20, pady=10, command=button_subtract, bg="#FF0000")
button_multiply = tk.Button(window, text="*", padx=20, pady=10, command=button_multiply, bg="#FF0000")
button_divide = tk.Button(window, text="/", padx=20, pady=10, command=button_divide, bg="#FF0000")

# Create other buttons
button_equal = tk.Button(window, text="=", padx=46, pady=10, command=button_equal, bg="#FF0000")
button_clear = tk.Button(window, text="Clear", padx=36, pady=10, command=button_clear, bg="#A9A9A9")

# Arrange buttons on the grid
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_divide.grid(row=4, column=3)

button_equal.grid(row=5, column=0, columnspan=4)

# Close program gracefully and clean up resources
window.protocol("WM_DELETE_WINDOW", on_closing)