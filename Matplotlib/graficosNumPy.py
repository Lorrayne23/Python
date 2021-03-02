
import numpy as np
from pylab import *
import matplotlib as mpl

plt.scatter(np.arange(50), np.random.randn(50))
plt.show()

#Plot e Scatter
fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax1.plot(np.random.randn(50),color='red')

ax2=fig.add_subplot(1,2,2)
ax2.scatter(np.arange(50),np.random.randn(50))
plt.show()

#Plots diversos
_, ax = plt.subplots(2,3)
ax[0,1].plot(np.random.randn(50),color='green',linestyle = '-')
ax[1,0].hist(np.random.randn(50))
ax[1,2].scatter(np.arange(50),np.random.randn(50),color='red')
plt.show()

# Color Map
alpha = 0.7
phi_ext = 2 * np.pi * 0.5

def ColorMap(phi_m, phi_p):
    return ( + alpha - 2 * np.cos(phi_p)*cos(phi_m) - alpha * np.cos(phi_ext - 2*phi_p))

phi_m = np.linspace(0, 2*np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
X,Y = np.meshgrid(phi_p, phi_m)
Z = ColorMap(X, Y).T

fig, ax = plt.subplots()

p = ax.pcolor(X/(2*np.pi), Y/(2*np.pi), Z, cmap=cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max())
cb = fig.colorbar(p, ax=ax)
plt.show()