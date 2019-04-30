# 190430 오전 Vue

1999 - AJAX(Asynchronous Javascript and XML) 등장. js를 비동기적으로 사용하고 XML로 데이터를 주고받음. 구글이 이걸 잘 이용해서 구글맵을 만듦. 당시엔 여전히 플래시를 많이 썼는데 쓰는 방식이 극혐이었다. 네이버가 여전히  플래시 사용 -> 스트리밍을 보기 위해 어도비 설치해야. 당시에 라이브러리가 많아서 많이 쓰였다. 

모바일로 넘어오며 AJAX가 더 커짐. 페이스북은 모든 요소가 AJAX로 만들어져있다. 하지만 일일이 다 짜려니 코드가 방대해짐

장고 framework - 파이썬으로 짜놓은 코드의 묶음. 무언가를 해준다.

코드가 방대해지며 js에서도 프레임워크가 등장했다. Vue는 중국계 미국인이 만들어져서 중국에서 핫함. JS 기반의 프레임워크를 **SPA(Single Page Application)**라고 한다. CRUD 등등이 하나의 페이지에서 가능. 페이지를 변경하지 않더라도, 페이지 렌더를 위한 request/response 통신이 아닌 다른 방식으로, js를 통해 request를 보내서 데이터 일부분에 대한 response를 받아와서 처리함. -> 데이터 받아오는 작업을 **JSON**으로 하고 있는 것(AJAJ, not AJAX) 그 중에서 Vue를 배울 것이다.

React는 자유도가 높다. 이해도가 높으면 내가 자유롭게 만들어서 쓸 수 있다. Angular는 자유도가 낮다 -> Django처럼 시키면 알아서 다 해준다. 장고가 쓰는 여러 feature를 이해해야하고, 그것만 잘 쓰면 원하는 것들을 다 해줌. 배워야 하는 규칙들과 거기 맞춰서 해줘야 하는 것들. React는 같은 것을 짜도 코드가 제각각. 약속을 최소화한 프레임워크

Vue는 React와 Angular의 장점들을 통합함. React, Angular에 비해 Vue가 가볍고, npm을 통해서 여러 것을 깔아야 한다. 바로 뷰를 써보자.





## CDN(index.html)

```html
<!-- Beautify Version. 도움되는 콘솔 경고를 포함한 개발 버전 -->
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

```html
<!-- Uglyfy Version. 상용버전, 속도와 용량이 최적화됨. -->
<script src="https://cdn.jsdelivr.net/npm/vue"></script>
```

띄어쓰기도 다 용량임.

cf. Online Javascript Beutifier에서 uglyfy 버전을 beutify 할 수 있다.

우리 학습은 Beautify version으로 할 것.

소스가 궁금할 때 src의 스크립트를 참조하면 됨.

DJango에 붙이는 등으로 상용화할 때는 상용버전을 쓰면 됨.



스크립트는 body 하단에 붙이는 것이 좋다. -> zzu.li/jsscript(<http://stevesouders.com/examples/rule-js-bottom.php>) 

Scripts Top vs. Bottom을 보면 차이가 확연하다.

js 로드를 위에서 하면 로드를 다 한 후에야 body 요소들을 렌더함. 네트워크 환경이 나쁠 경우에는 차이가 잘 드러나게 된다.

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
    <h1>이건 헤더</h1>
    <!-- Beautify Version. 도움되는 콘솔 경고를 포함한 개발 버전 -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</body>
</html>
```



event를 받아서 처리해보자

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
    <h1>이건 헤더</h1>
    <p id="app">눌러보세요</p>
    <button id="btn">버튼</button>
    <!-- Beautify Version. 도움되는 콘솔 경고를 포함한 개발 버전 -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        // btn이 눌러졌을때(클릭됐을때), p 태그 안에 "누르지마"
        const btn = document.querySelector('#btn')
        btn.addEventListener('click', function (event) {
            console.log(event)
            app = document.querySelector('#app')
            app.innerText = "누르지마"
        })
    </script>
</body>
</html>
```



버튼이 엄청나게 많다면 어떨까? vue로 만든다면 편하게 할 수 있다. 한번 써보자.

CDN을 통해 받아온 Vue라는 객체를 쓴다. 인자로 오브젝트를 넣게 되는데, property가 정해져있다.

data는 django의 view에서 context로 넘겨주던 dictionary랑 비슷한 것.

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>이건 헤더</h1>
    <p id="app">{{ msg }}</p>
    <button id="btn">버튼</button>
    <!-- Beautify Version. 도움되는 콘솔 경고를 포함한 개발 버전 -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        // btn이 눌러졌을때(클릭됐을때), p 태그 안에 "누르지마"
        // const btn = document.querySelector('#btn')
        // btn.addEventListener('click', function (event) {
        //     console.log(event)
        //     app = document.querySelector('#app')
        //     app.innerText = "누르지마"
        // })
        let app = new Vue({
            el: '#app', // element 명시
            data: {
                msg: 'Happy Hacking!'
            }  // object로 데이터를 넣어줌
        })
    </script>
</body>
</html>
```



