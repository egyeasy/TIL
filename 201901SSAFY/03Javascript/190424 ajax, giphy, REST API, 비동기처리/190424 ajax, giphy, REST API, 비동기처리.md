# 190424 오전 AJAX, giphy

## AJAX

Asynchronous Javascript and XML

비동기적인 자바스크립트와 XML

요청을 했을 때 화면 이동 하지 않고 데이터 가져와서 처리

XMLHttpRequest(XHR) : **모든 브라우저**마다 탑재되어있는 built-in 객체. object를 통해 웹페이지에 요청 보냄. node에서는 쓸 수 없으므로 API를 사용해야 함.

fetch : ES6 이후로 나온 ajax 함수. js에 built-in 되어있음



### koreanjson

json 타입의 요청을 보내주는 api 사이트.



### 1ajax.js

```js
const XHR = new XMLHttpRequest()  // new : 클래스 생성
const URL = 'https://koreanjson.com/posts/1'

XHR.open('GET', URL) // 콜(요청)을 보낼 준비 : method, url
XHR.send()  // GET이므로 데이터를 보내지 않고 요구만 할 것

// XHR.addEventListener('load', function(event) { // 아래와 같음
    
// })

XHR.addEventListener('load', (event) => { // 파일을 받아온다. 요청이 끝났을 때 처리.
    console.log(event)
})
```

node에서 쓸 수 없으므로 복사해서 브라우저 console창에 붙여넣기

ctrl + l -> clear console

const로 정의한 거라 다시 보내면 에러가 난다. 새로고침하고 보내야 보내진다.

받아온 event 안에 target > response에 원하는 내용이 있다.



```js
const XHR = new XMLHttpRequest()  // new : 클래스 생성
const URL = 'https://koreanjson.com/posts/1'

XHR.open('GET', URL) // 콜(요청)을 보낼 준비 : method, url
XHR.send()  // GET이므로 데이터를 보내지 않고 요구만 할 것

// XHR.addEventListener('load', function(event) { // 아래와 같음
    
// })

XHR.addEventListener('load', (event) => { // 파일을 받아온다. 요청이 끝났을 때 처리.
    console.log(event.target.response)
})
```

새로고침 -> 복붙

js 오브젝트로 그냥 보내버리면 다른 곳에서 문제가 발생할 수 있다. 따라서 표준적으로 json 타입(어느 언어에나 있는 key:value 데이터타입)에 string으로 내용을 담아서 데이터를 주고 받는다. 따라서 우리가 받아온 것도 string이므로 이것을 parsing해줘야 한다.





`JSON` 인터페이스에는 2가지 메소드가 있는데, 일단 `parse`를 써서 데이터를 원하는 형태로 가공할 것이다. `stringify`는 서버로 json을 보낼 때 string으로 만들어주는 것.

`JSON.parse()`  // string => object

`JSON.stringify()`  // object => string

```js
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
```





## giphy

2giphy.html, 2main.css 생성



### 2giphy.html

div.container.container-padding50 + tab

input.container-textinput + tab

button.container-button + tab

div.container.container-padding50.js-container + tab

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Giphy Search Engine</title>
    <link rel="stylesheet" href="./2main.css">
</head>
<body>
    <div class="container container-padding50">
        <input id="js-userinput" type="text" class="container-textinput" value="HPHK">
        <button id="js-go" class="container-button">Go!</button>
    </div>
    <div id="result-area" class="container container-padding50 js-container">

    </div>

    <script src="./2main.js"></script>
</body>
</html>
```



`2main.js` 생성



### 2main.css

슬랙에 보내주신 걸로 복붙

```css
body {
    width: 80%;
    max-width: 1024px;
    margin: 0 auto;
    background-color: black;
}

h1 {
    color: white;
}

.img-center {
    display: block;
    margin-left: auto;
    margin-right: auto;
}

.container-padding50 {
    padding-top: 50px;
}

.container-textinput {
    width: 80%;
    display: inline-block;
    padding: 20px;
    font-size: 16px;
    font-family: Helvetica, sans-serif;
}

.container-button {
    width: 10%;
    display: inline-block;
    padding: 20px;
    background-color: green;
    color: white;
    font-size: 16px;
    font-family: Helvetica, sans-serif;
    border: 1px solid green;
    border-radius: 5px;
}

