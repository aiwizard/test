# -*- coding: utf-8 -*-
import re
import json
import math
import datetime
import requests
import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup

# https://developers.naver.com/main/ 사이트에서 어플리케이션 등록
# Naver Development ID/SECRET 필요
naver_client_id = "YOUR_CLIENT_ID"
naver_client_secret = "YOUR_CLIENT_SECRET"


# 블로그 검색 결과 개수를 가져옴
# 네이버는 최대 1000개의 포스트 결과를 보여주기 때문에 그 이상이면 1000으로 고정
def get_blog_count(query, display):
    encode_query = urllib.parse.quote(query)
    search_url = "https://openapi.naver.com/v1/search/blog?query=" + encode_query
    request = urllib.request.Request(search_url)

    request.add_header("X-Naver-Client-Id", naver_client_id)
    request.add_header("X-Naver-Client-Secret", naver_client_secret)

    response = urllib.request.urlopen(request)
    response_code = response.getcode()

    if response_code is 200:
        response_body = response.read()
        response_body_dict = json.loads(response_body.decode('utf-8'))

        print("Last build date: " + str(response_body_dict['lastBuildDate']))
        print("Total: " + str(response_body_dict['total']))
        print("Start: " + str(response_body_dict['start']))
        print("Display: " + str(response_body_dict['display']))

        if response_body_dict['total'] == 0:
            blog_count = 0
        else:
            blog_total = math.ceil(response_body_dict['total'] / int(display))

            if blog_total >= 1000:
                blog_count = 1000
            else:
                blog_count = blog_total

            print("Blog total: " + str(blog_total))
            print("Blog count: " + str(blog_count))

        return blog_count


# 블로그의 내용을 가져오는 함수
def get_blog_post(query, display, start_index, sort):
    global no, fs
    
    encode_query = urllib.parse.quote(query)
    search_url = "https://openapi.naver.com/v1/search/blog?query=" + encode_query + "&display=" + str(display) + "&start=" + str(start_index) + "&sort=" + sort

    request = urllib.request.Request(search_url)

    request.add_header("X-Naver-Client-Id", naver_client_id)
    request.add_header("X-Naver-Client-Secret", naver_client_secret)

    response = urllib.request.urlopen(request)
    response_code = response.getcode()

    if response_code is 200:
        response_body = response.read()
        response_body_dict = json.loads(response_body.decode('utf-8'))
        for item_index in range(0, len(response_body_dict['items'])):
            try:
                remove_html_tag = re.compile('<.*?>')
                title = re.sub(remove_html_tag, '', response_body_dict['items'][item_index]['title'])
                link = response_body_dict['items'][item_index]['link'].replace("amp;", "")
                description = re.sub(remove_html_tag, '', response_body_dict['items'][item_index]['description'])
                blogger_name = response_body_dict['items'][item_index]['bloggername']
                blogger_link = response_body_dict['items'][item_index]['bloggerlink']
                post_date = datetime.datetime.strptime(response_body_dict['items'][item_index]['postdate'], "%Y%m%d").strftime("%y.%m.%d")

                no += 1
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print("#" + str(no))
                print("Title: " + title)
                print("Link: " + link)
                print("Description: " + description)
                print("Blogger Name: " + blogger_name)
                print("Blogger Link: " + blogger_link)
                print("Post Date: " + post_date)

                post_code = requests.get(link)
                post_text = post_code.text
                post_soup = BeautifulSoup(post_text, 'lxml')

                for mainFrame in post_soup.select('iframe#mainFrame'):
                    blog_post_url = "http://blog.naver.com" + mainFrame.get('src')
                    blog_post_code = requests.get(blog_post_url)
                    blog_post_text = blog_post_code.text
                    blog_post_soup = BeautifulSoup(blog_post_text, 'lxml')

                    for blog_post_content in blog_post_soup.select('div#postViewArea'):
                        blog_post_content_text = blog_post_content.get_text()
                        blog_post_full_contents = str(blog_post_content_text)
                        blog_post_full_contents = blog_post_full_contents.replace("\n\n", "\n")
                        # print("blog_post_contents : " + blog_post_full_contents + "\n")
                        fs.write(blog_post_full_contents + "\n")
                        fs.write("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
                        
            except:
                item_index += 1


if __name__ == '__main__':
    
    no = 0             # 몇개의 포스트를 저장하였는지 세기 위한 index
    query = "문재인"   # 검색을 원하는 문자열로서 UTF-8로 인코딩한다.
    display = 10       # 검색 결과 출력 건수 지정, 10(기본값),100(최대)
    start = 1          # 검색 시작 위치로 최대 1000까지 가능
    sort = "date"       # 정렬 옵션: sim(유사도순, 기본값), date(날짜순)

    # 블로그 콘텐츠의 한글 저장을 위해 encoding='utf-8'으로 설정
    fs = open(query + ".txt", 'a', encoding='utf-8')

    blog_count = get_blog_count(query, display)
    for start_index in range(start, blog_count + 1, display):
        get_blog_post(query, display, start_index, sort)

    fs.close()
