# A basic calculator built with Python and Tkinter that performs addition, subtraction, multiplication, and division. 
# This project is designed to help me deepen my understanding of Python programming and GUI development using the Tkinter library. 
import tkinter as tk

num1 = ""
num2 = ""
operator = ""

def calculate():
    global num1, num2, operator
    num2 = float(lbl_display.cget("text"))
    num1 = float(num1)
    match operator:
        case "+":
            answer = num1 + num2
        case "-":
            answer = num1 - num2
        case "x":
            answer = num1 * num2
        case "÷":
            answer = num1 / num2
    if float(answer).is_integer():
        lbl_display.config(text = str(int(answer)))
    else:
        lbl_display.config(text = str(answer))
    num1 = ""
    num2 = ""
    return

def handle_press(key):
    global num1, num2, operator
    curr = lbl_display.cget("text")
    # Number
    if key.isnumeric():
        lbl_display.config(text = curr + key)
    # Clear
    elif key == "C":
        num1 = ""
        num2 = ""
        operator = ""
        lbl_display.config(text = "")
    # Decimal point
    elif key == ".":
        if "." in lbl_display.cget("text"):
            return
        else:
            lbl_display.config(text = curr + key)
    # Main operators
    elif key in ["+", "-", "x", "÷"]:
        if num1 == "":
            operator = key
            num1 = lbl_display.cget("text")
            lbl_display.config(text = "")
        else:
            return
    # Equals
    elif key == "=":
        calculate()

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
lbl_display = tk.Label(frm_display, relief = tk.SUNKEN, text = "", font = ('Arial', 12, 'bold'), anchor = "e")

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

