# 190423 오전 nodejs lodash

js를 브라우저가 아닌 특정한 환경에서 구현하고자 하는 무브먼트의 결과물.

js를 하나의 제대로 된 언어로 만들고자 한 것.

react도 nodejs 위에서 돌아가는 라이브러리 중 하나.



## 인스톨

nodejs 사이트 > Windows Installer > 64-bit

setup 파일 all next > install

git bash 껐다 켜서

`$ node --version`

`$ npm --version` : node package manager. python pip와 비슷함. node에서 사용할 수 있는 패키지 설치 관리해줌. 우리가 node에 npm module을 올릴 수도 있다.

node 환경에서는 브라우저에서 쓸 수 있는 함수들을 지원하지 않는다.(prompt 등)



## 시작

vscode 190423/오전 폴더에서

`$ npm install lodash`

nodejs과 npm을 통해 브라우저만 조작하는 것이 아닌, 개발을 위한 언어로 사용될 수 있음.

`node_modules`와 `package-lock.json`이 생긴 걸 볼 수 있다.

`node_modules` - npm package들이 설치된 곳

`$ npm init` : `package.json`이 생긴 걸 볼 수 있다. 그 안에서 `dependencies`를 보면 설치된 package를 확인할 수 있음.



### 패키지 삭제

loadash를 잘못 설치했다.

`$ npm uninstall loadash`





### 1.menu.js 생성

변수 만들 때 항상 `var`라고 선언해야 함

import 하기 위해서도 var를 쓴다.

lodash = low dash라서 밑줄 변수로 받아서 씀.



여기서 console.log를 쓰면 terminal에 출력됨.

`console.error`는 에러를 출력

```js
var _ = require('lodash')
var menus = ['짜장면', '짬뽕', '볶음밥'] // Array 배열
menus[0]
// lodash로 python random.choice를 구현해보자
var pick = _.sample(menus)  // 랜덤으로 하나 꺼냄
console.log(pick)
console.log(`오늘의 메뉴는 ${pick}입니다.`) // string interpolation : 백틱 사용
```

실행 : `$ node 1.menu.js`



### 2.menu-with-photo.js 생성

```js
var _ = require('lodash') // 모듈 호출
var menus = ['짜장면', '짬뽕', '볶음밥'] // 배열 선언
var pick = _.sample(menus)
var object = { // 객체 선언
    "짜장면":'http://ojsfile.ohmynews.com/STD_IMG_FILE/2016/1214/IE002069160_STD.jpg',
    "짬뽕":'https://png.pngtree.com/element_origin_min_pic/00/00/11/095823383855d7e.jpg',
    "볶음밥":'http://food.chosun.com/site/data/img_dir/2012/08/08/2012080802054_0.jpg',
    key: 'value',
    
}
console.log(object['짜장면'])
console.log(object['key'])
console.log(object.key)

console.log(object[pick])  // 이것도 가능하다

// 이미지 주소 로드

```





### 3.lottery.js 생성

```js
var _ = require('lodash')
var numbers = _.range(1, 46)
console.log(numbers)
// node 3.lottery.js
var picks = _.sampleSize(numbers, 6)  // Camel case
console.log(`오늘의 행운의 번호는 ${picks}`)

var name = 'jack'
console.log(`제 이름은 ${name}`)
console.log('제 이름은 ' + name)

var baseURL = 'www.namer.com'
var article = '1'
console.log(`${baseURL}/${article}`)
```





### 4.min.js

매개변수 : 함수에서 주고받는 변수

