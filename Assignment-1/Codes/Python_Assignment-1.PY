# Code by Jupally Sriram
# May 08,2022
# To plot the graph of n^2 -20n -1500 = 0.

import numpy as np
from math import sqrt
from matplotlib import pyplot as plt


def f(n):
     return (n**2-20*n-1500)


n = []
y = []
with open("Data.txt","r") as fp:
    for lines in fp :
        n.append(lines[0:8])
        y.append(lines[10:-1])
n.remove(n[0])
y.remove(y[0])
for i in range(len(n)):
    n[i] = float(n[i])
    y[i] = float(y[i])
plt.grid()
plt.plot(n,y,color="red",label = 'y=f(x)')
x_values = np.linspace(-40,60,1000)
x_axis = np.zeros(1000)
plt.plot(x_values,x_axis,color="blue",label = "X-Axis")  # Can be considered as X-Axis

# coeffs are the coefficients of the quadratic equation.
coeffs = [1,-20,-1500]
# Roots are roots of the quadratic equation.
Roots = np.roots(coeffs)

plt.plot(Roots[0],0,marker='o',markersize=4,markerfacecolor='Black',markeredgecolor='Black')
plt.plot(Roots[1],0,marker='o',markersize=4,markerfacecolor='Black',markeredgecolor='Black')
plt.annotate((Roots[0],0),(Roots[0],0),(51.5,2))
plt.annotate((Roots[1],0),(Roots[1],0),(-29,2))
plt.legend()

plt.savefig("../Figures/Figure_1.png")
plt.show()
