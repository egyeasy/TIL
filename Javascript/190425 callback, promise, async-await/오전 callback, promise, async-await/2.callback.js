// 콜백을 써야만 하는 상황
// 상황
// 1. 손님이 카페에서 커피를 주문한다.
// 2. 직원은 커피를 만들고 손님에게 서빙한다.
// 3. 손님은 커피를 받고 마신다.

// 실패
const orderCoffee = (order) => {
    let coffee
    // 커피 만드는 데 1초가 걸림
    setTimeout(() => {
        coffee = order
    }, 1000);

    return coffee
}

const coffee = orderCoffee('Americano') // 이러면 undefined 출력
console.log(coffee)


// 성공하게 해보자
const orderCoffee = (order, callback) => {
    let coffee
    // 커피 만드는 데 1초가 걸림
    setTimeout(() => {
        coffee = order
        callback(coffee)
    }, 1000);

    return coffee
}

orderCoffee('Americano', console.log)


// 서빙하기 - 콜백지옥
const orderCoffee = (order, callback) => {
    let coffee
    // 커피 만드는 데 1초가 걸림
    setTimeout(() => {
        coffee = order
        serving(coffee, () => {}) // serving이 비동기처리 함수라면 콜백함수가 안에 또 필요하다.
    }, 1000);

    return coffee
}

orderCoffee('Americano', console.log)