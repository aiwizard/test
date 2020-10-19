
'''
http://blog.naver.com/PostView.nhn?blogId=doksg&logNo=221703321488

sudo apt install mpg321
sudo pip install gTTS
'''

from gtts import gTTS
import os

value = ['덴마크','노르웨이','스웨덴','핀란드','스페인']

with open("hello.txt","w") as f:
    for i in value:
        f.write("{}도 가고 싶고 \n".format(i))


f = open('hello.txt', 'r')
line = f.readlines()


for t in line:
	outfile = "output.mp3"
	print(outfile, t)

	tts = gTTS(text=t,lang='ko')	#정식 사용위해서는 여기에 KEY 를 넣어야...
	tts.save(outfile)

	# play sound and remove it	
	os.system("mpg321 {}".format(outfile))
	os.system("rm {}".format(outfile))

