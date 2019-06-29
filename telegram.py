import requests
import json
import os

token = os.getenv('TELEGRAM_TOKEN')
# 받은 메시지를 저장
url = 'https://api.hphk.io/telegram/bot{}/getUpdates'.format(token) # 원래의 요청이 우회해서 보내진다. 원래껄로 하면 c9에서 막아놔서 요청이 안 됨.

response = json.loads(requests.get(url).text)['result'][-1]
print(response) #내가 텔레그램 봇에 메시지를 보내면 여기서 메시지 수신 파악이 된다.


#메시지 보내면 답변 주는 기능
url = 'https://api.hphk.io/telegram/bot{}/sendMessage'.format(token)
# 받는 사람 id
chat_id = response['message']['from']['id']
msg = response['message']['text']

requests.get(url, params = {"chat_id": chat_id, "text": msg})