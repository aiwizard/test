import pandas as pd
import re

print('원본')
data = pd.DataFrame(['1,000.00', '2,000.00'])
print(data)

# 문자열 치환하기 - 1. 정규식 용
print('---------------------------------------------')
print('# 문자열 치환하기 - 1. 정규식 이용')
d = re.sub(",", "", data[0][0])
#print('type: ', type(pd.to_numeric(d))
print('결과')
print(d)

# 문자열 치환하기 - 2. apply 와 lambda 를 활용한 dataframe 에 적용하기
print('----------------------------------------------')
print('# 문자열 치환하기 - 2. apply와 lambda 를 활용한 dataframe 에 적용하기')
data[0] = data[0].apply(lambda x:re.sub(",","",x))
print(data[0])
print('----------------------------------------------')

print('data')
print(data)

print('len(data): ', len(data))
