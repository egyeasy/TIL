import requests, os, csv
from datetime import date, timedelta


token = os.getenv('KOBIS_TOKEN')
token_string = "key=" + token

naver_id = os.getenv('NAVER_SEARTCH_ID')
naver_pw = os.getenv('NAVER_SEARCH_PW')

former_acc = {}

# 영진위 상세 파일 헤더 작성
mode = 'w'
with open('movie.csv', mode) as f:
    field = ('movie_code', 'movie_name_ko','movie_name_en',
    'movie_name_og', 'open_year', 'show_time', 'genres',
     'directors', 'watch_grade_nm', 'actor1', 'actor2', 'actor3')
    writer = csv.DictWriter(f, fieldnames=field)
    writer.writeheader()



origin_date = date(2019, 1, 13)
for i in range(10):
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?"
    the_date = origin_date - timedelta(weeks=i)
    dt = ''.join(str(the_date).split('-'))
    dt_string = "&targetDt=" + dt
    weekGb = "&weekGb=0"
    
    # headers = {
    #     'key': token
    # }
    
    # data = {
    #     'targetDt': '20190101'
    # }
    
    response = requests.get(url + token_string + dt_string + weekGb)    
    
    doc = response.json()['boxOfficeResult']['weeklyBoxOfficeList']
    
    name_dic = {'movieCd':'movie_code', 'movieNm':'title', 'audiAcc':'audience'}
    
    wow_dic = {'movieCd': 'movie_code', 'movieNm': 'movie_name_ko', 'movieNmEn': 'movie_name_en',
    'movieNmOg': 'movie_name_og', 'showTm': 'show_time', 'genres': 'genres',
    'directors': 'directors', 'audits': 'watch_grade_nm'}
    
    new_list = []
    detail_list = []
    for dic in doc:
        new_dic = {}
        if dic['movieNm'] in former_acc:
            continue
        
        # 영진위 영화상세정보
        url2 = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?"
        movieCd = "&movieCd=" + dic['movieCd']
        response2 = requests.get(url2 + token_string + movieCd)
        doc2 = response2.json()['movieInfoResult']['movieInfo']
        
        detail_dic = {}
        
        for key in doc2:
            if key in ['movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'showTm']:
                detail_dic[wow_dic[key]] = doc2[key]
            elif key == 'openDt':
                detail_dic['open_year'] = doc2[key][:4]
            elif key == 'genres':
                detail_dic[wow_dic[key]] = doc2[key][0]['genreNm']
            elif key == 'directors':
                detail_dic[wow_dic[key]] = doc2[key][0]['peopleNm']
            elif key == 'audits':
                detail_dic[wow_dic[key]] = doc2[key][0]['watchGradeNm']
            elif key == 'actors':
                if len(doc2[key]) == 0:
                    for i in range(3):
                        actor_num = 'actor' + str(i+1)
                        detail_dic[actor_num] = ''
                    continue
                for i in range(3):
                    if i == len(doc2[key]) - 1:
                        break
                    actor_num = 'actor' + str(i+1)
                    detail_dic[actor_num] = doc2[key][i]['peopleNm']
        
        with open('movie.csv', 'a') as f:
            field = ('movie_code', 'movie_name_ko','movie_name_en',
            'movie_name_og', 'open_year', 'show_time', 'genres',
             'directors', 'watch_grade_nm', 'actor1', 'actor2', 'actor3')
            writer = csv.DictWriter(f, fieldnames=field)
            writer.writerow(detail_dic)            
        
        if i == 0:
            mode = 'w'
            with open('boxoffice.csv', mode) as f:
                field = ('movie_code', 'title', 'audience', 'recorded_at')
                writer = csv.DictWriter(f, fieldnames=field)
                writer.writeheader()
                for movie in new_list:
                    writer.writerow(movie)
        else:
            mode = 'a'
            with open('boxoffice.csv', mode) as f:
                field = ('movie_code', 'title', 'audience', 'recorded_at')
                writer = csv.DictWriter(f, fieldnames=field)
                for movie in new_list:
                    writer.writerow(movie)

        
        for key in dic:
            if key in ['movieCd', 'movieNm', 'audiAcc']:
                new_dic[name_dic[key]] = dic[key]
                if dic['movieNm'] not in former_acc:
                    former_acc[dic['movieNm']] = dic['audiAcc']
                else:
                    new_dic[name_dic['audiAcc']] = former_acc[dic['movieNm']]
        new_dic['recorded_at'] = dt
        new_list.append(new_dic)
    
    
    if i == 0:
        mode = 'w'
        with open('boxoffice.csv', mode) as f:
            field = ('movie_code', 'title', 'audience', 'recorded_at')
            writer = csv.DictWriter(f, fieldnames=field)
            writer.writeheader()
            for movie in new_list:
                writer.writerow(movie)
    else:
        mode = 'a'
        with open('boxoffice.csv', mode) as f:
            field = ('movie_code', 'title', 'audience', 'recorded_at')
            writer = csv.DictWriter(f, fieldnames=field)
            for movie in new_list:
                writer.writerow(movie)

        

