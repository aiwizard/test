#from konlpy.tag import Hannanum
#hannanum = Hannanum()
#print(hannanum.analyze(u'미국은 지금 대통령 선거기간이다.'))

from konlpy.tag import Komoran  # 코모란 형태소분석기, 제목을 모든 다음 그것을 형태소 단위로 쪼개어 토픽 모델링한다
komoran = Komoran(userdic='user_dic.txt')   # '호불호' 라는 핵심단어를 인식 못하므로 사전에 등록해야
