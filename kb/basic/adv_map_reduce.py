'''
	1. map: 특정한 f(x)를 적용하여 새롭게 값을 뽑아내는 것. (선형대수에서는 사상이라 한다)
			map_object = map(function, iterable)
					function: 함수
					iterable: 반복 가능한 객체
		
	2. reduce: 자료구조(list,tuple) 를 연산을 통해서 단 하나의 값으로 만드는 함수
'''

################################################## map
##### 기본 방법
mylist = [2, 3, 4, 5] # 여기에 있는 값을 제곱을 하여 하나씩 뽑아내보자.
map_obj = map(lambda x: x**2, mylist)
#next(map_obj)	# 하나씩 next 한다

#for i in map_obj:
#	print(i)


#### filter와 map을 함꼐 사용하여 풀어야 하는 문제
mylist = [ 2, 3, -5, 6, -2, 1, -10]

##### 양수를 골라내 제곱한 값을 리스트 리턴
a = list(map(lambda x: x**2 , filter(lambda y: y>0, mylist)))
#for i in a:
#	print(i)

################################################## reduce
#### 리스트 최대 요소 구하기
from functools import reduce
mylist = [3,6,8,-10,2,1, 100, 50, 46, -47]
result = reduce(lambda x,y : x if x>y else y, mylist)	#(삼차다항식이용)
#print(result)


#### 문자수 세기
'''
	i =["a", "b", "a", "b", "b", "a", "c", "a"]가 주어졌을 때
	dic ={'a':4, 'b':3, 'c':1} ---->크롤링해서 좋아요 혹은 싫어요 핸들링 할 때 사용
'''
from functools import reduce
li =["a", "b", "a", "b", "b", "a", "c", "a"]
result  = reduce(lambda dic,cha : dic.update({cha : dic.get(cha,0)+1}) or dic, li, {})
print(result)

