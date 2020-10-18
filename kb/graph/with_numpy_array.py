import numpy as np
import matplotlib.pyplot as plt

# ndarray 데이터로 그래프 그리기
x = np.linspace(0,10,11)
y1 = x**2
y2 = x*5
print(x)

plt.plot(x,y1)   #plot(선 그래프)
plt.scatter(x,y2)    #scatter (점 그래프)
plt.show()
