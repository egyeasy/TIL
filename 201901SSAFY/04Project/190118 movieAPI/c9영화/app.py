import requests, os, csv
from datetime import date, timedelta


token = os.getenv('KOBIS_TOKEN')
token_string = "key=" + token

naver_id = os.getenv('NAVER_SEARCH_ID')
naver_pw = os.getenv('NAVER_SEARCH_PW')
print(naver_id, naver_pw)

former_acc = {}

# 영진위 주간 박스오피스 파일 헤더 작성
with open('boxoffice.csv', 'w') as f:
    field = ('movie_code', 'title', 'audience', 'recorded_at')
    writer = csv.DictWriter(f, fieldnames=field)
    writer.writeheader()

# 영진위 상세 파일 헤더 작성
with open('movie.csv', 'w') as f:
    field = ('movie_code', 'movie_name_ko','movie_name_en',
    'movie_name_og', 'open_year', 'show_time', 'genres',
     'directors', 'watch_grade_nm', 'actor1', 'actor2', 'actor3')
    writer = csv.DictWriter(f, fieldnames=field)
    writer.writeheader()

# 네이버 영화 검색 API 파일 헤더 작성
with open('movie_naver.csv', 'w') as f:
    field = ('movie_code', 'thumb_url', 'link_url', 'user_rating')
    writer = csv.DictWriter(f, fieldnames=field)
    writer.writeheader()

url_nav = "https://openapi.naver.com/v1/search/movie.json"
movieCd = "20184105"
query_nav = "query="+movieCd
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

origin_date = date(2019, 1, 13)
for i in range(0):
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
        print(movieCd)
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

        
        for key in dic:
            if key in ['movieCd', 'movieNm', 'audiAcc']:
                new_dic[name_dic[key]] = dic[key]
                if dic['movieNm'] not in former_acc:
                    former_acc[dic['movieNm']] = dic['audiAcc']
                else:
                    new_dic[name_dic['audiAcc']] = former_acc[dic['movieNm']]
        new_dic['recorded_at'] = dt
        new_list.append(new_dic)
    
    

    mode = 'a'
    with open('boxoffice.csv', mode) as f:
        field = ('movie_code', 'title', 'audience', 'recorded_at')
        writer = csv.DictWriter(f, fieldnames=field)
        for movie in new_list:
            writer.writerow(movie)

        

