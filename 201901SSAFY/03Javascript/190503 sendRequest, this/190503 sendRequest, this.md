# sendRequest

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Document</title>
  <!-- CSS -->
  <link rel="stylesheet" href="./style.css">
  <!-- Axios -->
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <!-- Vue -->
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
  <div id="app">
    <div>
        <h3>Request</h3>
        <input v-model="post.title" type="text" placeholder="Title">
        <br />
        <input v-model="post.author" type="text" placeholder="Author">
        <br />
        <textarea v-model="post.content" name="content" cols="30" rows="10" placeholder="Content"></textarea>
        <br />
        <button @click="addPost">Post</button>
    </div>
    <div>
      <h3>Response</h3>
      <pre>{{ response }}</pre>
    </div>
  </div>
  <script>
    /*
      Vue request practice
      1. data 안에 post 객체를 생성하고 property 로 title, author, content 를 html 로 부터 입력받는다.
      2. button 에 클릭 이벤트가 발생하면 POST 방식으로 주어진 URL 에 post 객체를 담아서 요청을 보낸다.
      3. 응답이 오면 data 의 response 에 응답받은 객체를 바인딩하고 `pre` 태그 안에서 보여준다.
    */

    const URL = 'https://jsonplaceholder.typicode.com/posts'
    const app = new Vue({
      el: '#app',
      data: {
        post: {
          title: '',
          author: '',
          content: '',
        },
        response: '',
      },
      methods: {
        addPost: function() {
          axios.post('https://jsonplaceholder.typicode.com/posts', this.post)
            .then(response => {  // .then(function(response) { 로 짜면 this.response가 window.response를 찾게 됨
              console.log(response)
              this.response = response.data
            }, error => {
              console.log(error)
            })
        }
      }
    })
  </script>
</body>
</html>
```



## 함수별 this의 차이

```js
function def1 () {
    // this: 실행 시점의 객체를 바라본다.
}

const def2 = () {
    // this: 선언 시점의 객체를 바라본다.
}

// callback 함수는 전역객체(window)에서 실행된다.
```

`document.querySelector`는 사실 `window.document.querySelector` -> `window`라는 가장 큰 객체가 있음.



그냥 function은 실행 시점의 객체 -> window를 가리킴.

arrow function은 선언 시점의 객체 -> **Vue 안에서 선언했을 시 `this`가 Vue app을 가리키게 된다.** 



cf .var도 window 객체에 binding 됨

```js
var number = 123
window.number // 123
```

단, const는 window 객체에 binding되지 않음.





