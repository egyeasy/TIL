# 190501 todo, movie-search-app

# 오전 todo

### todo.html

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
        <p>{{ hello() }}</p>  <!-- return을 string으로 하는 함수는 실행된 결과를 바로 템플릿에서 출력 가능-->
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        // new Vue({  // 변수에 넣지 않아도 동작함. but console창 등에서 app.header로 변수들에 접근하기 위해 아래처럼 사용
        let app = new Vue({
            el: '#app',
            data: {
                header: 'Todo App',
            },
            methods: {
                hello: function() {
                    return 'hello'
                }
            }
        })
    </script>
</body>
</html>
```

프록시 -> `app.$data.header`라고 쓰지 않고 `app.header`로 바로 header에 접근할 수 있다.

methods의 경우에는 `app.hello()`로 바로 접근해야 한다.



data를 methods 안에서 사용 가능

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
        <p>{{ hello() }}</p>  <!-- return을 string으로 하는 함수는 실행된 결과를 바로 템플릿에서 출력 가능-->
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        // new Vue({  // 변수에 넣지 않아도 동작함. but console창 등에서 app.header로 변수들에 접근하기 위해 아래처럼 사용
        let app = new Vue({
            el: '#app',
            data: {
                header: 'Todo App',
                msg: 'hello'
            },
            methods: {
                hello: function() {
                    // return 'hello'
                    return this.msg
                }
            }
        })
    </script>
</body>
</html>
```



이렇게 하면?

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
        <p>함수 실행의 결과 : {{ hello() }}</p>  <!-- return을 string으로 하는 함수는 실행된 결과를 바로 템플릿에서 출력 가능-->
        <p>data 안의 data : {{ msg }}</p>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        // new Vue({  // 변수에 넣지 않아도 동작함. but console창 등에서 app.header로 변수들에 접근하기 위해 아래처럼 사용
        let app = new Vue({
            el: '#app',
            data: {
                header: 'Todo App',
                msg: 'hello'
            },
            methods: {
                hello: function() {
                    // return 'hello'
                    this.msg = 'happy hacking'
                    return this.msg
                }
            }
        })
    </script>
</body>
</html>
```

두 태그 다 happy hacking으로 바뀜. 두 태그 중 하나는 예전 버전으로 두고 싶다면?

`v-once`를 활용한다.

한번 렌더한 값이 있으면 변경하지 않고 그대로 쓴다.

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
        <p v-once>data 안의 data : {{ msg }}</p>  <!-- v-once : 한번 렌더한 값이 있으면 변경하지 않고 그대로 쓴다. -->
        <p>함수 실행의 결과 : {{ hello() }}</p>  <!-- return을 string으로 하는 함수는 실행된 결과를 바로 템플릿에서 출력 가능-->
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        // new Vue({  // 변수에 넣지 않아도 동작함. but console창 등에서 app.header로 변수들에 접근하기 위해 아래처럼 사용
        let app = new Vue({
            el: '#app',
            data: {
                header: 'Todo App',
                msg: 'hello'
            },
            methods: {
                hello: function() {
                    // return 'hello'
                    this.msg = 'happy hacking'
                    return this.msg
                }
            }
        })
    </script>
</body>
</html>
```





### directive(지시자)

`v-html`, `v-for`, `v-if`, `v-model`, `v-once`

vue js에게 html tag를 통해 지시하는 것. 열 몇 개 정도 있다.

but custom 정의를 통해 사용자 정의 directive를 만들 수 있다.



### v-model

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
        <p v-once>data 안의 data : {{ msg }}</p>  <!-- v-once : 한번 렌더한 값이 있으면 변경하지 않고 그대로 쓴다. -->
        <p>함수 실행의 결과 : {{ hello() }}</p>  <!-- return을 string으로 하는 함수는 실행된 결과를 바로 템플릿에서 출력 가능-->
        <input v-model="msg">
        <p>{{ msg }}</p>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        // new Vue({  // 변수에 넣지 않아도 동작함. but console창 등에서 app.header로 변수들에 접근하기 위해 아래처럼 사용
        let app = new Vue({
            el: '#app',
            data: {
                header: 'Todo App',
                msg: 'hello'
            },
            methods: {
                hello: function() {
                    // return 'hello'
                    // this.msg = 'happy hacking'  // 바꾸는 작업이 범인
                    return this.msg
                }
            }
        })
    </script>
