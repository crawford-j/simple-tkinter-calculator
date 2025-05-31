# A basic calculator built with Python and Tkinter that performs addition, subtraction, multiplication, and division. 
# This project is designed to help me deepen my understanding of Python programming and GUI development using the Tkinter library. 
import tkinter as tk

def handle_press():
    return

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.resizable(width = False, height = False)
window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 5)
window.columnconfigure(0, weight = 3)
window.columnconfigure(1, weight = 1)
window.minsize(300, 400)

# Create frames for the calculator
frm_display = tk.Frame(window)

frm_nums = tk.Frame(window)
for i in range(4):
    frm_nums.rowconfigure(i, weight = 5)
for j in range(3):
    frm_nums.columnconfigure(j, weight = 4)

frm_operators = tk.Frame(window)
for i in range(5):
    frm_operators.rowconfigure(i, weight = 4)
frm_operators.columnconfigure(0, weight = 1)

# Create result box that displays numbers being entered
lbl_display = tk.Label(frm_display, relief = tk.SUNKEN, text = "", anchor = "e")

# Create and place number Buttons within number Frame
num_labels = ["7", "8", "9",
              "4", "5", "6",
              "1", "2", "3",
              "C", "0", "."]
for i, label in enumerate(num_labels):
    btn = tk.Button(frm_nums, text = label, relief = tk.RAISED, font = ('Arial', 12, 'bold'))
    btn.config(command = lambda x = label: handle_press(x))
    row = i // 3
    col = i % 3
    btn.grid(row = row, column = col, sticky = "nesw")

# Create and place Buttons for operators within operator Frame
operator_labels = ["+", "-", "x", "÷", "="]
for i, label in enumerate(operator_labels):
    btn = tk.Button(frm_operators, text = label, relief = tk.RAISED, font = ('Arial', 12, 'bold'))
    btn.config(command = lambda x = label: handle_press(x))
    row = i
    col = 0
    btn.grid(row = row, column = col, sticky = "nesw")

# Place display label in diplay frame
lbl_display.pack(fill = tk.BOTH, expand = True)

# Place Frames within Window
frm_display.grid(row = 0, column = 0, columnspan = 2, sticky = "nesw")
frm_nums.grid(row = 1, column = 0, sticky = 'nesw')
frm_operators.grid(row = 1, column = 1, sticky = "nesw")

window.mainloop() 

