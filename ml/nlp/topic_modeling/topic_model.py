'''
토픽 모델링

    https://brunch.co.kr/@jiheon0105/38
'''

from tqdm import tqdm
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import konlpy
from konlpy.tag import Komoran  # 코모란 형태소분석기, 제목을 모든 다음 그것을 형태소 단위로 쪼개어 토픽 모델링한다
komoran = Komoran(userdic='user_dic.txt')   # '호불호' 라는 핵심단어를 인식 못하므로 사전에 등록해야
#komoran = Komoran()   # '호불호' 라는 핵심단어를 인식 못하므로 사전에 등록해야

# 크롤링 범위
title_nums = range(0, 300)

# 리스트
title_list = []

# 페이지 열기
#FA_url = 'https://www.google.com/search?q=호불호&sxsrf=ALeKk00EbuGshbJAe8dkk5NFGFKSJZchQA:1591979528843&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiNnLny2fzpAhUNc5QKHZ2KDfoQ_AUoAXoECBcQAw&biw=1707&bih=907'
FA_url = 'https://www.google.co.kr/search?hl=ko&tbm=isch&source=hp&biw=1054&bih=727&ei=IZuTX9LyDrGxmAXE65mQCw&q=%EC%9E%90%EC%97%B0%EC%96%B4+%EC%B2%98%EB%A6%AC&oq=%EC%9E%90%EC%97%B0%EC%96%B4+%EC%B2%98%EB%A6%AC&gs_lcp=CgNpbWcQAzICCAAyAggAMgIIADICCAAyBAgAEBgyBAgAEBgyBAgAEBgyBAgAEBgyBAgAEBgyBAgAEBg6BQgAELEDUNQSWMo8YNc8aAhwAHgDgAHVAYgBrQ2SAQYxLjExLjGYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABAA&sclient=img&ved=0ahUKEwiSh-DOoMzsAhWxGKYKHcR1BrIQ4dUDCAc&uact=5'
driver = webdriver.Chrome()
driver.get(FA_url)

# 스크롤 내리기
# body = driver.find_element_by_css_selector('body')
# for i in range(60):
#     body.send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)
#     print("scroll down: ", i)

# 파싱
source = driver.page_source
bs = BeautifulSoup(source, 'html.parser')
#data = bs.select('div.WGvvNb')
data = bs.select('a.WGvvNb')
L = list(data)
# print(data)
# print('----------------------------')
# print(L[0])
# print('----------------------------')
# print(L[1])
# print(len(L))

# 크롤링
print("1. crawling ...")
L_num = range(0, len(L))
#for title in tqdm(title_nums):
for i in tqdm(L_num):
    title = L[i].text
    title_list.append(title)
    i += 1
    if i > len(L):
        break
    time.sleep(0.3)

# title_list 에는 페이지 전체 이미지의 제목이 리스트 형태로 저장되었음
print('title_list: ', len(title_list))

# 토픽 모델링을 위한 특정 형식의 자료 생성(DTM과 폴더 형식), 단어빈도 보기
print("2. 토픽모델링 위한 자료 생성, 단어빈도")
from gensim import corpora
FA_noun = []    # title_list 의 모든 제목을 형태소 분석 결과 리스트
for title in tqdm(title_list):
    try:
        noun = list(term for term in komoran.nouns(title) if len(term) > 1 )
    except UnicodeDecodeError:
        # 코모란이 이모티콘 등의 특수문자를 처리할 때, 오류가 발생하는데 이를 무시한다
        pass

    #print(noun)
    FA_noun.append(noun)    # 형태소 단위로 분류한 각 단어들이 리스트에 추가된다

# https://blog.naver.com/pdc222/221360553916
FA_dic = corpora.Dictionary(FA_noun)    # 위 리스트를 바탕으로 단어 빈도별 목록을 생성
term_freq = FA_dic.cfs  # 각 단어의 개수를 센다
print('----------------- term_freq')
print('term_freq: ', term_freq)
print('----------------- FA_dic')
print(FA_dic)
print('----------------- term_freq')
print(term_freq)
print("3. term")
print("----------------- FA_dic.token2id.keys()")
print(FA_dic.token2id.keys())
keys1 = FA_dic.token2id.keys()
print(len(keys1))
print("----------------- term_freq.keys()")
print(term_freq.keys())
keys2 = term_freq.keys()
print(len(keys2))
'''
print("=================")
i = 0
k = 0
for term in tqdm(FA_dic.token2id.keys()):
    i+=1
    j = 0
    for term_id in term_freq.keys():
        k+=1
        j+=1
        print(f"%d\t\t %d %s %d key: %d" %(k, i, term, j, term_id))


print(type(term_freq))
i=0
for term in tqdm(FA_dic.token2id.keys()):
    for term_id in term_freq.keys():
        if FA_dic.token2id[term] == term_id:
            #term_freq[term] = term_freq.pop(term_id)
            i+=1
            #print(f"%d\t %-7s\t %d\t %d" %(i, term, term_id, term_freq[term_id]))
print(type(term_freq))
'''
print('---------------- 단어 빈도순 정렬')
#단어 빈도순 정렬
a = sorted(FA_dic.cfs.items(), key=lambda x:x[1], reverse=True)
print(a)
print('---------------- 토픽 모델링 위한 자료 형식인 DTM 생성')
# 토픽 모델링을 위한 자료 형식인 DTM을 생성
FA_dtm = [FA_dic.doc2bow(doc) for doc in FA_noun]
print(FA_dtm)


# 토픽 개수 결정 - 최적화된 토픽 모델링을 위해 토픽 개수에 따라 분석의 혼잡도와 일관성을 분석한다
# 이 부분까지 1차적으로 확인해서 최선의 토픽 갯수를 정한 후, 2차로 이 부분을 삭제하고 아래의 토픽 모델링을 코드를 작동시켜야 한다
import gensim
from gensim.models import CoherenceModel

Lda = gensim.models.ldamodel.LdaModel
perplexity_score = []
coherence_score = []
for i in [5,10,15,20,25,30]:    #제목 갯수가 5,10,15,20,25,30 인 6가지 경우 각각의 혼잡도와 일관성을 측정해서 바로 윗줄의 두 리스트에 담는다
    ldamodel = Lda(FA_dtm, num_topics=i, id2word=FA_dic, passes=10)
    perplexity_score.append(ldamodel.log_perplexity(FA_dtm))    #혼잡도
    coherence_score.append(CoherenceModel(model=ldamodel, texts=FA_noun, dictionary=FA_dic, coherence='c_v').get_coherence())   #일관성
    print(i, 'th process complete')


# 혼잡도/일관성 그래프화
import matplotlib.pyplot as plt
plt.subplot(1,2,1)
plt.plot([5,10,15,20,25,30], perplexity_score)
plt.subplot(1,2,2)
plt.plot([5,10,15,20,25,30], coherence_score)
plt.show()


print('---------------- 10개로 압축된 토픽')
# 그 정한 토픽 갯수로 토픽 모델링을 진행
FA_lda = Lda(FA_dtm, num_topics=10, id2word=FA_dic, passes=10)
topics = FA_lda.print_topics(num_words=5)
for topic in topics:    #num_topics=10 이므로 10개로 압축된 토픽을 각각 출력한다
    print(topic)

#시각화 - 각각의 토픽을 2차원 공간에서 시각적으로 나타낸다
import pyLDAvis.gensim
vis = pyLDAvis.gensim.prepare(FA_lda, FA_dtm, FA_dic)
pyLDAvis.save_html(vis, '호불호300LDA.html')    # 토픽모델링 결과를 저장