</body>
</html>
```

function에서 바꾸는 작업이 있으면 input으로 msg를 못바꾼다. 그래서 comment out



버튼을 클릭했을 때만 msg가 바뀌도록 하려면?

`v-on:click` 사용

form은 쓰지 않는다 -> 페이지 변경을 요구하는 태그이므로

v-on에 담을 메소드를 정의하고 써야 한다.

### 내가 한 방법

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
        <p v-once>data 안의 data : {{ msg }}</p>  <!-- v-once : 한번 렌더한 값이 있으면 변경하지 않고 그대로 쓴다. -->
        <p>함수 실행의 결과 : {{ hello() }}</p>  <!-- return을 string으로 하는 함수는 실행된 결과를 바로 템플릿에서 출력 가능-->
        <input ref="inputField">
        <button v-on:click="addInput">todo 추가</button>  <!-- 인자가 필요없는 함수일 경우 addInput()이라고 쓰지 않아도 됨-->
        <p>{{ userInput }}</p>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        // new Vue({  // 변수에 넣지 않아도 동작함. but console창 등에서 app.header로 변수들에 접근하기 위해 아래처럼 사용
        let app = new Vue({
            el: '#app',
            data: {
                header: 'Todo App',
                msg: 'hello',
                userInput: '',
            },
            methods: {
                hello: function() {
                    // return 'hello'
                    // this.msg = 'happy hacking'
                    return this.msg
                },
                addInput: function() {
                    this.userInput = this.$refs.inputField.value
                }
            }
        })
    </script>
</body>
</html>
```



### todos 데이터 만들기

v-model로 input 연결하고, array에 담아서 array의 데이터를 보여주는 것이 vue 스러운 방식

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
        <p v-once>data 안의 data : {{ msg }}</p>  <!-- v-once : 한번 렌더한 값이 있으면 변경하지 않고 그대로 쓴다. -->
        <p>함수 실행의 결과 : {{ hello() }}</p>  <!-- return을 string으로 하는 함수는 실행된 결과를 바로 템플릿에서 출력 가능-->
        <input v-model="userInput"> <!-- v-model로 bind한다 -->
        <button v-on:click="addInput">todo 추가</button>  <!-- 인자가 필요없는 함수일 경우 addInput()이라고 쓰지 않아도 됨-->
        <ul>
            <li v-for="(todo, index) in todos">  <!-- enumerate하고 싶다면 (value, key)로 지정 -->
                <span>{{ index + 1 }} : {{ todo }}</span> <!-- 혹시 styling이 필요할 때 작업해주기 위해 span 태그를 넣어둠 -->
            </li>
        </ul>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        // new Vue({  // 변수에 넣지 않아도 동작함. but console창 등에서 app.header로 변수들에 접근하기 위해 아래처럼 사용
        let app = new Vue({
            el: '#app',
            data: {
                header: 'Todo App',
                msg: 'hello',
                userInput: '',
                todos: []
            },
            methods: {
                hello: function() {
                    // return 'hello'
                    // this.msg = 'happy hacking'
                    return this.msg
                },
                addInput: function() {
                    this.todos.push(this.userInput)
                }
            }
        })
    </script>
