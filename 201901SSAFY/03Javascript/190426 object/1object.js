// 사람 (in Python)
// class Person():
//     def __init__(self, name):
//         self.name = name
// donghoon = Person('donghoon')

donghoon = {
    name: 'donghoon',

    poop() {
        return "poop"
    }
}

junse = {
    name: 'junse',

    poop: function () {  // 이렇게도 쓸 수 있다!(ES6)
        return "poop"
    }
}

console.log(donghoon.name)
console.log(donghoon.poop())

console.log(junse.name)
console.log(junse.poop())

console.log(junse.poop)

let greeting = "hello"


// class Person:
//     def __init__(self, name):  // 생성자 함수
//         self.name = name
//     def poop(self):
//         return "poop"
//     def hello(self):
//         return f"안녕 나는 {self.name}야"

donghoon = Person("동훈")

class Person {
    constructor(name) {  // 생성자 함수
        this.name = name  // detail하게 들어가면 this는 객체에 binding이 안 될 수도 있다. but 일단 객체처럼 알아두자.
    }

    poop() {
        return "poop"
    }

    hello() {
        return `안녕 나는 ${this.name}야`
    }
}

const donghoon = new Person("동훈")  // 새로운 객체를 만들겠다는 new. XHR에서 썼었다.

// const XHR = new XMLHttpRequest()

class XMLHttpRequest {  // ES6+
    open() {

    }

    send() {

    }

    addEventListener() {

    }
}

// 네이버 홈에서
const start = document.querySelector('.al_favorite')
start.addEventListener

console.log(typeof(start)) // object
console.dir(start) // start의 내부를 볼 수 있다. 파이썬의 dir함수와 비슷.