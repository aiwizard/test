'''
https://blackhippo.tistory.com/18
	1. 왼쪽/오른쪽 정렬
	2. 0 으로 채우기
	3. 기타 표현
'''


print('------------------------------- 1. 왼쪽/오른쪽 정렬')
'''
	ljust(전체자리수) : 왼쪽 정렬
	rjust(전체자리수) : 오른쪽 정렬
'''

num1=10; num2=300; num3=50000

# 오른쪽 정렬
print(str(num1).rjust(5)) # 5칸 자리수 & 오른쪽 정렬
print(str(num2).rjust(5))
print(str(num3).rjust(5))
print()

# 왼쪽 정렬
print(str(num1).ljust(5))
print(str(num2).ljust(5))
print(str(num3).ljust(5))

print('------------------------------- 2. 빈 공간 0 으로 채움')
num1=5; num2=55; num3=555

# 은행번호표
print(str(num1).zfill(3))
print(str(num2).zfill(3))
print(str(num3).zfill(3))

print('------------------------------- 3. 기타')
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일 땐 앞에 + 표시, 음수일 땐 앞에 - 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 나머지 빈 칸은 _으로 채움
print("{0:_<10}".format(500))

# 3자리수 마다 콤마를 찍어주기
print("{0:,}".format(10000000))

# 3자리수 마다 콤마 & +,-부호도 붙이기
print("{0:+,}".format(10000000))
print("{0:+,}".format(-10000000))

# 3자리수 마다 콤마 & +,-부호 & 자릿수 확보한 후 빈 자리는 _로 채우기
print("{0:_<+30,}".format(10000000))

# 소수점을 특정 자리수까지만 표시
print("{0:.6f}".format(5/3))

print("\n\n")

