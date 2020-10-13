'''
https://blog.naver.com/jenius14/221832383232
https://blog.naver.com/ji0eeeee/221643691727
https://blog.naver.com/soowon0109/221723297535
https://blog.naver.com/ekdldhrtlsda/221799757836

'''

# 1. Seaborn을 사용하여 tip 데이터 불러오고 시각화 하기

# library
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(style='darkgrid')


# Data load
tips = sns.load_dataset('tips')
print('tips.head(5): \n{}\n'.format(tips.head(5)))


'''
# relationship

relplot은 relation의 관계를 알아보는 그래프이며 단순히 x,y를 plot을 하는 것입니다
그래프를 보면 양의 상관 관계를 보이는 것을 보입니다
다시 말하자면 비싼 금액을 먹은 사람들이 팁을 많이 내는 경향성을 가집니다
- relplot을 사용하여 x축의 값은 total_bill을 주고 y축에는 tip을 준다.
'''
sns.relplot(x='total_bill', y='tip', data=tips)


# 2. 팁 데이터를 흡연 유/무로  분류하기 (hue 지정)
'''
hue를 넣어 기준을 하나 더 넣어 보도록 하겠습니다
담배를 피는 지 여부에 따른 분석입니다
'''
sns.relplot(x='total_bill', y='tip', hue='smoker',data=tips)


# 3. 흡연 유/무로 구분한 데이터의 마커를 다르게 표시하기 (Style 지정)
sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker", data=tips)


# 4. hue와 style을 각각 다르게 지정하기
sns.relplot(x="total_bill", y="tip", hue="smoker", style="time", data=tips)


# 5. 2가지 분류가 아닌 여러 분류일 경우
sns.relplot(x="total_bill", y="tip", hue="size", data=tips)


# 6. 마커의 색상 변경하기
sns.relplot(x="total_bill", y="tip", hue="size", palette="ch:r=-.5,l=.75", data=tips)


# Load Data (Iris & Titanic)
iris = sns.load_dataset('iris')
titanic = sns.load_dataset('titanic')
print('iris.shape: ', iris.shape)
print('iris.head(5): \n{}\n'.format(iris.head(5)))
print('titanic.shape: ', titanic.shape)
print('titanic.head(5): \n{}\n'.format(titanic.head(5)))


# FacetGrid
'''
tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips, row="sex", col="time", margin_titles=True)
bins = np.linspace(0, 60, 13)
g.map(plt.hist, "total_bill", color="steelblue", bins=bins)
'''


# Factorplot
#sns.factorplot(x='pclass',y='survived',hue='sex',data=titanic)


# Pairgrid
#h = sns.PairGrid(iris)
#h = h.map(plt.scatter)


# Pairplot(Pairgrid와 방식은 동일)
#sns.pairplot(iris)


# Jointplot
sns.jointplot('sepal_length','sepal_width',data=iris,kind='kde')


plt.show()