js로 짰을 때는 **imperative programming(명령적 프로그래밍)** -> 쿼리셀렉터를 통해 원하는 장소를 찾은 다음 그 안에 내용을 채워줘라. 찾을 것을 지정해줘야 함. 프로그램이 커지게 되면 힘든 부분이 생김.

- 상세하게 알려줘야 함
- 절차적으로(step by step)

이걸 극복하고자 **declarative(descriptive) programming** 등장



### id `app` element의 내용을 `hi`라고 바꿀 때

1. imperative(how-to)

   - id=`app` element를 찾는다.
   - 해당 element 내용을 바꾼다(`hi`)

2. delcarative(what만 정의하면 된다)

   설명하듯이 미리 설계한다.

   ```js
   el: '#app',
   data: {
       msg: 'Hi'
   }
   ```

   하나의 객체로 표현.

   

사람은 퉁쳐서 what으로 생각한다. how-to는 간단한 문제풀이에는 괜찮지만, 상용 프로그램을 만들기에는 난해한 점이 있다. but 선언적 프로그래밍에는 따라야하는 규칙들이 있다. 서브웨이에서 삼겹살 덮밥을 시킬 수 없음. 



### console

```js
app // vue 객체 볼 수 있음
app.msg = "곧 쉬는시간 힘내세요"
```

쌩js로 짰을 때 일일이 찾아서 바꿔주는 작업을 했던 과정을 거치지 않아도 된다. 객체만 잘 정의하면 바꾸고 보여주는 것은 vue가 알아서 다 해줌.



## vue devtools

vue devtools

크롬 확장프로그램 설치하면 개발하는 데 도움 많이 됨. 디버그 툴과 비슷. 객체를 포장해서 보여줌. 

cf. 뷰를 쓰는 서비스 : gitlab

뷰를 쓰는 페이지에서 개발자도구 탭 최우측에 vue 탭이 생긴것을 볼 수 있음

gitlab.com으로 가서 써보면

로그인해보면 detect는 되지만 product mode로 되어있어서 vue탭을 쓸 수 없다.





### Vue에 담는 것들 정리

methods, directives를 조합해서 자주 쓰게 될 것.

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
    <h1>이건 헤더</h1>
    <p id="app">{{ msg }}</p>
    <button id="btn">버튼</button>
    <!-- Beautify Version. 도움되는 콘솔 경고를 포함한 개발 버전 -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        // btn이 눌러졌을때(클릭됐을때), p 태그 안에 "누르지마"
        // const btn = document.querySelector('#btn')
        // btn.addEventListener('click', function (event) {
        //     console.log(event)
        //     app = document.querySelector('#app')
        //     app.innerText = "누르지마"
        // })
        let app = new Vue({
            el: '#app', // element 명시
            data: {
                msg: 'Happy Hacking!'
            },  // object로 데이터를 넣어줌
            methods: {

            },
            directives: {

            },
            watch: {

            },
            computed: {

            },
        })
    </script>
</body>
</html>
```



바꿔줄 대상을 지정하고(`app`), 그것이 담고 있는 속성과 행위를 정해준다.

`el`을 통해 element를 탑재(마운트)하고(`el: '#app'`)

`data`를 통해 속성으로서 변수들을 담는다

`app.msg`로 데이터에 접근하는 데 이렇게 부르는 건 별명을 쓰는 것이고, `app.$data`에서 오브젝트를 확인할 수 있고, 실제 이름은 `app.$data.msg`

`$`는 vue의 property라는 노테이션이므로 변수 이름 앞에 $를 붙이면 안된다.

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
    <h1>이건 헤더</h1>
    <p id="app">{{ msg }} - {{ count }}</p>
    <button id="btn">버튼</button>
    <!-- Beautify Version. 도움되는 콘솔 경고를 포함한 개발 버전 -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        // btn이 눌러졌을때(클릭됐을때), p 태그 안에 "누르지마"
        // const btn = document.querySelector('#btn')
        // btn.addEventListener('click', function (event) {
        //     console.log(event)
        //     app = document.querySelector('#app')
        //     app.innerText = "누르지마"
        // })
        let app = new Vue({
            // 주어(장소 부사구)
            el: '#app', // element 명시
            // 목적어
            data: {  // object로 데이터를 넣어줌
                msg: 'Happy Hacking!',
                count: 3+2,  // 5 출력. 연산도 수행한다.
            },
            // 동사
            methods: {
                plus: function() {
                    this.count++  // this는 app을 가리킨다.
                }
            },
            directives: {

            },
            watch: {

            },
            computed: {

            },
        })
        app.plus()  // 메소드를 여기서 불러와서 쓸 수 있다.
    </script>
</body>
</html>
```

