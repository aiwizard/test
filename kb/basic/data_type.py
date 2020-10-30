'''
tuple = ()	# (1, 2 ...)
list = []		# [ 1, 2, 3 ... ]
dict = {}		# {'key': 'value', ...}
'''

################################################# tuple
'''
count()
index()
'''

# 변경되지 않는 데이터의 집합
a = ('a', 'b' ,'c')
b = ('D' , 'F')
print(a+b)	#	('a', 'b', 'c', 'D', 'F')	
print(b*2)	#	('D', 'F', 'D', 'F')

a = ('Chevrolet', 'KIA', 'Mercedes')  
print (a[0])		# Chevrolet
print (a[1:2])	# ('KIA',) 1 위치 전에 자르고 2(즉 3번째) 이전에 자른다.
print (a[:2])	# ('Chevrolet', 'KIA') 2(즉 3번째 위치) 이후 것은 모두 자른다.

print (a.count('KIA'))		# 1
print (a.index('Mercedes'))	# 2

################################################# list
'''
	list.append(값)	# 리스트의 끝에 값을 추가
	list.insert(idx, 값)	# 리스트의 특정 위치에 아이템 추가
	list.extend(리스트)	# list를 list 에 concatenation
	list.copy()		# 리스트 복사	
	list.remove(값)	# '값'을 삭제
	list.pop(index)	# 인덱스에 위치한 값을 리턴하면서 삭제 (인자가 없으면 맨 뒤 값을 pop)
	list.clear()		# 모두 삭제
	list.count()		# 특정 아이템 갯수
	list.index()		# 특정 아이템이 index 리턴
	list.reverse()	# 역순
	list.sort(reverse=True)	# 내림차순
'''

my_list = [1, 2, 3, "a", "a", "b", "c"]

print (my_list[0:2])	#0번째 부터 2-1번째 까지
print (my_list[1:])	#1번째 부터 끝까지
print("--------------------------------")
cnt = my_list.count("a")
print ('my_list에서 a 는 {} 개입니다'.format(cnt))
print("--------------------------------")

################################################# dictionary
'''
	items()	# 아이템들을 list 형식으로 변환
	keys()		# key를 list 형식으로 변환
	values()	# value를 list 형식으로 변환
	clear()	# 모든 요소들을 없앤다
	copy()		# 복제된 값을 반환
	get()		# 특정 key의 value값을 반환
'''

bizcard = {}
bizcard["name"] = "Joshua"
bizcard["phone"] = "55512345678"
bizcard["company"] = "ai2learn"

print (bizcard)
print (bizcard["phone"])

# 출력>>
#	{'name': 'Joshua', 'phone': '55512345678', 'company': 'ai2learn'}   
#	55512345678


test = { 'model' : 'Camaro', 'maker': 'Chevrolet', 'year': 2020}

print (test.items())
print (test.keys()) 
print (test.values())
print (test.get('year'))

# 출력>>
#	dict_items([('model', 'Camaro'), ('maker', 'Chevrolet'), ('year', 2020)])
#	dict_keys(['model', 'maker', 'year'])
#	dict_values(['Camaro', 'Chevrolet', 2020])
#	2020

