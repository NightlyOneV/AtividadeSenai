import tkinter as tk
from tkinter import ttk

#Configuração da Janela
janela = tk.Tk()
janela.title('Cotação de Moedas')
janela.rowconfigure(0,weight=1)
janela.columnconfigure(0,weight=1)

#Funções
def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text='Cotação não encontrada')
    mensagem_cotacao.grid(row=2,column=0)
    if cotacao_moeda:
        mensagem_cotacao['text'] = f'Cotacão do {moeda_preenchida} é de {cotacao_moeda} reais'

def buscar_cotacoes():
    texto = caixa_texto.get('1.0',tk.END)
    lista_moedas = texto.split('\n')
    mensagem_cotacoes = []
    
    for item in lista_moedas:
        cotacao = dicionario_cotacoes.get(item)
        if cotacao:
            mensagem_cotacoes.append(f"{item}:{cotacao}")
    
    mensagem4.config(text="\n".join(mensagem_cotacoes))
        
dicionario_cotacoes = {
    'Dólar': 5.47,
    'Euro': 6.68,
    'Bitcoin': 20000
}

#Botão Multiplas Cotações
Botao_NCotacoes = tk.Button(text='Buscar Cotações', command=buscar_cotacoes)
Botao_NCotacoes.grid(row=5,column=1)

#ComboBox
moedas = list(dicionario_cotacoes.keys())
moeda = ttk.Combobox(janela,values=moedas)
moeda.grid(row=1, column=1)

#TextBox
caixa_texto = tk.Text( width= 10, height= 0)
caixa_texto.grid(row = 5, column=0, sticky='nswe')

#Mensagens
Mensagem = tk.Label(text='Sistema de Busca de Cotação de Moedas',bg='Black',fg='White')
Mensagem.grid(row=0,column=0,columnspan=2, sticky='NSEW')

Mensagem2 = tk.Label(text='Selecione a Moeda Desejada')
Mensagem2.grid(row=1,column=0)

Mensagem3 = tk.Label(text='Sistema de Cotação Múltipla',bg='Black',fg='White')
Mensagem3.grid(row=4, column= 0, columnspan= 2,sticky='NSEW')

mensagem4 = tk.Label(text="\n")
mensagem4.grid(row=6,column=1)

#Botão
botao = tk.Button(text='Buscar Cotação',command=buscar_cotacao)
botao.grid(row=2,column=1)

janela.mainloop()