import numpy as np
import matplotlib.pyplot as plt

# Histogram
data = np.random.randint(1, 100, size=200)
plt.hist(data, bins=20, alpha=0.3)  #bins: 막대의 갯수, alpha: 0~1
plt.xlabel('numbers')
plt.ylabel('values')
plt.title('random data')
plt.grid(True)
plt.show()


# Bar
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
plt.bar(movies, num_oscars)
plt.title("My Favorite Movies")
plt.ylabel("# of Academy Awards")
plt.show()


# Histogram
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
histogram = Counter(min(90, grade // 10 * 10) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()], histogram.values(),
width=10, edgecolor="black")

plt.xticks(range(0, 101, 10))
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")

plt.show()


# 산점도 (scatterplot): 두 변수 간의 연관 관계를 보일 때 활용
friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes, marker='^', color='darkgreen')

for l, f, m in zip(labels, friends, minutes):
    plt.annotate(l, xy=(f, m),
    xytext=(5,-5), textcoords="offset points")

plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")

plt.show()



# 네트워크 시각화 (network visualization) - networkx : 네트워크 분석용 python 패키지
import networkx as nx

G = nx.Graph()

G.add_edge('A','B', color='r', weight=1)
G.add_edge('C','B', color='g', weight=2)
G.add_edge('B','D', color='b', weight=5)

pos = nx.spring_layout(G)

colors = list(nx.get_edge_attributes(G, 'color').values())
weights = list(nx.get_edge_attributes(G, 'weight').values())

nx.draw(G, pos, edge_color=colors, width=weights, with_labels=True)
plt.show()


# scatter() 함수를 이용해서 3차원 산점도(3D Scatter plot) 그리기
# 3차원 그래프를 그리기 위해서 from mpl_toolkits.mplot3d import Axes3D를 추가해줍니다.
from mpl_toolkits.mplot3d import Axes3D

# figure 최초 창 크기 설정
fig = plt.figure(figsize=(12, 12))

# figure에 들어갈 개별 subplot
# 3D axes를 만들기 위해 add_subplot()에 projection=’3d’ 키워드를 입력해줍니다.
ax = fig.add_subplot(111, projection='3d')

# scatter() 함수에 준비된 x, y, z 배열 값을 입력해줍니다.
# 마커 (marker)의 형태를 원형 (circle)으로 정해줍니다.
# s 는 점의 크기입니다.
ax.scatter(X_train[:,0], X_train[:,1], X_train[:,2], marker='o', s=15)

plt.show()
