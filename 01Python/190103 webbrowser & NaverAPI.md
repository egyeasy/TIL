# Webbrowser

- 파이썬에서 웹페이지 탐색을 더 쉽게 만들어줌

```python
import webbrowser

# 모모랜드 모든 멤버들의 검색 페이지를 한번에 여는 코드
# keyword = input("검색어를 입력해 주세요: ")

url = "https://search.daum.net/search?q="

# webbrowser.open(url)

momo = ["나윤", "혜빈", "아인", "낸시", "주이",
    "연우", "제인", "데이지", "태하"]

#momo라고 하는 리스트를 한번씩 돌면서 웹브라우저를 연다.

for member in momo:
    webbrowser.open(url + member)
```





# Naver API

### API - Application Programming Interface

Application : 어플리케이션에 대해/관하여
Programming : 코딩을 통해서 접근이 가능한
Interface : 사용자와 제품/서비스 간의 통로

- 일반적으로 key를 제공하고 그걸 발급 받아야 접근 가능



## Naver API 신청

- ide.c9.io 에서 github 아이디로 로그인
- create workspace -> blank 템플릿(우분투 리눅스 파이썬 설치돼있음)
- 만들어진 c9 서버 우측상단 share -> application이 공개 주소임
- 이 주소를 네이버 신청란에 입력



## Application 초기상태

#### Client ID / Client Secret은 정말 중요한 정보! 잘 숨겨둬야 함

우편 서비스 작동방식을 모르지만 편지봉투를 쓰는 법만 알면 된다. -> API 가이드라인도 마찬가지

결국은 특정 url을 어떤 서비스에 보내고 응답을 받게 되는 것.

python3의 pip를 쓰기 위해 c9 workspace 터미널에서

`sudo pip3 install requests`

이미 깔려있다.



### 복습 겸 테스트 코드

`$ python3 naver.py`

```python
import requests

# 사이트에서 클릭하는 대신 파이썬에서 웹에 요청하는 기능
url = "https://finance.naver.com/sise/"

response = requests.get(url) # 결과는 크롬 우클릭 페이지 소스 보기와 같음

print(response.text) # html문서가 text로 출력된다.
```



beautiful soup를 사용해서 html문서를 파싱하자.

`$ sudo pip3 install bs4`

```python
import requests
import bs4

# 사이트에서 클릭하는 대신 파이썬에서 웹에 요청하는 기능
url = "https://finance.naver.com/sise/"

response = requests.get(url)

doc = bs4.BeautifulSoup(response.text, 'html.parser')

# 크롬 > 요소 우클릭 > copy > copy selector -> 검색어를 찾을 수 있음
print(doc.select_one('#KOSPI_now').text) # 내용만 출력
```



## Papago NMT

'2. API 기본 정보'가 제일 중요하다!



### 서버에 대한 요청 방식 : GET과 POST

1. GET : 정보를 요청해서 '받아오는 것'이 목적인 요청 행위
2. POST : 정보를 입력, 게시하는 것이 목적인 요청 행위. ex) 로그인 시 아이디와 비번을 입력하는 것



### Request Headers

크롬 네이버 홈 네트워크 -> www.naver.com -> reuqests headers

1. :authority: www.naver.com
2. :method: GET
3. :path: /
4. :scheme: https
5. accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
6. accept-encoding: gzip, deflate, br
7. accept-language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
8. cache-control: max-age=0
9. cookie: npic=OAyVF4j6KOQBCrbqTahDdjpHvCZgrDP4hY6vr6tVE4j7p+RQTrG11JLwyvQoWMVgCA==; NNB=RZWNQRGYDUJFY; nx_ssl=2; nid_inf=2004575614; NID_AUT=Mv/GFuwIwdn5UN5K5U3uHsucFEZh2827qYHHfbZ9Jg+Lz7BiD9vU+VayLLiKoVvP; NID_JKL=SRKv3fjfEGia2bERtStDme+/+y4fijh4tKmFRxVrBaw=; PM_CK_rcode=09680101; page_uid=Uu2XcdpySDlssZDHuH4ssssssvw-163947; NID_SES=AAABnSXZtc+TdSUfzjFPaUjtwvZNl6HKuLEvLWMdToglHKQI+XcXLHcBo6emQKzicXlygk+dE4VLy2sUo3N/5I6CF7VDqxGNamEL4VZv8M7igKAiAWTDc2QZTUZZp7yKKCg19/T2MZ1AYFoAOj116guZkQa1Z+0OpbUQLLxS7WkbBcbm4kSGkHZzz5jsIYM+cmmdjVNOgmQI5snsB9dNBmk/4Ifmg58wq2gktKDDV/3Y2XpHk9v04JBg1RKt8vkSfsOY1+Fkl0tb4IYLeZ7s2Cln75YUXjC5JOR4X7vO1kJSxC52w1OcHJ3IzpyMOsaeAgAtDZyuEhYH+hN+fQzdJ7ePDgseLX3TM9wTWBqu7DzkyaOw5NJygJ+BQ76tN+lM9F/YRS64NzobqLbBEBZ1XFz4cHyEfIGTeIsnYxjDaGCDU5MdmdMbhRxuhKcvAhOHiVY/LBN3op2SOfxd8GZhaNhpKNel8tB3Pouz/tCU/hhNPtuCT4ZpssIojWIpGvHucdtijbzTUzG6zLBe1zbFDY04SWuNlNpDs5LnI2J/r8Uq/kCD; NIPD=1
10. referer: https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%BD%94%EC%8A%A4%ED%94%BC
11. upgrade-insecure-requests: 1
12. user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36



12 요청한 사람의 브라우저 정보까지 서버에 보내게 됨.



### 네이버에 API 요청해보기

- !! naver_secret은 절대 github에서 언급되지 않도록 할 것 !!

- 요청(POST) : Headers(요청자의 정보), 데이터(번역할 텍스트, 언어)

  예제 코드를 참조해서 포맷을 작성해볼 것
  요청자의 신원 정보는 headers, 다른 요청 정보는 data(페일로드)에 넣는다. -> 'rest API 표준' 검색해보면 될 것

```python
# 네이버(파파고)야 내가 단어 하나 전달할테니, 번역해줘


# 0. 사용자에게 단어를 입력 받는다.
# 1. papago API 요청 주소에 요청을 보낸다.
# 2. 응답을 받아 번역된 단어를 출력한다.

import requests

naver_id = ""
naver_secret = ""

# '2. API 기본정보'에서 복사한 요청 url
url = "https://openapi.naver.com/v1/papago/n2mt"

text = input('번역할 영어 단어 또는 문장을 입력해주세요.')

# 요청 예시를 참고하여 필요한 파라미터를 파악
headers = {
    'X-Naver-Client-Id': naver_id,
    'X-Naver-Client-Secret': naver_secret
}

data = {
    'source': 'en',
    'target': 'ko',
    'text': text
}

res = requests.post(url, headers=headers, data=data)

doc = res.json()
print(doc['message']['result']['translatedText'])
```

























