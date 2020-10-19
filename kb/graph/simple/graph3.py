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

plt.subplot(2, 2, 1)
plt.plot(x, y_sin)
#plt.xlabel('x label')
#plt.ylabel('y label')
#plt.legend(['Sine'])
plt.title('Sine')

plt.subplot(2, 2, 2)
plt.plot(x, y_cos)
#plt.xlabel('x label')
#plt.ylabel('y label')
#plt.legend(['Cosine'])
plt.title('Cosine')

plt.subplot(2, 2, 3)
plt.plot(x, k)
#plt.xlabel('x label')
#plt.ylabel('y label')
#plt.legend(['k'])
plt.title('k')


plt.show()