```js
// 4.min.js
// 목표 : 최소값을 찾는다!
function getMin(a, b) {
    if (a > b) {
        return b
    }
    return a
}

// 또는

function getMin2(a, b) {
    var min;
    if (a > b) {
        min = b
    } else {
        min = a
    }
    return min
}

var min = getMin(3, 4)
console.log(min)
var min = getMin2(3, 4)
console.log(min)


function getMinFromArray(numbers) {
    var min = Infinity  // 어떠한 값보다 큰 값
    // TODO: 배열에서 최소값을 구하여 min에 할당
    for (num of numbers) {
        // 삼항 연산자
        min = min > num ? num : min
        // if (min > num) {
        //     min = num
        // }   
    }
    return min
}
var numbers = [1, 2, 3, 4, 5]
var min = getMinFromArray(numbers) // 1
console.log(min)

```



정수, 실수 모두 number type으로 인식

`$ npm init` -> package.json 생성. 앱을 어떻게 실행시킬지에 대한 스크립트를 담고 있고, 앱의 이름 버전 등을 담고 있음.

`$ npm install lodash` -> node_modules 생성. package.json dependencies에 lodash 추가

var 안 붙여도 선언 되지만, 명시적으로 해두는 걸로 습관을 들일 것.

string interpolation을 template literal이라고 부른다.





## ECMA 인터내셔널

2009 ES5 -> 2015 ES6(==ES2015)로 넘어오며 언어답게 만들기 위해 새로운 문법이 등장.

그 문법 중 하나를 소개.

**변수를 선언할 때 `var` 대신 `let`, `const`를 쓴다**

다음에 재할당이 없는 수에 대해 실수를 방지하기 위해 `const`를 씀



### 5.let-const.js

```js
let name = 'name'  // 변수: 재할당이 가능. 변할 수 있다.
name = 'jason'
console.log(name)

let sum = 0
sum += 2
console.log(sum)

const gender = 'man'  // 상수: 변하지 않음
// gender = 'woman'  // 에러 출력
console.log(gender)
```



그렇다면 `var`는? : 함수단위 스코프

`let`, `const` : 블록단위 스코프

if, for문 : 블록에 해당. 



```js
function test() {

    if (true) {
        var car = '소나타'
    }
    console.log(car)
}

test()  // '소나타' 출력

console.log(car)  // 에러 출력
```

같은 함수 스코프 이내이므로 제대로 출력된다.





```js
function test() {
    const color = 'red'
    if (true) {
        console.log(color)
        let car = '소나타'
    }
    console.log(car)
}

test()  // 에러 출력
```

상위 스코프에서 선언된 변수는 하위 스코프에서 접근 가능. but 하위 스코프에서 선언된 변수는 상위 스코프에서 접근 불가능



앞으로는 블록 단위 스코프 변수만 사용할 것이다. (if문 안에서 선언한 변수는 if문 밖에서 접근할 수 없다)



lodash documentation이 잘 되어있고 쓸 수 있는 게 많아서 잘 참고해볼 것.



### 6개 숫자 두 배열 중 겹치는 것 개수 찾기

```js
// 동훈
function match() {
    const numbers = _.range(1, 46)
    const picks = _.sampleSize(numbers, 6)
    console.log(`오늘의 행운의 번호는 ${picks}`)
    const lucky = _.size(_.intersection(luckyNumbers, picks))
    return lucky
}

console.log(match())

// jason
function match() {
    const numbers = _.range(1, 46)
    const picks = _.sampleSize(numbers, 6)
    let count = 0
    for (pick of picks) {
        if (_.includes(luckyNumbers, pick)) {
        // 또는 if (luckyNumbers.includes(pick)) {
            count += 1
        }
    }
    console.log(`My numbers ${picks}`)
    console.log(`Lucky numbers ${luckyNumbers}`)
    console.log(`Matches ${count}`)
}

match()
```

include 메소드는 lodash에서 가져와도 되고, array의 메소드로 써도 된다.

반환만 하는 것 : 순수함수

다른 대상을 바꾸는 것 : side-effect 발생시키는 것





# 190423 오후 event listener

vscode 확장 프로그램 : **Live Server(자동 리로드), bracket pair colorizer(괄호 색깔 매칭)**

파일 우클릭 -> open with live server를 하면 자동 리로딩(hot reload라고도 함)



