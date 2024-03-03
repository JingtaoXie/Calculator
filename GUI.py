# noinspection PyUnresolvedReferences
import tkinter as tk


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.create_widgets()

    def create_widgets(self):
        # 创建显示结果的文本框
        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(self.root, textvariable=self.result_var, font=('Arial', 14), bd=10, insertwidth=4,
                                     width=15, justify='left')
        self.result_entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]
        for text, row, col in buttons:
            button = tk.Button(self.root, text=text, font=('Arial', 14), padx=20, pady=10,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)
#
    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            self.result_var.set(self.result_var.get() + text)
#
#
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()