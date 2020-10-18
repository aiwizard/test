'''
ndarray 생성하기

https://seong6496.tistory.com/48
'''

import numpy as np

# np.array 함수로 생성
print('1---------------------------- np.array 함수로 생성')
x = np.array([1,2,3,4])
y = np.array([[2,3,4],[1,2,3]])
print(x.shape, x)
print(x.shape, y)
print()

# np.arange 함수로 생성
print('2---------------------------- np.arange 함수로 생성')
x1 = np.arange(1,10,2)
print(x1.shape, x1)
print()

# np.ones, np.zeros
print('3---------------------------- np.ones, np.zeros')
print('np.ones((3,5)):\n', np.ones((3,5))) #3행5열 모두 1로 
print('np.zeros((3,5)):\n', np.ones((3,5))) #3행5열 모두 0으로 
print('np.ones((2,3,5)):\n', np.ones((2,3,5))) #2x3행x5열 모두 1로
print()

# np.empty, np.full
print('4---------------------------- np.empty, np.full')
print('np.empty((4,4)):\n', np.empty((4,4)))  #초기값을 생성할 때 씁니다. 모든 값을 제로로 만들지 않으면서 필요한 초기값을 만든다
print('np.full((3,5),5):\n', np.full((3,5),5))    #모두 같은 값 5로 설정한다
print()

# np.eye, np.linspace
print('5---------------------------- np.eye, np.linspace')
print('np.eye(5):\n', np.eye(5))  # 단위 행렬 생성
print('np.linspace(1,10,4): ', np.linspace(1,10,4))    # 1~10 까지 4등분 결과 리턴. 이 함수는 1차원만 할 수 있다
print('np.linspace(2,3,5): ', np.linspace(2,3,5))    # 2~3 까지 5등분 결과 리턴. 이 함수는 1차원만 할 수 있다
print()

# np.reshape
print('6---------------------------- np.reshape')
x = np.arange(1,16)  # 1~15 까지 배열
x2 = x.reshape((3,5))    # 3x5 로 변경
print('x = np.arange(1,16): {}'.format(x))
print('x.reshape((3,5)):\n', x2)
print()
