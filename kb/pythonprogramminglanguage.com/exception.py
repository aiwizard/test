
print('------------------------------------------')

try:
  print(z)
except NameError:
  print("1 Variable z is not defined")
except:
  print("2 Another type of exception has occured")
finally:
  print("3 The 'try except' is finished")

print('------------------------------------------')

try:
  raise Exception("1 Exception is raised")
except NameError:
  print("2 Variable z is not defined")
except:
  print("333333333333")

print('------------------------------------------')