.container-image {
    width: 30%;
    display: block;
    float: left;
    margin-right: 3%;
    margin-bottom: 5%
}
```



open with liveserver로 html 파일 열어본다.

giphy 사이트에서 검색한 내용을 우리 사이트를 통해서 검색해서 보여주는 검색 엔진을 만들어볼 것.



### 2main.js

테스트

```js
// 1. input 태그안의 값을 잡는다.
const input = document.querySelector('#js-userinput');
const value = input.value
console.log(value)

// 2. Giphy API를 통해 data를 받아서 가공한다.

// 3. gif 파일들을 index.html(DOM)에 밀어넣어서 보여준다.
```



### 2giphy.html

테스트가 끝났으니 HPHK value를 지워주자.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Giphy Search Engine</title>
    <link rel="stylesheet" href="./2main.css">
</head>
<body>
    <div class="container container-padding50">
        <input id="js-userinput" type="text" class="container-textinput">
        <button id="js-go" class="container-button">Go!</button>
    </div>
    <div id="result-area" class="container container-padding50 js-container">

    </div>

    <script src="./2main.js"></script>
</body>
</html>
```



### 2main.js

버튼 클릭 혹은 엔터 쳤을 때 value를 보여주도록 해보자.

```js
// 1. input 태그안의 값을 잡는다.
// const input = document.querySelector('#js-userinput');
// const value = input.value
// console.log(value)

const button = document.querySelector('#js-go')
const input = document.querySelector('#js-userinput')

button.addEventListener('click', (e) => {  // event를 줄여서 e
    const value = input.value
    console.log(`click : ${value}`)
})

input.addEventListener('keypress', (e) => {
    if (e.keyCode === 13) {  // enter = 13번 코드
        const value = input.value
        console.log(`enter : ${value}`)
    }
})

// 2. Giphy API를 통해 data를 받아서 가공한다.

// 3. gif 파일들을 index.html(DOM)에 밀어넣어서 보여준다.
```





### 2main.js

검색어를 받아서 보여주도록 하자.

```js
// 1. input 태그안의 값을 잡는다.
const button = document.querySelector('#js-go')
const input = document.querySelector('#js-userinput')
const resultArea = document.querySelector('#result-area')

button.addEventListener('click', (e) => {  // event를 줄여서 e
    const value = input.value
    pushToDom(value)
})

input.addEventListener('keypress', (e) => {
    if (e.keyCode === 13) {  // enter = 13번 코드
        const value = input.value
        pushToDom(value)
    }
})

// 2. Giphy API를 통해 data를 받아서 가공한다.

// 3. gif 파일들을 index.html(DOM)에 밀어넣어서 보여준다.
const pushToDom = (data) => {
    resultArea.innerHTML = data  // 해당 태그에 넣겠다는 얘기
}
```



<https://developers.giphy.com/>에서 api키를 받아오자.

페북 로그인해서 api 키 만들어놓은 걸 쓴다.



```js
// 1. input 태그안의 값을 잡는다.
// const input = document.querySelector('#js-userinput');
// const value = input.value
// console.log(value)

const button = document.querySelector('#js-go')
const input = document.querySelector('#js-userinput')
const resultArea = document.querySelector('#result-area')

button.addEventListener('click', (e) => {  // event를 줄여서 e
    const value = input.value
    // console.log(`click : ${value}`)
    pushToDom(value)
})

input.addEventListener('keypress', (e) => {
    if (e.keyCode === 13) {  // enter = 13번 코드
        const value = input.value
        // console.log(`enter : ${value}`)
        pushToDom(value)
    }
})

// 2. Giphy API를 통해 data를 받아서 가공한다.
const API_KEY = 'SbNqUCzzoaLl25zJ80gBTun5I7aXrGZq'
let keyword = 'matrix'
const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${API_KEY}`

// 데이터 요청
const GiphyXHR = new XMLHttpRequest()
GiphyXHR.open('GET', URL)
GiphyXHR.send()

// 이제 데이터를 받아온다
GiphyXHR.addEventListener('load', (e) => {
    const rawData = e.target.response
    const parsedData = JSON.parse(rawData)
    console.log(parsedData)
})

// 3. gif 파일들을 index.html(DOM)에 밀어넣어서 보여준다.
const pushToDom = (data) => {
    resultArea.innerHTML = data  // 해당 태그에 넣겠다는 얘기
}
```



`const pushToDom`의 의미?

```js
function sum1 (a, b) {
    return a + b
}
sum = sum1(a, b)

