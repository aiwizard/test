'''
https://infograph.tistory.com/212
'''

import pandas as pd

data = [
    [100, 100, 55],
    [90, 90, 85],
    [80,100,80],
    [80,70,100],   #제일 뒤에 여분의 콤마가 있어도 에러가 아님
]

df = pd.DataFrame(data)
print(df)


print('\n\n---------------------------------')
과목 = ['국어', '영어', '수학']
이름 = ['김유신', '이순신', '홍길동', '트럼프']

df = pd.DataFrame(data, index=이름, columns=과목)

print(df)
print(df.index)
print(df.columns)
print(df.values)  #DataFrame의 data값 출력

print('\n\n---------------------------------')
tmp = {'지능': ['aaa','bbb','ccc'], '지능2': ['aaa2','bbb2','ccc2'] }
df = pd.DataFrame(tmp)
print(df)