console 창에서도 `app.plus()`를 통해 count++ 할 수 있다.



## MVVM

지금 보고 있는 Vue 구조를 MVVM이라고 한다. (Django는 MVT - url(문지기), model, view, template)

View - 템플릿에 해당(django의 template)

View Model - 중간에서 템플릿을 보여주는 역할 -> 이게 Vue js라고 보면 됨

Model



![mvvmì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://www.oreilly.com/library/view/learning-javascript-design/9781449334840/httpatomoreillycomsourceoreillyimages1547825.png)

간단하게 말하면, 화면에서 보여줄 내용을 javascript 객체로 선언(묘사)해서 전달하는 것. + how-to는 전달하지 않는다.





## todo 앱 만들기(todo.html)

특정하는 부분을 vue에 mount시키자.

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Todo App</title>
</head>
<body>
    <div id="app">
        <h1>{{ header }}</h1>
        {{ header2 }}
        <span v-html="header2"></span>  <!-- v-html을 지정해주면 vue가 조작해준다. -->
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        let app = new Vue({  // 무언가를 상속받아서 쓰는 객체라고 보면 될 것(models.Model과 같은 것이라 보면 됨)
            el: '#app',
            data: {
                header: 'Todo App',
                header2: '<h1>Todo App</h1>',  // 이렇게는 안 된다.
            }
        })
    </script>
</body>
</html>
```

v-html은 크롤링이 힘들게 한다. span 태그를 먼저 렌더링 하고(일반적으로 이 시점에 크롤링을 하게 됨), v-html을 통해 데이터를 넣어주기 때문.



배열 넘기기, v-for, v-if 사용 가능

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Todo App</title>
</head>
<body>
    <div id="app">
        <h1>{{ header }}</h1>
        {{ header2 }}
        <span v-html="header2"></span>  <!-- v-html을 지정해주면 vue가 조작해준다. -->
        <h2>{{ subheader }}</h2>
        <ul>
            <li v-for="t in todo">{{ t }}</li>
        </ul>
        <p v-if="checked">{{ todo }}</p>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        let app = new Vue({  // 무언가를 상속받아서 쓰는 객체라고 보면 될 것(models.Model과 같은 것이라 보면 됨)
            el: '#app',
            data: {
                header: 'Todo App',
                header2: '<h1>Todo App</h1>',  // 이렇게는 안 된다.
                subheader: 'This is todo app',
                todo: ['동사무소 가기', '입대확인증 뽑기', '재입대하기'],  // 배열도 넘길 수 있다.
                checked: true,
            }
        })
    </script>
</body>
</html>
```



오브젝트도 넘길 수 있다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Todo App</title>
</head>
<body>
    <div id="app">
        <h1>{{ header }}</h1>
        {{ header2 }}
        <span v-html="header2"></span>  <!-- v-html을 지정해주면 vue가 조작해준다. -->
        <h2>{{ subheader }}</h2>
        <ul>
            <li v-for="t in todo">{{ t }}</li>
        </ul>
        <p v-if="checked">{{ todo }}</p>
        <ol>
            <li v-for="dh in donghoon">{{ dh }}</li> <!-- python과 다르게 key가 아니라 value가 나온다 -->
        </ol>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        let app = new Vue({  // 무언가를 상속받아서 쓰는 객체라고 보면 될 것(models.Model과 같은 것이라 보면 됨)
            el: '#app',
            data: {
                header: 'Todo App',
                header2: '<h1>Todo App</h1>',  // 이렇게는 안 된다.
                subheader: 'This is todo app',
                todo: ['동사무소 가기', '입대확인증 뽑기', '재입대하기'],  // 배열도 넘길 수 있다
                checked: true,
                donghoon: {
                    name: "동훈",
                    gunPil: true,
                    major: "기계공학",
                },
                posts: [  // 이런 자료들을 많이 보게 될 것
                    {
                        id: 1,
                        title: '제목1',
                        content: '내용2',
                    }, {}, {}, {}
                ],
                posts: fetch('/posts')  // json으로 posts를 받아와서 템플릿에 출력하는 패턴이 될 것.
            }
        })
    </script>
</body>
</html>
```





### v-model

폼 입력도 가능. 이젠 form을 브라우저에게 맡길 필요가 없다. form을 쓰면 페이지를 리로드 해야하는데, SPA에서는 리로드 없이 하므로 다르다.

``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Todo App</title>
</head>
<body>
    <div id="app">
        <h1>{{ header }}</h1>
        {{ header2 }}
        <span v-html="header2"></span>  <!-- v-html을 지정해주면 vue가 조작해준다. -->
        <h2>{{ subheader }}</h2>
        <h2>{{ subheader }}</h2>
        <h2>{{ subheader }}</h2>
        <h2>{{ subheader }}</h2>
        <ul>
            <li v-for="t in todo">{{ t }}</li>
        </ul>
        <p v-if="checked">{{ todo }}</p>
        <ol>
            <li v-for="dh in donghoon">{{ dh }}</li> <!-- python과 다르게 key가 아니라 value가 나온다 -->
        </ol>
        <input v-model="subheader">  <!-- subheader를 이 페이지에서 바로 수정할 수 있다(양방향 바인딩) -->
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        let app = new Vue({  // 무언가를 상속받아서 쓰는 객체라고 보면 될 것(models.Model과 같은 것이라 보면 됨)
            el: '#app',
            data: {
                header: 'Todo App',
                header2: '<h1>Todo App</h1>',  // 이렇게는 안 된다.
                subheader: 'This is todo app',
                todo: ['동사무소 가기', '입대확인증 뽑기', '재입대하기'],  // 배열도 넘길 수 있다
                checked: true,
                donghoon: {
                    name: "동훈",
                    gunPil: true,
                    major: "기계공학",
                },
                posts: [  // 이런 자료들을 많이 보게 될 것
                    {
                        id: 1,
                        title: '제목1',
                        content: '내용2',
                    }, {}, {}, {}
                ],
                posts: fetch('/posts')  // json으로 posts를 받아와서 템플릿에 출력하는 패턴이 될 것.
            }
        })
    </script>
</body>
</html>
```





# 오후 axios

vue에서 python의 `requests`와 비슷한 것

cf. `git commit`만 쓰면 edit 창이 열리면서 commit 메시지 쓸 수 있다. 그 내용은

1. 나는 로그인 로직을 구현했음 ex) Implement login logic
2. blank
3. Install module ...



