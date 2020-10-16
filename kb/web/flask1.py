'''
https://bskyvision.com/944?category=751609

Flask로 웹 어플리케이션 만들기 (코로나19 오늘 확진자 수 알림)
'''

from flask import Flask
from urllib import request
from bs4 import BeautifulSoup
 
app = Flask(__name__)
@app.route("/")
 
def hello():
    target = request.urlopen("http://ncov.mohw.go.kr/")
    soup = BeautifulSoup(target, "html.parser")
    nums = []
 
    for item in soup.select("div.datalist"):
        for data in item.select("span.data"):
            nums.append(int(data.string))
 
    print("오늘 코로나 확진자수: ", sum(nums), "명")
 
    return "<h1>오늘 코로나 확진자수: "+str(sum(nums))+"명</h1>"
 
app.run(host="0.0.0.0", port="5000", debug=True)
