
class InputOne(Exception):
	def __init__(self):
		super().__init__("1 입력됨")
		
class InputTwo(Exception):
	def __init__(self):
		super().__init__("2 입력됨")

class InputThree(Exception):
	def __init__(self):
		super().__init__("3 입력됨")


while True:
	n = input('숫자 입력: ')
	assert n == int(0), "n은 0이 아님"

	try:
		if int(n) == 1:
			raise InputOne
		elif int(n) == 2:
			raise InputTwo
		elif int(n) == 3:
			raise InputThree
			
		print('입력값은: ', float(n))
	except Exception as e:
		print("예외 발생: ", e)
	else:
		print('예외 없음')
		break
	finally:
		print('------------------- finally')
		