const sum2 = function (a, b) {
    this // <= 실행하는 시점의 객체
    return a + b
}

const sum3 = (a, b) => {
    this // <= 선언하는 시점의 객체
    return a + b
}
```

변수에 바로 받아서 쓰도록 하는 것.



```js
// 1. input 태그안의 값을 잡는다.
// const input = document.querySelector('#js-userinput');
// const value = input.value
// console.log(value)

const button = document.querySelector('#js-go')
const input = document.querySelector('#js-userinput')
const resultArea = document.querySelector('#result-area')

button.addEventListener('click', (e) => {  // event를 줄여서 e
    const value = input.value
    // console.log(`click : ${value}`)
    pushToDom(value)
})

input.addEventListener('keypress', (e) => {
    if (e.keyCode === 13) {  // enter = 13번 코드
        const value = input.value
        // console.log(`enter : ${value}`)
        pushToDom(value)
    }
})

// 2. Giphy API를 통해 data를 받아서 가공한다.
const API_KEY = 'SbNqUCzzoaLl25zJ80gBTun5I7aXrGZq'
let keyword = 'matrix'
const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${API_KEY}`

// 데이터 요청
const GiphyXHR = new XMLHttpRequest()
GiphyXHR.open('GET', URL)
GiphyXHR.send()

// 이제 데이터를 받아온다
GiphyXHR.addEventListener('load', (e) => {
    const rawData = e.target.response
    const parsedData = JSON.parse(rawData)
    console.log(parsedData)
    console.log(parsedData.data[0].images.fixed_height.url)
})

console.log(123) // 이게 위의 console.log보다 더 일찍 출력하게 된다.

// 3. gif 파일들을 index.html(DOM)에 밀어넣어서 보여준다.
const pushToDom = (data) => {
    resultArea.innerHTML = data  // 해당 태그에 넣겠다는 얘기
}
```





```js
// 1. input 태그안의 값을 잡는다.
// const input = document.querySelector('#js-userinput');
// const value = input.value
// console.log(value)

const button = document.querySelector('#js-go')
const input = document.querySelector('#js-userinput')
const resultArea = document.querySelector('#result-area')

button.addEventListener('click', (e) => {  // event를 줄여서 e
    const value = input.value
    // console.log(`click : ${value}`)
    pushToDom(value)
})

input.addEventListener('keypress', (e) => {
    if (e.keyCode === 13) {  // enter = 13번 코드
        const value = input.value
        // console.log(`enter : ${value}`)
        pushToDom(value)
    }
})

// 2. Giphy API를 통해 data를 받아서 가공한다.
const API_KEY = 'SbNqUCzzoaLl25zJ80gBTun5I7aXrGZq'
let keyword = 'matrix'
const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${API_KEY}`

// 데이터 요청
const GiphyXHR = new XMLHttpRequest()
GiphyXHR.open('GET', URL)
GiphyXHR.send()

// 이제 데이터를 받아온다
GiphyXHR.addEventListener('load', (e) => {
    const rawData = e.target.response
    const parsedData = JSON.parse(rawData)
    console.log(parsedData)
    console.log(parsedData.data[0].images.fixed_height.url)
    // pushToDom(parsedData.data[2].images.fixed_height.url) // 이렇게 하나의 data 이미지를 보여줄 수 있다.
    for (data of parsedData.data) {
        console.log(data.images.fixed_height.url)
        pushToDom(data.images.fixed_height.url)
    }
})

console.log(123) // 이게 위의 console.log보다 더 일찍 출력하게 된다.

// 3. gif 파일들을 index.html(DOM)에 밀어넣어서 보여준다.
const pushToDom = (data) => {
    // resultArea.innerHTML = data  // 해당 태그에 넣겠다는 얘기
    // resultArea.innerHTML = `<img src="${data}"/>` // 이렇게 짜면 맨 마지막 것만 출력됨
    resultArea.innerHTML += `<img src="${data}"/>`  // 하나씩 더하기
}


```



url을 search버튼을 누를 때마다 만들어주면 변경되는 url을 update할 수 있을 것.

현재는 한번 검색하면 끝이다.

이걸 해결하기 위해 작성한 코드를 함수로 싸서 넣어준다.

검색할 때마다 `resultArea.innerHTML`를 초기화해주는 작업도 필요

```js
// 1. input 태그안의 값을 잡는다.
const button = document.querySelector('#js-go')
const input = document.querySelector('#js-userinput')
const resultArea = document.querySelector('#result-area')

