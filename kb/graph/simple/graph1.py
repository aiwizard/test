import numpy as np
import matplotlib.pyplot as plt

#arr = np.random.randint(0, 32767, size=50000)
arr_uniform = np.random.rand(5000)
arr_gaussian = np.random.randn(5000)

plt.figure()
plt.xlabel('x')
plt.ylabel('y')
plt.title('test')
#plt.plot(arr_uniform)
plt.plot(arr_gaussian)
plt.show()
