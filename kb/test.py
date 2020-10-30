
def test():
	print(x)				# NameError is occurred
	
	a = []
	a.append("aaa")
	a.append("bbb")
	str = a[5]			# IndexError is occurred

try:
	test()
except Exception as e:
	print(e)
else:
	print("There are no exceptions")
finally:
	print("Finally done")
	