button.addEventListener('click', (e) => {  // event를 줄여서 e
    const value = input.value
    // console.log(`click : ${value}`)
    // pushToDom(value)
    searchAndPush(value)
})

input.addEventListener('keypress', (e) => {
    if (e.keyCode === 13) {  // enter = 13번 코드
        const value = input.value
        // console.log(`enter : ${value}`)
        // pushToDom(value)
        searchAndPush(value)
    }
})

// 2. Giphy API를 통해 data를 받아서 가공한다.
const searchAndPush = (keyword) => {  // 함수 안에 넣어줌. keyword를 안에서 선언하지 않고 인자로 만들어준다
    resultArea.innerHTML = null; // search 할 때마다 초기화
    const API_KEY = 'SbNqUCzzoaLl25zJ80gBTun5I7aXrGZq'
    // let keyword = 'matrix'
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${API_KEY}`

    // 데이터 요청
    const GiphyXHR = new XMLHttpRequest()
    GiphyXHR.open('GET', URL)
    GiphyXHR.send()

    // 이제 데이터를 받아온다
    GiphyXHR.addEventListener('load', (e) => {
        const rawData = e.target.response
        const parsedData = JSON.parse(rawData)
        console.log(parsedData)
        console.log(parsedData.data[0].images.fixed_height.url)
        for (data of parsedData.data) {
            console.log(data.images.fixed_height.url)
            pushToDom(data.images.fixed_height.url)
        }
    })

    console.log(123) // 이게 위의 console.log보다 더 일찍 출력하게 된다.

    // 3. gif 파일들을 index.html(DOM)에 밀어넣어서 보여준다.
    const pushToDom = (data) => {
        resultArea.innerHTML += `<img src="${data}"/>`  // 하나씩 더하기
    }
}
```



innerHTML에 태그를 append하는 작업은 비효율적.

좀 더 효율적인 방법을 사용해보자.



```js
// 1. input 태그안의 값을 잡는다.
// const input = document.querySelector('#js-userinput');
// const value = input.value
// console.log(value)

const button = document.querySelector('#js-go')
const input = document.querySelector('#js-userinput')
const resultArea = document.querySelector('#result-area')

button.addEventListener('click', (e) => {  // event를 줄여서 e
    const value = input.value
    // console.log(`click : ${value}`)
    // pushToDom(value)
    searchAndPush(value)
})

input.addEventListener('keypress', (e) => {
    if (e.keyCode === 13) {  // enter = 13번 코드
        const value = input.value
        // console.log(`enter : ${value}`)
        // pushToDom(value)
        searchAndPush(value)
    }
})

// 2. Giphy API를 통해 data를 받아서 가공한다.
const searchAndPush = (keyword) => {  // 함수 안에 넣어줌. keyword를 안에서 선언하지 않고 인자로 만들어준다
    resultArea.innerHTML = null; // search 할 때마다 초기화
    const API_KEY = 'SbNqUCzzoaLl25zJ80gBTun5I7aXrGZq'
    // let keyword = 'matrix'
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${API_KEY}`

    // 데이터 요청
    const GiphyXHR = new XMLHttpRequest()
    GiphyXHR.open('GET', URL)
    GiphyXHR.send()

    // 이제 데이터를 받아온다
    GiphyXHR.addEventListener('load', (e) => {
        const rawData = e.target.response
        const parsedData = JSON.parse(rawData)
        console.log(parsedData)
        console.log(parsedData.data[0].images.fixed_height.url)
        // pushToDom(parsedData.data[2].images.fixed_height.url) // 이렇게 하나의 data 이미지를 보여줄 수 있다.
        for (data of parsedData.data) {
            console.log(data.images.fixed_height.url)
            pushToDom(data.images.fixed_height.url)
        }
    })

    console.log(123) // 이게 위의 console.log보다 더 일찍 출력하게 된다.

    // 3. gif 파일들을 index.html(DOM)에 밀어넣어서 보여준다.
    const pushToDom = (data) => {
        // resultArea.innerHTML = data  // 해당 태그에 넣겠다는 얘기
        // resultArea.innerHTML = `<img src="${data}"/>`
        // resultArea.innerHTML += `<img src="${data}"/>`  // 하나씩 더하기
        const img = document.createElement('img') // img 태그 만들기. <img></img>
        img.setAttribute('src', data) // <img src="${data}" />
        img.className = 'container-image' // container에 담기. img.setAttribute('class', 'container-image') 와 같은 작업
        resultArea.appendChild(img)  // child : 안쪽에 다른 element를 쌓는 것
    }
}
```





# 오후 REST API, 비동기처리

PPT REST API 참조



## REST API

JSON		 -> 		Object

string -> parse -> object

​	   	JSON.parse



카카오 2차 코딩테스트에 등장, 카카오 네이버 전공면접에 자주 등장.

`XMLHttpRequest()` - XML은 HTML이랑 닮은 형태의 데이터 형식. 웹 초창기에는 사람들이 HTML에 익숙해서 XML을 많이 씀. but JSON에 비해 불편.(안드로이드 프로그래밍의 뷰는 여전히 xml로 쓰게 되어있다) XML이 불편해서 YAML을 만들었다.

YAML(예믈) - "YAML Ain't Markup Language" 이름이 recursive. 열고 닫는 태그가 없어짐. JSON이랑 비슷해짐. 언어마다 XML을 YAML로 바꿔주는 기능이 있다. 근데 이것도 불편해서 js object 스럽게 데이터를 주고받게 되었고, 그게 바로 JSON(JavaScript Object Notation). JSON이 많이 쓰이기 전에 XHR이 등장해서 X가 붙은 것.



주소창에 입력하는 URL(URI와 유사)을 통해 원하는 곳으로 이동한다. 

but URL이 난잡하게 구성되어있으면 자신은 잘 알지 몰라도 서버 간 요청을 주고 받는 요즘의 시대에서는 좋지 못함. 따라서 정리된 URL 법칙이 필요로 해지게 된다. 

/posts/upgrade/1

/posts/1/update

update/1/posts

이러한 다양한 표현 방법을 하나로 정해보자. 



**RESTful**하게 만든다 : 최대한 심플하게 만든다. URL, 요청 주소의 꽃길이자 약속



1. 행위 - **HTTP Verb(Method)**

   기본적으로 동사를 어떻게 처리할지가 곤란. 어디에 배치해야할지 모르겠다.

   동사 다 뺀다.

   그리고 모든 작업은 CRUD로 수렴된다.

   C -> `POST`는 Create할 때만 쓰자

   R -> `GET`이라는 http 메소드는 Read할 때만 쓰자

   U -> `PUT`을 새로 만듦

   D -> `DELETE`을 새로 만듦

2. 자원(URI) - 

   1) 여러 개의 list -> `/posts` : 복수형

   2) 하나의 show/detail -> `/posts/1` : 자원(데이터)의 unique id를 써줌

   Update -> `posts/1`

   Delete -> `posts/1`

   URL은 두 가지밖에 없고 작업은 HTTP Verb를 통해 구분한다.

   

### REST 중심 규칙

1. URI는 정보의 자원(데이터)을 표현해야 한다.
2. 자원에 대한 행위(동사)는 HTTP Method로 표현한다.



다른 관계들도 표현해야 해서 이걸 정리하고자 페북에서 만든 것 -> **GraphQL**





## Koreanjson

REST API를 어떻게 짜는지 예시를 잘 보여줌



### POSTMAN

다운로드

PUT - 간단한 하나의 레코드 수정, PATCH - 여럿 수정. but 요즘 잘 구분하지 않음

body > raw 에서 직접 json파일을 만들어서 POST 요청을 보내보자.

```json
{
	"title": "제목 테스트",
    "body": "내용이다",
    "userId": 1
}
```

post 작성하는 url은 사이트 routes에서 확인 가능. `/posts`로 보내면 된다.

이걸 vscode에서 해보자





### 1REST.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>REST API</title>
</head>
<body>
    <script src="1app.js"></script>
</body>
</html>
```



