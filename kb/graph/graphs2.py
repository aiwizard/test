import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,11)
y = x**2

# grid 와 x축,y축 범위 변경
plt.grid(True)
plt.xlim(0, 20)     # x limit
plt.ylim(0, 200)    # y limit
plt.plot(x, y)

plt.show()