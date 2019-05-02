# 190502 localStorage, draw, random 개냥이

# 오전 localStorage, draw

### shorthand expression

`v-on` === `@`

`v-bind:` === `:`



### todo.html

원래 form에서는 엔터 치면 submit 됐지만 현재 form에서는 엔터가 작동하지 않는다.

이걸 바꿔보자.



`<input v-model="userInput" @keyup.enter="addInput">` : 엔터 쳤을 때 addInput

엔터의 keycode는 13

`@keyup.13="addInput"` 로도 가능

자주 쓰는 키들은 키코드뿐만 아니라 키워드로 지정되어있다.



`@keyup.space.enter`라고 하면 스페이스와 엔터 두 개 다 적용.

`delete` : delete와 backspace 모두 캡처



```html
        <h1>{{ header }}</h1>
        <p v-once>data 안의 data : {{ msg | capitalize }}</p>  <!-- v-once : 한번 렌더한 값이 있으면 변경하지 않고 그대로 쓴다. -->
        <p>{{ reverseMsg }}</p>
        <p>함수 실행의 결과 : {{ hello() }}</p>  <!-- return을 string으로 하는 함수는 실행된 결과를 바로 템플릿에서 출력 가능-->
        <img v-bind:src="imageSource" height=200 width=100>
        <br>
        <!-- v-bind -->
        <a :href="insta">오바마</a>
        <input v-model="userInput" @keyup.enter=> <!-- v-model로 bind한다 -->
        <!-- v-on -->
        <button @click="addInput">todo 추가</button>  <!-- 인자가 필요없는 함수일 경우 addInput()이라고 쓰지 않아도 됨-->
```





### 데이터를 저장하고 싶다

MVVM

VM은 Vuejs 그 자체

M이 Model -> DB

DB는 다루는 것이 다소 번거로움

브라우저의 저장소를 써보자.



## Local Storage

chrome 개발자 도구 > application > local storage

console 창에서 local storage를 다뤄보자.



### console

`window.localStorage`로 부르는 것이 원칙.

but window를 떼고 써도 된다.

키, 벨류를 지정하여 js object처럼 데이터를 넣어보자

`localStorage.setItem('name', 'jack')`

`localStorage.getItem('name')`

`localStorage.name`으로 바로 접근할 수도 있다.



배열을 넣고 싶다면?

`localStorage.setItem('students', ["junse", "donghoon", "boyoon"])`

`localStorage.getItem('students')` => `"junse,donghoon,boyoon"` : 그냥 쌩 string으로 들어가있음.



string으로 넣지만 배열을 넣은 것과 같은 효과를 만들어보자.

`localStorage.setItem('people', '["junse", "donghoon", "boyoon"]')`

배열처럼 생긴 string을 넣도록 하자.



JSON은 실제로 string이지만 받아온 JSON을 object처럼 쓸 수 있다.

`const arr = localStorage.getItem('people')`

`JSON.parse(arr)[0]`



object를 넣고 싶다면?

`let person = JSON.stringify({name: 'john', job: 'lecturer', address: 'seoul'})`

`localStorage.setItem('person', person)`

`localStorage.person`

`JSON.parse(localStorage.person)`

`JSON.parse(localStorage.person).name`

`JSON.parse(localStorage.person).job`



local storage는 반 영구적. 크롬을 지우거나 쿠키 캐시 삭제하거나 `localStorage.clear()`만 쓰지 않으면 남아있다. 창을 닫았다가 열어도 그대로 있다.



### localStorage를 vue에 적용해보자

