'''
https://banana-media-lab.tistory.com/entry/정규표현식-모음

	메서드			내용
	--------------------	------------------------------------------------
	match(패턴, 문자열)	문자열의 시작부터 매칭되는지 검색
	search(패턴, 문자열)	문자열에 패턴과 매칭되는 곳이 있는지 검색
	findall(패턴, 문자열)	정규식과 매치되는 모든 문자열을 리스트로 반환
	finditer(패턴, 문자열)	정규식과 매치되는 모든 문자열을 iterator 객체로 반환
'''

import re

#1. 이메일이 본문에 포함되어 있는지 검사
p = re.compile('.*[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+.*')

#2. HTML tag 
p = re.compile('.*\<+[a-zA-Z0-9-.]+\>.*')
p = re.compile('\<.+?\>') 

#3. Hash tag
p = re.compile('\\#([0-9a-zA-Z가-힣]*)')

#4. 개체명 추출
p = re.compile('\<.+?:.+?\>')

#5. 특수문자 추출
result = re.sub('[^0-9a-zA-Zㄱ-힗]', '', myStr)

m = p.match(input)
bool(m)

