# 37homework

1. ```js
   const URL = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1"
   const XHR = new XMLHttpRequest()
   
   XHR.open('GET', URL);
   XHR.send();
   
   XHR.addEventListener('load', e => {
       // rawdata를 콘솔에 출력한다.
       const rawData = e.target.response
       console.log(rawData)
       // lottoData 상수에 rawData 를 Object 로 변환하여 저장한다.
       const lottoData = JSON.parse(rawData)
       // lottoData 를 콘솔에 출력한다.
       console.log(lottoData)
       // lottoData 에서 추첨 날짜(drwNoDate)를 콘솔에 출력한다.
       console.log(lottoData.drwNoDate)
   })
   ```

2. 