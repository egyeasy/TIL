// POST를 통한 posts 생성
const URL = "https://jsonplaceholder.typicode.com/posts"

const XHR = new XMLHttpRequest()

// 1. XHR.open()
XHR.open('POST', URL)

// 2. POST에서 필요 - setRequestHeader(헤더정보)
XHR.setRequestHeader(
    'Content-Type',
    'application/json;charset=UTF-8' // charset: 언어 인코딩 알려줌
)

// 2. XHR.send(데이터)
const data = {
	title: "제목 테스트",  // 키값 "" 필요없음
    body: "내용이다",
    userId: 1
}

XHR.send(JSON.stringify(data)) // 그냥 바로 요청을 보내느 GET과는 다르게 POST에서는 뭘 할지 알려줘야 함. 그걸 위의 setRequestHeader에서 수행

// 3. XHR.addEventListener()
XHR.addEventListener('load', function(donghoon) {  // donghoon : 받아온 데이터
    console.log(donghoon)  // progressEvent를 보여줌
    console.log(donghoon.target.response)
})  // 결과의 조건을 설정해줌. load : 성공적으로 받아옴. 


