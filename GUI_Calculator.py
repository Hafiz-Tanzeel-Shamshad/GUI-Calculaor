import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x400")
        
        self.equation = tk.StringVar()
        self.expression = ""
        
        self.create_widgets()
    
    def create_widgets(self):
        entry = tk.Entry(self.root, textvariable=self.equation, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self.root, text=button, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        clear_button = tk.Button(self.root, text='Clear', padx=95, pady=20, font=('Arial', 18), command=self.clear)
        clear_button.grid(row=row_val, column=0, columnspan=4)
    
    def on_button_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.equation.set(result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
                self.equation.set("")
        else:
            self.expression += str(char)
            self.equation.set(self.expression)
    
    def clear(self):
        self.expression = ""
        self.equation.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
