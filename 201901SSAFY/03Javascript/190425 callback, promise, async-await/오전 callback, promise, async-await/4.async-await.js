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

// const coffee = orderCoffee('Americano')  // Americano를 출력해서 담고 싶다
// console.log(coffee) // Americano를 그대로 출력하고 싶다.

// 함수 안에 넣고
const getCoffee = async () => {  // 내부적으로 비동기적으로 작동하는 요소가 있다고 명시해주고
    const coffee = await orderCoffee('Americano')  // 비동기처리가 들어있는 함수 앞에 await -> 다 실행될 때까지 (1초 동안) 멈춰있는다. 그 다음에 다음 라인 실행
    console.log(coffee)  // Americano
}

getCoffee()


const getData = async () => {
    try {  // 에러 핸들링을 해야한다면
        const URL = 'https://koreanjson.com/posts/1'
        const response = await fetch(URL) // 데이터 불러오기
        const data = await response.json() // 파싱
        console.log(data)
    } catch (error) {
        console.log(error)
    }
}

getData()