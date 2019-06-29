from flask import Flask, render_template, request #request 추가
import requests
import time
from bs4 import BeautifulSoup as bs
import json

app = Flask(__name__)

@app.route('/')
def index():
    url = 'http://mblogthumb3.phinf.naver.net/20141013_10/kimin3400_1413165171761IOrIC_JPEG/20141008_212821.jpg?type=w2'
    return render_template('index.html')

@app.route('/lotto')
def lotto():
    # 챗봇 로또코드 복붙
    return render_template('lotto.html')

@app.route('/toon')
def toon():
    cat = request.args.get('type')
    toons = []
    if(cat == 'naver'):

        # 1. 네이버 웹툰을 가져올 수 있는 주소(url)을 파악하고 url 변수에 저장한다.
        today = time.strftime("%a").lower()
        print(today)
        url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week='+today
        
        # 2. 해당 주소로 요청을 보내 정보를 가져온다.
        response = requests.get(url).text
        
        # 3. 받은 정보를 bs를 이용해 검색하기 좋게 만든다.
        soup = bs(response, 'html.parser')
        # 4. 네이버 웹툰 페이지로 가서, 내가 원하는 정보가 어디에 있는지 파악한다.
        # 내가 원하는 정보는 웹툰을 볼 수 있는 링크, 웹툰의 제목 + 해당 웹툰의 썸네일(이미지의 주소)
        toons = []
        
        li = soup.select('.img_list li')
        length = 0
        for item in li:
            toon = {"title": item.select_one('dt a').text,
                "url": "https://comic.naver.com"+item.select('dt a')[0]["href"],
                "img_url": item.select('.thumb img')[0]["src"]}
            toons.append(toon)
            print(toon['url'])
    
    elif(cat == 'daum'):
        # 1. 내가 원하는 정보를 얻을 수 있는 주소를 url이라고 하는 변수에 담는다.
        today = time.strftime("%a").lower()
        url = 'http://webtoon.daum.net/data/pc/webtoon/list_serialized/'+today+'?'
        
        # 2. 해당 url에 요청을 보내 응답을 받아 저장한다.
        response = requests.get(url).json()
        
        # 3. 구글신에게 파이썬으로 어떻게 json을 파싱(딕셔너리 형으로 변환)하는지 물어본다.
        # 4. 파싱한다.(변환한다)
        # 5. 내가 원하는 데이터를 꺼내서 조합한다.
        data = response['data']
        toons = []
        for toon in data:
            toon_url = 'http://webtoon.daum.net/webtoon/view/'+ toon['nickname']
            one_toon = {"title": toon['title'],
                "url": toon_url,
                "img_url": toon['thumbnailImage2']['url']}
            print(one_toon["url"])
            toons.append(one_toon)
    return render_template('toon.html', cat = cat, t = toons)
    

@app.route('/apart')
def apart():
    # 1. 내가 원하는 정보를 얻을 수 있는 url을 url 변수에 저장한다.
    url = 'http://rt.molit.go.kr/new/gis/getDanjiInfoDetail.do?menuGubun=A&p_apt_code=2363&p_house_cd=1&p_acc_year=2018&areaCode=&priceCode='
    # 1-1. request header에 추가할 정보를 dictionary 형태로 저장한다.
    headers = {
        "Host": "rt.molit.go.kr",
        "Referer": "http://rt.molit.go.kr/new/gis/srh.do?menuGubun=B&gubunCode=LAND"
    }
    
    # 2. requests의 get 기능을 이용하여 해당 url에 header와 함께 요청을 보낸다.
    response = requests.get(url, headers = headers).json() # request 했을 때 서버에서 받는 정보의 이름도 headers, "DEAL_MM"(거래월)
    document = response['result']
    """
    response = requests.get(url, headers = headers).text
    document = json.loads(response)
    """
    results = {}
    for one in document:
        results['location'] = document['JIBUN_NAME']
        results['square'] = document['BLDG_AREA']
        results['sum_amt'] = document['SUM_AMT']
        results['deal_mm'] = document['DEAL_MM']
        results['deal_dd'] = document['DEAL_DD']
    
    # 3. 응답으로 온 코드의 형태를 살펴본다.(json/xml/html)
    return render_template('/apart.html', cat=name, results=results)
    
@app.route('/exchange')
def exchange():
    # 어느 사이트든
    url = 'https://spib.wooribank.com/pib/jcc?withyou=CMCOM0184&__ID=c012238'
    # 크롤링을 통해서 가장 많은 환율 정보를 끌어오시는 분께 커피
    response = requests.get(url).text
    soup = bs(response, 'html.parser')
    document = soup.select('tbody')[0]
    tr2 = document.select('tr')
    count = 0;
    for country in tr2:
        if (country.select('td')[1].text == 'GOLD 1g'):
            break
        print(country.select('td')[1].text)
        print(country.select('td')[9].text)
        count += 1
    print("총 {}개".format(count))

    
    return render_template('exchange.html', res=response)

@app.route('/exchange2')
def exchange2():
    # 어느 사이트든
    url = 'https://www.xe.com/currencytables/?from=KRW&date=2018-12-20'
    # 크롤링을 통해서 가장 많은 환율 정보를 끌어오시는 분께 커피
    response = requests.get(url).text
    soup = bs(response, 'html.parser')
    print(soup)
    # document = soup.select('tbody')[0]
    # tr2 = document.select('tr')
    # count = 0;
    # for country in tr2:
    #     print(country.select('td')[1].text)
    #     print(country.select('td')[9].text)
    #     count += 1
    # print("총 {}개".format(count))

    
    return render_template('exchange.html', res=response)
