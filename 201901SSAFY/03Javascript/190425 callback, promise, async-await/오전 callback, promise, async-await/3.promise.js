// 다 만들면 커피를 줄게라는 약속을 할거임
// 중간에 무슨일이 생기면 알려줄거임

const orderCoffee = (order) => {
    let coffee

    setTimeout(() => {
        coffee = order
    }, 1000); 
}


// cf.
const sum = (a, b) => a + b  // 한줄만에 반환이 되면 중괄호, return 쓰지 않아도 됨!


// 약속을 받아보자
// resolve -> 성공시 넘겨줄 객체, reject -> 무슨 일이 생길시 발생시킬 에러를 담음
const orderCoffee = (order) => new Promise((resolve, reject) => {  // 새로운 객체 생성
    let coffee

    setTimeout(() => {
        if (order === undefined) {
            reject('형님 주문 안하셨는데요;')
        }
        coffee = order
        resolve(coffee)
    }, 1000); 
})

// orderCoffee('Americano')  // Promise 반환
    
// 그리고 할 작업을 넣기
// orderCoffee('Americano').then()  // 아래와 같음

orderCoffee('Americano')
    .then((coffee) => {  // 그리고 - resolve
        console.log(`${coffee} 잘 마실게요!`)
    })
    .catch((error) => {  // 에러를 캐치 - reject
        console.log(error)
    })
    

// orderCoffee('Americano')
//     .then(coffee => console.log(`첫번째 ${coffee}`))  // Americano
//     .then(test => console.log(`두번째 ${test}`))  // undefined


orderCoffee('Americano')
    .then(coffee => {
        console.log(coffee)  // Latte
        return orderCoffee('Latte')
    })
    .then(coffee => {
        console.log(coffee)  // Latte
        return
    })  // Promise = undefined
    .then((coffee) => {
        console.log(coffee)  // undefined
    })

const XHR = new XMLHttpRequest()
const URL = 'http://koreanjson.com/posts/1'

XHR.open('GET', URL)
XHR.send()

XHR.addEventListener('load', (event) => {
    const rawData = event.target.response
    const parsedData = JSON.parse(rawData)
    console.log(parsedData)
})


fetch(URL)  // 외부 데이터를 resolve 해줌
    // .then((response) => console.log(response))  // 응답 결과를 받을 수 있다.
    .then((response) => response.json()) // 응답 결과를 object로 parsing
    .then((object) => {
        console.log(object)  // parsedData 출력
    })
