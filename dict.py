"""
파이썬 dictionary 활용 기초!
"""

# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q1=====")
summ = 0
avg = 0
for key in iu_score.keys():
    summ += iu_score[key]
avg = summ/len(iu_score)
print(avg)

scores = list(iu_score.values())
print(sum(scores)/len(scores))





# 2. 반 평균을 구하세요.
score = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}
# 답변 코드는 아래에 작성해주세요.
print("=====Q2=====")
summ = 0
sums = {}
avg = 0
avgs = {}
for classs in score.keys():
    summ = 0
    for key in score[classs].keys():
        summ += score[classs][key]
    avgs[classs] = summ/len(score[classs])
    print("{}반 평균: {}".format(classs, avgs[classs]))


for cl in score:
    tmp = list(score[cl].values())
    print("{}: {}".format(cl, sum(tmp)/len(tmp)))

# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
city = {
    "서울": [-6, -10, 2],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -10, 10],
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q3=====")
summ = 0
avg = 0
avgs = {}
for one_city in city.keys():
    summ = 0
    for value in city[one_city]:
    # 도시별로 총 온도 합을 구한다
        summ += value
    # 평균을 구한다
    avg = round(summ/3, 2)
    
    # dict에 넣는다
    avgs[one_city] = avg
    print("{} : {}".format(one_city, avg))
    
# 풀이
for cit in city:
    temp = city[cit]
    print("{}의 평균기온: {}".format(cit, round(sum(temp)/len(temp), 1)))
    print("{}의 평균기온: {:0.1f}".format(cit, sum(temp)/len(temp)))

# round/ceil/floor


# 답변 코드는 아래에 작성해주세요.
print("=====Q3-1=====")
#min, max 정의
minn = 0
maxx = 0
city_min = []
city_max = []
#서울 첫번째를 가장 추운 곳, 더운 곳으로 잡는다.
minn = city[list(city.keys())[0]][0]
maxx = city[list(city.keys())[0]][0]
city_min.append(list(city.keys())[0])
city_max.append(list(city.keys())[0])

#도시 내, 도시 별 for 문 돌면서 최소 최대값을 갱신한다.
for one_city in city.keys():
    for value in city[one_city]:
        if value == maxx:
            if not one_city in city_max:
                city_max.append(one_city)
        elif value > maxx:
            maxx = value
            city_max = []
            city_max.append(one_city)
        if value == minn:
            if not one_city in city_min:
                city_min.append(one_city)
        elif value < minn:
            minn = value            
            city_min = []
            city_min.append(one_city)

#출력
print("가장 추웠던 곳: {} {}, 가장 더웠던 곳: {} {}".format(city_min, minn, city_max, maxx))

# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.
print("=====Q4=====")
quest_city = "서울"
quest_value = 2
answer = "아니요"
for value in city[quest_city]:
    if value == quest_value:
        answer = "네"
print(answer)