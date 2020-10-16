'''
https://aigong.tistory.com/45
'''

import numpy as np

# hyperparameter 로 정수, tuple 형태의 array의 차원 혹은 shape (optional: 미입력시 1개의 값 리턴)

# 1. np.random.rand(d1, d2, ..., dn) : 0~1 사이의 값, uniform distribution (균일 또는 균등 분포) 값을 리턴
#    np.random.random 도 위와 동일
arr_u1 = np.random.rand(5)      # 1개 반환
arr_u2 = np.random.rand(1,5)    # 2차원 shape(1x5)  에 맞게 반환
arr_u3 = np.random.rand(2,3,5)  # 3차원 shape(2x3x5)에 맞게 반환
print(arr_u1)

# 2. np.random.randn(d1, d2, ..., dn) : 0~1 사이의 값, Normal(Gaussian) distribution (정규 또는 가우시안 분포) 리턴
arr_g1 = np.random.randn()      # 1개 반환
arr_g2 = np.random.randn(3)     # 3개 반환
arr_g3 = np.random.randn(3,2)   # 2차원 shape(3x2)에 맞게 반환
#print(arr_g1, arr_g2, arr_g3)

# 3. np.random.randint() : 정수값만 리턴, 파라미터는 반드시 1개 이상 필수
arr_n1 = np.random.randint(5)                   # 5 까지의 숫자 1개 반환
arr_n2 = np.random.randint(5, 10, size=7)       # 5~10 사이의 숫자를 7개 맞게 반환
arr_n3 = np.random.randint(5, 10, size=(3,2))   # 2차원 shape(3x2)에 맞게 반환
arr_n4 = np.random.randint(5, 10, size=7, dtype='int64')    # 반환할 data type 지정
#print(arr_n2)