```js
        let app = new Vue({
            el: '#app',
            data: {
                header: 'Todo App',
                msg: 'hello',
                userInput: '',
                // todos: [],
                todos: JSON.parse(localStorage.getItem('vue-app')),
                imageSource: 'http://file3.instiz.net/data/file3/2018/12/10/6/f/f/6ff7f02f2034b3da7144e8215aeba198.jpg',
                insta: 'https://www.instagram.com/barackobama/?hl=ko'
            },
			methods: {
                hello: function() {
                    // return 'hello'
                    // this.msg = 'happy hacking'
                    return this.msg
                },
                addInput: function() {
                    this.todos.push(this.userInput)
                    localStorage.setItem('vue-app', JSON.stringify(this.todos))
                    this.clearInput()
                },
                clearInput: function() {
                    // input을 클리어하기
                    this.userInput = ''
                },
            },
```

storage는 브라우저 명세 중의 하나. key value pair로 저장할 수 있도록. 

추천 광고는 쿠키나 브라우저 내의 어딘가에 저장된 데이터들을 참조한 것 -> `localStorage`, `sessionStorage`



`sessionStorage` : 로그인을 했을 때 데이터가 저장됨. 로그아웃 하면 비게 된다. 키와 밸류가 우리가 해석할 수 없는 것들. -> 쿠키와 세션을 배우게 되면 알게 될 것. restAPI 할 때 csrf token을 쿠키와 세션으로 관리하게 될 것인데 그것과 관련된 것. django가 브라우저에 몰래 숨겨둠.



특정 유저가 네이버 웹페이지를 사용할 때 모바일 버전/PC 버전 사용 여부에 대한 조각이 브라우저에 남겨짐 -> 다음 번 사용할 때 그 조각이 요청에 함께 담겨서 서버로 전송되고, 서버는 그것에 맞춰서 모바일/PC 버전 화면을 보여줌.



local이 session보다 좀 더 영구성이 있음. session은 탭만 닫으면 사라진다. local은 브라우저 베이스에 데이터가 저장되므로 사용자의 하드디스크에 데이터가 남게 됨(RAM에 두고 쓰다가 브라우저가 꺼지면 하드디스크에 저장)





### 코드를 좀 더 정리해보자

나중엔 키를 uglify하든지 해서 숨겨둬야 할 것. 코드 자체에 그대로 보여주면 안 됨.

또한 데이터베이스를 조작하는 로직은 따로 떼어서 써야함. (models.py를 따로 떼어내는 것과 같다)

```js
        // 일종의 작은 DB 부분(Model)
        const STORAGE_KEY = 'vue-app'
        const todoStorage = {  // ORM을 만들기 -> 미들웨어(중간에서 작업해주는 애들)
            fetch: function() {
                const data = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]')  // STORAGY_KEY가 스토리지에 저장되어있지 않을 때 [] 반환
                return data
            },
            save: function(todos) {
                localStorage.setItem(STORAGE_KEY, JSON.stringify(todos))
            }
        }
        // todoStorage.save()  // 저장
        // todoStorage.fetch()  // 불러오기

        // new Vue({  // 변수에 넣지 않아도 동작함. but console창 등에서 app.header로 변수들에 접근하기 위해 아래처럼 사용
        let app = new Vue({
            el: '#app',
            data: {
                header: 'Todo App',
                msg: 'hello',
                userInput: '',
                // todos: [],
                // todos: JSON.parse(localStorage.getItem('vue-app')),
                todos: todoStorage.fetch(),
                imageSource: 'http://file3.instiz.net/data/file3/2018/12/10/6/f/f/6ff7f02f2034b3da7144e8215aeba198.jpg',
                insta: 'https://www.instagram.com/barackobama/?hl=ko'
            },
            methods: {
                hello: function() {
                    // return 'hello'
                    // this.msg = 'happy hacking'
                    return this.msg
                },
                addInput: function() {
                    this.todos.push(this.userInput)
                    // localStorage.setItem(STORAGE_KEY, JSON.stringify(this.todos))
                    todoStorage.save(this.todos)
                    this.clearInput()
                },
                clearInput: function() {
                    // input을 클리어하기
                    this.userInput = ''
                },
            },
```

`||`는 python의 `or`와 같다. 앞의 것이 참이면 뒤의 것은 쳐다도 안 봄. STORAGE_KEY가 등록되어있지 않을 때 데이터를 가져오면 `null`을 출력하는데, 이 때 빈 배열을 반환하도록 함.



