
import pandas as pd


news_df = pd.DataFrame(columns=("Title", "Press", "Datetime", "Article"))
idx = 0


news_df.loc[idx] = ['인공지능', 'zdnet', '2020.11.10', '텐서플로우와 파이토치']
idx += 1
news_df.loc[idx] = ['풍력발전 영향', '한겨레', '2020.5.3', '해상에서 사용하는']
idx += 1
news_df.loc[idx] = ['미국 대선 2020', '오마이뉴스', '2020.7.4', '바이든과 트럼프 경합']
idx += 1


print('\n---------------------------------- news_df')
print(news_df)
print('\n---------------------------------- news_df[''Press'']')
print(news_df['Press'])
print('\n---------------------------------- news_df.loc[1]')
print(news_df.loc[1])
print('\n---------------------------------- news_df.iloc[1]')
print(news_df.iloc[1])

