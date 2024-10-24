import tkinter as tk 
from tkinter import ttk

Janela = tk.Tk()
Janela.resizable = False
Janela.title = "Robux DEVEX Calculator."

Rate = 0.0035 # USD 

Currencies = {
    "BRL": Rate * 5.69,
    "USD": Rate * 1,
    "YEN": Rate * 152.85,
    "EURO": Rate * 0.93,
}

def RobuxConvert():
    Prompt = RobuxInsert.get()
    try:
        Currency = _CurrencySel.get()
        Calc =  Currencies[Currency] * int(Prompt)
        
        Converted.config(text=f"{Currency}: {Calc}")
        
    except:
        print("Error!")

_RobuxInsert = tk.Label(Janela, text="Type the Robux Amount", width=20, height=3)
RobuxInsert = tk.Entry(Janela)

_CurrencyList = list(Currencies.keys())
_CurrencySel = ttk.Combobox(Janela, values=_CurrencyList)
CurrencySel = tk.Label(Janela, text="Select a currency")
CurrencySel.grid(row=3,column=1)
_CurrencySel.grid(row=3,column=2)

_RobuxInsert.grid(row=2,column=1)
RobuxInsert.grid(row=2,column=2)

Converted = tk.Label(Janela, text="(Insert)", width=20, height=3)
Converted.grid(row= 5, column=2)

Convert = tk.Button(Janela, text="Convert Robux", command=RobuxConvert)
Convert.grid(row= 6, column=2)

Janela.mainloop()