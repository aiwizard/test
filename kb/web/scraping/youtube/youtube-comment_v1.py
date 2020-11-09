
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


def youtube_scraping(url, wd):
	'''
	press = wd.find_element_by_xpath('//*[@id="main_content"]/div[1]/div[1]/a/img').get_attribute('title')
	title = wd.find_element_by_id('articleTitle').text
	datetime = wd.find_element_by_class_name('t11').text
	article = wd.find_element_by_id('articleBodyContents').text
	'''

	# 영상url, 좋아요, 싫어요, 스크립트, 소유자, 내용
	
	# 불필요 부분 제거
	'''
	article = article.replace("// flash 오류를 우회하기 위한 함수 추가", "")
	article = article.replace("function _flash_removeCallback(){}", "")
	article = article.replace("\n", "")
	article = article.replace("\t", "")
	'''

	# 좋아요 등
	'''
	good = wd.find_element_by_xpath('//*[@id="spiLayer"]/div[1]/ul/li[1]/a/span[2]').text
	warm = wd.find_element_by_xpath('//*[@id="spiLayer"]/div[1]/ul/li[2]/a/span[2]').text
	sad  = wd.find_element_by_xpath('//*[@id="spiLayer"]/div[1]/ul/li[3]/a/span[2]').text
	angry= wd.find_element_by_xpath('//*[@id="spiLayer"]/div[1]/ul/li[4]/a/span[2]').text
	want = wd.find_element_by_xpath('//*[@id="spiLayer"]/div[1]/ul/li[5]/a/span[2]').text
	recommend = wd.find_element_by_xpath('//*[@id="toMainContainer"]/a/em[2]').text
	'''

	title = wd.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string').text
	#like2 = wd.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[2]/a/yt-formatted-string').text
	print(title)
	#print(like2)
	
	#print("뉴스:", [title, press, datetime, article, good, warm, sad, angry, want, recommend, news_url])
	
	#return [title, press, datetime, article, good, warm, sad, angry, want, recommend, news_url]
	return ["aaa", "aaa"]


# def scroll_down(wd):	#스크롤을 내리는 함수
# 	print("[스크롤 다운 시작]")
# 	scroll_count = 0

# 	last_height = wd.execute_script("return document.body.scrollHeight")
# 	after_click = False

# 	while True:
# 		print(f"[스크롤 다운: {scroll_count}]")
# 		wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 		scroll_count += 1
# 		time.sleep(1)

# 		# 스크롤 위치값 얻고 new_height 에 저장
# 		new_height = wd.execute_script("return document.body.scrollHeight")

# 		# 스크롤이 최하단이면
# 		if last_height == new_height:
# 			break

# 		last_height = new_height

'''
def scroll_down(wd):
    print("[scroll_down(): 스크롤 다운 시작]")
    scroll_count = 0

    last_height = wd.execute_script("return document.body.scrollHeight")
    after_click = False

    while True:
        print(f"\t[스크롤 다운: {scroll_count}]", end='\n')
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        scroll_count += 1
        time.sleep(1)

        # 스크롤 위치값 얻고 new_height 에 저장
        new_height = wd.execute_script("return document.body.scrollHeight")

        # 스크롤이 최하단이면
        if last_height == new_height:
            print('끝')
            break
            # # 결과 더보기 버튼을 클릭한 적이 있는 경우
            # if after_click is True:
            #     break
            # # [결과 더보기] 버튼을 클릭한 적이 없는 경우
            # else:
            #     try:
            #         more_button = wd.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input')
            #         if more_button.is_displayed():
            #             more_button.click()
            #             after_click = True
            #     except NoSuchElementException as e:
            #         print(e)
            #         break

        last_height = new_height

    print("[scroll_down(): 스크롤 다운 끝]\n")
'''
def scroll_down(wd):
	last_page_height = wd.execute_script("return document.documentElement.scrollHeight")
	while True:
		wd.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
		time.sleep(3.0)
		#wd.implicitly_wait(3)
		new_page_height = wd.execute_script("return document.documentElement.scrollHeight")

		if new_page_height == last_page_height:
			break
		last_page_height = new_page_height
	

