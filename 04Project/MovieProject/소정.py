# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import os

# python file의 위치
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(table.prettify())

# 목표 : 한 방송사가 한 행, 시간이 칼럼
# date도 넣어주어야
# db에 넣을 때 date, 방송사, 시간 - 영화 pair
# '선샤인<1부>'같은건 링크 없으면 못 찾을 듯

# 일주일치

#### 채널 원래대로 다 넣어놓고, movie_title 구한 후 해당 movie_title이 없을 때 movie info 검색
#### 영어 + 한글에서 한글 남겨둬야 할 수도...? 뭘 버려야 
#### 유명한 시리즈물은 미리 DB에 넣어두어도 될 것 같다 -> 분노의 질주
def make_schedule_for_seven_days():
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
    
    def cleanedTitle(Title):
        flag=False
        for j in range(len(Title)):
            #[오스카4관왕]버드맨
            if Title[3] == '[':
                # 뒤에 진짜 제목이 있어야 해
                for jj in range(4, len(Title)-1):
                    if Title[jj] == ']':
                        flag = True
                        # [007시리즈]007카지노로얄 <3부>, 십의 자리까지 있는 부는 없겠지
                        # [영상미폭발] 알로하 <1부>
                        if Title[len(Title)-2:len(Title)]=='부>' and 49 <= ord(str(Title[len(Title)-3])) <= 57:
                            Title = '영화' + Title[jj+1:len(Title)-4]
                            break
                        else:
                            Title = '영화' + Title[jj+1:len(Title)]
                            break
                # 바깥쪽 for문 깨기
                if flag:
                    break
            # R.I.P.D.유령퇴치전담반 : 영어만 쓴다
            if 97 <= ord(Title[3]) <= 122 or 65 <= ord(Title[3]) <= 90:
                end_point = 3
                for jj in range(3, len(Title)):
                    # 숫자인 것도 넣어야, GP506
                    if 97 <= ord(Title[jj]) <= 122 or 65 <= ord(Title[jj]) <= 90 or  48 <= ord(Title[jj]) <= 56:
                        end_point = jj
                Title = Title[:end_point+1]
                break
            
            # 브이아이피(V.I.P)라고 치면 검색이 제대로 이루어지지 않아서 추가, 등등 괄호 빼버리기
            if Title[j] == '(':
                Title = Title[:j]
                break
            # '잭 리처2:네버 고 백'인데 이렇게 검색하면 잘 안 나와, 잭 리처:네버 고 백 이어야
            # 이렇게 하면 쥬라기 공원2가 망해 -> 그냥 잭 리처2, 쥬라기 공원2로만 검색한다
            # 시리즈물일 때, :이나 - 다음 부제 나올 때 부제 빼버려
            #  or Title[j+1] == '-' : 이거 조건에서 지워야지
            if 48 <= ord(str(Title[j])) <= 57 and j>0:
                if j+1<len(Title)-1 and (Title[j+1] == ':'):
                    Title = Title[:j]
                    break
                elif j+2 < len(Title)-1 and (Title[j+2] == ':'):
                    Title = Title[:j+1]            
                    break

            if (j+5 <= len(Title)-1) and Title[j:j+6] == '분노의 질주':
                if j+5 == len(Title)-1:
                    Title = '분노의 질주1'
                    break
                elif (48 > ord(str(Title[j+6])) or ord(str(Title[j+6])) > 57) and ('부>' in Title):
                    Title = '분노의 질주1'
                    break
                    
            if Title[j:] == '<1부>' or Title[j:] == '<2부>':
                Title = Title[:j]
                break

        print("cleaned Title :",Title)
        return Title

    # beautifulSoup으로 파싱한 것 인자로
    def movieInfo(searchTitle, searchMovie):
        # 마지막에 try, except
        box = searchMovie.find("div", class_="api_subject_bx _au_movie_info")
        try:
            movieTitle = box.find("div", class_="main_spot_wrap").find("h2", class_="movie_title").text
            ProductionYear = box.find("span", class_="movie_sub_title").text
            # 오류대비
            is_year = False
            for i in range(len(ProductionYear)-1,-1,-1):
                if 48 <= ord(str(ProductionYear[i])) <= 57:
                    is_year = True
                    ProductionYear = int(ProductionYear[i-3:i+1])
                    break
            if not is_year:
                ProductionYear = None
        except:
            # 다음 : 쥬라기 공원 2 : 잃어버린 세계, naver : 쥬라기 공원 2 - 잃어버린 세계
            movieTitle = box.find("div", class_="detail_info").find("strong", class_="title").text
            ProductionYear = None
        unboxing = box.find("div", class_="main_info _lp_animation").find("div", class_="detail_info").dl
        print(movieTitle)
        posterURL = box.find("div", class_="main_info _lp_animation").a.img.get('src')
        
        
        ddPack = unboxing.find_all("dd")
        # span만 들어있다
        for i in range(len(ddPack)-1):
            print(ddPack[i])
        
        info = []
        for el in ddPack[0].find_all("span"):
            if el.text:
                info.append(el.text)
        if len(info) ==3:
            genre = info[0]
            country = info[1]
            runningTime = int(info[2][:len(info[2])-1])
        else:
            genre = country = runningTime = None
            print("genre, countr, runningTime 없는 영화 : ", movieTitle)
        if ProductionYear == None:
            try:
                ProductionYear = int(ddPack[1][:4])
            except:
                ProductionYear = None
        try:
            score = float(ddPack[2].find("span", class_="star_count").text)
        except:
            score = None
        # 쥬라기 공원에 관객 수 없었어, 원래 0번째부터 있을 때 3번째에 있었는데
        # 별달리 특정할 수 있는 class가 없어서 이렇게 해본다.
        if len(ddPack) == 5: # 관객 수 있을 때
            audience = ddPack[3].text
            content = ddPack[4].find("span", class_="_text").text
        elif len(ddPack) == 4:
            audience = None
            content = ddPack[3].find("span", class_="_text").text
        else:
            audience = None
            content = box.find("div", class_="main_info _lp_animation").find("div", class_="detail_info").find("span", class_="_text").text
        try:
            director = searchMovie.find("ul", class_="api_list_scroll movie_list_scroll").find("li", class_="bx").find("strong", class_="name").text
        except: #잭 리처2:네버 고 백 버려
            director = None
        #print(movieTitle, "content :", content, "director :", director)
        #print(movieTitle, posterURL, ProductionYear, genre, country, runningTime, score, audience, content, director)
        return movieTitle, posterURL, ProductionYear, genre, country, runningTime, score, audience, content, director

    def not_movie(td):
        title = td.dl.dd.find("span").text
        # 데어데블 10회
        for t in range(len(title)):
            if 48 <= ord(title[t]) <= 57 and t+1 < len(title) and title[t+1] == '회':
                return True

    # DB에 현금사냥꾼, 캐리비안, RIPD movie Info 넣기
    # 잠시 ocn, cgv 을 빼놓는다.
    # 시간 순으로 들어간다(시간 -> 날짜 ), 가장 크게는 ocn, cgv, super_action, 스크린 순으로 크롤링된다. 
    # 분노의 질주 검색하면 아직 개봉하지 않은 영화 분노의 질주:홉스&쇼가 나와                             
    for channel in ['ocn', 'cgv', 'super+action', '스크린']:
        source = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={}+편성표'.format(channel)).text
        soup = BeautifulSoup(source, "html.parser")

        table = soup.find('table', class_="tbl")
        if channel == 'super+action':
            channel = 'super_action'
        for tr in table.tbody.find_all('tr'):
            hour = tr.th.text[:3]
            i = 0
            for td in tr.find_all('td'):
                data[dayList[i]][channel][hour] = ''
                if td.dl:  # 이 시간에 새롭게 시작하는 영화가 있으면
                    minute = td.dl.dt.text  # 몇 분 시작인지 구하고
                    # 링크가 달려있는지, 영화인지 확인
                    if td.dl.dd.a and "tv-program" not in td.dl.dd.a.get('href'):
                        title = td.dl.dd.a.text
                        # 1부, 2부 구별하고 저장
                        data[dayList[i]][channel][hour] = minute + ' ' + title
                        # 다음 영화 정보에서 title 가져다가 검색한다.
                        search = requests.get('https://search.daum.net/search' + td.dl.dd.a.get('href')).text
                        searchM = BeautifulSoup(search, "html.parser")
                        movieTitle = '영화 '+ searchM.find("div",{"id":"movieTitle"}).a.b.text
                        if '캐리비안의 해적 :' in movieTitle:
                            movieTitle = movieTitle[:8+3] + '-' + movieTitle[11+3:]
                        movieTitle = cleanedTitle(movieTitle)
                        search = requests.get('https://m.search.naver.com/search.naver?query={}'.format(movieTitle)).text
                        searchM = BeautifulSoup(search, "html.parser")
                        movieTitle, posterURL, ProductionYear, genre, country, runningTime, score, audience, content, director = movieInfo(movieTitle, searchM)

                    # 링크가 있고 tv 프로그램인게 명백한 경우
                    elif td.dl.dd.a and "tv-program" in td.dl.dd.a.get('href'):
                        pass
                    # 데어데블 10회
                    elif not_movie(td):
                        pass
                    # 영화인지 본격적으로 체크
                    else:
                        # 영화를 붙일 때 성공률이 더 높다
                        titleInSchedule = "영화 " + td.dl.dd.find("span").text
                        # title은 영화인지 검사할 때 쓰는 키워드일뿐 편성표에 넣을 때는 titleInSchedule로 넣는다
                        title = titleInSchedule

                        if "감독판" in title:
                            for j in range(len(title)):
                                if title[j:j+3] == "감독판":
                                    title = title[:j]
                                    print(title)
                                    break
                            title = cleanedTitle(title)
                            print(title)
                            data[dayList[i]][channel][hour] = minute + ' ' + title[3:]
                            search = requests.get('https://m.search.naver.com/search.naver?query={}'.format(title)).text
                            searchM = BeautifulSoup(search, "html.parser")
                            movieTitle, posterURL, ProductionYear, genre, country, runningTime, score, audience, content, director = movieInfo(title, searchM)
                        elif ("영화 바운티 헌터스: 현금사냥꾼" in title) or ("R.I.P.D" in title):
                            data[dayList[i]][channel][hour] = minute + ' ' + title[3:]
                        else:
                            title = cleanedTitle(title)
                            temp = requests.get('https://m.search.naver.com/search.naver?query={}'.format(title)).text
                            temp2 = BeautifulSoup(temp, 'html.parser')

                            temp1 = requests.get('https://m.search.naver.com/search.naver?query={}'.format(title[3:])).text
                            temp22 = BeautifulSoup(temp1, 'html.parser')
                            # 검색했을 때 영화가 바로 뜨는 경우
                            try:
                                # text가 있으면 영화인 것
                                movie_title = temp2.find("div", class_="title_area _lp_load _lp_animation").find("h2", class_="movie_title").text
                                print(11111111,title)
                                data[dayList[i]][channel][hour] = minute + ' ' + titleInSchedule[3:]
                                movieTitle, posterURL, ProductionYear, genre, country, runningTime, score, audience, content, director = movieInfo(title, temp2)
                            except:
                                try:
                                    movie_title = temp22.find("div", class_="title_area _lp_load _lp_animation").find("h2", class_="movie_title").text
                                    print(22222222222, title[3:])
                                    data[dayList[i]][channel][hour] = minute + ' ' + titleInSchedule[3:]
                                    movieTitle, posterURL, ProductionYear, genre, country, runningTime, score, audience, content, director = movieInfo(title[3:], temp22)
                                except:
                                    # try:                                        
                                        is_movie = temp22.find("div", class_="api_subject_bx _au_movie_info").find("h2", class_="api_title").text
                                        print(33333, title[3:])
                                        if "영화" in is_movie:
                                            data[dayList[i]][channel][hour] = minute + ' ' + titleInSchedule[3:]
                                            movieTitle, posterURL, ProductionYear, genre, country, runningTime, score, audience, content, director = movieInfo(title[3:], temp22)
                                    # except:
                                        # print("크롤링 실패한 영화입니다: ", title)

                i += 1
    return data
data = make_schedule_for_seven_days()
print(data)