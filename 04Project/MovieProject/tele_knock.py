import telegram, os, requests   #텔레그램 모듈을 가져옵니다.
import urllib.request

my_token = '812794335:AAF1mRDe2JYB922Mj3rAndK2TAQv7xU7LnI'   #토큰을 변수에 저장합니다.
bot = telegram.Bot(token = my_token)   #bot을 선언합니다.
updates = bot.getUpdates()  #업데이트 내역을 받아옵니다.

querys = []

for u in updates:   # 내역중 메세지를 출력합니다.
    querys.append(u.message['text'])
    print(u.message['text'])
    print(u.message)
    print()

querys.pop(0)
print(querys)


naver_id = 'd00SP7JEdZRtLTS28EmG'
naver_pw = 'Xt0R1rmu7w'


url_nav = "https://openapi.naver.com/v1/search/movie.json"

movieCd = "어벤져스".encode('utf-8')
# query_nav = "query="+movieCd
headers = {
    'X-Naver-Client-Id': naver_id,
    'X-Naver-Client-Secret': naver_pw,
}
params = {
    'query': movieCd
}
res_nav = requests.get(url_nav, headers=headers, params=params)
doc_nav = res_nav.json()
print(doc_nav)