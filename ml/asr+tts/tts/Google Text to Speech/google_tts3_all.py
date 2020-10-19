
'''
http://blog.naver.com/PostView.nhn?blogId=doksg&logNo=221703321488

sudo apt install mpg321
sudo pip install gTTS
'''

from gtts import gTTS
import os

value = ['나는 그대가 곁에 있어도 그대가 그립다.','지금 내가 아는 것을 그 때도 알았더라면.','우주는 11차원이래.']

with open("hello.txt","w") as f:
    for i in value:
        f.write("{}\n".format(i))


f = open('hello.txt', 'r')
content = f.read()


outfile = "output.mp3"
print(outfile, content)

tts = gTTS(text=content,lang='ko')	#정식 사용위해서는 여기에 KEY 를 넣어야...
tts.save(outfile)

# play sound and remove it	
os.system("mpg321 {}".format(outfile))
os.system("rm {}".format(outfile))

