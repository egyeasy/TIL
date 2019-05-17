import telegram  # python-telegram-bot 라이브러리
from telegram.ext import Updater, MessageHandler, Filters
import os, requests

my_token = '812794335:AAF1mRDe2JYB922Mj3rAndK2TAQv7xU7LnI'  # 토큰을 변수에 저장
bot = telegram.Bot(token = my_token)  # bot 선언


# 1. 챗봇 꺼져있는 동안 업데이트된 메시지 보여주기
updates = bot.getUpdates()  #업데이트 내역 받아오기
querys = []

print("========== 받은 메시지(첫번째 메시지는 API Key) ============")
for u in updates:  # 메시지 출력
    print("u", u)
    querys.append(u.channel_post['text'])
    print(u.channel_post['text'])
    print()

print("메시지 리스트:", querys)



# 3. Naver 영화검색 API
naver_id = 'd00SP7JEdZRtLTS28EmG'
naver_pw = 'Xt0R1rmu7w'

url_nav = "https://openapi.naver.com/v1/search/movie.json"

query_text = "투모로우"
movieCd = query_text.encode('utf-8')
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
print("========= 검색결과 =========")
for mov in doc_nav['items']:
    print(mov)
    print()


# 2. 메시지 받았을 때 반응하는 기능 - 갠톡으로 봇에게 메시지를 보내면 똑같이 따라함
def get_message(bot, update) :
    update.message.reply_text("got text")
    update.message.reply_text(update.message.text)
    

updater = Updater(my_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()
