import matplotlib.pyplot as plt
import numpy as np 

venda_meses = np.random.randint(1000,3000,50)
meses = np.arange(1,51)

plt.plot(meses, venda_meses, color="red")
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.axis([0,50,0, max(venda_meses)+200])
plt.show()