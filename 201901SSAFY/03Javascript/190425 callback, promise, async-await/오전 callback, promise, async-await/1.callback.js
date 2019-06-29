// 1급 객체

// 1. 인자로 넘길 수 있어야 한다.
// addEventListener('load', (event) => {
    
// })

// 2. 변수나 데이터에 할당할 수 있어야 한다.
const sum = (a, b) => {
    return a + b
}

// 3. 객체의 리턴값으로 리턴할 수 있어야 한다.
const log = () => {
    return sum
}


const sumCopy = log() // sum
// sumCopy(1, 2) // 3




// 숫자로 된 배열을 받아서 모두 더한다.
const numbersAddEach = (numbers) => {  // [1, 2, 3]
    let sum = 0
    for (const number of numbers) {
        sum += number
    }
    return sum
}

// 숫자로 된 배열을 받아서 모두 뺀다.
const numbersSubEach = (nubmers) => {
    let sum = 0
    for (const number of numbers) {
        sum -= number
    }
    return sum
}

// 숫자로 된 배열을 받아서 모두 곱한다.
const numbersMulEach = (numbers) => {
    let sum = 1
    for (const number of numbers) {
        sum *= number
    }
    return sum
}

// numbersMulEach(numbers) // 곱하기 해줌


numbers = [4, 5, 6]

// 돌려만 주는 함수를 만들고 일을 시키는 콜백 함수 만든다.
const numbersEach = (numbers, callback) => {
    for (const number of numbers) {
        callback(number)
    }
}

let sum_call = 0

// 함수 호출할 때 콜백함수를 정의
numbersEach(numbers, (number) => {
    console.log(`numbersEach `, number)  // 4, 5, 6
    sum_call += number
})

console.log(sum_call)

sum_call = 0
// forEach
numbers.forEach((number) => {
    sum_call += number
})

console.log(sum_call)