import tkinter as tk 

Janela = tk.Tk()
Janela.resizable = False
Janela.title = "Robux DEVEX Calculator."

Rate = 0.0035 # USD 

def RobuxConvert():
    Prompt = RobuxInsert.get()
    try:
        Calc = Rate * int(Prompt)
        
        Converted.config(text=f"USD: {Calc}")
        
    except:
        print("Error!")

_RobuxInsert = tk.Label(Janela, text="Type the Robux Amount", width=20, height=3)
RobuxInsert = tk.Entry(Janela)

_RobuxInsert.grid(row=2,column=1)
RobuxInsert.grid(row=2,column=2)

Converted = tk.Label(Janela, text="USD: (Insert)", width=20, height=3)
Converted.grid(row= 4, column=2)

Convert = tk.Button(Janela, text="Convert Robux to USD", command=RobuxConvert)
Convert.grid(row= 3, column=2)

Janela.mainloop()