# O Pylab combina funcionalidades do pyplot com funcionalidades do Numpy
from pylab import *
import matplotlib as mpl
import matplotlib.pyplot as plt

x = linspace(0,5,10)
y = x ** 2
fig = plt.figure()

#Definindo os eixos
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y,'r')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Gráfico de Linha');
plt.show()


# Gráfico com 2 figuras
x = linspace(0,5,10)
y = x ** 2
fig = plt.figure()

axes1= fig.add_axes([0.1,0.1,0.8,0.8])#eixos da figura principal
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])#eixos da figura secundária

#Figura principal
axes1.plot(x,y,'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('Figura Principal')

# Figura Secundária
axes2.plot(x,y,'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('Figura Secundária')
plt.show()


# Gráficos em Paralelo
fig, axes = plt.subplots(nrows = 1, ncols = 2)
for ax in axes:
    ax.plot(x,y,'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Título')
    fig.tight_layout()
plt.show()
