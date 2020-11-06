import pandas as pd


news_df = pd.DataFrame(index=("idx1", "idx2", "idx3"), columns=("col1", "col2", "col3", "col4"))
df = pd.DataFrame(columns=("col1", "col2", "col3", "col4"))
print(news_df)
print()

i = 0

df.loc[i]= ['a', 'b', 'c', 'd']
i += 1
print(df)
print()
news_df = pd.concat([news_df, df])

df.loc[i]= ['aa', 'bb', 'cc', 'dd']
i += 1
print(df)
print()
news_df = pd.concat([news_df, df])
print(news_df)

print('------------------------------')
print(df['col2'])