### 1app.js

네이버 얼굴인식 API에서 POST로 요청을 보냈는데, 그때 data, headers에 요청을 담아서 보냈다. 이와 비슷하게 해볼 것.

요청 문서를 구성하는 것

- GET /posts
- Headers
  - 누가 보내는지(User-Agent)
  - 뭘 보내는지(파일 형태)
  - 어떤 언어로 보내는지(언어 인코딩)
- Body
  - 데이터

크롬이 하는 것은 이 요청 문서를 서버에 보내주는 것.

```js
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

XHR.send(JSON.stringify(data)) // 그냥 바로 요청을 보내는 GET과는 다르게 POST에서는 뭘 할지 알려줘야 함. 그걸 위의 setRequestHeader에서 수행

// 3. XHR.addEventListener()
XHR.addEventListener('load', function(donghoon) {  // donghoon : 받아온 데이터
    console.log(donghoon)  // progressEvent를 보여줌
    console.log(donghoon.target.response)
})  // 결과의 조건을 설정해줌. load : 성공적으로 받아옴. 
```





## 비동기처리

### 2dogjs.js

```js
// 30분 뒤에 종료를 알리는 js 코드

function finish() {
    setTimeout(function() {
        console.log("수업이 종료되었습니다.")
    }, 3000)  // 1000마이크로세컨드 = 1초
    // console.log("수업이 종료되었습니다.") // 여기에 넣은건 기다리지 않고 바로 출력되게 됨
}

console.log("수업 중")
finish()
console.log("땡땡땡")  // 시간 인자가 앞에 있을 때 -> 땡땡땡은 뜨는데 finish 내의 consolelog가 안됨.
```