### 1.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        .bg {
            background-color: #F7F7F7;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh; /* 100 vertical height */
        }
    </style>
</head>
<body>
    <div class="bg">
        <img height="150px" width="150px" src="teemo.png">
    </div>
    <script src="app.js"></script>
</body>
</html>
```



console 창에서 `document`라고 치면 html 정보를 객체화해서 띄워준다.

`document.title`, `document.body` 가능. HTML의 정보를 모두 객체화해서 담고 있다.

html 태그를 트리 구조로 담고 있다.

root : html - head - title

​								- meta

​					- body

`document.head.title`, `document.head.style` 가능

`document.title = "둘리야"`

```python
document = {
    head: {
        style: {
            
        }
    }
}
```

이렇게 거대한 오브젝트 안에 document를 담아서 처리하는 시스템 : **DOM(Document Object Model)**





## Event

Trigger(조건)			->			어떤 것이 일어난다

마우스 클릭

키보드 누르기



방향키를 누르면 둘리가 그 방향으로 움직이도록 해보자.



### 1.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Dooly</title>
    <style>
        .bg {
            background-color: #F7F7F7;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh; /* 100 vertical height */
        }
    </style>
</head>
<body>
    <div class="bg">
        <img id="teemo" height="150px" width="150px" src="teemo.png">
    </div>
    <script src="app.js"></script>
</body>
</html>
```



cf. const는 rebind가 안될 뿐이지, update는 가능. 항상 같은 주소값을 가리키도록 한다고 보면 될 듯. -> immutable한 값은 무조건 rebind를 해야하므로 const로 지정되어있다면 업데이트가 불가능하다.

```js
const me = {name: 'john', age: 34}
me.name = "ashley" // 이렇게 가능
```

### mutable/immutable

mutable : 사용자 정의 자료형 == 객체 in Javascript -> javascript는 모든 것이 객체다(원시 빼고)

immutable : 원시자료형(number, string, boolean, ...) -> 우리가 정의하지 않은 자료형



1. reassign : 초기화. let은 한번 초기화 하면 다시 let을 이 자리에 만들 수 없다.

2. rebind

3. update



​					var		let		const

reassign	  O			X			X

rebind		 O			O			X

update		O			O			O





```js
var name = "john"
var name = "john"
// 이건 되지만

let name = "john"
let name = "john"
// 이건 안된다
```





### app.js

클릭 이벤트

```js
const teemo = document.querySelector('#teemo')

console.log(typeof(teemo)) // object. not tag

// 티모를 클릭하면, "출동준비"라고 한다.

// 클릭이라는 이벤트가 일어나면 반응하게 함. 두번째 인자는 이벤트가 발생시 실행할 함수.
teemo.addEventListener('click', function() { alert('출동준비!')})
```



html 어떤 부분에서든 누르면 alert를 하게 하고 싶다면?

```js
const teemo = document.querySelector('#teemo')

console.log(typeof(teemo)) // object. not tag

// 티모를 클릭하면, "출동준비"라고 한다.

// 클릭이라는 이벤트가 일어나면 반응하게 함. 두번째 인자는 이벤트가 발생시 실행할 함수.
teemo.addEventListener('click', function() {
    alert('출동준비!')
})

// document에 대해 이뤄지는 이벤트를 알아서 받아서 print할 수 있다.
document.addEventListener('keydown', function(event) {
    // console.log(event)
    console.log(event.keyCode)
    document.write(`<h1>${event.keyCode}</h1>`)
})
```

