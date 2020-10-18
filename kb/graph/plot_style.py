import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 11)
y1 = x**2
y2 = x+1
y3 = x*2
y4 = x*5

'''
x, y
marker='o'
color='r', color='green', color='0.8', color='#ff0000'
linestyle='-', '--', '-.', ';'

'''
plt.plot(x, y1, 'm:', label='y1')
plt.plot(x, y2, linewidth=5, label='y2')
plt.plot(x, y3, linestyle='-.', label='y3', color='green')
plt.plot(x, y4, '#ff000f', label='y4')

plt.legend()
plt.show()
