'''
에러발생의 위험이 있는 코드는 try 에
에러 발생시 실행하고픈 코드는 except 에
에러 미발생시 실행하고픈 코드는 else 에
에러 발생여부에 상관없이 실행하고픈 코드는 finally 에 작성
'''


print('\n------------------------------------------')

try:
  print('1 Hello world')			# 실행됨
except:
  print("2 An error occurred")
else:
  print("else")						# 실행됨
finally:
  print("4 Finally finished")	# 실행됨

print('\n------------------------------------------')

try:
  print(z)
except:
  print("2 An error occurred")	# 실행됨
else:
  print("else")
finally:
  print("4 Finally finished")	# 실행됨

print('\n------------------------------------------')

try:
  print(z)
except NameError:
  print("21 Variable z is not defined")	# 실행됨
except:
  print("2 An error occurred")
else:
  print("else")
finally:
  print("4 Finally finished")	# 실행됨

print('\n------------------------------------------')

try:
  #print('1 Hello world')
  #raise Exception("이런! 에러 발생")
  print(z)
except Exception as e:
  print(e)							# 실행됨
else:
  print("else")
finally:
  print("4 Finally finished")	# 실행됨

print('\n')

