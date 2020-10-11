'''
https://www.tensorflow.org/tutorials/keras/regression?hl=ko

자동차 연비 예측하기
'''

import pathlib

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

print(tf.__version__)

########################### 데이터 구하기 - Auto MPG 데이터셋
dataset_path = keras.utils.get_file("auto-mpg.data", "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")
print('dataset_path: ', dataset_path)

# 판다스를 사용하여 데이터를 읽는다
column_names = ['MPG','Cylinders','Displacement','Horsepower','Weight', 'Acceleration', 'Model Year', 'Origin']
raw_dataset = pd.read_csv(dataset_path, names=column_names,
                      na_values = "?", comment='\t',
                      sep=" ", skipinitialspace=True)

dataset = raw_dataset.copy()
dataset.tail()

########################### 데이터 정제하기
dataset.isna().sum()    # 이 데이터셋은 일부 데이터가 누락되어 있다
dataset = dataset.dropna()  # 문제를 간단하게 만들기 위해서 누락된 행을 삭제한다

# "Origin" 열은 수치형이 아니고 범주형이므로 원-핫 인코딩(one-hot encoding)으로 변환
origin = dataset.pop('Origin')
dataset['USA'] = (origin == 1)*1.0
dataset['Europe'] = (origin == 2)*1.0
dataset['Japan'] = (origin == 3)*1.0
dataset.tail()

########################### 데이터셋을 훈련 세트와 테스트 세트로 분할
train_dataset = dataset.sample(frac=0.8,random_state=0)
test_dataset = dataset.drop(train_dataset.index)

########################### 데이터 조사하기
# 훈련 세트에서 몇 개의 열을 선택해 산점도 행렬을 만들어 살펴 본다
sns.pairplot(train_dataset[["MPG", "Cylinders", "Displacement", "Weight"]], diag_kind="kde")

# 전반적인 통계도 확인
train_stats = train_dataset.describe()
train_stats.pop("MPG")
train_stats = train_stats.transpose()
print('train_stats: ', train_stats)

########################### 특성과 레이블 분리하기
# 특성에서 타깃 값 또는 "레이블"을 분리한다. 이 레이블을 예측하기 위해 모델을 훈련시킬 거다.
train_labels = train_dataset.pop('MPG')
test_labels = test_dataset.pop('MPG')

########################### 데이터 정규화
def norm(x):
  return (x - train_stats['mean']) / train_stats['std']
normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)

########################################################################
########################### 모델 만들기
def build_model():
  model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[len(train_dataset.keys())]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
  ])

  optimizer = tf.keras.optimizers.RMSprop(0.001)

  model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
  return model

model = build_model()


########################### 모델 확인
model.summary()

# 모델을 한 번 실행해 본다. 훈련 세트에서 10 샘플을 하나의 배치로 만들어 model.predict 메서드를 호출해 본다
example_batch = normed_train_data[:10]
example_result = model.predict(example_batch)
print('example_result: ', example_result)

########################### 모델 훈련
# 1,000번의 에포크(epoch) 동안 훈련합니다. 훈련 정확도와 검증 정확도는 history 객체에 기록된다
# 에포크가 끝날 때마다 점(.)을 출력해 훈련 진행 과정을 표시
class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')

EPOCHS = 1000

history = model.fit(
  normed_train_data, train_labels,
  epochs=EPOCHS, validation_split = 0.2, verbose=0,
  callbacks=[PrintDot()])

# history 객체에 저장된 통계치를 사용해 모델의 훈련 과정을 시각화
hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
print('hist.tail()', hist.tail())


import matplotlib.pyplot as plt

def plot_history(history):
  hist = pd.DataFrame(history.history)
  hist['epoch'] = history.epoch

  plt.figure(figsize=(8,12))

  plt.subplot(2,1,1)
  plt.xlabel('Epoch')
  plt.ylabel('Mean Abs Error [MPG]')
  plt.plot(hist['epoch'], hist['mae'], label='Train Error')
  plt.plot(hist['epoch'], hist['val_mae'], label = 'Val Error')
  plt.ylim([0,5])
  plt.legend()

  plt.subplot(2,1,2)
  plt.xlabel('Epoch')
  plt.ylabel('Mean Square Error [$MPG^2$]')
  plt.plot(hist['epoch'], hist['mse'], label='Train Error')
  plt.plot(hist['epoch'], hist['val_mse'], label = 'Val Error')
  plt.ylim([0,20])
  plt.legend()
  plt.show()

plot_history(history)
'''
이 그래프를 보면 수 백번 에포크를 진행한 이후에는 모델이 거의 향상되지 않는 것 같다. 
model.fit 메서드를 수정하여 검증 점수가 향상되지 않으면 자동으로 훈련을 멈추도록 만들어 본다. 
에포크마다 훈련 상태를 점검하기 위해 EarlyStopping 콜백(callback)을 사용한다. 
지정된 에포크 횟수 동안 성능 향상이 없으면 자동으로 훈련이 멈춘다
'''

model = build_model()

# patience 매개변수는 성능 향상을 체크할 에포크 횟수입니다
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

history = model.fit(normed_train_data, train_labels, epochs=EPOCHS,
                    validation_split = 0.2, verbose=0, callbacks=[early_stop, PrintDot()])

plot_history(history)
'''
이 그래프를 보면 검증 세트의 평균 오차가 약 +/- 2 MPG입니다. 좋은 결과인가? 이에 대한 평가는 여러분에게 맡기겠다.

모델을 훈련할 때 사용하지 않았던 테스트 세트에서 모델의 성능을 확인해 보죠.
이를 통해 모델이 실전에 투입되었을 때 모델의 성능을 짐작할 수 있다
'''

loss, mae, mse = model.evaluate(normed_test_data, test_labels, verbose=2)

print("테스트 세트의 평균 절대 오차: {:5.2f} MPG".format(mae))

########################### 예측
# 마지막으로 테스트 세트에 있는 샘플을 사용해 MPG 값을 예측해 보자
test_predictions = model.predict(normed_test_data).flatten()

plt.scatter(test_labels, test_predictions)
plt.xlabel('True Values [MPG]')
plt.ylabel('Predictions [MPG]')
plt.axis('equal')
plt.axis('square')
plt.xlim([0,plt.xlim()[1]])
plt.ylim([0,plt.ylim()[1]])
_ = plt.plot([-100, 100], [-100, 100])

# 모델이 꽤 잘 예측한 것 같습니다. 오차의 분포를 살펴 보자
error = test_predictions - test_labels
plt.hist(error, bins = 25)
plt.xlabel("Prediction Error [MPG]")
_ = plt.ylabel("Count")
'''
가우시안 분포가 아니지만 아마도 훈련 샘플의 수가 매우 작기 때문일 것
'''

''' 결론
    - MSE (평균 제곱 오차):   회귀 문제에서 사용하는 손실 함수
    - MAE (평균 절댓값 오차): 회귀 문제에서 사용되는 평가 지표

    - 수치 입력 데이터의 특성이 여러 가지 범위를 가질 때 동일한 범위가 되도록 각 특성의 스케일을 독립적으로 조정해야 한다.
    - 훈련 데이터가 많지 않다면 오버피팅을 피하기 위해 은닉층의 개수가 적은 소규모 네트워크를 선택하는 방법이 좋다.
    - 조기 종료(Early stopping)은 과대적합을 방지하기 위한 좋은 방법이다.
'''