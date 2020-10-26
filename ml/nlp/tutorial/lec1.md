딥러닝을 이용한 자연어 처리 입문 (https://wikidocs.net/book/2155)

##========Part 1. 기본 과정========
###01. 자연어 처리(natural language processing)란?
	1) 아나콘다(Anaconda)와 코랩(Colab)
	2) 필요 프레임워크와 라이브러리
	3) 자연어 처리를 위한 NLTK와 KoNLPy 설치하기
	4) 판다스(Pandas) and 넘파이(Numpy) and 맷플롭립(Matplotlib)
	5) 판다스 프로파일링(Pandas-Profiling)
	6) 머신 러닝 워크플로우(Machine Learning Workflow)
###02. 텍스트 전처리(Text preprocessing)
	01) 토큰화(Tokenization)
	02) 정제(Cleaning) and 정규화(Normalization)
	03) 어간 추출(Stemming) and 표제어 추출(Lemmatization)
	04) 불용어(Stopword)
	05) 정규 표현식(Regular Expression)
	06) 정수 인코딩(Integer Encoding)
	07) 패딩(Padding)
	08) 원-핫 인코딩(One-Hot Encoding)
	09) 데이터의 분리(Splitting Data)
	10) 한국어 전처리 패키지(Text Preprocessing Tools for Korean Text)
###03. 언어 모델(Language Model)
	1) 언어 모델(Language Model)이란?
	2) 통계적 언어 모델(Statistical Language Model, SLM)
	3) N-gram 언어 모델(N-gram Language Model)
	4) 한국어에서의 언어 모델(Language Model for Korean Sentences)
	5) 펄플렉서티(Perplexity)
	6) 조건부 확률(Conditional Probability)
###04. 카운트 기반의 단어 표현(Count based word Representation)
	1) 다양한 단어의 표현 방법
	2) Bag of Words(BoW)
	3) 문서 단어 행렬(Document-Term Matrix, DTM)
	4) TF-IDF(Term Frequency-Inverse Document Frequency)
###05. 문서 유사도(Document Similarity)
	1) 코사인 유사도(Cosine Similarity)
	2) 여러가지 유사도 기법
###06. 토픽 모델링(Topic Modeling)
	1) 잠재 의미 분석(Latent Semantic Analysis, LSA)
	2) 잠재 디리클레 할당(Latent Dirichlet Allocation, LDA)
	3) 잠재 디리클레 할당(LDA) 실습2
###07. 머신 러닝(Machine Learning) 개요
	1) 머신 러닝이란(What is Machine Learning?)
	2) 머신 러닝 훑어보기
	3) 선형 회귀(Linear Regression)
	4) 로지스틱 회귀(Logistic Regression) - 이진 분류
	5) 다중 입력에 대한 실습
	6) 벡터와 행렬 연산
	7) 소프트맥스 회귀(Softmax Regression) - 다중 클래스 분류
###08. 딥 러닝(Deep Learning) 개요
	1) 퍼셉트론(Perceptron)
	2) 인공 신경망(Artificial Neural Network) 훑어보기
	3) 딥 러닝의 학습 방법
	3-4) 역전파(BackPropagation) 이해하기
	4) 과적합(Overfitting)을 막는 방법들
	5) 기울기 소실(Gradient Vanishing)과 폭주(Exploding)
	6) 케라스(Keras) 훑어보기
	6-7) 케라스의 함수형 API(Keras Functional API)
	7) 다층 퍼셉트론(MultiLayer Perceptron, MLP)으로 텍스트 분류하기
	8) 피드 포워드 신경망 언어 모델(Neural Network Language Model, NNLM)
###09. 순환 신경망(Recurrent Neural Network)
	1) 순환 신경망(Recurrent Neural Network, RNN)
	2) 장단기 메모리(Long Short-Term Memory, LSTM)
	3) 게이트 순환 유닛(Gated Recurrent Unit, GRU)
	4) RNN 언어 모델(Recurrent Neural Network Language Model, RNNLM)
	5) RNN을 이용한 텍스트 생성(Text Generation using RNN)
	6) 글자 단위 RNN(Char RNN)