</body>
</html>
```

오후엔 브라우저의 Local Storage(브라우저의 임시저장소)에 저장해서 쓰는 것을 해볼 것.





### v-bind

img, a 태그

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
        <p v-once>data 안의 data : {{ msg }}</p>  <!-- v-once : 한번 렌더한 값이 있으면 변경하지 않고 그대로 쓴다. -->
        <p>함수 실행의 결과 : {{ hello() }}</p>  <!-- return을 string으로 하는 함수는 실행된 결과를 바로 템플릿에서 출력 가능-->
        <img v-bind:src="imageSource">
        <a v-bind:href="insta">오바마</a>
        <input v-model="userInput"> <!-- v-model로 bind한다 -->
        <button v-on:click="addInput, clearInput">todo 추가</button>  <!-- 인자가 필요없는 함수일 경우 addInput()이라고 쓰지 않아도 됨-->
        <ul>
            <li v-for="(todo, index) in todos">  <!-- enumerate하고 싶다면 (value, key)로 지정 -->
                <span>{{ index + 1 }} : {{ todo }}</span> <!-- 혹시 styling이 필요할 때 작업해주기 위해 span 태그를 넣어둠 -->
            </li>
        </ul>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        // new Vue({  // 변수에 넣지 않아도 동작함. but console창 등에서 app.header로 변수들에 접근하기 위해 아래처럼 사용
        let app = new Vue({
            el: '#app',
            data: {
                header: 'Todo App',
                msg: 'hello',
                userInput: '',
                todos: [],
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
                },
                clearInput: function() {
                    // input을 클리어하기
                    this.userInput = ''
                }
            }
        })
    </script>
</body>
</html>
```



### input 입력 후 clear하기

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
        <p v-once>data 안의 data : {{ msg }}</p>  <!-- v-once : 한번 렌더한 값이 있으면 변경하지 않고 그대로 쓴다. -->
        <p>함수 실행의 결과 : {{ hello() }}</p>  <!-- return을 string으로 하는 함수는 실행된 결과를 바로 템플릿에서 출력 가능-->
        <img v-bind:src="imageSource" height=200 width=100>
        <br>
        <a v-bind:href="insta">오바마</a>
        <input v-model="userInput"> <!-- v-model로 bind한다 -->
        <button v-on:click="addInput">todo 추가</button>  <!-- 인자가 필요없는 함수일 경우 addInput()이라고 쓰지 않아도 됨-->
        <ul>
            <li v-for="(todo, index) in todos">  <!-- enumerate하고 싶다면 (value, key)로 지정 -->
                <span>{{ index + 1 }} : {{ todo }}</span> <!-- 혹시 styling이 필요할 때 작업해주기 위해 span 태그를 넣어둠 -->
            </li>
        </ul>
        <p>{{ todos }}</p>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        // new Vue({  // 변수에 넣지 않아도 동작함. but console창 등에서 app.header로 변수들에 접근하기 위해 아래처럼 사용
        let app = new Vue({
            el: '#app',
            data: {
                header: 'Todo App',
                msg: 'hello',
                userInput: '',
                todos: [],
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
                    this.clearInput()
                },
                clearInput: function() {
                    // input을 클리어하기
                    this.userInput = ''
                },
            },
            filters: {
                
            }
        })
    </script>
</body>
</html>
```







### filters

todos를 뒤집어서 보여줄 수도 있다.

```html
<p>{{ todos.reverse() }}</p>
```



join을 할 수도 있다.

```html
<p>{{ todos.reverse().join(" ") }}</p>
```



이런 작업을 filter를 통해 미리 정의할 수 있다.

```html
        <p>{{ todos | reverseJoin }}</p>  <!-- 인자 | 필터이름-->

...
            filters: {
                reverseJoin: function(val) {  // 받으려는 인자 value
                    return val.reverse().join(' ')
                }
            }
```



string의 0번째 : `"hello"[0]`, `"hello".charat(0)`

charAt이 undefined를 반환하지 않아서 안전한 편

`"hello".slice(1)` : 1번부터 끝까지 슬라이스



```html

        <p>{{ todos | reverseJoin }}</p>  <!-- 인자 | 필터이름-->

        
        
        
            },
            filters: {
                reverseJoin: function(val) {  // 받으려는 인자 value
                    return val.reverse().join(' ')
                },
                capitalize: function(val) {  // 첫번째 글자만 대문자로 바꾸기
                    if (!val) return ''  // value가 없으면
                    val = val.toString()  // value에 숫자가 들어왔을 때 등 커버하지 못할 경우 대비
                    return val.charAt(0).toUpperCase() + val.slice(1)
                }
            }
        })
    </script>
