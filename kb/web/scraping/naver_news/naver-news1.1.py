## 네이버 뉴스 댓글 스크래핑
## https://www.youtube.com/watch?v=IFyhTEBSto0


## selenium 및 웹 드라이버 설치
'''
pip3 install selenium
apt-get update
apt install chromium-chromedriver
cp /usr/lib/chromium-browser/chromedriver /usr/bin
'''

import sys
sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')


## 라이브러리 import
import time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

## news_scraping(): 뉴스 스크래핑 함수
def news_scraping(news_url, wd):
    try:
        press = wd.find_element_by_xpath('//*[@id="main_content"]/div[1]/div[1]/a/img').get_attribute('title')
        title = wd.find_element_by_id('articleTitle').text
        datetime = wd.find_element_by_class_name('t11').text
        article = wd.find_element_by_id('articleBodyContents').text
        
        # 불필요 부분 제거
        article = article.replace("// flash 오류를 우회하기 위한 함수 추가", "")
        article = article.replace("function _flash_removeCallback(){}", "")
        article = article.replace("\n", "")
        article = article.replace("\t", "")

        # 좋아요 등
        good = wd.find_element_by_xpath('//*[@id="spiLayer"]/div[1]/ul/li[1]/a/span[2]').text
        warm = wd.find_element_by_xpath('//*[@id="spiLayer"]/div[1]/ul/li[2]/a/span[2]').text
        sad  = wd.find_element_by_xpath('//*[@id="spiLayer"]/div[1]/ul/li[3]/a/span[2]').text
        angry= wd.find_element_by_xpath('//*[@id="spiLayer"]/div[1]/ul/li[4]/a/span[2]').text
        want = wd.find_element_by_xpath('//*[@id="spiLayer"]/div[1]/ul/li[5]/a/span[2]').text
        recommend = wd.find_element_by_xpath('//*[@id="toMainContainer"]/a/em[2]').text
    except Exception as e:
        print("error: ", e)
        return ["","","","","","","","","","",""]

    #print("뉴스:", [title, press, datetime, article, good, warm, sad, angry, want, recommend, news_url])

    return [title, press, datetime, article, good, warm, sad, angry, want, recommend, news_url]


## scraping(): 스크래핑 함수
def scraping():
    wd = webdriver.Chrome('chromedriver', options=chrome_options)
    wd.implicitly_wait(3)

    news_idx = 0
    news_df = pd.DataFrame(columns=("Title", "Press", "DateTime", "Article", "Good", "Warm", "Sad", "Angry", "Want", "Recommend", "URL"))

    #news_url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=023&aid=0003573742'
    news_url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=106&oid=465&aid=0000004065'
    wd.get(news_url)

    # News
    news_df.loc[news_idx] = news_scraping(news_url, wd)
    news_idx += 1


    wd.close()

    return news_df


news_df = scraping()
print("\n----------------------------------------------- news_df")
print(news_df)

