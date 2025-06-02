# A basic calculator built with Python and Tkinter that performs addition, subtraction, multiplication, and division. 
# This project is designed to help me deepen my understanding of Python programming and GUI development using the Tkinter library. 
import tkinter as tk 

num1 = ""
num2 = ""
operator = ""

# Function to process calculations based on the operator chosen by the user
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

# Function to handle button presses
# String label of button passed in as parameter 
def handle_press(key):
    global num1, num2, operator, curr
    curr = lbl_display.cget("text")
    # Number
    if key.isnumeric():
        lbl_display.config(text = curr + key)

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
    # Percent
    elif key == "%":
        if curr:
            percent = float(curr) / 100
            if percent.is_integer():
                lbl_display.config(text = str(int(percent)))
            else:
                lbl_display.config(text = str(percent))
    # Clear
    elif key == "C":
        num1 = ""
        num2 = ""
        operator = ""
        lbl_display.config(text = "")
    # Change Sign
    elif key == "±":
        opposite = float(curr) * (-1)
        if opposite.is_integer():
            lbl_display.config(text = int(opposite))
        else:
            lbl_display.config(text = opposite)
    # Backspace
    elif key == "⌫":
        lbl_display.config(text = curr[:-1])
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
window.columnconfigure(0, weight = 1)
window.minsize(300, 400)

# Create frames for the calculator
frm_display = tk.Frame(window)

frm_buttons = tk.Frame(window)
for i in range(5):
    frm_buttons.rowconfigure(i, weight = 1)
for j in range(4):
    frm_buttons.columnconfigure(j, weight = 1)

# Create result box that displays numbers being entered
lbl_display = tk.Label(frm_display, relief = tk.SUNKEN, text = "", font = ('Arial', 20, 'bold'), anchor = "e")

# Create and place number Buttons within number Frame
labels = ["%", "C", "⌫", "+",
          "7", "8", "9", "-",
          "4", "5", "6", "x",
          "1", "2", "3", "÷",
          "±", "0", ".", "="]
for i, label in enumerate(labels):
    if i != 19:
        btn = tk.Button(frm_buttons, text = label, relief = tk.RAISED, font = ('Arial', 15, 'bold'))
    else:
        btn = tk.Button(frm_buttons, text = label, relief = tk.RAISED, font = ('Arial', 15, 'bold'), bg = "green")
    btn.config(command = lambda x = label: handle_press(x))
    row = i // 4
    col = i % 4
    btn.grid(row = row, column = col, sticky = "nesw")

# Place display label in diplay frame
lbl_display.pack(fill = tk.BOTH, expand = True)

# Place Frames within Window
frm_display.grid(row = 0, column = 0, columnspan = 2, sticky = "nesw")
frm_buttons.grid(row = 1, column = 0, sticky = 'nesw')

window.mainloop() 