def comments_scraping(url, wd):
	try:
		seen = wd.find_element_by_xpath('//*[@id="count"]/yt-view-count-renderer/span[1]').text
		datetime = wd.find_element_by_xpath('//*[@id="date"]/yt-formatted-string').text
		
		tmp = wd.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a')
		#like = tmp.find_element_by_tag_name('yt-formatted-string').text
		like = tmp.find_element_by_tag_name('yt-formatted-string').get_attribute('aria-label')

		tmp = wd.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[2]/a')
		#unlike = tmp.find_element_by_tag_name('yt-formatted-string').text
		unlike = tmp.find_element_by_tag_name('yt-formatted-string').get_attribute('aria-label')


		desc = wd.find_element_by_xpath('//*[@id="description"]/yt-formatted-string').text
		
		#tmp = wd.find_element_by_xpath('//*[@id="sections"]')
		comments_num = wd.find_element_by_xpath('//*[@id="count"]/yt-formatted-string').text

		print(f'seen: {seen} date: {datetime} like: {like} unlike: {unlike}')
		print(f'desc: {desc}')
		print(f'조회수: {comments_num}')
	except:
		print('exceptoin')
		
	return ["aa", "aa"]


## scraping(): 스크래핑 함수
def scraping():
	#wd = webdriver.Chrome('chromedriver', options=chrome_options)
	wd = webdriver.Chrome()
	wd.implicitly_wait(3)
	wd.maximize_window()
	#wd.set_window_size(800, 600)

	# 새로운 탭
	# wd.execute_script('window.open("about:blank", "_blank");')
	# tabs = wd.window_handles

	# # 첫 번째 탭
	# wd.switch_to.window(tabs[0])

	#query = input("검색어 입력: ")
	query = "우주의 끝을 찾아서"
	search_url = 'https://www.youtube.com/results?search_query=' + query
	wd.get(search_url)
	wd.implicitly_wait(6)

	scroll_down(wd)

	idx = 0
	video_df = pd.DataFrame(columns=("Thumbnail", "Time", "Title", "Views", "When", "Author"))
	comments_df = pd.DataFrame()

	video_max = 0
	while True:
		#content_list = wd.find_elements_by_class_name('style-scope.ytd-item-section-renderer')
		content_list = wd.find_elements_by_tag_name('ytd-video-renderer')
		video_max = len(content_list)
		print("--------컨텐츠: %d 개------------" %(video_max))
		
		for content in content_list:
			#print(content.text)
			try:
				video_url = content.find_element_by_class_name('yt-simple-endpoint.inline-block.style-scope.ytd-thumbnail').get_attribute('href')
				thumbnail = content.find_element_by_xpath('//*[@id="img"]').get_attribute('src')
				#title = content.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string').text
				title = content.find_element_by_class_name('yt-simple-endpoint.style-scope.ytd-video-renderer').get_attribute('title')
				desc = content.find_element_by_id('description-text').text
				view = content.find_element_by_xpath('//*[@id="metadata-line"]/span[1]').text
				when = content.find_element_by_xpath('//*[@id="metadata-line"]/span[2]').text
				owner = content.find_element_by_xpath('//*[@id="text"]/a').text
				channel = content.find_element_by_xpath('//*[@id="text"]/a').get_attribute('href')
				# print('***', video_url)
				# print('***', thumbnail)
				# print('***', title)
				# print('***', desc)
				# print('***', view)
				# print('***', when)
				# print('***', owner)
				# print('***', channel)
				print('%s, %s, %s' %(video_url, owner, title))
			except:
				print("continue")
				continue
			
			#return
			
			# 두 번째 탭
			# wd.switch_to.window(tabs[1])
			# wd.get(video_url)
			
			#video_df.loc[news_idx] = news_scraping(content_url, wd)
			#idx += 1
			
			# 댓글
			#df = comments_scraping(video_url, wd)
			#comments_df = pd.concat([comments_df, df])
			idx += 1

			if idx >= video_max:
				break

			time.sleep(0.5)
			
		'''
		if news_idx >= news_max:
			break
				
		# 다음 페이지 클릭
		try:
			wd.switch_to.window(tabs[0])
			wd.find_element_by_class_name('next').click()
			time.sleep(1)
		except:
			break
		'''
		break
	
	wd.close()
	
	return video_df, comments_df
	

'''
df1, df2 = scraping()
print('----------------------------------')
print(df1)
print('----------------------------------')
print(df2)
'''
scraping()
