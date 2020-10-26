# filter는 특정한 f(x)에 대해 bloolean값을 필터하여 뽑아낸다

# 음수를 제거하고자 할 때

def print_result(datalist, title):
	print(f'--------- %s' %(title))
	for item in datalist:
		print(item)
		
	print()


mylist = [-3, 5, 1, 2, -5, -4, 14]
print_result(mylist, '원본 리스트')

# filter 이용
result = filter(lambda a: a>0, mylist)
print_result(result, 'filter 이용한 양수 추출')

# 리스트 아이템 마다 비교해서 새로운 리스트를 만드는 방법
newdata = []
for elem in mylist:
    if elem>0:
        newdata.append(elem)

print_result(newdata, '기본 방법')


# 홀수 리스트로 한번에 뽑아내기
result = list(filter(lambda x: x%2, mylist))
print_result(result, '홀수 리스트 한 번에')

# 짝수 리스트 한번에 뽑아내기
result = list(filter(lambda x:x%2==0, mylist))
print_result(result, '짝수 리스트 한 번에')

