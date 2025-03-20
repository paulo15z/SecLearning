print("calmo")


#rede neural

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')
plt.rcParams['figure.figsize'] = (10,8)


def get_linear_curve(x, w, b=0, noise_scale=0):
    return w*x + b + noise_scale*np.random.randn(x.shape[0])

x = np.arange(-10, 30.1, 0.5)
Y = get_linear_curve(x, 1.8, 32, noise_scale=2.5)

print(plt.scatter(x, Y))
plt.xlabel('C', fontsize=20)
plt.ylabel('F', fontsize=20)

plt.show() 

#MODELO






#aprendizado

#algoritmo de detecção

#algoritmo de resposta a incidente

#interface?