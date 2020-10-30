'''
	https://hwasun-knowledge.tistory.com/81
	
	lambda: 익명 함수
	
	# 일반 함수
	def test(x, y):
		return x+y
		
	# 람다식
	lambda x,y: x+y
'''

# 변수 만들어 호출하기
out = lambda x,y: x + y
print( out(1,2) )

# 함수포인터 처럼 사용하기
out = (lambda x,y: x + y)(1,2)
print(out)

# 함수의 인자로 넣기
lam = lambda x,y: x+y
def print_xy(lam):
	result = lam
	print(result)

print_xy(lam(1,2))

# 함수 호출시 인자로 넣기
def print_xy(func, hello):
	print(func(1,2))
	print(hello)
	
print_xy((lambda x,y: x+y), "hello")


# 람다식의 대표적인 예는 map 내장함수이다
list(map(lambda x,y: x+y, [1,2,3]))
l = map(int, [i for i in range(1,10)])
print(l)