Axios는 github 페이지를 가보면

0.19 version임에도 별이 6만개

**Ajax 콜을 해주는 라이브러리**

`fetch`, `XMLHttpRequest` 대신에 axios를 쓸 것이다.



### 설치방법

1. npm:

   ```bash
   $ npm install axios
   ```

2. cdn:

   ```html
   <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
   ```



## 시작(1.index.html, 1.useAxios.js)

### 1.index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <!-- axios -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
    <div id="img-div"></div>
    <script src="./1.useAxios.js"></script>
</body>
</html>
```

`1.useAxios.js`를 사용할 것이기 때문에 그 이전에 미리 axios를 호출해둬야한다. 그래서 head에 넣었다. body script 위에 넣어도 되긴 함.



### 1.useAxios.js

```js
// useAxios.js

const URL = 'https://dog.ceo/api/breeds/image/random'
// html에서 axios를 불러왔으므로 바로 접근 가능
axios.get(URL)  // AJAX call - 비동기적으로 동작. promise를 반환
    .then(response => {
        console.log(response)
    })

```

html 파일을 열어서 확인해보면 이미 js object로 parsing이 되어있음을 확인할 수 있다.



이미지를 출력해보자

```js
// useAxios.js

const URL = 'https://dog.ceo/api/breeds/image/random'
console.log(URL, axios)
// html에서 axios를 불러왔으므로 바로 접근 가능
axios.get(URL)  // AJAX call - 비동기적으로 동작. promise를 반환
    .then(response => {
        console.log(response)  // 객체가 parsing 되어 반환
        const imageUrl = response.data.message
        const imageBox = document.querySelector('#img-div')
        const image = document.createElement('img')
        image.src = imageUrl
        imageBox.appendChild(image)
    })

```



위 코드를 async-await로 바꾸기

```js
// TODO: 위 코드를 async-await로 바꾸기
const getImage = async () => {
    const res = await axios.get(URL)
    console.log(res)
    const imageUrl = res.data.message
    const imageBox = document.querySelector('#img-div')
    const image = document.createElement('img')
    image.src = imageUrl
    imageBox.appendChild(image)
}

// 3개 이미지 가능
getImage()
getImage()
getImage()
```

`await`을 쓰지 않고 response를 출력해보면 Promise만 반환된다 -> 이러면 비동기처리 함수임을 파악하고 async, await을 붙여주면 된다.	





## 37 homework

CORS: Cross Origin Resource Sharing

에러 발생 -> 서비스 하는 서버 내에서 요청을 보내야 허가한 요청이라고 인식해서 통과시켜줌.

서버 : https://www.dhlottery.co.kr/...

현재 : localhost

사이트 페이지 안의 console 창에서 코드를 치면 제대로 작동한다.



















