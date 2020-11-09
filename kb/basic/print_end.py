
import time

for i in range(10):
    print(i, end="\r")
	time.sleep(0.5)

for i in range(10):
	print('\r', i, end='')
	time.sleep(0.5)
    
for i in range(10):
	print("\r  time: {}".format(i), end='')
	time.sleep(0.5)

for i in range(10):
	print("\r  time: {0}, {1}".format(i, i+10), end='')
	time.sleep(0.5)



import sys
import time

def countdown(n):
    for x in reversed(range(n)):
        #sys.stdout.write('\r' + str(x))
        print('\r{}'.format( str(x) ), end='')
        time.sleep(0.5)

countdown(60)


for i in range(15):
	print('\r{}'.format(15-i), end='')
	time.sleep(0.5)

