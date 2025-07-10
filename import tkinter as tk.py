import tkinter as tk
from tkinter import ttk, messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("400x500")
        self.root.configure(bg='#2c3e50')
        
        # Variables
        self.current = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        # History
        self.history = []
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Display frame
        display_frame = tk.Frame(main_frame, bg='#34495e', relief=tk.RAISED, bd=2)
        display_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Current calculation display
        self.display = tk.Entry(display_frame, textvariable=self.result_var, 
                               font=('Arial', 20), justify='right', 
                               bg='#ecf0f1', fg='#2c3e50', bd=0, 
                               state='readonly', relief=tk.FLAT)
        self.display.pack(fill=tk.X, padx=10, pady=10)
        
        # History display
        history_label = tk.Label(display_frame, text="History:", 
                                font=('Arial', 10), bg='#34495e', fg='white')
        history_label.pack(anchor='w', padx=10)
        
        self.history_text = tk.Text(display_frame, height=3, 
                                   font=('Arial', 9), bg='#ecf0f1', 
                                   fg='#2c3e50', bd=0, state='disabled')
        self.history_text.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg='#2c3e50')
        buttons_frame.pack(fill=tk.BOTH, expand=True)
        
        # Button configuration
        button_style = {
            'font': ('Arial', 14, 'bold'),
            'width': 5,
            'height': 2,
            'relief': tk.RAISED,
            'bd': 1
        }
        
        # Button colors
        number_color = '#3498db'
        operator_color = '#e74c3c'
        function_color = '#f39c12'
        special_color = '#9b59b6'
        
        # Create buttons
        buttons = [
            ('C', 0, 0, special_color, self.clear),
            ('CE', 0, 1, special_color, self.clear_entry),
            ('⌫', 0, 2, special_color, self.backspace),
            ('÷', 0, 3, operator_color, lambda: self.add_to_current('/')),
            
            ('√', 1, 0, function_color, self.sqrt),
            ('x²', 1, 1, function_color, self.square),
            ('1/x', 1, 2, function_color, self.reciprocal),
            ('×', 1, 3, operator_color, lambda: self.add_to_current('*')),
            
            ('7', 2, 0, number_color, lambda: self.add_to_current('7')),
            ('8', 2, 1, number_color, lambda: self.add_to_current('8')),
            ('9', 2, 2, number_color, lambda: self.add_to_current('9')),
            ('-', 2, 3, operator_color, lambda: self.add_to_current('-')),
            
            ('4', 3, 0, number_color, lambda: self.add_to_current('4')),
            ('5', 3, 1, number_color, lambda: self.add_to_current('5')),
            ('6', 3, 2, number_color, lambda: self.add_to_current('6')),
            ('+', 3, 3, operator_color, lambda: self.add_to_current('+')),
            
            ('1', 4, 0, number_color, lambda: self.add_to_current('1')),
            ('2', 4, 1, number_color, lambda: self.add_to_current('2')),
            ('3', 4, 2, number_color, lambda: self.add_to_current('3')),
            ('=', 4, 3, special_color, self.calculate),
            
            ('±', 5, 0, function_color, self.toggle_sign),
            ('0', 5, 1, number_color, lambda: self.add_to_current('0')),
            ('.', 5, 2, number_color, lambda: self.add_to_current('.')),
        ]
        
        # Create and place buttons
        for text, row, col, color, command in buttons:
            if text == '=':
                # Make equals button span 2 rows
                btn = tk.Button(buttons_frame, text=text, bg=color, fg='white',
                               command=command, **button_style)
                btn.grid(row=row, column=col, rowspan=2, sticky='nsew', padx=1, pady=1)
            else:
                btn = tk.Button(buttons_frame, text=text, bg=color, fg='white',
                               command=command, **button_style)
                btn.grid(row=row, column=col, sticky='nsew', padx=1, pady=1)
        
        # Configure grid weights
        for i in range(6):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
            
        # Bind keyboard events
        self.root.bind('<Key>', self.key_press)
        self.root.focus_set()
    
    def add_to_current(self, char):
        if self.current == "Error":
            self.current = ""
        self.current += char
        self.result_var.set(self.current)
    
    def clear(self):
        self.current = ""
        self.result_var.set("0")
    
    def clear_entry(self):
        if self.current:
            self.current = self.current[:-1]
            self.result_var.set(self.current if self.current else "0")
    
    def backspace(self):
        if self.current:
            self.current = self.current[:-1]
            self.result_var.set(self.current if self.current else "0")
    
    def calculate(self):
        try:
            if self.current:
                # Replace display operators with Python operators
                expression = self.current.replace('×', '*').replace('÷', '/')
                result = eval(expression)
                
                # Add to history
                self.add_to_history(f"{self.current} = {result}")
                
                self.current = str(result)
                self.result_var.set(self.current)
        except:
            self.result_var.set("Error")
            self.current = "Error"
    
    def sqrt(self):
        try:
            if self.current:
                num = float(self.current)
                if num < 0:
                    raise ValueError("Cannot take square root of negative number")
                result = math.sqrt(num)
                self.add_to_history(f"√{num} = {result}")
                self.current = str(result)
                self.result_var.set(self.current)
        except:
            self.result_var.set("Error")
            self.current = "Error"
    
    def square(self):
        try:
            if self.current:
                num = float(self.current)
                result = num ** 2
                self.add_to_history(f"{num}² = {result}")
                self.current = str(result)
                self.result_var.set(self.current)
        except:
            self.result_var.set("Error")
            self.current = "Error"
    
    def reciprocal(self):
        try:
            if self.current:
                num = float(self.current)
                if num == 0:
                    raise ValueError("Cannot divide by zero")
                result = 1 / num
                self.add_to_history(f"1/{num} = {result}")
                self.current = str(result)
                self.result_var.set(self.current)
        except:
            self.result_var.set("Error")
            self.current = "Error"
    
    def toggle_sign(self):
        try:
            if self.current and self.current != "0":
                num = float(self.current)
                result = -num
                self.current = str(result)
                self.result_var.set(self.current)
        except:
            pass
    
    def add_to_history(self, calculation):
        self.history.append(calculation)
        if len(self.history) > 3:  # Keep only last 3 calculations
            self.history.pop(0)
        
        self.history_text.config(state='normal')
        self.history_text.delete(1.0, tk.END)
        self.history_text.insert(tk.END, '\n'.join(self.history))
        self.history_text.config(state='disabled')
    
    def key_press(self, event):
        """Handle keyboard input"""
        key = event.char
        if key.isdigit():
            self.add_to_current(key)
        elif key in '+-*/':
            if key == '*':
                self.add_to_current('×')
            elif key == '/':
                self.add_to_current('÷')
            else:
                self.add_to_current(key)
        elif key == '.':
            self.add_to_current('.')
        elif key == '\r':  # Enter key
            self.calculate()
        elif key == '\b':  # Backspace
            self.backspace()
        elif key == 'c' or key == 'C':
            self.clear()

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()