import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 11)
y = x**2


plt.subplot(2,2,1)
plt.plot(x,y,'r')

plt.subplot(2,2,2)
plt.plot(x,y,'g')

plt.subplot(2,2,3)
plt.plot(x,y,'b')

plt.subplot(2,2,4)
plt.plot(x,np.exp(x),'y')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()


plt.show()