</body>
</html>
```





### computed

API 등을 통해 데이터를 가져오게 되면 많이 씀.

필터의 주목적은 데이터 보여줄 때 필요한 operation.

computed는 데이터를 조작. methods와 비슷한데, **caching**에 있어서 차이가 있다(캐싱). 

`"hello".split('').reverse().join('')`

computed는 템플릿 단에서 ()를 쓰면 안된다. compted는 function이 아니라 하나의 값으로 생각할 것.

```html
    <div id="app">
        <h1>{{ header }}</h1>
        <p v-once>data 안의 data : {{ msg | capitalize }}</p>  <!-- v-once : 한번 렌더한 값이 있으면 변경하지 않고 그대로 쓴다. -->
        <p>{{ reverseMsg }}</p>
        <p>함수 실행의 결과 : {{ hello() }}</p>  <!-- return을 string으로 하는 함수는 실행된 결과를 바로 템플릿에서 출력 가능-->
        <img v-bind:src="imageSource" height=200 width=100>
        
        
        
        	computed: {
                reverseMsg: function() {
                    return this.msg.split('').reverse().join('')
                }
            }
```





### watch

데이터가 변경되는 것을 지켜보고, 변경시 할 일을 정의

cf. 원래 있던 애를 건드려서 infinite loop 경고가 발생. 그걸 없애기 위해 filter 첫번째 comment out

```html
        <input v-model="userInput"> <!-- v-model로 bind한다 -->
        <button v-on:click="addInput">todo 추가</button>  <!-- 인자가 필요없는 함수일 경우 addInput()이라고 쓰지 않아도 됨-->
        <ul>
            <li v-for="(todo, index) in todos">  <!-- enumerate하고 싶다면 (value, key)로 지정 -->


            // 데이터가 변경되는 것을 지켜보고, 변경시 할 일을 정의
            watch: {
                // 지켜볼 대상 : 
                todos: {
                    // handler key는 반드시 필요
                    handler: function() {
                        console.log('todos 변경 됐어요!ㅋ')
                    }
                }
            }
        })
    </script>
</body>
</html>
```







## 오후 movie-search-app

## 초기세팅

### style.css

slack에 주신 코드 가져오기

```css
*{
    margin:0;
    padding:0;
}

body{
    font:15px/1.3 'Open Sans', sans-serif;
    color: #5e5b64;
    text-align:center;
}

a, a:visited {
    outline:none;
    color:#389dc1;
}

a:hover{
    text-decoration:none;
}

section, footer, header, aside, nav{
    display: block;
}

/*-------------------------
    The search input
--------------------------*/

