'''
https://bskyvision.com/941?category=751609

오늘의 코로나 확진자수 스크레이핑하기 (Beautiful Soup 활용)
'''

from urllib import request
from bs4 import BeautifulSoup
 
target = request.urlopen("http://ncov.mohw.go.kr/")
 
soup = BeautifulSoup(target, "html.parser")
 
nums = []
 
for item in soup.select("div.datalist"):
    for data in item.select("span.data"):
        nums.append(int(data.string))

print("오늘 코로나 확진자수: {} 명".format( sum(nums) ))
