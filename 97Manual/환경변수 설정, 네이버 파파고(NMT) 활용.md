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



### 활용

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

