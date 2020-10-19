'''
https://island-developer.tistory.com/71
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3*np.pi, 0.1)

y_sin = np.sin(x)
y_cos = np.cos(x)
k = np.random.rand(len(y_sin))


#plt.figure()

plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.plot(x, k)

plt.xlabel('x label')
plt.ylabel('y label')
plt.title('test')
plt.legend(['Sine', 'Cosine'], 'k')

plt.show()
