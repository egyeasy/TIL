let name = 'name'  // 변수: 재할당이 가능. 변할 수 있다.
name = 'jason'
console.log(name)

let sum = 0
sum += 2
console.log(sum)

const gender = 'man'  // 상수: 변하지 않음
// gender = 'woman'  // 에러 출력
console.log(gender)


// function test() {
//     var car = '소나타'
//     console.log(car)
// }

// test()  // '소나타' 출력

// function test() {

//     if (true) {
//         var car = '소나타'
//     }
//     console.log(car)
// }

// test()  // '소나타' 출력

// console.log(car)  // 에러 출력


function test() {
    const color = 'red'
    if (true) {
        console.log(color)
        let car = '소나타'
    }
    console.log(car)
}

test()  // 에러 출력