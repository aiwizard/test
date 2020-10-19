'''
한/영 구분
'''

import re

pkor = re.compile('[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]')
peng = re.compile('[a-z|A-Z]')

text = "Hello world 한글 인가"
text = "Hello world"
text = "한글"
text = "123-12"

mkor = pkor.search(text)
meng = peng.search(text)

if mkor and meng:
    print("KOR + ENG")
elif mkor and not meng:
    print("KOR only")
elif not mkor and meng:
    print("ENG only")
else:
    print("no KOR or ENG")
    
