import numpy as np
import matplotlib.pyplot as plt

###################### 선 그래프 (line chart)
# x,y 축 데이터
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# 표 내부 설정
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# 표 외부 설정
plt.title("Nominal GDP")
plt.ylabel("Billions of $")
plt.xlabel("Years")

# 표 그리기
plt.show()

# 파일 저장
plt.savefig("hello.pdf", dpi=300)



###################### 하나의 figure 안에 여러 line 그리기
variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = range(len(variance))

# 표 내부 설정
plt.plot(xs, variance, 'g-', label='variance')
plt.plot(xs, bias_squared, 'r-.', label='bias^2')
plt.plot(xs, total_error, 'b:', label='total error')

# 라벨 위치
plt.legend(loc="upper center")

# 표 외부 설정
plt.xlabel("model complexity")
plt.xticks([])
plt.title("The Bias-Variance Tradeoff")

# 표 그리기
plt.show()



###################### 여러개의 figure 
# figsize=(9,9)를 사용하여 최초 창의 크기를 가로 세로 9인치로 설정한다.
fig = plt.figure(figsize=(9,9))

# 가로 1칸, 세로 2칸으로 쪼개고 그 중 첫 번째 칸에 ax라는 이름의 axes를 생성한다는 뜻이다.
ax1 = fig.add_subplot(1,2,1)
# 가로 1칸, 세로 2칸으로 쪼개고 그 중 두 번째 칸에 ax라는 이름의 axes를 생성한다는 뜻이다.
ax2 = fig.add_subplot(1,2,2)

# set() 메서드를 이용해 표 외부를 설정
# x축 및 y축의 최댓값과 최솟값, 그래프의 제목, x축 및 y축의 이름을 설정
ax1.set(xlim=[1930., 2020.], ylim=[0, 16000], title='Example', xlabel='xAxis', ylabel='yAxis')
ax2.set(xlim=[1930., 2020.], ylim=[0, 16000], title='Example', xlabel='xAxis', ylabel='yAxis')

# 아래와 같이 파라미터를 나눠서 설정도 가능하다.
#ax.set_xlim([0., 1.])
#ax.set_ylim([-0.5, 2.5])
#ax.set_title('Example', size=20)
#ax.set_xlabel('xAxis', size=10)
#ax.set_ylabel('yAxis', size=15)

x = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
y = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# plot() 메서드를 이용해 표 내부를 설정
ax1.plot(x, y, marker='o', color='green', linewidth=3, linestyle ="solid")
ax2.plot(x, y, marker='o', color='green', linewidth=3, linestyle ="solid")

# plt.show()는 생성된 모든 figure를 보여준다.
plt.show()