.bar{
    background-color:#5c9bb7;

    background-image:-webkit-linear-gradient(top, #5c9bb7, #5392ad);
    background-image:-moz-linear-gradient(top, #5c9bb7, #5392ad);
    background-image:linear-gradient(top, #5c9bb7, #5392ad);

    box-shadow: 0 1px 1px #ccc;
    border-radius: 2px;
    width: 400px;
    padding: 14px;
    margin: 45px auto 20px;
    position:relative;
}

.bar input{
    background:#fff no-repeat 13px 13px;
    background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyBpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMC1jMDYwIDYxLjEzNDc3NywgMjAxMC8wMi8xMi0xNzozMjowMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNSBXaW5kb3dzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkU5NEY0RTlFMTA4NzExRTM5RTEzQkFBQzMyRjkyQzVBIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkU5NEY0RTlGMTA4NzExRTM5RTEzQkFBQzMyRjkyQzVBIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6RTk0RjRFOUMxMDg3MTFFMzlFMTNCQUFDMzJGOTJDNUEiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6RTk0RjRFOUQxMDg3MTFFMzlFMTNCQUFDMzJGOTJDNUEiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz4DjA/RAAABK0lEQVR42pTSQUdEURjG8dOY0TqmPkGmRcqYD9CmzZAWJRHVRIa0iFYtM6uofYaiEW2SRJtEi9YxIklp07ZkWswu0v/wnByve7vm5ee8M+85zz1jbt9Os+WiGkYdYxjCOx5wgFeXUHmtBSzpcCGa+5BJTCjEP+0nKWAT8xqe4ArPGEEVC1hHEbs2oBwdXkM7mj/JLZrad437sCGHOfUtcziutuYu2v8XUFF/4f6vMK/YgAH1HxkBYV60AR31gxkBYd6xAeF3VzMCwvzOBpypX8V4yuFRzX2d2gD/l5yjH4fYQEnzkj4fae5rJulF2sMXVrAsaTWttRFu4Osb+1jEDT71/ZveyhouTch2fINQL9hKefKjuYFfuznXWzXMTabyrvfyIV3M4vhXgAEAUMs7K0J9UJAAAAAASUVORK5CYII=);

    border: none;
    width: 100%;
    line-height: 19px;
    padding: 11px 0;

    border-radius: 2px;
    box-shadow: 0 2px 8px #c4c4c4 inset;
    text-align: left;
    font-size: 14px;
    font-family: inherit;
    color: #738289;
    font-weight: bold;
    outline: none;
    text-indent: 40px;
}

ul{
    list-style: none;
    width: 428px;
    margin: 0 auto;
    text-align: left;
}

ul li{
    border-bottom: 1px solid #ddd;
    padding: 10px;
    overflow: hidden;
}

ul li img{
    width:60px;
    height:90px;
    float:left;
    border:none;
}

ul li p{
    margin-left: 75px;
    font-weight: bold;
    padding-top: 12px;
    color:#6e7a7f;
}
```





### index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <!-- CSS -->
    <link rel="stylesheet" href="./style.css">
    <!-- Vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!-- Axios cdn -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
    
    <script src="./vue.js"></script>
</body>
</html>
```





<https://www.themoviedb.org/> 접속

회원가입

username: egyeasy

profile and settings > API > api 키 신청



API Key(v3 auth) 복사

### vue.js

```js
// https://www.themoviedb.org/
const API_KEY = '88f1070777b1fdd9907d7213d1f516b1'
const URL = `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}`

axios.get(URL)
    .then(response => {
        console.log(response.data)
    })
```

console을 보고 영화 정보가 들어있는 곳을 확인



```js
// https://www.themoviedb.org/
const API_KEY = '88f1070777b1fdd9907d7213d1f516b1'
const URL = `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}`

axios.get(URL)
    .then(response => {
        console.log(response.data)
        const movies = response.data.results
    })

const app = new Vue({
    data: {
        movies: []
    }
})
```

movies 가져오는 법 일단 모르겠으니까 빈 리스트로 만들어 놓는다.



### index.html

검색창 만들기 -> input 데이터를 vue와 연동하기

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <!-- CSS -->
    <link rel="stylesheet" href="./style.css">
    <!-- Vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!-- Axios cdn -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
    <form id="main">
        <div class="bar">
            <input
                type="text"
                placeholder="검색어를 입력해 주세욧!"
            >
        </div>
        <ul>
            <li>
                <p></p>
            </li>
        </ul>
    </form>
    
    <script src="./vue.js"></script>
</body>
</html>
```





## Created

Vue 인스턴스가 생성되고 난 후 실행하는 함수

async await도 그대로 적용할 수 있다.



### vue.js

```js
// https://www.themoviedb.org/
const API_KEY = '88f1070777b1fdd9907d7213d1f516b1'
const URL = `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}`

axios.get(URL)
    .then(response => {
        console.log(response.data)
        const movies = response.data.results
    })

