import pandas as pd

df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
 }, index = [0,1,2,3])

df2 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7'],
    'D': ['D4', 'D5', 'D6', 'D7']
 }, index = [4,5,6,7])

df3 = pd.DataFrame({
    'A': ['A8', 'A9', 'A10', 'A11'],
    'B': ['B8', 'B9', 'B10', 'B11'],
    'C': ['C8', 'C9', 'C10', 'C11'],
    'D': ['D8', 'D9', 'D10', 'D11']
 }, index = [8,9,10,11])

print(df1)
print(df2)
print(df3)

result = pd.concat([df1, df2, df3])
print(result)

result = pd.concat([df1, df2, df3], keys=['x', 'y', 'z'])
print(result)

# 특별히 concat 명령에 keys 옵션으로 구분할 수 있다.
# 이렇게 key 지정된 구분은 다중 index가 되어서 level을 형성하게 된다. 이를 확인하면
print(result.index)

print(result.index.get_level_values(0))
print(result.index.get_level_values(1))


df4 = pd.DataFrame({
    'B' : ['B2', 'B3', 'B6', 'B7'],
    'D' : ['D2', 'D3', 'D6', 'D7'],
    'F' : ['F2', 'F3', 'F6', 'F7'],
}, index = [2,3,6,7])

result = pd.concat([df1, df4], axis=1)  # axis: 병합하고자 하는 방향 (0:위, 1:오른쪽)
print(df1)
print(df4)
print(result)

result2 = pd.concat([df1, df4], axis=0) # axis: 병합하고자 하는 방향 (0:위, 1:오른쪽)
print(result2)


result = pd.concat([df1, df4], axis=1, join='inner')
print(result)
