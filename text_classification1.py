'''
영화 리뷰를 사용한 텍스트 분류

https://www.tensorflow.org/tutorials/keras/text_classification?hl=ko
'''

import tensorflow as tf
from tensorflow import keras

import numpy as np

print(tf.__version__)

# IMDB dataset 다운로드
imdb = keras.datasets.imdb
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)
# num_words=10000은 훈련 데이터에서 가장 많이 등장하는 상위 10,000개의 단어를 선택


# 데이터 탐색
print("훈련 샘플: {}, 레이블: {}".format(len(train_data), len(train_labels)))
print(train_data[0])    # 리뷰 텍스트는 어휘 사전의 특정 단어를 나타내는 정수로 변환되어 있다
len(train_data[0]), len(train_data[1])  # 영화 리뷰는 각각 길이가 다르다. 첫 번째 리뷰와 두 번째 리뷰에서 단어의 개수를 출력
                                        # 신경망의 입력은 길이가 같아야 하기 때문에 나중에 이 문제를 해결한다

# 정수를 단어로 다시 변환
# 정수와 문자열을 매핑한 딕셔너리(dictionary) 객체에 질의하는 헬퍼(helper) 함수를 만든다
word_index = imdb.get_word_index()  # 단어와 정수 인덱스를 매핑한 딕셔너리

# 처음 몇 개 인덱스는 사전에 정의되어 있다
word_index = {k:(v+3) for k,v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2  # unknown
word_index["<UNUSED>"] = 3

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

def decode_review(text):
    return ' '.join([reverse_word_index.get(i, '?') for i in text])

decode_review(train_data[0])    # 첫 번째 리뷰 텍스트를 출력

####################################### 데이터 준비
'''
리뷰-정수 배열-는 신경망에 주입하기 전에 텐서로 변환되어야 한다
   1. 원-핫 인코딩 벡터로 변환한다. 예로 배열 [3, 5]을 인덱스 3과 5만 1이고 나머지는 모두 0인 10,000차원 벡터로 변환할 수 있다.
        그다음 실수 벡터 데이터를 다룰 수 있는 Dense layer를 신경망의 첫 번째 층으로 사용한다. 
        이 방법은 num_words * num_reviews 크기의 행렬이 필요하므로 메모리를 많이 사용한다
   2. 정수 배열의 길이가 모두 같도록 padding 을 추가해 max_length * num_reviews 크기의 정수 텐서를 만든다.
        이런 형태의 텐서를 다룰 수 있는 embedding 층을 신경망의 첫 번째 층으로 사용할 수 있다.

여기서는 두 번째 방식을 사용한다.
'''
# 영화 리뷰의 길이가 같아야 하므로 pad_sequences 함수를 사용해 길이를 맞춘다
train_data = keras.preprocessing.sequence.pad_sequences(train_data,
                                                        value=word_index["<PAD>"],
                                                        padding='post',
                                                        maxlen=256)

test_data = keras.preprocessing.sequence.pad_sequences(test_data,
                                                       value=word_index["<PAD>"],
                                                       padding='post',
                                                       maxlen=256)

print('샘플 길이 확인 - train_data: {}, test_data: {}'.format(len(train_data[0]), len(train_data[1])))
print('패딩된 첫 번째 리뷰 내용 train_data[0]: {}'.format(train_data[0]))  # 첫 번째 리뷰 내용 확인

####################################### 모델 구성
'''
결정 사항
    1. 모델에서 얼마나 많은 층을 사용할 것인가?
    2. 각 층에서 얼마나 많은 hidden unit을 사용할 것인가?

    이 예제의 입력 데이터는 단어 인덱스의 배열이다. 예측할 레이블은 0 또는 1 이다. 이에 맞는 모델을 구성한다
'''
# 입력 크기는 영화 리뷰 데이터셋에 적용된 어휘 사전의 크기입니다(10,000개의 단어)
vocab_size = 10000

model = keras.Sequential()
model.add(keras.layers.Embedding(vocab_size, 16, input_shape=(None,)))  # 이 층은 정수로 인코딩된 단어를 입력 받고 각 단어 인덱스에 해당하는 임베딩 벡터를 찾는다. 이 벡터는 모델이 훈련되면서 학습된다. 이 벡터는 출력 배열에 새로운 차원으로 추가된다. 최종 차원은 (batch, sequence, embedding)이 된다.
model.add(keras.layers.GlobalAveragePooling1D())        # 그 다음 GlobalAveragePooling1D 층은 sequence 차원에 대해 평균을 계산하여 각 샘플에 대해 고정된 길이의 출력 벡터를 반환한다. 이는 길이가 다른 입력을 다루는 가장 간단한 방법이다.
model.add(keras.layers.Dense(16, activation='relu'))    # 이 고정 길이의 출력 벡터는 16개의 은닉 유닛을 가진 완전 연결 층(Dense)을 거친다
model.add(keras.layers.Dense(1, activation='sigmoid'))  # 마지막 층은 하나의 출력 노드(node)를 가진 완전 연결 층이다. sigmoid 활성화 함수를 사용하여 0과 1 사이의 실수를 출력한. 이 값은 확률 또는 신뢰도를 나타낸다.

model.summary()

####################################### 손실 함수와 옵티마이저
'''
모델이 훈련하려면 loss function, optimizer 가 필요하다. 이 예제는 이진 분류 문제이고 모델이 확률을 출력하므로(출력층의 유닛이 하나이고 sigmoid 활성화 함수를 사용한다), binary_crossentropy 손실 함수를 사용한다
다른 손실 함수도 가능은 하다.
    mean_squared_error를 선택할 수 있고 이 함수는 확률 분포 간의 거리를 측정한다.
    하지만 일반적으로 binary_crossentropy가 확률을 다루는데 적합하다.
    여기에서는 정답인 타깃 분포와 예측 분포 사이의 거리이다
회귀(regression) 문제(예를 들어 주택 가격을 예측하는 문제)에 대해 살펴 볼 때 평균 제곱 오차(mean squared error) 손실 함수를 어떻게 사용하는지 알아본다
'''
# 이제 모델이 사용할 옵티마이저와 손실 함수를 설정:
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

####################################### 검증 세트 만들기
x_val = train_data[:10000]
partial_x_train = train_data[10000:]

y_val = train_labels[:10000]
partial_y_train = train_labels[10000:]

####################################### 모델 훈련
'''
이 모델을 512개의 샘플로 이루어진 mini-batch 에서 40번의 에포크 동안 훈련한다. x_train과 y_train 텐서에 있는 모든 샘플에 대해 40번 반복한다는 뜻이다. 훈련하는 동안 10,000개의 검증 세트에서 모델의 손실과 정확도를 모니터링 한다.
'''
history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=40,
                    batch_size=512,
                    validation_data=(x_val, y_val),
                    verbose=1)

####################################### 모델 평가
results = model.evaluate(test_data,  test_labels, verbose=2)

print('loss, accuracy: ', results)


####################################### 정확도와 손실 그래프 그리기
history_dict = history.history
history_dict.keys()

import matplotlib.pyplot as plt

acc = history_dict['accuracy']
val_acc = history_dict['val_accuracy']
loss = history_dict['loss']
val_loss = history_dict['val_loss']

epochs = range(1, len(acc) + 1)

# "bo"는 "파란색 점"입니다
plt.plot(epochs, loss, 'bo', label='Training loss')
# b는 "파란 실선"입니다
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()


plt.clf()   # 그림을 초기화합니다

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()