from sklearn.datasets import load_iris
import pandas as pd

# iris 데이터로 DataFrame 생성
iris_dataset = load_iris()

iris_df = pd.DataFrame(iris_dataset['data'], columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)',
   'petal width (cm)'])

print(iris_df)

# Pandas를 이용해 산점도 행렬 표현
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

scatter_matrix(iris_df, 
               alpha=0.5, 
               figsize=(10, 10), 
               diagonal='kde')
plt.show()


# label 별로 색을 다르게 하고 싶다면
scatter_matrix(iris_df, 
               c=iris_dataset['target'],
               alpha=0.5, 
               figsize=(10, 10), 
               diagonal='kde')
plt.show()