// 1. 빈 movies를 가지고 있는 vue 인스턴스 생성
// 2. created 함수가 실행되면서 api를 통해 movies를 가져옴
// 3. vue의 movies 안에 가져온 movies 데이터를 할당
// 4. vue의 데이터에 변화가 생기면서 새롭게 렌더링
const app = new Vue({
    data: {
        query: '',
        movies: []
    },
    // Vue 인스턴스가 생성되고 난 후 실행하는 함수
    async created() {
        const response = await axios.get(URL)
        const movies = response.data.results
        this.movies = movies
        console.log(movies)
    }
})
```



### index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <!-- CSS -->
    <link rel="stylesheet" href="./style.css">
    <!-- Vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!-- Axios cdn -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
    <form id="main">
        <div class="bar">
            <input
                type="text"
                v-model="query"
                placeholder="검색어를 입력해 주세욧!"
            >
        </div>
        <ul>
            <li v-for="movie in movies">
                <p>{{ movie.title }}</p>
            </li>
        </ul>
    </form>
    
    <script src="./vue.js"></script>
</body>
</html>
```



poster_path를 어떻게 이미지로 가져올 수 있을까?

moviedb 도메인과 path를 합쳐야 함!

`map()`을 써서 title과 imageURL만 있는 movies를 얻어보자.

```js
// https://www.themoviedb.org/
const API_KEY = '88f1070777b1fdd9907d7213d1f516b1'
const URL = `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}`
const IMG_URL = 'https://image.tmdb.org/t/p/w500'

axios.get(URL)
    .then(response => {
        console.log(response.data)
        const movies = response.data.results
    })

// 1. 빈 movies를 가지고 있는 vue 인스턴스 생성
// 2. created 함수가 실행되면서 api를 통해 movies를 가져옴
// 3. vue의 movies 안에 가져온 movies 데이터를 할당
// 4. vue의 데이터에 변화가 생기면서 새롭게 렌더링
const app = new Vue({
    data: {
        query: '',
        movies: []
    },
    // Vue 인스턴스가 생성되고 난 후 실행하는 함수
    async created() {
        const response = await axios.get(URL)
        const movies = response.data.results
        // this.movies = movies
        console.log(movies)
        // poster image url을 수정해주는 작업
        // map: callback 함수에서 return 되는 아이템으로 새롭게 배열을 만듦
        this.movies = movies.map(movie => {
            return { title: movie.title, image: IMG_URL + movie.poster_path}
        })
        console.log(this.movies)
        
    }
})
```



### index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <!-- CSS -->
    <link rel="stylesheet" href="./style.css">
    <!-- Vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!-- Axios cdn -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
    <form id="main">
        <div class="bar">
            <input
                type="text"
                v-model="query"
                placeholder="검색어를 입력해 주세욧!"
            >
        </div>
        <ul>
            <li v-for="movie in movies">
                <img v-bind:src="movie.image" />
                <p>{{ movie.title }}</p>
            </li>
        </ul>
    </form>
    
    <script src="./vue.js"></script>
</body>
</html>
```





## computed - 검색 기능 추가

computed : 함수를 정의하는 곳. caching이 됨 = 함수가 실행되면서 반환되는 값을 Vue가 알고 있게 됨 -> html파일에서 반환되는 값을 바로 접근 가능.



### 그냥 data 그대로 반환해서 vue가 알고 있는지 테스트

```js
// https://www.themoviedb.org/
const API_KEY = '88f1070777b1fdd9907d7213d1f516b1'
const URL = `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}`
const IMG_URL = 'https://image.tmdb.org/t/p/w500'

axios.get(URL)
    .then(response => {
        console.log(response.data)
        const movies = response.data.results
    })

