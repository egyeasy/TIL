from bs4 import BeautifulSoup as bs
import requests

def master_key_info(cd):
    url = "http://www.master-key.co.kr/booking/booking_list_new"
    params = {
        'date': '2018-12-22',
        'store': cd, #지점 위치
        'room': ''
    }
    response = requests.post(url, params).text
    document = bs(response, 'html.parser')
    ul = document.select('.reserve .escape_view')
    
    theme_list = []
    for li in ul:
        title = li.select('p')[0].text
        info = ''
        for col in li.select('.col'):
            info = info + '{} - {}\n'.format(col.select_one('.time').text, col.select_one('.state').text)
        theme = {
            'title': title,
            'info': info
        }
        theme_list.append(theme)
        
    print(theme_list)

def master_key_list():
    url = 'http://www.master-key.co.kr/home/office'

    response = requests.get(url).text
    
    document = bs(response, 'html.parser')
    
    # ul = document.select('.escape_list') #지점들의 리스트를 클래스로 검색 -> ul 태그 시작부터 끝까지 전체 하나로 나옴
    
    lis = document.select('.escape_list .escape_view')
    cafe_list = []
    for li in lis:
        title = li.select_one('p').text
        # python how to eliminate string from string
        if(title.endswith('NEW')):
            title = title[:-3]
        address = li.select('dd')[0].text
        tel = li.select('dd')[1].text
        link = 'http://www.master-key.co.kr' + li.select_one('a')["href"]
        cafe = {
            'title': title,
            'tel': tel,
            'address': address,
            'link': link
        }
        cafe_list.append(cafe)
    
    return cafe_list

# 사용자로부터 '마스터키 ****점'이라는 메시지를 받으면
print(master_key_info(21))

# 해당 지점에 대한 오늘의 정보를 요청하고(크롤링)

# 메시지(예약정보)를 보내준다.



for cafe in master_key_list():
    print('{}: {}'.format(cafe["title"], cafe["link"].split('=')[1]))