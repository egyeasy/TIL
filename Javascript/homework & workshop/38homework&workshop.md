# 38homework

1. blocking 함수는 절차 지향적 프로그래밍에서의 함수와 같이 함수 호출이 일어났을 때 해당 함수의 호출부터 return까지의 작업을 모두 수행한 후 다음 줄의 코드로 넘어가도록 하는 함수이다. 반면 non-blocking 함수는 javascript만의 특별한 함수 유형으로 해당 함수의 호출이 일어났을 때 함수의 return까지의 작업을 시작함과 동시에 바로 다음 줄의 코드로 넘어간다. 따라서 처리에 시간이 오래 소요되는 작업들을 non-blocking 함수로 구현함으로써 우선순위에 있는 작업들을 먼저 처리할 수 있게 된다. 만약 JS의 모든 함수들이 blocking 하다면 시간이 오래걸리는 작업들 때문에 프론트엔드 렌더링에 있어서 UX 만족도의 큰 저하가 발생할 것이다.
2. 해당 코드는 `sendXHR()`이라는 함수를 정의하고, XHR Promise의 처리를 통해 GET 방식의 요청을 보내고 응답을 처리하는 프로그램이다. 함수의 인자로 지정된 url을 GET 방식으로 요청하고, 요청이 **성공**적으로 전달되면 **`resolve`**를 통해 그 다음에 실행할 **익명함수**에 인자를 전달해준다. 해당 인자를 받을 익명함수는, 함수를 호출한 다음 **`.then`**을 통해 정의할 수 있다. 한편 요청이 **실패**하면 **`reject`** 를 통해 그 다음에 실행할 익명함수에 인자를 전달해준다. 해당 인자를 받을 익명함수는, `.then` 의 익명함수를 지정해준 다음 **`.catch`** 를 통해 정의할 수 있다.



# 38workshop

```js
const waitNSeconds = (n) => new Promise((resolve, reject) => {
    if (typeof n !== 'number') {
        reject(n)
    }
    setTimeout(() => {
        console.log(`${n} second(s) passed`)
        resolve()
    }, n * 1000)
    
}) 

  
const waitFor10Seconds = async () => {
    await waitNSeconds(1)
    await waitNSeconds(2)
    await waitNSeconds(3)
    await waitNSeconds(4)
    console.log('Total 10 seconds!')
}

waitFor10Seconds()
```

























