from datetime import datetime
import pytz
from random import randint
from cartao import CartaoCredito
from contacorrente import ContaCorrente

conta_Lira = ContaCorrente("Lira", "111.222.333-45", "Banco ITAU", "12932193")
cartao_Lira = CartaoCredito("Lira", conta_Lira)
print(cartao_Lira.conta_corrente.Numero)
print(cartao_Lira.conta_corrente.Cartoes[0].Numero)
print(conta_Lira.__dict__)

conta_maeLira = ContaCorrente("Beth", "222.333.444-55", "Banco INTER", "219312")

conta_Lira.ganharSalario(100)
conta_Lira.printarInfo()
conta_Lira.depositarDinheiro(35)
conta_Lira.depositarDinheiro(35)
conta_Lira.depositarDinheiro(35)
conta_Lira.printarInfo()
conta_Lira.consultar_historico_trans()

