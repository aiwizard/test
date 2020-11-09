'''
BeautifulSoup 네이버 뉴스 기사 스크래핑

https://www.youtube.com/watch?v=In5KCBqzViU
'''

from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
import pandas as pd


def get_news(query, page_num=10):
	news_df = pd.DataFrame(columns=("Title", "Link", "Press", "Datetime", "Article"))
	idx = 0

	url_query = quote(query)
	url = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=" + url_query
	
	for _ in range(0, page_num):
		search_url = urllib.request.urlopen(url).read()
		soup = BeautifulSoup(search_url, 'html.parser')
		#links = soup.find_all('div', {'class':'info_group'})
		links = soup.find_all('div', {'class':'info_group'})
		print('뉴스: ', len(links))
		
		for link in links:
			print('aaa: ', len(link))
			links.select('a')
			return news_df
			#print('aaaaaaaaaaaaaa:', link.get_text())
			press = link.find('div', {'class':'info_group'}).getchildren()
			print('press: ', len(press))
			#news_url = link.find('a').get('href')
			#--------------------------------
			
			#news_url = link.get_text()
			#print('url: ', news_url)
			#--------------------------------
			'''
			if(news_url == '#'):	# '네이버 기사' 가 없을 때
				continue
			else:
				news_link = urllib.request.urlopen(news_url).read()
				news_html = BeautifulSoup(news_link, 'html.parser')
				
				title = news_html.find('h3', {'id':'articleTitle'}).get_text()
				datetime = news_html.find('span', {'class':'t11'}).get_text()
				article = news_html.find('div', {'id':'articleBodyContents'}).get_text()
				
				news_df.loc[idx] = [title, news_url, press, datetime, article]
				idx += 1
				print("#", end="")
			'''
		return news_df
		try:		
			next = soup.find('a', {'class':'next'}).get('href')
			url = "https://search.naver.com/search.naver" + next
		except:
			break

	return news_df
	

#query = input('검색 질의: ')
query = "인공지능"
news_df = get_news(query, 1)
print('Done')

print(news_df)

