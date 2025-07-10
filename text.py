import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Visual Calculator")
root.geometry("300x400")

# Entry widget to display the expression/result
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# Function to update expression in entry box
def press(key):
    entry.insert(tk.END, key)

# Function to clear entry
def clear():
    entry.delete(0, tk.END)

# Function to evaluate expression
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Create buttons
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                  command=equal).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, width=22, height=2, font=('Arial', 18),
                  command=clear).grid(row=row, column=col, columnspan=4)
    else:
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                  command=lambda key=text: press(key)).grid(row=row, column=col)

# Start the application
root.mainloop()