cf. 맞왜에러? -> 캐시 삭제 또는 파이어폭스에서 실행해볼 것



소스는 `github.com/edu-john/vue` 참조





## 그림 그리기 - css property 조작

### draw.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>색깔놀이</title>
    <style>
        .box {
            width: 50px;
            height: 50px;
            background-color: gray;
            margin: 5px;
            display: inline-block;
        }

        .red {
            background-color: red;
        }

        .green {
            background-color: green;
        }

        .yellow {
            background-color: yellow;
        }
    </style>
</head>
<body>
    <div id="app">
        <div class="box red"></div>
        <div class="box yellow"></div>
        <div class="box green"></div>
        <div class="box"></div>
        <input>        
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        
    </script>
</body>
</html>
```



input에 작성하는 값에 따라 색깔이 바뀌도록 설정.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>색깔놀이</title>
    <style>
        .box {
            width: 50px;
            height: 50px;
            background-color: gray;
            margin: 5px;
            display: inline-block;
        }

        .red {
            background-color: red;
        }

        .green {
            background-color: green;
        }

        .yellow {
            background-color: yellow;
        }
    </style>
</head>
<body>
    <div id="app">
        <!-- v-bind: -->
        <div :class="color" class="box"></div>  
        <div :class="color" class="box"></div>
        <div :class="color" class="box"></div>
        <div class="box"></div>
        <input v-model="color">
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        new Vue({
            el: '#app',
            data: {
                color: 'red'
            }
        })
    </script>
</body>
</html>
```





### 입력하고  click한 신호등에 대해 changeColor 하도록 만들기

특정한 요소에 대해 css를 적용할지 여부를 설정해줄 수 있음

`:class='{color: Boolean}'`

```html
<body>
    <div id="app">
        <!-- v-bind: -->
        <div @click="changeColor" :class='{red: isChanged}' class="box"></div>  
        <div @click="changeColor" :class='{yellow: isChanged}' :class="color" class="box"></div>
        <div @click="changeColor" :class='{green: isChanged}' :class="color" class="box"></div>
        <div class="box"></div>
        <input v-model="color">
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        new Vue({
            el: '#app',
            data: {
                color: 'red',
                isChanged: true,
            },
            methods: {
                changeColor: function() {
                    this.isChanged = !this.isChanged  // 참일 경우 거짓, 거짓일 경우 참
                }
            }
        })
    </script>
</body>
</html>
```





### methods, computed 차이

mothods: 캐싱이 안된다. template에서 괄호를 써도 돌아가고, 안 써도 돌아간다. 이벤트가 발생될 때만 불린다.

computed: 캐싱이 된다. template에서 괄호를 쓰면 제대로 돌아가지 않는다. 페이지가 처음 렌더 될 때 불리고, 이벤트가 발생될 때도 불린다. 값을 물고 있기 때문에 성능상으로 효율적. property와 비슷하게 취급되지만(괄호 없이 씀) 메소드를 짜듯이 만든다.



```html
<body>
    <div id="app">
        <!-- v-bind: -->
        <div @click="changeColor" :class='{red: isChanged}' class="box"></div>  
        <div @click="changeColor" :class='{yellow: isChanged}' :class="color" class="box"></div>
        <div @click="changeColor" :class='{green: changeClass}' :class="color" class="box"></div>
        <div class="box"></div>
        <input v-model="color">
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        new Vue({
            el: '#app',
            data: {
                color: 'red',
                isChanged: true,
            },
            methods: {
                changeColor: function() {
                    console.log("저는 메쏘드요")  // 클릭할 때 컴퓨티드와 함께 불린다.
                    this.isChanged = !this.isChanged  // 참일 경우 거짓, 거짓일 경우 참
                }
            },
            computed: {
                changeClass: function() {
                    console.log("저는 컴퓨티드요")  // 렌더되는 시점에 바로 불린다.
                    return this.isChanged
                }
            }
        })
    </script>
</body>
</html>
```





