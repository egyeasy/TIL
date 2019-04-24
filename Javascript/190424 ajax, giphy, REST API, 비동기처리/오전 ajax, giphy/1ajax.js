const XHR = new XMLHttpRequest()  // new : 클래스 생성
const URL = 'https://koreanjson.com/posts/1'

XHR.open('GET', URL) // 콜(요청)을 보낼 준비 : method, url
XHR.send()  // GET이므로 데이터를 보내지 않고 요구만 할 것

// XHR.addEventListener('load', function(event) { // 아래와 같음
    
// })

XHR.addEventListener('load', (event) => { // 파일을 받아온다. 요청이 끝났을 때 처리.
    // console.log(event)
    // console.log(event.target.response)
    const rawData = event.target.response
    // JSON이라는 인터페이스가 잇다.
    const parsedData = JSON.parse(rawData)  // string => object
    // JSON.stringify()  // object => string
    document.write(parsedData.content)
})