###10. 워드 임베딩(Word Embedding)
	1) 워드 임베딩(Word Embedding)
	2) 워드투벡터(Word2Vec)
	3) 영어/한국어 Word2Vec 실습
	4) Word2Vec 구현하기(Skip-Gram with Negative Sampling, SGNS)
	5) 글로브(GloVe)
	6) 사전 훈련된 워드 임베딩(Pre-trained Word Embedding)
	7) 엘모(Embeddings from Language Model, ELMo)
	8) 임베딩 벡터의 시각화(Embedding Visualization)
###11. RNN을 이용한 텍스트 분류(Text Classification)
	1) 케라스를 이용한 텍스트 분류 개요(Text Classification using Keras)
	2) 스팸 메일 분류하기(Spam Detection)
	3) 로이터 뉴스 분류하기(Reuters News Classification)
	4) IMDB 리뷰 감성 분류하기(IMDB Movie Review Sentiment Analysis)
	5) 나이브 베이즈 분류기(Naive Bayes Classifier)
	6) 네이버 영화 리뷰 감성 분류하기(Naver Movie Review Sentiment Analysis)
	7) 네이버 쇼핑 리뷰 감성 분류하기(Naver Shopping Review Sentiment Analysis)
	8) BiLSTM으로 한국어 스팀 리뷰 감성 분류하기
###12. NLP를 위한 합성곱 신경망(Convolution Neural Network) - 작성 중 챕터
	1) 합성곱 신경망(Convolution Neural Network)
	2) 자연어 처리를 위한 1D CNN
	3) 1D CNN으로 IMDB 리뷰 분류하기
	4) 1D CNN으로 스팸 메일 분류하기
	5) Multi-Kernel 1D CNN으로 네이버 영화 리뷰 분류하기
	6) 사전 훈련된 워드 임베딩을 이용한 의도 분류(Intent Classification using Pre-trained Word Embedding)
###13. 태깅 작업(Tagging Task)
	1) 케라스를 이용한 태깅 작업 개요(Tagging Task using Keras)
	2) 양방향 LSTM을 이용한 품사 태깅(Part-of-speech Tagging using Bi-LSTM)
	3) 개체명 인식(Named Entity Recognition)
	4) 개체명 인식의 BIO 표현 이해하기
	5) 양방향 LSTM을 이용한 개체명 인식(Named Entity Recognition using Bi-LSTM)
	6) 양방향 LSTM과 CRF(Bidirectional LSTM + CRF)
	7) 양방향 LSTM과 글자 임베딩(Char embedding)
##========Part 2. 심화 과정========
###14. 서브워드 토크나이저(Subword Tokenizer)
	01) 바이트 페어 인코딩(Byte Pair Encoding, BPE)
	02) 센텐스피스(SentencePiece)
	03) 서브워드텍스트인코더(SubwordTextEncoder)
###15. RNN을 이용한 인코더-디코더
	1) 시퀀스-투-시퀀스(Sequence-to-Sequence, seq2seq)
	2) Word-Level 번역기 만들기(Neural Machine Translation (seq2seq) Tutorial)
	3) 간단한 seq2seq 만들기(Simple seq2seq)
	4) BLEU Score(Bilingual Evaluation Understudy Score)
###16. 어텐션 메커니즘 (Attention Mechanism)
	1) 어텐션 메커니즘 (Attention Mechanism)
	2) 바다나우 어텐션(Bahdanau Attention)
	4) 양방향 LSTM과 어텐션 메커니즘(BiLSTM with Attention mechanism)
###17. 트랜스포머(Transformer)
	1) 트랜스포머(Transformer)
###18. 텍스트 요약(Text Summarization)
	1) 어텐션을 이용한 텍스트 요약(Text Summarization with Attention mechanism)
	2) 문장 임베딩 기반 텍스트 랭크(TextRank Based on Sentence Embedding)
###19. 질의 응답(Question Answering, QA)
	1) 메모리 네트워크(Memory Network, MemN)를 이용한 QA
	2) MemN으로 한국어 QA 해보기

