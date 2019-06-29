# 190625 1-2강 Clustering

클러스터링 - 추천 시스템에 많이 쓰임



#### Partitional algorithms

전수조사는 시간이 많이 걸리기 때문에 일부만 조사함



#### K-means clustering

k개의 cluster로 나누기

처음에 랜덤하게 클러스터링 한 후 어디에 가까운지에 따라 다르게 assgin

다시 그룹을 지어 반복 작업

No change => stop



K-medoids - 실제 있는 데이터 중에 평균에 가장 가까이 있는 점을 사용. outlier가 있어도 큭 ㅔ영향받지 않게 된다.



#### Hierarchical Clustering

top-down < bottom-up 방식이 많이 이용된다.

n개의 클러스터로 시작 -> 가장 가까운 거리에 있는 한 쌍을 클러스터로 만듦

-> 또 다시 가장 가까운 거리 클러스터화 -> k개의 클러스터가 될 때까지 반복



#### Agglomerative Hierarchical Clustering Algorithms

Single-link - 클러스터 간 가장 가까운 점들의 거리 기준

complete-link - 클러스터 간 가장 먼 점들의 거리 기준

Average-link - 클러스터 간 잇는 선들의 길이 총합 평균

Mean-link - merge를 한 다음 모든 점들 간의 거리 평균

Centroid-link - 클러스터 별 중앙점 간의 거리 기준





## DBSCAN Clustering Algorithms

**Density-based algorithm**에 해당

Eps : 거리

MinPts : core point, border point

점 p로부터 Eps 거리만큼의 범위 내에 다른 점이 있으면 같은 그룹

density reachable - 찾아갈 수 있음

density-connected



두 가지 property를 만족해야한다

1. (Maximality) pi가 C에 속했고 pj가 pi로부터 density-reachable하면 pj도 C에 속함
2. (Connectivity) pi와 pj가 C에 속하면 pi와 pj과 density-connected



minimum number of points 이상이면 하나의 클러스터로 만들어주기

더 이상 늘릴 수 없으면 다른 점을 선택하여 새로 클러스터 만들기

![19062501](.\images\19062501.PNG)

epsilon과 MinPts를 다르게 설정함에 따라 다른 클러스터링 결과를 얻게 된다.





# 2강

## EM Clustering

#### Probabilistic Modeling for Generating Documents

Generative model - 모델에 의해 데이터들이 만들어져있다고 가정

데이터로부터 모델을 추론하고 싶다.

특정한 주머니 셋(hidden parameters)에서 현재의 공 구성이 나올 확률을 계산 -> 모든 확률을 곱해서 최종 확률을 얻는다. 

maximum likelihood - parameter로 미분을 해서 데이터셋을 얻을 확률을 가장 높이는 파라미터를 얻을 수 있다 -> parameter들이 converge 할 때 중단



#### Gaussian mixture: the weighted sum of k Gaussian probability distributions

![19062502](.\images\19062502.PNG)

역으로 생성 모델을 추정하는 것. 평균점, 표준편차, 모델이 선택될 확률 3가지를 추정해야 함

k개의 cluster라면 k개의 확률 분포를 찾아내자는 것

- 특정한 data point가 여러 분포에서 나올 수 있으므로 다 더해야 한다.

  ![19062503](.\images\19062503.PNG)

- 동시에 일어나야 하므로 그것들을 다시 다 곱한다.

  로그를 취하면 더하기로 바뀜

  ![19062504](.\images\19062504.PNG)

- 관측된 데이터 x가 특정 그룹에 속할 확률을 다음과 같이 정의할 수 있다.

  ![19062505](.\images\19062505.PNG)

- 최적화 산식

  ![19062506](.\images\19062506.PNG)
  ![19062506-2](.\images\19062506-2.PNG)![19062507](.\images\19062507.PNG)


![19062508](.\images\19062508.PNG)

- E-step, M-step의 식을 서로 대입하며 반복하다보면 특정한 값으로 수렴하게 된다.

![19062509](.\images\19062509.PNG)

- multidimension에서도 행렬을 활용하여 산식을 도출 가능
- 예제에 적용해보면 제대로 클러스터링해줌을 알 수 있다.



## Probabilistic Latent Semantic Indexing(PLSI)

- A generative model

![19062510](.\images\19062510.PNG)

- 문서를 쓰는 것을 가지고 모델링
- k개의 주제가 있고, 문서들을 주제로 클러스터링
- 매 단어를 글에 쓸 때마다 랜덤 주제 선택 -> 랜덤하게 단어 선택 했다고 가정

![19062511](.\images\19062511.PNG)



- log-likelihood - 단어가 나타날 때마다 단어의 확률을 곱함 - 지수로 나타난 횟수를 표시 -> 로그 하면 지수가 앞으로 나옴

  ![19062512](.\images\19062512.PNG)



- 문서가 나올 확률은 1/D로 모두 동일하므로 상수 취급 -> optimization 때 무시 가능

![19062513](.\images\19062513.PNG)

![19062514](.\images\19062514.PNG)

- EM algorithm - parameter를 랜덤하게 assign하고 두 식 사이를 왔다갔다 하며 최적해 converge

![19062515](.\images\19062515.PNG)



## Twitobi

팔로우하고 있는 정보 -> PLSI만으로 주제를 나타내기엔 무리가 있음

자기가 팔로우하고 있는 사람이 쓴 글을 보고 내가 글을 쓸 수도 있다 -> 팔로우하는 사람이 쓰는 주제 또한 고려해야 한다

- top-k followee recommendation problem
- top-k tweet recommendation problem

자신의 주제 distribution(확률 a)에서 주제를 선택할 수도 있고,

팔로우하는 사람의 주제 distribution(확률 1-a)에서 주제를 선택할 수도 있다.

p(f|u) : 팔로이에 의해 유저가 주제 선택에 영향을 받을 확률

마찬가지로 EM algorithm 사용 - converge 시 스탑

![19062516](.\images\19062516.PNG)

## Recommendation systems

- content based filtering method

  각 item 간의 similarity를 이용해서 추천

- collaborative filtering method

  비슷한 다른 유저와 동일하게 행동한다는 가정 -> User가 직접 점수를 매긴 item들에 대한 rating을 이용해서 추천



#### Collaborative filtering method

- memory based method - 데이터를 기반

  c, p matrix - 유저(각 행)끼리 내적하면 비슷한 물건일수록 값이 크게 나온다

- model based method - model 생성

  matrix factorization



#### Matrix Factorization

user x 평점 매트릭스라는 결과를 얻기 위해 어떤 user vector와 item vector를 곱해야 하는지를 구하는 문제 -> 구한 U와 V를 곱한 값으로 채워지는 값들이 추천할 수 있는 영화 정보

![19062517](.\images\19062517.PNG)

![19062518](.\images\19062518.PNG)



#### Improving Matrix Factorization with PLSI

- 평점이 있는 것들만 맞추면 되는데, 그 결과를 도출할 수 있는 값의 쌍은 여러가지가 있음. 
- 영화에 대한 summary 등 text data가 있으면 그걸 통해 주제를 찾고, 이걸 item vector(V)를 찾는 데에 써보자 -> 주제가 비슷한 영화들의 추천 확률을 높일 수 있을 듯

![19062519](.\images\19062519.PNG)

![19062520](.\images\19062520.PNG)















