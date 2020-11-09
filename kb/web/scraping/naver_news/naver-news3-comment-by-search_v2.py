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
	
	#print("뉴스:", [title, press, datetime, article, good, warm, sad, angry, want, recommend, news_url])
	return [title, press, datetime, article, good, warm, sad, angry, want, recommend, news_url]
	

## 'comments_scraping()': 뉴스 댓글 스크래핑
def comments_scraping(news_url, wd):
	print("[댓글 펼치기]")
	try:
		wd.find_element_by_class_name('u_cbox_btn_view_comment').click()
		print("[댓글 더보기]", end="")
		time.sleep(1)
		
		while True:
			wd.find_element_by_class_name('u_cbox_btn_more').click()
			print("[더보기]", end="")
			time.sleep(1)
	except:
		pass
	
	
	btn_reply_list = wd.find_elements_by_class_name('u_cbox_btn_reply')
	for btn_reply in btn_reply_list:
		btn_reply.send_keys('\n')
		print("[답글]", end="")
		time.sleep(1)
		
	print("[댓글 스크레이핑 시작]")
	comments_idx = 0
	comments_df = pd.DataFrame(columns=("Contents", "Name", "Datetime", "Recommend", "Unrecommend", "URL"))
	
	comments = wd.find_elements_by_class_name('u_cbox_comment_box')
	print('{} comments exist: '.format(len(comments)))
	for comment in comments:
		try:
			name    = comment.find_element_by_class_name('u_cbox_nick').text
			date    = comment.find_element_by_class_name('u_cbox_date').text
			contents= comment.find_element_by_class_name('u_cbox_contents').text
			recomm  = comment.find_element_by_class_name('u_cbox_cnt_recomm').text
			unrecomm= comment.find_element_by_class_name('u_cbox_cnt_unrecomm').text
			print(f"  댓글 #{comments_idx+1}:", [contents, name, date, recomm, unrecomm, news_url])
			
			comments_df.loc[comments_idx] = [contents, name, date, recomm, unrecomm, news_url]
			comments_idx += 1
		except NoSuchElementException:
			print("  댓글 ===> skip [삭제되거나 부적절한 댓글]")
			continue
	
	print("[댓글 스크레이핑 끝]")

	return comments_df


## scraping(): 스크래핑 함수
def scraping(news_max=20):
	#wd = webdriver.Chrome('chromedriver', options=chrome_options)
	wd = webdriver.Chrome()
	wd.implicitly_wait(3)
	
	# 새로운 탭
	wd.execute_script('window.open("about:blank", "_blank");')
	tabs = wd.window_handles
	
	wd.switch_to.window(tabs[0])
	query = input("검색어 입력: ")
	search_url = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=" + query
	wd.get(search_url)
	
	
	news_idx = 0
	news_df = pd.DataFrame(columns=("Title", "Press", "DateTime", "Article", "Good", "Warm", "Sad", "Angry", "Want", "Recommend", "URL"))
	comments_df = pd.DataFrame()
	
	while True:
		news_list = wd.find_elements_by_css_selector('ul.list_news > li.bx > div.news_wrap.api_ani_send')
		print("--------네이버 기사: %d 개------------" %(len(news_list)))

		page_no = 1
		for news in news_list:
			#input('1네이버 뉴스 검출#########################################')
			try:
				press = news.find_element_by_css_selector('div.news_area div.info_group > a').text
				#when = news.find_element_by_css_selector('div.news_area div.info_group > span.info').text
				news_url = news.find_element_by_css_selector('div.news_area div > a:nth-child(3)').get_attribute('href')
				title = news.find_element_by_css_selector('div.news_area > a.news_tit').get_attribute('title')
				#print('*** {0}, {1}, {2}, {3}'.format(press, when, title, news_url))
				print('*** {0}, {1}'.format(title, news_url))
			except:
				print(">>> 네이버뉴스 없음, continue")
				continue
			
			if press == "스포츠동아":
				print("### 스포츠동아, continue")
				continue

			# 두 번째 탭
			wd.switch_to.window(tabs[1])
			wd.get(news_url)

			# 뉴스 스크레이핑
			news_df.loc[news_idx] = news_scraping(news_url, wd)
			news_idx += 1
			
			# 댓글 스크레이핑
			df = comments_scraping(news_url, wd)
			comments_df = pd.concat([comments_df, df])
			
			if news_idx >= news_max:
				print("news_idx1: ", news_idx)
				break

			# 첫 번째 탭 (없으면 에러 발생)
			wd.switch_to.window(tabs[0])
			time.sleep(1)
		
		if news_idx >= news_max:
			print("news_idx2: ", news_idx)
			break
		
		# 다음 페이지 클릭
		try:
			print("[다음 페이지 cur:{}]".format(page_no))
			page_no += 1
			
			wd.switch_to.window(tabs[0])
			wd.find_element_by_class_name('btn_next').click()
			time.sleep(1)
		except:
			break
			
	wd.close()
	
	return news_df, comments_df
	

news_df, comments_df = scraping()

print("\n----------------------------------------------- news_df")
print(news_df)
print("\n----------------------------------------------- comments_df")
print(comments_df)
