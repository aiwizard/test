'''
https://dan-di.tistory.com/10
'''

import matplotlib.pyplot as plt
#%matplotlib inline

plt.figure()
plt.plot([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0])
plt.show()



import numpy as np
t = np.arange(0, 12, 0.01)
y = np.sin(t)

plt.figure()
plt.plot(t,y)
plt.show()



plt.figure( figsize = (10, 6) )
plt.plot(t,y)
plt.grid()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sin wave')
plt.show()



plt.figure( figsize = (10, 6) )
plt.plot(t, np.sin(t))
plt.plot(t, np.cos(t))
plt.grid()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sin wave')
plt.show()



plt.figure( figsize = (10, 6) )
plt.plot(t, np.sin(t), label='sin')
plt.plot(t, np.cos(t), label='cos')
plt.grid()
plt.legend()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sin wave')
plt.show()



# lw 옵션으로 선의 굵기 지정, color 옵션으로 선의 색상 지정
plt.figure( figsize = (10, 6) )
plt.plot(t, np.sin(t), lw=3, label='sin')
plt.plot(t, np.cos(t), 'r', label='cos')
plt.grid()
plt.legend()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sin wave')
plt.show()



t = [0,1,2,3,4,5,6]
y = [1,4,5,8,9,5,3]
plt.figure( figsize = (10, 6) )
plt.plot(t,y,color='green')
plt.show()


# linestyle : 선의 스타일, marker : 마킹
# markerfacecolor 옵션과 markersize 옵션으로 마커의 크기와 색상도 지정
t = [0,1,2,3,4,5,6]
y = [1,4,5,8,9,5,3]
plt.figure( figsize = (10, 6) )
plt.plot(t,y,color='green', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=12)
plt.show()


# 선을 그리는 plot 명령 외에 점만 그리는 scatter 명령
t = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([9,8,7,9,8,3,2,4,3,4])
plt.figure( figsize = (10, 6) )
plt.scatter(t,y)
plt.show()


# 선을 그리는 plot 명령 외에 점만 그리는 scatter 명령
t = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([9,8,7,9,8,3,2,4,3,4])
plt.figure( figsize = (10, 6) )
plt.scatter(t,y, marker='>')
plt.show()



# x축 값인 t에 따라 색상을 바꾸는 color map을 지정
# 이 때, s 옵션은 마커의 크기
colormap = t

plt.figure( figsize = (10, 6) )
plt.scatter(t, y, s=50, c=colormap, marker='>')
plt.colorbar()
plt.show()



# numpy의 랜덤변수 함수를 이용해서 데이터 세 개를 만들어보자.
# 이 때 loc 옵션으로 평균값과 scale 옵션으로 표준편차도 지정하자.
#   ex) s1 : 평균값이 0이고, 표준편차가 1인 0~1000 사이의 수들의 집합
s1 = np.random.normal(loc=0, scale=1, size=1000)
s2 = np.random.normal(loc=5, scale=0.5, size=1000)
s3 = np.random.normal(loc=10, scale=2, size=1000)

plt.figure( figsize = (10, 6) )
plt.plot(s1, label='s1')
plt.plot(s2, label='s2')
plt.plot(s3, label='s3')
plt.legend()
plt.show()



# 이것을 boxplot 으로도 표현
plt.figure( figsize = (10, 6) )
plt.boxplot((s1, s2, s3))
plt.grid()
plt.show()
