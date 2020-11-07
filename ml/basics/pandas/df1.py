'''
https://saltyzun.tistory.com/m/9
'''

import numpy as np
import pandas as pd

# 1. 데이터 프레임 생성하기
print('=========================================== 1. 데이터 프레임 생성하기')
data = {'가격':[1000,2100,3000,700],
        '판매량':[20,40,35,60],
        '재고':[100,50,200,70]}

df = pd.DataFrame(data, index=['컵라면','커피','도시락','사탕'])
print('-------------------------------- df')
print(  df  )

# 2. 원하는 컬럼 데이터 조회하기
print('=========================================== 2. 원하는 컬럼 데이터 조회하기')
print('-------------------------------- df[''가격'']')
print(  df['가격']  )

print('-------------------------------- df[[''가격'',''판매량'']]')
print(  df[['가격','판매량']]  )

# 3. 원하는 Row 그룹 데이터 조회하기
print('=========================================== 3. 원하는 Row 그룹 데이터 조회하기')
print('-------------------------------- df.loc[''사탕'']')
print(  df.loc['사탕']  )
print('-------------------------------- df.loc[[''컵라면'', ''도시락'']]')
print(  df.loc[['컵라면', '도시락']]  )
print('-------------------------------- df.loc[''커피'':] # 인덱스 slicing')
print(  df.loc['커피':]  ) # 인덱스 slicing
print('')
print('-------------------------------- df.iloc[0]')
print(  df.iloc[0]  )
print('-------------------------------- df.iloc[[0,2]]')
print(  df.iloc[[0,2]]  )
print('-------------------------------- df.iloc[0:3] # 인덱스 slicing')
print(  df.iloc[0:3]  ) # 인덱스 slicing
print('')
print('-------------------------------- df.loc[''커피'':,[''가격'',''판매량'']] # ''커피''부터 끝까지 row group의 ''가격'', ''판매량'' 정보''')
print(  df.loc['커피':,['가격','판매량']]  ) # '커피'부터 끝까지 row group의 '가격', '판매량' 정보
print('-------------------------------- df.iloc[0:,1:3] # index number 0 부터 끝까지 row group의 column 1 ~ 2 정보')
print(  df.iloc[0:,1:3]  ) # index number 0 부터 끝까지 row group의 column 1 ~ 2 정보