`수업 중`, `땡땡땡`이 먼저 출력되고 `수업이 종료되었습니다`가 출력됨.

지금까지 배웠던 프로그래밍 언어는 한줄이 끝나면 다음줄로 가는 방식.

JS는 실행 순서가 다른 것 같은 느낌 -> **Non-blocking**적인 특징.

다른 일반적인 언어들은 blocking한다 -> 앞에 있는 코드가 끝나지 않으면 넘어가지 않는다(block한다)

js에는 non-blocking적인 성격을 갖는 함수들이 있고, 이들에 대해서는 막지 않는다.

-> 한 코드가 끝나기까지 기다리지 않는다 = 다른 코드가 먼저 실행되는 것을 막지 않는다. 



settimeout 외엔 기다리는 함수 다른 것이 없으므로 sleep과 유사한 함수를 직접 만들어보자.

`Date.now()`는 Unix epoch time 기준, 1마이크로세컨드 단위(1/1000초). 세계의 시작을 1970년 1월 1일 00:00:00(UTC) 기준으로 보고 있음.

```js
// 30분 뒤에 종료를 알리는 js 코드

function sleep() {
    let start = Date.now()
    while (Date.now() < start + 5000) {}  // 5초 동안 아무짓도 하지 말고 대기
}

function finish() {
    sleep()
    console.log("수업이 종료되었습니다.")
}

console.log("수업 중")
finish()
console.log("땡땡땡")  // 시간 인자가 앞에 있을 때 -> 땡땡땡은 뜨는데 finish 내의 consolelog가 안됨.
```

수업중

수업 종료

땡땡땡

순으로 순서대로 나온 것을 볼 수 있다 -> blocking하지 않음. 



왜 그런걸까? html에서 링크로 가보자

### 2index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <a href="https://www.naver.com">네이버</a>
    <script src="2dogjs.js"></script>
</body>
</html>
```

반복문이 돌고 있는 동안은 naver에 들어갈 수 없다.

js파일에서 `finish()`를 comment out 하고 콘솔창에서 직접 `finish()`를 입력해보자. 그렇게 해도 네이버 링크를 클릭해도 안 들어가짐 -> 5초 후에 자동으로 이동됨.

JS는 **single thread**의 언어. while문을 돌리기 시작하면 그걸 돌리는 동안 다른 것을 아무 것도 실행시키지 못함. 그래서 **시간이 많이 걸리는 명령**들은 나중에 돌리도록 하게 한 것. ex) IO operation(입출력 operation은 시간이 많이 걸림) -  파일 조작(3테라짜리 파일 열기), XHR request, API call

event loop가 감시한다 -> setTimeout을 만나면 완료되지 않은 함수 리스트 위에 `finish()`를 올려놓는 것. 

call stack에 마치지 못한 애들을 다 집어넣는다. 이벤트가 완료되면 콜스택에서 꺼내오는 것.



#### @기다리게 하고 싶으면 해당하는 non-blocking 함수에 콜백으로 넣어서 써라@



개발자가 짤 수 있는 thread가 single. 실제로 돌아가는 엔진은 멀티 스레드 방식.

setTimeout을 만난 순간부터 시간을 재기 시작. 선순위 작업을 수행하다가 시간이 다 지나면 선순위 작업 수행 도중에 setTimeout의 결과를 리턴.



프로세스, 스레드에 대한 개념 설명 -> ops-class, Geoffrey Challen















































