## 컴퓨티드와 메소드 차이 좀 더 분명하게 알아보자

### computed.html

클릭하면 숫자 올라가기 -> 메소드로 구현해보자

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
    <div id="app">
        <p>{{ number }}</p>
        <button @click="increase">UP</button>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
    new Vue({
        el: '#app',
        data: {
            number: 0
        },
        methods: {
            increase: function() {
                this.number++
            }
        }
    })
    </script>
</body>
</html>
```



더 간단한 방법

```html
    <div id="app">
        <p>{{ number }}</p>
        <!-- <button @click="increase">UP</button> -->
        <button @click="number++">UP</button>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
    new Vue({
        el: '#app',
        data: {
            number: 0
        },
        methods: {
            increase: function() {
                this.number++
            }
        }
    })
    </script>
```



메소드 불렀음 표시해보자

```html
<body>
    <div id="app">
        <p>{{ number }}</p>
        <button @click="increase">UP</button>
        <!-- <button @click="number++">UP</button> -->
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
    new Vue({
        el: '#app',
        data: {
            number: 0
        },
        methods: {
            increase: function() {
                console.log('메소드 불렀음')
                this.number++
            }
        }
    })
    </script>
</body>
```



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
    <div id="app">
        <p>{{ number }}</p>
        <button @click="increase">UP</button>
        <!-- <button @click="number++">UP</button> -->
        <p>{{ increase2 }}</p>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
    new Vue({
        el: '#app',
        data: {
            number: 0
        },
        methods: {
            increase: function() {
                console.log('메소드 불렀음')
                this.number++
            }
        },
        computed: {
            increase2: function() {
                console.log('컴퓨티드 불렀음')
                if (this.number > 10) {
                    return '10보다 커요'
                } else {
                    return '10보다 작아요'
                }
            }
        }
    })
    </script>
</body>
</html>
```

본질적으로 동일한 기능을 하지만 불리는 형태가 다르다. computed 변화가 없는 static한 데이터를 쓸 때 씀. async하게 fetching하는 데이터를 가져올 때는 computed를 쓰면 안 됨.





# 오후 random 강아지, 고양이 이미지

### index.html

초기 설정

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <!-- Vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!-- Axios -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
    <div id="main">
        <input type="radio" id="dog">
        <!-- label for에는 input id 지정해주면 됨 -->
        <label for="dog">댕댕이</label>
        <br />
        <input type="radio" id="cat">
        <label for="cat">고양이</label>
        <br />
    </div>
    <script>
        const dogAndCat = new Vue({
            el: '#main',
            data: {
                picked: '',
                image: '',  // imageURL 담을 곳
            }
        })
    </script>
</body>
</html>
```



input에 value가 없어서 클릭했을 때 똑같은 값으로 눌리게 된다. 

```html
    <div id="main">
        <input type="radio" id="dog" v-model="picked" value="야옹">
        <!-- label for에는 input id 지정해주면 됨 -->
        <label for="dog">댕댕이</label>
        <br />
        <input type="radio" id="cat" v-model="picked" value="때껄룩">
        <label for="cat">고양이</label>
        <br />
        <span>{{ picked }}</span>
    </div>
```



특정 버튼을 선택하고 console에서 `dogAndCat.picked`를 호출했을 때 해당 input의 value가 출력된다.



API에서 이미지를 가져오자

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <!-- Vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!-- Axios -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
    <div id="main">
        <input type="radio" id="dog" v-model="picked" value="야옹">
        <!-- label for에는 input id 지정해주면 됨 -->
        <label for="dog">댕댕이</label>
        <br />
        <input type="radio" id="cat" v-model="picked" value="때껄룩">
        <label for="cat">고양이</label>
        <br />
        <span>{{ picked }}</span>
        <img v-bind:src="" alt="">
    </div>
    <script>
        // 댕댕이 가지고 온다
        const getDogImage = function() {
            const URL = 'https://dog.ceo/api/breeds/image/random'
            axios.get(URL)
                .then(function (response) {
                    const imageUrl = response.data.message
                    console.log(imageUrl)
                    
                })
        }

        // 고양이 가지고 온다
        const getCatImage = function() {
            const URL = 'https://api.thecatapi.com/v1/images/search'
            axios.get(URL)
                .then(function (response) {
                    const imageUrl = response.data[0].url
                    console.log(imageUrl)
                })
        }

        getDogImage()
        getCatImage()

        const dogAndCat = new Vue({
            el: '#main',
            data: {
                picked: '',
                image: '',  // imageURL 담을 곳
            }
        })
    </script>
</body>
</html>
```





