# 텔레그램 편성표 봇 개발

## 1. 목표

- 낙낙(Knock Knock) 서비스의 MVP 텔레그램 봇을 개발한다.
- 사용자가 입력하는 영화 검색어에 해당하는 영화가 채널 CGV의 편성표에 존재하는지 여부, 존재한다면 언제 방영하는지를 알려주도록 한다.



## 2. 레퍼런스

<https://blog.psangwoo.com/coding/2016/12/08/python-telegram-bot-1.html>



## 3. 구현 사항

### 환경

Python, Naver 검색 API

pip modules : python-telegram-bot, requests

### Knock Knock 봇 등록

1. <https://telegram.me/botfather> 접속

2. 채팅창에 다음을 입력하여 봇을 생성한다.

   ```python
   /newbot  # 새로운 봇 생성 명령어
   KnockKnock 영화 편성표 알리미  # 채팅방에서 보이는 봇 이름
   KnockAlarmBot  # 봇의 채팅방 url
   ```

   입력하면 다음과 같은 메시지를 얻을 수 있다.

   ```txt
   Done! Congratulations on your new bot. You will find it at t.me/KnockAlarmBot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.
   
   Use this token to access the HTTP API: <비공개처리>
   Keep your token secure and store it safely, it can be used by anyone to control your bot.
   
   For a description of the Bot API, see this page: https://core.telegram.org/bots/api
   ```



### 채널 생성

1. 개인 텔레그램 아이디에서 채널 생성

2. 비공개 채널

   https://t.me/joinchat/AAAAAENiCbFNaZxigXhAJA

3. info -> add administer -> 만들어준 봇 추가

4. info -> 채널 public으로 전환 -> 채팅방 링크 : t.me/movie_schedule



### 봇에게 말하기 하기 url

다음과 같은 형식으로 보내면 text를 해당 채널에 보낸다.

`<https://api.telegram.org/bot<APIkey>/sendMessage?chat_id=@movie_schedule&text=123>`



### 봇에게 채팅 듣게 하기

```python
import telegram  # python-telegram-bot 라이브러리
from telegram.ext import Updater, MessageHandler, Filters
import os, requests

my_token = ''  # 토큰을 변수에 저장
bot = telegram.Bot(token = my_token)  # bot 선언


# 1. 챗봇 꺼져있는 동안 업데이트된 메시지 보여주기
updates = bot.getUpdates()  #업데이트 내역 받아오기
querys = []

print("========== 받은 메시지(첫번째 메시지는 API Key) ============")
for u in updates:  # 메시지 출력
    querys.append(u.message['text'])
    print(u.message['text'])
    print()

print("메시지 리스트:", querys)


# 2. 메시지 받았을 때 반응하는 기능 - 갠톡으로 봇에게 메시지를 보내면 똑같이 따라함
def get_message(bot, update) :
    update.message.reply_text("got text")
    update.message.reply_text(update.message.text)
    

updater = Updater(my_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()
```





### Naver API 등록

- localhost에서 API 이용이 가능하게 하려면 WEB 서비스 환경에 'http://127.0.0.1'을 추가해줘야 한다.
- 나중엔 API key를 환경변수로 저장해서 쓰도록 하자.
- 검색어를 utf-8으로 인코딩해줘야 한다.

```python
# 3. Naver 영화검색 API
naver_id = ''
naver_pw = ''

url_nav = "https://openapi.naver.com/v1/search/movie.json"

movieCd = "어벤져스".encode('utf-8')
headers = {
    'X-Naver-Client-Id': naver_id,
    'X-Naver-Client-Secret': naver_pw,
}
params = {
    'query': movieCd
}
res_nav = requests.get(url_nav, headers=headers, params=params)
doc_nav = res_nav.json()

print()
print("========= '어벤져스' 검색결과 =========")
for mov in doc_nav['items']:
    print(mov)
    print()
```