// 1. 빈 movies를 가지고 있는 vue 인스턴스 생성
// 2. created 함수가 실행되면서 api를 통해 movies를 가져옴
// 3. vue의 movies 안에 가져온 movies 데이터를 할당
// 4. vue의 데이터에 변화가 생기면서 새롭게 렌더링
const app = new Vue({
    data: {
        query: '',
        movies: []
    },
    // 함수를 정의하는 곳, caching이 됨 
    computed: {
        filteredMovies: function() {
            return this.movies  // 그냥 data 그대로 반환해서 vue가 알고 있는지 테스트
        }
    },
```



``` html
    <form id="main">
        <div class="bar">
            <input
                type="text"
                v-model="query"
                placeholder="검색어를 입력해 주세욧!"
            >
        </div>
        <ul>
            <li v-for="movie in filteredMovies">
                <img v-bind:src="movie.image" />
                <p>{{ movie.title }}</p>
            </li>
        </ul>
    </form>
```

이상이 없으므로 vue가 알고 있음을 알 수 있다.



### 내가 짠 코드

`trim()` : string 앞뒤 공백 제거

```js
// https://www.themoviedb.org/
const API_KEY = '88f1070777b1fdd9907d7213d1f516b1'
const URL = `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}`
const IMG_URL = 'https://image.tmdb.org/t/p/w500'

axios.get(URL)
    .then(response => {
        console.log(response.data)
        const movies = response.data.results
    })

// 1. 빈 movies를 가지고 있는 vue 인스턴스 생성
// 2. created 함수가 실행되면서 api를 통해 movies를 가져옴
// 3. vue의 movies 안에 가져온 movies 데이터를 할당
// 4. vue의 데이터에 변화가 생기면서 새롭게 렌더링
const app = new Vue({
    el: '#main',
    data: {
        query: '',
        movies: []
    },
    // 함수를 정의하는 곳, caching이 됨 
    computed: {
        filteredMovies: function() {
            // return this.movies  // 그냥 data 그대로 반환해서 vue가 알고 있는지 테스트
            // query로 filtering한 movie만 반환
            const filtered = []
            for (movie of this.movies) {
                if (movie.title.toLowerCase().trim().includes(this.query.toLowerCase().trim())) {
                    filtered.push(movie)
                }
            }
            console.log(filtered)
            return filtered
        }
    },
    // Vue 인스턴스가 생성되고 난 후 실행하는 함수
    async created() {
        const response = await axios.get(URL)
        const movies = response.data.results
        // this.movies = movies
        console.log(movies)
        // poster image url을 수정해주는 작업
        // map: callback 함수에서 return 되는 아이템으로 새롭게 배열을 만듦
        this.movies = movies.map(movie => {
            return { title: movie.title, image: IMG_URL + movie.poster_path}
        })
        console.log(this.movies)
    }
})
```



`for key in` : index를 반환

`for value of` : value를 반환



### 강사님 코드

```js
    computed: {
        filteredMovies: function() {
            // return this.movies  // 그냥 data 그대로 반환해서 vue가 알고 있는지 테스트
            // query로 filtering한 movie만 반환
            const filtered = []
            const query = this.query.trim().toLowerCase()
            for (const movie of this.movies) {
                if (movie.title.trim().toLowerCase().includes(query)) {
                    filtered.push(movie)
                }
            }

            return filtered
        }
    },
```



### for문 안도는 코드 - filter 사용

`배열.filter` : callback 함수에서 반환되는 값이 true인 아이템만으로 새로운 배열 생성

cf. **Falsian 값**: 다음은 모두 True - `0 === ''`, `0 === []`, `'' !== []`, `0 === false`, `1 === true`, 

```js
    computed: {
        filteredMovies: function() {
            // for 문 안 도는 코드
            // if (this.query === '') {  // '' <= 사용자가 검색을 안함
            if (!this.query) {
                return this.movies
            }

            const query = this.query.trim().toLowerCase()
            // callback 함수에서 반환되는 값이 true인 아이템만으로 새로운 배열 생성
            const filtered = this.movies.filter(movie => {
                return movie.title.toLowerCase().trim().includes(query)
            })
            return filtered
        }
    },
```



### const num of numbers

```js
const numbers = [1, 2, 3, 4, 5]

for (const num of numbers) {
    console.log(num)
}

// 이건 새로운 block들을 생성하며 그 안에서만 존재하는 const를 만들어주는 것
{
    const num
}
{
    const num
}
{
    const num
}
```



