'''
https://wikidocs.net/15213
'''

import os
import sys
import urllib.request

# 네이버 OpenAPI 신청시 주어지는 값으로 대체
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

encText = urllib.parse.quote("반갑습니다 네이버")
data = "speaker=mijin&speed=0&text=" + encText
'''
speaker
	한국 남여 : jinho, mijin
	영어 남녀 : matt, clara
	일본어 남여 : shinji, yuri
	중국어 남여 : liangliang, meimei
	스페인어 남여 : jose, carmen
speed
	-5~5사이의 정수로 음성 재생속도를 지정
	-5이면 0.5배 빠른
	5이면 0.5배 느린
text
	합성할 문자열을 지정.
	원 문자열이 반드시 UTF-8로 인코딩되어 있어야 하며, 
	이를 다시 URL encoding으로 변환한 값을 전송해야 한다.
	이 때문에 Python 소스는 반드시 UTF-8로 저장해야 한다. 한번에 최대 5000자의 텍스트를 합성할 수 있다.
'''

url = "https://openapi.naver.com/v1/voice/tts.bin"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()

if(rescode==200):
    print("TTS mp3 저장")
    response_body = response.read()
    with open('1111.mp3', 'wb') as f:
        f.write(response_body)
else:
    print("Error Code:" + rescode)
    