키보드들이 다 다르게 배열되어 있어서, 키의 unique 값을 설정해둠([http://keycode.info](http://keycode.info/))



`===`의 의미 :  `1 == '1'`은 True를 반환하는데(대충등호), 이렇게 type을 알아서 cohersion하지 않도록 더욱 빡센 등호조건 강제(<https://dorey.github.io/JavaScript-Equality-Table/> 참조)

```js
const teemo = document.querySelector('#teemo')

console.log(typeof(teemo)) // object. not tag

// 티모를 클릭하면, "출동준비"라고 한다.

// 클릭이라는 이벤트가 일어나면 반응하게 함. 두번째 인자는 이벤트가 발생시 실행할 함수.
teemo.addEventListener('click', function() {
    alert('출동준비!')
})

// document에 대해 이뤄지는 이벤트를 알아서 받아서 print할 수 있다.
document.addEventListener('keydown', function(event) {
    // console.log(event)
    console.log(event.keyCode)
    // document.write(`<h1>${event.keyCode}</h1>`)
    if (event.keyCode === 38) {
        
    }
})
```



움직이게 해보자

```js
const teemo = document.querySelector('#teemo')

console.log(typeof(teemo)) // object. not tag

// 티모를 클릭하면, "출동준비"라고 한다.

// 클릭이라는 이벤트가 일어나면 반응하게 함. 두번째 인자는 이벤트가 발생시 실행할 함수.
teemo.addEventListener('click', function() {
    alert('출동준비!')
})

// document에 대해 이뤄지는 이벤트를 알아서 받아서 print할 수 있다.
document.addEventListener('keydown', function(event) {
    // console.log(event)
    console.log(event.keyCode)
    // document.write(`<h1>${event.keyCode}</h1>`)
    if (event.keyCode === 38) {
        teemo.style.marginBottom = "300px"
    } else if (event.keyCode === 40) {
        teemo.style.marginTop = "300px"
    }
})
```



여러번 눌러도 움직이게 해보자

```js
let x = 0
let y = 0

// document에 대해 이뤄지는 이벤트를 알아서 받아서 print할 수 있다.
document.addEventListener('keydown', function(event) {
    // console.log(event)
    console.log(event.keyCode)
    // document.write(`<h1>${event.keyCode}</h1>`)
    if (event.keyCode === 38) {
        y += 30
        teemo.style.marginBottom = `${y}px`
    } else if (event.keyCode === 40) {
        y -= 30
        teemo.style.marginBottom = `${y}px`
    }
})
```



상하좌우로 움직이게 해보자.

```js
let x = 0
let y = 0

// document에 대해 이뤄지는 이벤트를 알아서 받아서 print할 수 있다.
document.addEventListener('keydown', function(event) {
    // console.log(event)
    console.log(event.keyCode)
    // document.write(`<h1>${event.keyCode}</h1>`)
    if (event.keyCode === 38) {
        y += 30
        teemo.style.marginBottom = `${y}px`
    } else if (event.keyCode === 40) {
        y -= 30
        teemo.style.marginBottom = `${y}px`
    } else if (event.keyCode === 39) {
        x += 30
        teemo.style.marginLeft = `${x}px`
    } else if (event.keyCode === 37) {
        x -= 30
        teemo.style.marginLeft = `${x}px`
    }
})
```



## JSON

```js
JSONData = "{ 'coffee': 'Americano', 'iceCream': 'Red Velvet' }" // 키값은 string을 명시해줘야 제대로 인식함

const parsedData = JSON.parse(JSONData)

console.log(parsedData.coffee)
```



데이터를 저렇게 생성하면 안되고, key와 밸류를 

```js
const stringObject = JSON.stringify({"coffee": "Americano", "iceCream": "Red Velvet"})
const stringObject = JSON.stringify({'coffee': 'Americano', 'iceCream': 'Red Velvet'}) // 홑따옴표로 만들어도 쌍따옴표로 출력된다 -> 쌍따옴표로 만들자!
console.log(stringObject)

JSONData = '{"coffee": "Americano", "iceCream": "Red Velvet"}'
const parsedData = JSON.parse(JSONData)
console.log(parsedData.coffee)
```

직접 string으로 JSON을 만들어주려면 바깥에 홑따옴표, 안의 키, 밸류에 쌍따옴표를 써야 한다.