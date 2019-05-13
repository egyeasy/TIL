import telegram  # python-telegram-bot 라이브러리
from telegram.ext import Updater, MessageHandler, Filters
import os, requests, json
from bs4 import BeautifulSoup


my_token = '812794335:AAF1mRDe2JYB922Mj3rAndK2TAQv7xU7LnI'  # 토큰을 변수에 저장
bot = telegram.Bot(token = my_token)  # bot 선언


# 1. 챗봇 꺼져있는 동안 업데이트된 메시지 보여주기
# updates = bot.getUpdates()  #업데이트 내역 받아오기
# querys = []

# print("========== 받은 메시지(첫번째 메시지는 API Key) ============")
# for u in updates:  # 메시지 출력
#     querys.append(u.message['text'])
#     print(u.message['text'])
#     print()

# print("메시지 리스트:", querys)



# 3. Naver 영화검색 API






# 4. 4개 채널 편성표 크롤링
def find_movie(query_movie):
    # python file의 위치
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # print(table.prettify())

    # 목표 : 한 방송사가 한 행, 시간이 칼럼
    # date도 넣어주어야
    # db에 넣을 때 date, 방송사, 시간 - 영화 pair
    # '선샤인<1부>'같은건 링크 없으면 못 찾을 듯
    source = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=cgv+편성표').text
    soup = BeautifulSoup(source, "html.parser")
    data = {}

    Days = soup.find('div', class_="tbl_head head_type2")
    dayList = []
    for day in Days.find_all('span'):
        # day.span.text하니까 여러 개가 뽑혀서 이렇게
        if len(day.text) == 5:
            # print(day, day.text)
            data[day.text] = {'cgv':{}, 'ocn' : {}, 'super_action' : {}, '스크린': {}}
            dayList.append(day.text)

    for channel in ['ocn', 'cgv', 'super+action', '스크린']:
        source = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={}+편성표'.format(channel)).text
        soup = BeautifulSoup(source, "html.parser")

        table = soup.find('table', class_="tbl")
        if channel == 'super+action':
            channel = 'super_action'
        for tr in table.tbody.find_all('tr'):
            hour = tr.th.text[:3]
            # print(hour)
            i = 0
            for td in tr.find_all('td'):
                data[dayList[i]][channel][hour] = ''
                if td.dl:  # 이 시간에 새롭게 시작하는 영화가 있으면
                    minute = td.dl.dt.text  # 몇 분 시작인지 구하고
                    # 링크가 달려있는지, 영화인지 확인
                    if td.dl.dd.a and "tv-program" not in td.dl.dd.a.get('href'):
                        title = td.dl.dd.a.text
                        data[dayList[i]][channel][hour] = minute + ' ' + title
                i += 1

    print(data)

    # with open(os.path.join(BASE_DIR, 'schedule.json'), 'w+', encoding="utf-8") as json_file:
    #     # 화면에 직접 출력할 때는 dumps, file로 저장할 때는 dump
    #     json.dump(data, json_file, ensure_ascii=False, indent="\t")


    # 5. 텔레그램 메시지로 입력받은 영화를 편성표에서 검색
    found_movies = []
    for date in data:
        for channel in data[date]:
            for hour, movie_str in data[date][channel].items():
                splited = movie_str.split()
                if splited:
                    if splited[-1] == '<2부>':
                        continue
                    elif splited[-1] == '<1부>':
                        splited.pop(-1)
                    compressed_movie_str = ''.join(splited)
                    if query_movie in compressed_movie_str:
                        start_time = hour + ":" + compressed_movie_str[:2]
                        movie_name = ' '.join(splited[1:])
                        print(date, start_time, channel, movie_name)
                        # found_movies.append({'date': date, 'channel': channel, 'time': start_time, 'title': movie_name})
                        found_movies.append([date, start_time, channel, movie_name])

    # 날짜 시간 순으로 정렬
    # print((''.join(found_movies[0][0].split('.')), ''.join(found_movies[0][1].split(':')).strip()))
    found_movies.sort(key=lambda x: (int(''.join(x[0].split('.'))), int(''.join(x[1].split(':')).strip())))
    # print(found_movies)

    # print("response")
    # response = "{}에 대한 편성표 검색 결과 :\n".format(query_movie)   
    # for found in found_movies:
    #     print(found)
    #     response += ' '.join(found) + '\n'
    # print("response", response)
    
    return found_movies





# 2. 메시지 받았을 때 반응하는 기능 - 갠톡으로 봇에게 메시지를 보내면 똑같이 따라함
def get_message(bot, update) :
    query = update.message.text
    compressed_query = ''.join(list(query.strip().split()))
    founds = find_movie(compressed_query)
    response = "'{}'에 대한 편성표 검색 결과 :\n".format(query)
    for found in founds:
        response += ' '.join(found) + '\n'
    update.message.reply_text(response)
    # update.message.reply_text(update.message.text)
    

updater = Updater(my_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()