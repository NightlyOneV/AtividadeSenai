import tkinter as tk 
from tkinter import ttk

Janela = tk.Tk()

var_promocoes = tk.IntVar()
var_privacidade = tk.IntVar()

check_promocoes = tk.Checkbutton(Janela, text="Receber Promoções", variable=var_promocoes)
var_privacidade = tk.Checkbutton(Janela, text="Aceito os termos de uso e privacidade", variable=var_privacidade)

check_promocoes.grid(row=1,column=1)
var_privacidade.grid(row=2,column=1)

def enviar():
    print(var_promocoes.get())


Botao_enviar = tk.Button(Janela, text="Enviar", command=enviar)
Botao_enviar.grid(row=3,column=1)


Janela.mainloop()