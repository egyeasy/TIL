# 190425 오전 콜백

### 1급 객체

1. 인자로 넘길 수 있어야 한다.

   ```js
   addEventListener('load', (event) => {
       
   })
   ```

2. 변수나 데이터에 할당할 수 있어야 한다.

   ```js
   const sum = (a, b) => {
       return a + b
   }
   ```

3. 객체의 리턴값으로 리턴할 수 있어야 한다.

   ```js
   const log = () => {
       return sum
   }
   
   const sumCopy = log() // sum
   sumCopy(1, 2) // 3
   ```

   

ex) string, number, boolean, function(in js), 



### 1.callback.js

```js
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

```



이런 반복을 줄여주고자 콜백 함수를 고안, 돌려만 주는 함수를 만들 것

```js
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
```



### 자동으로 for문 돌아주는 array helper method(since ES6)

```js
// forEach
numbers.forEach((number) => {
    sum_call += number
})

console.log(sum_call)
```

for문 안의 each를 콜백 함수의 인자로 설정해준다



`addEventListener('load')`는 데이터가 다 불러와져야 인자의 콜백함수를 실행하게 된다(비동기 처리)

따라서 콜백함수를 실행해야만 불러올 수 있는 값을 이벤트 리스너 직후에 부르면 안된다.





## 콜백을 써야만 하는 상황(2.callback.js)

```js
// 상황
// 1. 손님이 카페에서 커피를 주문한다.
// 2. 직원은 커피를 만들고 손님에게 서빙한다.
// 3. 손님은 커피를 받고 마신다.

const orderCoffee = (order) => {
    let coffee
    // 커피 만드는 데 1초가 걸림
    setTimeout(() => {
        coffee = order
    }, 1000);

    return coffee
}

const coffee = orderCoffee('Americano')
console.log(coffee)
```

이렇게 하면 coffee = undefined로 출력된다.



성공하게 해보자

```js
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
```



서빙하기가 필요하다면?

```js
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
```

계속해서 비동기함수를 써서 depth를 들어가게 되면 '콜백지옥'에 빠질 수 있다.(callback hell.com 참고 -> 도움이 많이 됨)

이를 벗어나기 위해 고안된 문법이 있다.





## 콜백지옥 만들지 않기(3.promise.js)

### 만드려는 형태

```js
const orderCoffee = (order) => {
    let coffee

    setTimeout(() => {
        coffee = order
    }, 1000);
}
```



### cf.

```js
const sum = (a, b) => a + b  // 한줄만에 반환이 되면 중괄호, return 쓰지 않아도 됨!
```



### 완성

```js
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
```

잘 마실게요! 출력

`orderCoffee()`로 함수 호출하면 에러 메시지 출력 - 인자가 없을 때는 error로 인식해서 catch 실행

이 코드를 콘솔에 쳐보면 `Promise` 객체가 만들어진 것을 볼 수 있고, `PromiseStatus`에는 `resolved`가, `PromiseValue`에는 `Americano`가 들어가있다.

계속 `Promise` 객체가 나오는 것은, `.then`이 `Promise` 객체를 반환하기 때문이다. 



```js
orderCoffee('Americano')
    .then(coffee => console.log(`첫번째 ${coffee}`))  // Americano
    .then(test => console.log(`두번째 ${test}`))  // undefined
```

orderCoffee의 반환값은 Promise. `.then()`이 return하는 값은 새로운 Promise.



```js
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
```

catch는 then 여러개라도 맨 마지막에 하나만 쓰는 것이 가능하고, 맨 마지막에 쓰는 것이 convention

js에서 비동기처리 함수들은 대부분 Promise를 return하도록 만들어놨다. 그대로 실행시키고 then catch만 추가하면 됨. 



### 어제꺼 XHR 복습

```js
const XHR = new XMLHttpRequest()
const URL = 'http://koreanjson.com/posts/1'

XHR.open('GET', URL)
XHR.send()

XHR.addEventListener('load', (event) => {
    const rawData = event.target.response
    const parsedData = JSON.parse(rawData)
    console.log(parsedData)
})
```



### fetch()

마찬가지로 외부에서 response를 받아오는 메소드인데, promise로 만들어져 있음.

```js
fetch(URL)  // 외부 데이터를 resolve 해줌
    // .then((response) => console.log(response))  // 응답 결과를 받을 수 있다.
    .then((response) => response.json()) // 응답 결과를 object로 parsing
    .then((object) => {
        console.log(object)  // parsedData 출력
    })
```





## async-await

```js
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
```

reject를 겪었을 때는 에러를 발생시킴 -> 코드는 멈추고 '형님 주문 안하셨는데요;' 출력, 뒤의 절차는 실행하지 않게 됨.



마찬가지로

```js
const getData = async () => {
    const URL = 'https://koreanjson.com/posts/1'
    const response = await fetch(URL) // 데이터 불러오기
    const data = await response.json() // 파싱
    console.log(data)
}

getData()
```



에러 핸들링을 해야한다면

```js
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
```





# 오후 

## 일타싸피

나인볼의 변형판. 1번공부터 쳐야 한다. 넣지 않더라도 1번을 가장 먼저 쳐서 다른 공을 넣을 수 있다.

각도 계산은 12시가 0도~ 360도, 그리고 힘을 정해준다. 힘의 max는 200이고, 힘이 어느 정도 세기인지는 와서 확인해볼 것.

likelion alggago 코드 찾아보기

```python
def xxx(gamedata):
    
```



## M:N

난이도 높였다.

User model + accounts

signin, 로그인, 로그아웃

auth 관련된 import 까지

Post CRUD

모델 3개



















