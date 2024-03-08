import tkinter as tk

def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + value)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

root = tk.Tk()
root.title("My Calculator")

display = tk.Entry(root, width=30, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0
for button_val in buttons:
    if button_val == '=':
        tk.Button(root, text=button_val, padx=40, pady=20, command=calculate).grid(row=row_val, column=col_val)
    elif button_val == 'C':
        tk.Button(root, text=button_val, padx=40, pady=20, command=lambda: display.delete(0, tk.END)).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button_val, padx=40, pady=20, command=lambda value=button_val: button_click(value)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
