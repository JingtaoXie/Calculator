import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.creat_content()

    def creat_content(self):
        self.content = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.content, font=('Arial', 14), bd=10, insertwidth=4,
                              width=20, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('AC', 1, 0, 1), ('+/-', 1, 1, 1), ('%', 1, 2, 1), ('/', 1, 3, 1),
            ('7', 2, 0, 1), ('8', 2, 1, 1), ('9', 2, 2, 1), ('*', 2, 3, 1),
            ('4', 3, 0, 1), ('5', 3, 1, 1), ('6', 3, 2, 1), ('-', 3, 3, 1),
            ('1', 4, 0, 1), ('2', 4, 1, 1), ('3', 4, 2, 1), ('+', 4, 3, 1),
            ('0', 5, 0, 2), ('.', 5, 2, 1), ('=', 5, 3, 1),
        ]

        for text, row, column, span in buttons:
            padx_value = 30 if text != '0' else 80
            button = tk.Button(self.root, text=text, font=('Arial', 14), padx=padx_value, pady=10,
                               command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=column, columnspan=span)

    def button_click(self, text):
        if self.content.get() == "0" or self.content.get() == "Error":
            self.content.set("")
        if text == "AC":
            self.content.set("0")
        elif text == "%":
            result = float(self.content.get()) / 100
            self.content.set(result)
        elif text == "+/-":
            content = self.content.get()
            if content[0] == '-':
                result = content[1:]
            else:
                result = "-" + content
            self.content.set(result)
        elif text == "=":
            try:
                result = eval(self.content.get())
                self.content.set(result)
            except Exception as e:
                self.content.set("Error")
        else:
            self.content.set(self.content.get() + text)


root = tk.Tk()
app = App(root)
root.mainloop()