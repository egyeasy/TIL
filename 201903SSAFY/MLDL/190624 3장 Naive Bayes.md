# 190624 3장 Naive Bayes

#### 이걸 배우는 이유

1. 모형 자체가 말이 된다 - 사람이라면 무얼 가지고 데이터를 이렇게 분류했을까? 직관적인 모델
2. 굉장히 많은 머신러닝 연구 및 응용 상황에서 이것을 기본 모형으로 씀.

결과가 그렇게 좋지는 않으나 성능의 baseline으로 씀



#### A problem for ML

분류 문제 - 인간들은 특정 분류에 대한 이유를 설명할 수 있음. 이런 방법을 써보자.



#### Features

성질, data detail

- we use features to simplify the classification and clustering problems
- 이미지, document 등을 숫자로 바꿔서 써야 한다.



#### Problems

- Digit Recognition

  숫자들의 이미지 

- Email spam filtering

  메일의 내용 텍스트 -> 어떻게 feature화 할 것인가?



#### Is he married?

사진을 보고 이 사람이 결혼했을지를 판단하는 문제

아이와 같이 있다. 선글라스와 모자를 쓰고 있다.



#### Simple Classification

![3-1](.\3-1.png)

P(S|M) : 결혼을 했는데 아이를 안고 있을 확률

P(F|M) : 결혼을 했는데 이런 스타일을 하고 있을 확률



#### Digit Recognizer - MNIST

8x8 grid에 각각의 픽셀에 번호를 매겨서 white~black scale로 나타냄. 단순화하여 0 또는 1(흰색, 검은색)이라고 하자.

![3-2](.\3-2.png)

Y는 클래스(0~9까지의 넘버)

3이 주어졌을 때 각 픽셀의 값이 0일 확률 or 1일 확률을 모두 곱하기

3일 때 어떤 픽셀이 1일 확률이 높을 것이고 어떤 픽셀이 0일 확률이 높을지



#### Non-uniform values

전화번호 데이터라면 0이 많을 것



#### How do we get those P(F|Y) tables?

- Empirically from Training Data. 1000개의 데이터에서 이 부분이 칠해져있었을 확률이 몇이었는지를 확인.
- Elicitationt : Expert에게 물어본다. 사진에서 이 부분이 이렇게 되어있을 때 이것이 종양일 확률이 얼마인가? to 의사



#### A Spam Filter

Spam일 때 "Free"라는 단어가 나올 확률

not Spam일 때 "hello"라는 단어가 나올 확률

CPT를 데이터로부터 empirically 얻을 수 있다.



1. Feature : 단어의 빈도 수. Free가 열번이 나왔다면 spam일 확률이 높을 것

2. word order - free의 의미가 다를 수 있음. 문맥의 문제.

   -> 하지만 나이브베이즈를 비롯한 단순한 텍스트 모델에서는 그걸 고려하지 않고
   	Bag-of-Words 모델(빈도만 측정) 사용



#### Overfitting

나이브베이즈에서도 문제가 될 수 있다.

잘못 찍힌 점인데 나올 확률이 0이라면 곱하기 0이 되어서 결과가 0이 됨 -> 절대 그럴수 없다는 결과가 도출되는 오류



#### 방지책 : Smoothing

단순한 해결법 - (몇번이나 나왔는지에 대한 실제 데이터) += 1

좀 더 잘해보자면 += k

-> 라플라스 Smoothing



#### Tuning on Held-out data

- Now we've got two kinds of unknowns
  - Parameters: the probabilities
  - Hyperparameters: +k와 같이 regularization에 들어가는 변수

- held-out data(validation data)가 따로 있다.

  training data - CPT, w를 학습하기 위한 데이터인 반면

  validation data - 람다, k와 같은 하이퍼파라미터 학습용 데이터

  test data - 학습한 파라미터들의 성능이 얼마나 좋은지 확인

  1000개 데이터 -> 800 train, 100 val, 100 test 등으로 사용



#### Baselines

베이스라인과의 비교가 중요하다.

 나이브베이즈는 베이스라인이 되곤 한다.

- Weak baseline : most frequent label classifier

  모든 메일이 스팸이 아니라고 답하는 모델

  모든 이미지를 강아지라고 답하는 모델(강아지가 전체 이미지 중 60%로 가장 빈번하게 나올 때)



#### What to do about Errors

- problem : spam이 여전히 남아있다면?

- need more features

  보낸 사람이 누구인지 등 활용

- 나이브베이즈는 flexible한 모델로 다양한 feature를 사용할 수 있지만, homogeneous cases에서 가장 잘 성ㅇ능을 낸다(e.g. 모든 feature가 1~10)



#### Features

- 나이브 베이즈 : feature가 random variable(조건부 확률)

  대부분의 classifier : real-valued functions

- feature를 선택하는 데에도 다른 classifier나 모델이 필요할 수 있다.

  이럴 때 domain knowledge가 중요함.



#### summary

- 베이즈룰은 조건부 확률을 사용
- 나이브 베이즈 가정은 모든 feature들이 주어진 class label에 대해 독립적일 것.
- We can build classifiers out of a naive Bayes model using training data
- Smoothing estimates(generalization)이 실제 시스템에서 중요





