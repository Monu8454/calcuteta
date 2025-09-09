import tkinter as tk

def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + button_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Window banate hain
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Input box
entry = tk.Entry(root, width=20, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: click(x) if x not in ['='] else calculate()
    tk.Button(root, text=button, width=5, height=2, command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(root, text="C", width=22, height=2, command=clear).grid(row=row_val, column=0, columnspan=4)

root.mainloop()
