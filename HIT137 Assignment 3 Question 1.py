# This simple interactive calculator Tkinter application incorporate Object-oriented programming concepts like multiple inheritance, multiple decorators, encapsulation, polymorphism, and method overriding.
#Encapsulation: Encapsulation involves bundling the data (attributes) and methods (functions) that operate on the data into a single unit (class). In our calculator application, we can encapsulate the calculator logic within a class.
#Polymorphism:  In our calculator application, we can implement polymorphism by defining different types of operations (addition, subtraction, multiplication, division) as methods that can be called based on user input.
#Method Overriding: In our calculator application, we can override methods for specific operations to customize their behavior.
#Multiple Inheritance: In our calculator application, we can create a class that inherits functionalities from multiple classes, such as a basic calculator class and a scientific calculator class.
#Multiple Decorators: In our calculator application, we can use decorators to add additional functionalities or validations to specific methods, like checking input values or logging operations.

# Display Entry: A text entry field at the top to show the result and input.
# Button Frame: A frame to hold all buttons, organized in a grid layout.
# Buttons: Number buttons (0-9) and operation buttons (+, -, *, /, =, C).
# Button Click Handling:
# 'C' clears the display.
# '=' evaluates the expression in the display using eval().
# Numbers and operations are appended to the current text in the display.
# Grid Configuration: Ensures buttons expand to fill available space.

import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("300x400")
        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Create display entry
        self.display = tk.Entry(self, textvariable=self.result_var, font=('Arial', 20), justify='right', bd=10, insertwidth=2)
        self.display.pack(fill=tk.BOTH, expand=True)

        # Create a frame for buttons
        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.BOTH, expand=True)

        # Create number buttons
        for i in range(9, -1, -1):
            btn = tk.Button(button_frame, text=str(i), command=lambda num=i: self.on_button_click(num), font=('Arial', 20), bd=1)
            btn.grid(row=(9-i)//3, column=(i-1)%3, sticky=tk.NSEW)

        # Create operation buttons
        operations = ['+', '-', '*', '/', '=', 'C']
        for idx, op in enumerate(operations):
            btn = tk.Button(button_frame, text=op, command=lambda symbol=op: self.on_button_click(symbol), font=('Arial', 20), bd=1)
            btn.grid(row=idx//2, column=3+idx%2, sticky=tk.NSEW)

        # Configure row and column weights for button frame
        for i in range(4):
            button_frame.rowconfigure(i, weight=1)
            button_frame.columnconfigure(i, weight=1)

    def on_button_click(self, value):
        current_text = self.result_var.get()

        if value == 'C':
            self.result_var.set('')
        elif value == '=':
            try:
                result = str(eval(current_text))
                self.result_var.set(result)
            except:
                self.result_var.set('Error')
        else:
            self.result_var.set(current_text + str(value))

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
