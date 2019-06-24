# 190624 2장 Linear Regression

회귀는 지도학습에 해당.

지도학습 중 많은 형태를 회귀를 사용함.

Line fitting이라고 봐도 됨. 주어진 데이터에 대해 특정한 실수 값을 내주는 모델.

주택 가격 예측, customer가 매장에서 쓸 금액 예측 등

지도 학습에 해당하는 이유 - 주어진 데이터의 모든 y값을 알고 있음



#### Modeling non-linear relationships

![2-1](.\2-1.png)



#### Polynomial regression

1차원으로 잘 설명되지 않는 데이터에 좀 더 적합하게 line을 그을 수 있다. 



#### multivariate linear regression

다변수 regression도 가능하다 -> 입체적인 그래프



#### Maximum likelihood estimation

가장 적합한 계수를 찾기



#### Residual Sum of Squares

![2-2](.\2-2.png)

RSS(Residual Sum of Squares) - 모델과 실제 데이터의 오차의 합. 모델이 얼마나 설명력이 있는지를 나타냄



#### Ridge Regression

MLE can overfit - 지나치게 데이터에 맞출 수 있다. 이 때 regularization - 심플한 것이 좋다.계수

복잡한 모델에서는 계수들이 굉장히 크게 나온다 -> 이걸 줄이기 위해 penalty를 부여

![2-3](.\2-3.png)

이를 통해 좀 더 smooth한 선을 얻을 수 있다.

1) l2 norm을 활용하든지, 2) 데이터가 크다면 자연스럽게 regularization 가능



#### Regularization effect of big data

적어도 트레이닝 데이터에 대해서는 맞춰야 하는데, 1차원 모델로는 이걸 잘 못하고 있음.

2차원에서는 훨씬 좋고, 데이터셋이 커짐에 따라 성능이 좋아짐을 알 수 있다(120 - 180 데이터)

모델 degree 10일 때 test data와 training data의 차이가 굉장히 큼을 알 수 있다. 그래도 데이터가 많으면 성능이 괜찮게 나옴.

degree 25하면 데이터셋 커져도 문제가 잘 해결되지 않음 -> 모델이 너무 복잡하면 안 된다.

