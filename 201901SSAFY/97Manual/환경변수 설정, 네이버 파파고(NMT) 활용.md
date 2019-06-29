# 네이버 환경변수 설정, 번역(NMT) 활용

### 설정

`$ vi ~/.bashrc`

```vim
# 맨 아래에
export NAVER_ID="아이디"
export NAVER_PW="비번"
```

`$ source ~/.bashrc`



### 불러올 때

```python
import os

naver_id = os.getenv("NAVER_ID")
naver_secret = os.getenv("NAVER_PW")
```



### POST(파파고 NMT API)

인자 : headers, data

```python
url = "https://openapi.naver.com/v1/papago/n2mt"

headers = {
    'X-Naver-Client-Id': naver_id,
    'X-Naver-Client-Secret': naver_secret
}

data = {
    'source': 'ko',
    'target': 'en',
    'text': text
}

res = requests.post(url, headers=headers, data=data)
doc = res.json()

result = doc['message']['result']['translatedText']
```

​

### GET(이미지 검색 API)

인자 : headers, params

```python
# naver image API
naver_id = os.getenv("NAVER_ID")
naver_pw = os.getenv("NAVER_PW")
print(naver_id, naver_pw)

url = "https://openapi.naver.com/v1/search/image.json"

headers = {
    'X-Naver-Client-Id': naver_id,
    'X-Naver-Client-Secret': naver_pw
}

params = {
    'query': job,
    'display': 1
}

res = requests.get(url, headers=headers, params=params)
doc = res.json()
nav_url = doc['items'][0]['link']
```

