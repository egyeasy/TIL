# 190624 4장 Neural Network 및 NLP

## Word, Sentence, and Document Embedding

모든 과정들에서 의미를 추출해내는 것이 중요함.

최근 연구에서 중요한 것이 Embedding

word embedding을 살펴 보겠다.



#### Word Vector Representations : "Word Embedding"

document word matrix : 각각의 document마다 단어별로 빈도 수를 정리한 2차원 matrix

(e.g. 1번 다큐먼트에서 dog는 1번 나옴) -> one-hot encoding -> hi와 hello는 비슷한 단어. one-hot에서는 단어간의 관계를 고려할 수 없음

그래서 나온 것이 word vector representations

- 하나의 단어가 하나의 vector가 됨

- Continuous (dense) Vector Representations

  where : [6.2, 1.0, 2.4, 3.3, ..., 3.5]

- One-hot Vector Representations

  where : [0.0, 1.0, 0.0, 0.0, ..., 0.0]



#### Continuous Vector Representation

- 벡터 공간 상에서 cat은 cats와 가까이에 위치해있다.

- cat -> cats, dog -> dogs로 가는 방향과 거리가 같다.

  Paris -> France, London -> England도 마찬가지



#### Representations

Hypothetical internal cognitive symbol that represents external reality

사람이 사물을 인지하는 방식을 모방. furniture라는 큰 클래스 안에 의자, 옷장, 테이블을 포함시킴



#### Distributed Representations

**many-to-many relationship**:

- a concept - many neurons

- a neuron - many concepts로 나타내어질 수 있다.

![4-1](.\4-1.png)



#### Distributional Hypothesis

"Words that occur in the same contexts tend to have similar meanings"

문맥을 보면 단어의 뜻을 알 수 있다.

puppy is cute, kitten is cute, baby is cute -> puppy, kitten, baby를 word vector 상에서 비슷한 공간상에 위치시킴

![4-2](.\4-2.png)



#### Word2Vec

이걸 실제 벡터로 구현한 유명한 버전

두 가지 실제 구현 모델이 있음

1. CBOW

   양 사이드의 단어가 주어지고 가운데의 단어가 무엇인지 예측하는 모델

2. Skip-Gram

   가운데 단어가 주어지고 그 주변의 단어들을 예측



#### Evaluation 1: Word Similarity Task

인간이 평가하는 유사도(소년-청년, 식품-수탉)를 측정.

벡터 상에서의 cosine similarity를 측정하여 얼마나 비슷한지 비교



#### Evaluation 2: Word Analogy Task

King : Queen = Man : ?

Walking : Walked = Swimming : ?

Spain : Madrid = ? : Italy

?를 찾아내는 task로 성능 측정



#### Problems of word-level approach

- Out-of-vocabularies : 학습 때 한번도 나온 적이 없는 단어.

  Morphologically rich languages : 예쁘다, 예쁜, 예쁨, 예뻤다

  Compositionality of words : 미인 = 예쁜 사람. 미인을 본 적이 없더라도 예쁜, 사람을 학습했다면 의미를 알 수 있어야 함

- rare words : 적은 횟수로 나온 단어들에 대해서는 성능이 좋지 않게 나올 수 있다



이를 해결하기 위해 word가 아니라 다른 unit들에 대해서도 embedding을 함

Skip Gram vs FastText

#### Subword information Skip-Gram(a.k.a FastText) by Facebook

예쁨 : ㅇ ㅖ ㅃ ㅡ ㅁ 으로 나누고 여러 개씩 묶어서 학습 -> 새로운 단어도 더 예측을 잘학 ㅔ됨





#### 2018 NLP Trend : Transfer Learning from Language Models

Elmo & Bert가 가장 핫한 모델



#### Contextualized Word Embedding

"I **left** my phone on the **left** side of the room"

엘모에서는 양 옆에 어떤 단어가 나오는지를 고려 -> 다른 embedding의 단어로 분류



#### model overview

input이 I, left, my 등으로 각각의 단어가 들어가게 됨

Lstm을 활용해 my를 학습할 때 앞에 나온 단어들(I, left) 또한 함께 고려

![4-3](.\4-3.png)



#### "Transformers" as a Bidirectional Language Model

엘모는 단어가 가진 의미 뿐만 아니라 단어가 어떤 문맥에서 나왔는지를 캡쳐하는 모델

but 두 가지 문제가 여전히 존재.

document에서는 처음에 나왔던 단어의 의미는 뒤로 갈수록 희미해짐. 따라서 가까이 있는 단어들을 중요하게 여기는 모델

but 한국어 등에서는 어순 때문에 가까이 있다고 해서 연관이 높다고 볼 수도 없는 경우가 있음

=> 긴 sequence에 대해 잘 학습하지 못함

=> 그래서 등장하는 것이 transformer : 각각의 단어마다 중요하게 여겨지는 단어가 다른 위치에 등장한다.

(self-attention) e.g. eat은 apple과 멀리 있더라도 연관성이 있는 걸로 캡쳐함

(bidirectional) 문장의 앞에서 뒤로 가는 것 뿐만 아니라 앞으로의 문맥 또한 살펴보자.



bert는 2018년에 나온 굉장히 최신 모델

다양한 task에 활용 중



#### Elmo, Bert 뿐만 아니라 GPT도 있음

ELMo - Lstm + 단방향

GPT는 하나의 유닛이 Transformer. but 방향성이 하나

BERT - Transformer + 양방향



#### BERT inputs

단어 임베딩이 들어가는 것은 마찬가지인데,

Position Embeddings - bidirection을 반영하기 위함



#### BERT usage

(a) 두 개의 sentence가 주어졌을 때 이게 어떤 관계인지

(b) single sentence classification tasks - positive/negative 판단

(c) question answering tasks

(d) single sentence tagging tasks - "Michael likes you에서 Michael는 name에 해당한다"