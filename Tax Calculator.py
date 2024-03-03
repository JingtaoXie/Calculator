
import tkinter as tk

#Add a list to record all previous results, then can use it to get the result back.
result_record=[]


#a function to do the maths logic
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        result_record.append(result)
        result_label.config(text=f"Result: {result}")
    except Exception as e:
        result_label.config(text="Error")


def clear():
    entry.delete(0, tk.END)

def lastresult():
    clear()
    entry.insert(tk.END, result_record[-1])


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("280x500")
root.resizable(False, False)

entry = tk.Entry(root, width=20, font=('Arial', 14, 'bold'))
entry.grid(row=0, column=0, columnspan=4, pady=10,sticky="nsew")

button_clear=tk.Button(root, text="Reset", font=('Arial', 14, 'bold'),command=clear)
button_clear.grid(row=1,column=0,columnspan=5,sticky="nsew")

button_lastresult=tk.Button(root, text="Last Result", font=('Arial', 14, 'bold'),command=lastresult)
button_lastresult.grid(row=2,column=0,columnspan=5,sticky="nsew")

button_taxrate1=tk.Button(root, text="SB", font=('Arial', 14, 'bold'),command=lambda:entry.insert(tk.END,0.105))
button_taxrate1.grid(row=3,column=0,columnspan=2)

button_taxrate2=tk.Button(root, text="S", font=('Arial', 14, 'bold'),command=lambda:entry.insert(tk.END,0.175))
button_taxrate2.grid(row=3,column=2,columnspan=2)

button_taxrate3=tk.Button(root, text="SH", font=('Arial', 14, 'bold'),command=lambda:entry.insert(tk.END,0.30))
button_taxrate3.grid(row=4,column=0,columnspan=2)

button_taxrate4=tk.Button(root, text="ST", font=('Arial', 14, 'bold'),command=lambda:entry.insert(tk.END,0.33))
button_taxrate4.grid(row=4,column=2,columnspan=2)

button_taxrate5=tk.Button(root, text="SA", font=('Arial', 14, 'bold'),command=lambda:entry.insert(tk.END,0.39))
button_taxrate5.grid(row=5,column=2,columnspan=2)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

rows = 6
columns = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, font=('Arial', 12,'bold'), command=lambda btn=button: entry.insert(tk.END, btn) if btn != '=' else calculate()).grid(row=rows, column=columns)
    columns += 1
    if columns > 3:
        columns = 0
        rows += 1


result_label = tk.Label(root, text="Result: ", font=('Arial', 14))
result_label.grid(row=rows, column=0, columnspan=4,sticky="nsew")


note1 = tk.Label(root, font=('Arial', 10, 'bold'), text="SB($14000 or less)")
note2 = tk.Label(root, font=('Arial', 10, 'bold'), text="S(Between $14001 and 48000)")
note3 = tk.Label(root, font=('Arial', 10, 'bold'), text="SH(Between $48001 and 70000)")
note4 = tk.Label(root, font=('Arial', 10, 'bold'), text="ST(Between $70001 and 180000)")
note5 = tk.Label(root, font=('Arial', 10, 'bold'), text="SA(more than $180000)")
note1.grid(row=11, column=0, columnspan=4, sticky="nsew")
note2.grid(row=12, column=0, columnspan=4, sticky="nsew")
note3.grid(row=13, column=0, columnspan=4, sticky="nsew")
note4.grid(row=14, column=0, columnspan=4, sticky="nsew")
note5.grid(row=15, column=0, columnspan=4, sticky="nsew")





root.mainloop()