function을 메소드로 만들어보자.

```html
    <script>
        const dogAndCat = new Vue({
            el: '#main',
            data: {
                picked: '',
                image: '',  // imageURL 담을 곳
            },
            watch: {
                
            },
            methods: {
                // 댕댕이 가지고 온다
                getDogImage: function() {
                    const URL = 'https://dog.ceo/api/breeds/image/random'
                    axios.get(URL)
                        .then(function (response) {
                            const imageUrl = response.data.message
                            console.log(imageUrl)
                            
                        })
                },
                // 고양이 가지고 온다
                getCatImage: function() {
                    const URL = 'https://api.thecatapi.com/v1/images/search'
                    axios.get(URL)
                        .then(function (response) {
                            const imageUrl = response.data[0].url
                            console.log(imageUrl)
                        })
                }
            }
        })
    </script>
</body>
</html>
```





### test watch

```html
        <input type="text" v-model="test" />
    </div>
    <script>
        const dogAndCat = new Vue({
            el: '#main',
            data: {
                picked: '',
                image: '',  // imageURL 담을 곳
                test: '',
            },
            watch: {
                test: function(newValue, prevValue) {
                    console.log('new value ', newValue)
                    console.log('previous value ', prevValue)
                    console.log()
                }
            },
```





### 선택한 버튼에 맞는 개/고양이 이미지 보여주기

```html
    <div id="main">
        <input type="radio" id="dog" v-model="picked" value="야옹">
        <!-- label for에는 input id 지정해주면 됨 -->
        <label for="dog">댕댕이</label>
        <br />
        <input type="radio" id="cat" v-model="picked" value="때껄룩">
        <label for="cat">고양이</label>
        <br />
        <span>{{ picked }}</span>
        <img v-bind:src="image" />
        <!-- <input type="text" v-model="test" /> -->
    </div>
    <script>
        const dogAndCat = new Vue({
            el: '#main',
            data: {
                picked: '',
                image: '',  // imageURL 담을 곳
                test: '',
            },
            watch: {
                test: function(newValue, prevValue) {
                    console.log('new value ', newValue)
                    console.log('previous value ', prevValue)
                    console.log()
                },
                // data의 값을 보고 있다가 data의 값이 바뀌면 특정 함수를 실행
                // TODO: radio 버튼이 눌리면 해당 동물 이미지가 나오도록 하세요!
                picked: function(newPicked) {
                    if (newPicked === '야옹') {
                        this.getDogImage()
                    } else { // convention상 두 가지 조건으로 분기할 때는 else로 처리
                        this.getCatImage()
                    }
                }
            },
            methods: {
                // 댕댕이 가지고 온다
                getDogImage: function() {
                    const URL = 'https://dog.ceo/api/breeds/image/random'
                    axios.get(URL)
                        .then((response) => {
                            const imageUrl = response.data.message
                            console.log(imageUrl)
                            this.image = imageUrl
                        })
                },
                // 고양이 가지고 온다
                getCatImage: function() {
                    const URL = 'https://api.thecatapi.com/v1/images/search'
                    axios.get(URL)
                        .then((response) => {
                            const imageUrl = response.data[0].url
                            console.log(imageUrl)
                            this.image = imageUrl
                        })
                }
            }
        })
    </script>
```

















