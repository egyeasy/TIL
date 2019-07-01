[TOC]

# Vue.js

뷰(Vue.js)는 UI화면 개발 방법 중 하나인 MVVM 패턴의 뷰 모델(ViewModel)에 해당하는 프론트엔드 라이브러리이다. 뷰 모델은 뷰와 모델의 중간 영역으로 DOM 리스너와 데이터 바인딩을 제공하는 영역이다.

**CDN**

```html
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

## 1. life cycle

life cycle은 일반적으로 app 가지고 있는 생성부터 제거까지의 생명주기를 말한다. 다음으로 설명할 method들은 인스턴스가 생성되었을 때 호출할 동작을 정의하는 속성들을 말한다. 그리고 각 life cycle 속성에서 실행되는 커스텀 로직을 life cycle hook 이라고 한다.

### 1.1 인스턴스를 DOM에 부착할 때까지

- beforeCreate: data, methods가 아직 인스턴스에 정의되지 않음, DOM도 접근불가
- created: component와 data, methods가 정의됨, HTTP 통신 가능
- beforeMount: DOM에 인스턴스가 부착되기 직전, 로직을 추가하기 좋음.
- mounted: DOM에 인스턴스가 부착된 후의 시점, DOM에 접근 가능

### 1.2 인스턴스의 데이터가 갱신 될 때까지

- beforeUpdate: 관찰하고 있는 데이터가 변경되면 가상 DOM에 화면을 다시 그리기 전에 호출되는 단계, 변경 예정인 새 데이터에 접근할 수 있으나 그 데이터를 변경하는 로직을 넣더라도 화면이 다시 그려지지 않음.
- updated: 데이터가 변경되고 나서 가상 돔으로 다시 화면을 그리고 나면 실행되는 단계, 변경이 완료된 시점이므로 DOM 제어와 관련한 로직을 추가하기 좋음. 만약 데이터 값을 변경하면 무한 루프에 빠질 수 있으므로 computed나 watch를 사용해야함. 데이터 값을 갱신하는 로직은 beforeUpdate을, DOM와 관련 로직은 updated에 추가하는 것이 좋음.

### 1.3 인스턴스가 소멸 될 때까지

- beforeDestroy: 뷰 인스턴스가 파괴되기 직전, 아직 인스턴스에 접근할 수 있으므로 뷰 인스턴스의 데이터를 삭제하기 좋음.
- destroyed: 뷰 인스턴스가 파괴되고 나서 호출되는 단계, 하위를 포함한 뷰 인스턴스에 정의한 모든 속성이 제거됨.

**예제**

```html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Document</title>
  </head>
  <body>
    <div id="app">
      {{message}}
    </div>
    <!-- Vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: "#app",
        data: {
          message: "hello"
        },
        beforeCreate: function() {
          console.log("beforeCreate");
        },
        created: function() {
          console.log("created");
        },
        mounted: function() {
          console.log("mounted");
          this.message = "HoU!";
        },
        updated: function() {
          console.log("updated");
        }
      });
    </script>
  </body>
</html>
```

## 2. 컴포넌트(component)

컴포넌트는 화면을 구성할 수 있는 블록 또는 특정 영역을 의미한다. 컴포넌트 간의 관계는 자료구조의 Tree 모양과 유사하다.

컴포넌트의 등록 방법은 전역(Global)과 지역(Local) 방식으로 선언할 수 있는데 전역 컴포넌트는 여러 인스턴스에서 공통으로 사용할 수 있고 지역 컴포넌트는 특정 인스턴스에서 사용할 수 있다.

**예제**

```html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Document</title>
  </head>
  <body>
    <div id="app">
      <h1>첫 번째 인스턴스 영역</h1>
      <global-component></global-component>
      <local-component></local-component>
    </div>
    <div id="app2">
      <h1>두 번째 인스턴스 영역</h1>
      <global-component></global-component>
      <local-component></local-component>
      <!-- 오류 발생 -->
    </div>
    <!-- Vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      // 전역 컴포넌트
      Vue.component("global-component", {
        template: "<div>Global Component</div>"
      });

      // 지역 컴포넌트 내용
      let cmp = {
        template: "<div>Local Component</div>"
      };

      // 첫 번째 인스턴스
      const app = new Vue({
        el: "#app",
        // 지역 컴포넌트
        components: {
          "local-component": cmp
        }
      });

      // 두 번째 인스턴스
      const app2 = new Vue({
        el: "#app2"
      });
    </script>
  </body>
</html>
```

## 3. 뷰 컴포넌트 통신

뷰는 컴포넌트로 화면을 구성하므로 같은 웹 페이지라도 데이터를 공유할 수 없다. 왜냐하면 컴포넌트마다 고유한 유효 범위(Scope)를 갖기 때문이다.

**예제**

```html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Document</title>
  </head>
  <body>
    <div id="app">
      <h1>첫 번째 인스턴스 영역</h1>
      <global-component></global-component>
      <local-component></local-component>
    </div>
    <div id="app2">
      <h1>두 번째 인스턴스 영역</h1>
      <global-component></global-component>
      <local-component></local-component>
      <!-- 오류 발생 -->
    </div>
    <!-- Vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      // 전역 컴포넌트
      Vue.component("global-component", {
        // cmp1Data만 출력된다.
        template: "<div>Global Component {{cmp1Data, cmp2Data}}</div>",
        data: function() {
          return {
            cmp1Data: 100
          };
        }
      });

      // 지역 컴포넌트 내용
      let cmp = {
        // cmp2Data만 출력된다.
        template: "<div>Local Component {{cmp2Data, cmp1Data}}</div>",
        data: function() {
          return {
            cmp2Data: 50
          };
        }
      };

      // 첫 번째 인스턴스
      const app = new Vue({
        el: "#app",
        // 지역 컴포넌트
        components: {
          "local-component": cmp
        }
      });

      // 두 번째 인스턴스
      const app2 = new Vue({
        el: "#app2"
      });
    </script>
  </body>
</html>
```

그러나 상-하위 컴포넌트 관계(부모-자식 관계)이면 서로 통신이 가능하다. 부모가 자식에게 통신할 경우에는 `props`를 전달하고 자식이 부모에게 전달할 때는 이벤트 발생을 통해 통신할 수 있다.

### 3.1 부모->자식

```javascript
Vue.component("child-component", {
  props: ["props 속성 이름"]
});
```

`props`를 통해 값을 전달하기 때문에 자식 컴포넌트에 props를 선언해놔야한다.

```html
<child-component
  v-bind:props
  속성
  이름="부모 컴포넌트의 data 속성"
></child-component>
```

html에서 컴포넌트를 사용할 때는 `v-bind`를 이용해 부모 컴포넌트로 부터 data를 받으면 된다.

**예제**

```html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Document</title>
  </head>
  <body>
    <div id="app">
      <child-component v-bind:pdata="message"></child-component>
    </div>
    <!-- Vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      // 전역 컴포넌트
      Vue.component("child-component", {
        template: "<div>child Component: {{pdata}}</div>",
        props: ["pdata"]
      });

      // 인스턴스도 컴포넌트이다.
      const app = new Vue({
        el: "#app",
        data: {
          message: "data from Parent Component"
        }
      });
    </script>
  </body>
</html>
```

### 3.2 자식->부모

자식 컴포넌트에서 특정 이벤트가 발생하면 상위 컴포넌트에서 해당 이벤트를 수신하여 부모 컴포넌트의 메서드를 호출한다.

이벤트 발생과 수신은 `$emit('이벤트명')`과 `v-on:속성`을 사용하여 구현한다.

```javascript
// 이벤트 발생
this.$emit("이벤트");
```

```html
<!-- 이벤트 수신 -->
<child-component v-on:이벤트명="상위 컴포넌트의 메서드명"></child-component>
```

**예제**

```html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Document</title>
  </head>
  <body>
    <div id="app">
      <child-component v-on:show-log="printText"></child-component>
    </div>
    <!-- Vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      // 전역 컴포넌트
      Vue.component("child-component", {
        template: "<button v-on:click='showLog'>show</button>",
        methods: {
          showLog: function() {
            this.$emit("show-log");
          }
        }
      });
      s;

      // 인스턴스도 컴포넌트이다.
      const app = new Vue({
        el: "#app",
        data: {
          message: "data from Parent Component"
        },
        methods: {
          printText: function() {
            console.log("이벤트 수신");
          }
        }
      });
    </script>
  </body>
</html>
```

### 3.3 이벤트 버스

같은 레벨, 또는 다른 레벨의 컴포넌트 간의 통신을 하기 위해서는 이벤트 버스(Event Bus)를 사용해야한다. 이벤트 버스를 사용하면 부모 컴포넌트를 거쳐갈 필요 없이 바로 보낼 수 있다.

```javascript
// 이벤트 버스를 위한 추가 인스턴스 1개 생성
let eventBus = new Vue();

//...
// 이벤트를 보내는 컴포넌트
methods:{
  메서드명: function(){
    eventBus.$emit('이벤트명',데이터);
  }
}

//...
// 이벤트를 받는 컴포넌트
methods:{
  created: function(){
    eventBus.$on('이벤트명',function(데이터){
      //...
    });
  }
}
```

**예제**

```html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Document</title>
  </head>
  <body>
    <div id="app">
      <child-component></child-component>
    </div>
    <!-- Vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      // 이벤트 버스 생성
      let eventBus = new Vue();

      Vue.component("child-component", {
        template: "<button v-on:click='showLog'>show</button>",
        methods: {
          showLog: function() {
            // 이벤트 버스 송신
            eventBus.$emit("triggerEventBus", 100);
          }
        }
      });

      const app = new Vue({
        el: "#app",
        created: function() {
          // 이벤트 버스 수신
          eventBus.$on("triggerEventBus", function(value) {
            console.log("이벤트를 전달받음. 전달받은 값 : ", value);
          });
        }
      });
    </script>
  </body>
</html>
```

이벤트 버스를 활용하면 props 속성을 이용하지 않아도 되지만 컴포넌트가 많아지면 어디로 보냈는지 관리가 되지 않기에 뷰엑스(Vuex)와 같은 상태 관리 도구가 필요하다.

## 4. 라우터

라우팅(Routing)은 웹페이지 간의 이동 방법을 말하며 SPA에서 주로 사용하고 있다. 라우팅을 이용하면 화면 간의 전환 시에 화면 상의 깜빡거리는 현상이 없는 부드러운 전환을 구현할 수 있다. 이런 라우팅을 구현하기 위해서는 라우터를 만들어야 한다.

### 4.1 뷰 라우터

뷰 라우터는 뷰에서 라우팅 기능을 구현할 수 있도록 지원하는 공식 라이브러리이다. 뷰 라우터는 아래의 CDN 주소를 입력해야 사용할 수 있다.

**CDN**

```html
<!-- Vue-Router -->
<script src="https://unpkg.com/vue-router@2.0.0/dist/vue-router.js"></script>
```

뷰 라우터의 사용법은 다음과 같다.

```html
<!-- 페이지 이동 태그 -->
<router-link to="URL 값"></router-link>

<!-- 페이지 표시 태그,  -->
<router-view></router-view>
```

```javascript
//...
// URL 값에 따라 표시될 컴포넌트 지정
let routes = [
  { path: 'URL 값', component: 컴포넌트 변수명},
  //...
]

// routes를 VueRouter에 연결
let router = new VueRouter({
  routes
})

// Vue 인스턴스에 router 삽입
const app = new Vue({
  router
}).$mount('#app')
```

`$mount()` API는 el 속성과 동일하게 인스턴스 화면에 붙이는 역할을 한다.

**예제**

```html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Document</title>
  </head>
  <body>
    <div id="app">
      <p>
        <!-- 링크 정의 -->
        <router-link to="/Message1">Message1</router-link>
        <router-link to="/Message2">Message2</router-link>
      </p>
      <!-- 라우팅 영역 정의 -->
      <router-view></router-view>
    </div>
    <!-- Vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!-- Vue-Router -->
    <script src="https://unpkg.com/vue-router@2.0.0/dist/vue-router.js"></script>
    <script>
      const Message1 = Vue.component("Message1-component", {
        template: "<button v-on:click='showLog'>Message1</button>",
        methods: {
          showLog: function() {
            console.log("Message1");
          }
        }
      });

      const Message2 = Vue.component("Message2-component", {
        template: "<button v-on:click='showLog'>Message2</button>",
        methods: {
          showLog: function() {
            console.log("Message2");
          }
        }
      });

      let routes = [
        // 뷰 라우팅
        { path: "/Message1", component: Message1 },
        { path: "/Message2", component: Message2 }
      ];

      let router = new VueRouter({
        mode: "history", // 라우터 URL의 해시 값(#)을 없앤다.
        routes
      });

      const app = new Vue({
        router
      }).$mount("#app");
    </script>
  </body>
</html>
```

`mode: 'history'`는 해시 값을 없애줄 때 사용하지만 서버가 있어야 제 기능을 활용할 수 있다. 자세한 내용은 [공식 문서](https://router.vuejs.org/kr/guide/essentials/history-mode.html#%EC%84%9C%EB%B2%84-%EC%84%A4%EC%A0%95-%EC%98%88%EC%A0%9C)를 통해 확인하길 바란다.

### 4.2 네스티드 라우터

네스티드 라우터(Nested Router)는 라우터로 페이지를 이동할 때 최소 2개 이상의 컴포넌트를 화면에 나타낼 수 있다. 부모 컴포넌트 1개에 자식 컴포넌트 1개를 포함하는 구조로 구성되지만 URL에 따라 서로 다른 부모 컴포넌트의 자식 컴포넌트가 표시된다.

**예제**

```html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Document</title>
  </head>
  <body>
    <div id="app">
      <!-- 라우팅 영역 정의 -->
      <router-view></router-view>
    </div>
    <!-- Vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!-- Vue-Router -->
    <script src="https://unpkg.com/vue-router@2.0.0/dist/vue-router.js"></script>
    <script>
      const User = {
        template: `
        <div>
          User Component
          <router-view></router-view>
        </div>
        `
      };
      const Message1 = Vue.component("Message1-component", {
        template: "<button v-on:click='showLog'>Message1</button>",
        methods: {
          showLog: function() {
            console.log("Message1");
          }
        }
      });

      const Message2 = Vue.component("Message2-component", {
        template: "<button v-on:click='showLog'>Message2</button>",
        methods: {
          showLog: function() {
            console.log("Message2");
          }
        }
      });

      let routes = [
        {
          path: "/user",
          component: User,
          // 네스티드 라우팅 정의
          children: [
            // '/'는 떼고 path를 작성해야한다.
            // /user/message1
            { path: "message1", component: Message1 },
            // /user/message2
            { path: "message2", component: Message2 }
          ]
        }
      ];

      let router = new VueRouter({
        routes
      });

      const app = new Vue({
        router
      }).$mount("#app");
    </script>
  </body>
</html>
```

네스티드 라우터는 화면을 구성하는 컴포넌트의 수가 적을 떄는 유용하지만 한 번에 더 많은 컴포넌트를 표시하는데는 한계가 있다.

### 4.3 네임드 뷰

네임드 뷰(Named View)는 특정 페이지로 이동했을 때 같은 레벨의 여러 컴포넌트들을 동시에 표시하는 라우팅 방식이다.

**예제**

```html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Document</title>
  </head>
  <body>
    <div id="app">
      <!-- 라우팅 영역 정의 -->
      <router-view name="header"></router-view>
      <router-view></router-view>
      <!-- name이 없으면 default로 인식 -->
      <router-view name="footer"></router-view>
    </div>
    <!-- Vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!-- Vue-Router -->
    <script src="https://unpkg.com/vue-router@2.0.0/dist/vue-router.js"></script>
    <script>
      const User = {
        template: `
        <div>
          User Component
          <router-view></router-view>
        </div>
        `
      };
      const Message1 = Vue.component("Message1-component", {
        template: "<button v-on:click='showLog'>Message1</button>",
        methods: {
          showLog: function() {
            console.log("Message1");
          }
        }
      });

      const Message2 = Vue.component("Message2-component", {
        template: "<button v-on:click='showLog'>Message2</button>",
        methods: {
          showLog: function() {
            console.log("Message2");
          }
        }
      });

      let router = new VueRouter({
        routes: [
          {
            path: "/",
            // 네임드 뷰
            components: {
              default: User,
              header: Message1,
              footer: Message2
            }
          }
        ]
      });

      const app = new Vue({
        router
      }).$mount("#app");
    </script>
  </body>
</html>
```

## 5. 뷰 HTTP 통신

HTTP(HyperText Transfer Protocol)는 브라워저와 서버 간에 데이터를 주고 받는 통신 프로토콜이다. 브라우저에서 특정 데이터를 보내달라고 요청(request)을 보내면 서버에서 응답(response)으로 해당 데이터를 보내주는 방식으로 동작한다.

HTTP 통신의 대표적인 사례로는 jQuery의 ajax가 있다. ajax는 서버에서 받아온 데이터를 표시할 때 화면 전체를 갱신하지 않고도 화면의 이부분만 변경할 수 있게 하는 javascript 기법이다. 뷰 리소스가 과거에는 뷰의 코어 팀에서 공식적으로 권하는 라이브러리였지만 현재는 `axios`가 많이 사용된다.

axios는 Promise 기반의 API 형식이 다양하게 제공되어 별도의 로직을 구현할 필요 없이 주어진 API만으로도 간편하게 원하는 로직을 구현할 수 있다는 것이 장점이다. 또한 뷰 리소스와 다르게 일반 문자열 형식이 아닌 객체 형식으로 data 속성을 받기 때문에 별도로 `JSON.parse()`를 사용할 필요가 없다.

**CDN**

```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

**예제**

```html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Document</title>
  </head>
  <body>
    <div id="app">
      <button v-on:click="getData">유저 목록 가져오기</button>
      <ol>
        <li v-for="user in users">
          이름: {{user.name}}<br />아이디: {{user.username}}
        </li>
      </ol>
    </div>
    <!-- Vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!-- axios -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <script>
      const app = new Vue({
        data: {
          users: []
        },
        methods: {
          getData: function() {
            axios.get("https://www.koreanjson.com/users").then(response => {
              this.users = response.data;
            });
          }
        }
      }).$mount("#app");
    </script>
  </body>
</html>
```

## 6. 뷰 템플릿

뷰 템플릿(Template)은 HTML, CSS 등의 마크업 속성과 뷰 인스턴스에서 정의한 데이터 및 로직들을 연결하여 사용자가 브라우저에서 볼 수 있는 형태의 HTML로 변환해주는 속성이다.

라이브러리 내부적으로 template 속성에서 정의한 마크업 + 뷰 데이터를 가상 돔 기반의 render() 함수로 변환한다. 변환된 render() 함수는 최종적으로 사용자가 볼 수 있게 화면을 그리는 역할을 하고 변환 과정에서 뷰의 반응성(Reactivity)이 화면에 더해진다.

뷰의 반응성과 가상 돔에 대해 충분히 이해하면 `template` 속성을 사용하지 않고 JSX 기반의 render() 함수를 사용하여 구현할 수 있다. 이 경우 화면 요소의 동작마다 직접 관여할 수 있어 더 빠르게 화면을 렌더링할 수 있다.

`computed` 속성을 이용하여 계산 후 최종 결과 값만 표시되게끔 하는 것이 좋다. 이렇게 되면 화면단 코드를 훨씬 빠르게 읽을 수 있어 화면의 UI구조를 쉽게 파악할 수 있다.

### 6.1 데이터 바인딩

- {{}} (콧수염 괄호): data나 methods의 속성을 가져와 사용할 수 있고 선언문, if 문, 복잡한 연산을 제외한 javascript 코드를 사용할 수 있다.
- v-once: 뷰 데이터가 변경되어도 값이 변경되지 않도록 함.
- v-bind: html 속성 값에 뷰 데이터 값을 연결할 때 사용함.
  - `v-bind:id="k"`이라면 `:id="k"`로 줄여 사용할 수 있음.

### 6.2 디렉티브

- v-if: 지정한 뷰 데이터 값의 참과 거짓에 따라 해당 요소를 화면에 표시하거나 표시하지 않음.
- v-for: 지정한 뷰 데이터의 개수만큼 해당 요소를 반복 출력함.
- v-show: v-if와 비슷하지만 `display:none;`으로 숨겨져 있음.
- v-bind: 요소의 기본 속성과 뷰 데이터 속성을 연결함.
- v-on: 화면 요소의 이벤트를 감지하여 처리할 때 사용함.
- v-model: form에서 주로 사용되며 form에 입력한 값을 뷰 인스턴스의 데이터와 즉시 동기화함. input, select, textarea에만 적용 가능함.

```html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Document</title>
  </head>
  <body>
    <div id="app">
      <a v-if="flag">하와와</a>
      <ul>
        <li v-for="system in systems">{{system}}</li>
      </ul>
      <p v-show="flag">하와와</p>
      <h5 v-bind:id="uid">디렉티브</h5>
      <button v-on:click="popUp">팝업</button>
      <p><input type="text" v-model="text" /></p>
      <p>{{text}}</p>
    </div>
    <!-- Vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue({
        data: {
          flag: true,
          systems: ["an", "ro", "id"],
          uid: 10,
          text: ""
        },
        methods: {
          popUp: function() {
            this.flag = !this.flag;
            return alert("호잇!");
          }
        }
      }).$mount("#app");
    </script>
  </body>
</html>
```

### 6.3 computed 속성과 methods 속성의 차이

computed는 해당 데이터 값이 변경되면 자동으로 실행되고 methods는 호출할 때만 실행된다. 그리고 computed는 동일 연산을 하지 않도록 값을 미리 저장(캐싱)하기 때문에 여러 곳에 값을 표시할 때 유용하다.

### 6.4 watch 속성

watch는 데이터 변화를 감시하여 자동으로 특정 로직을 수행한다. computed는 내장 API를 활용한 간단한 연산에 적합한 반면, watch는 데이터 호출과 같이 시간이 상대적으로 더 많이 소모되는 비동기 처리에 적합하다.

## 7. 프로젝트 생성
### 7.1 single file component

지금까지 html에서 뷰 코드를 작성했지만 규모가 커지면 파일 구조의 한계를 맞이하게 된다. 그렇기 때문에 확장자 `.vue`인 single file component 체계를 사용하게 되었다. 다음의 구조와 같이 한 파일에 html, javascript, css가 담겨 있다.

```html
<template>
  <!--html 내용 -->
</template>

<script>
  export default {
    // javascript 내용
  };
</script>

<style>
  /* css 스타일 내용 */
</style>
```

### 7.2 뷰 CLI

`.vue` 파일을 사용하기 위해서는 Webpack이나 Browserify 등의 도구들이 담긴 뷰 CLI를 설치하여 별도로 빌드를 해야한다. 뷰 CLI 관련 내용은 [공식문서](https://cli.vuejs.org/guide/installation.html)를 통해 확인할 수 있다.

Webpack은 HTML, CSS, 이미지 등의 자원들을 JS 모듈로 변환해 하나로 묶어주어 웹 성능을 향상시켜 주는 JS 모듈 번들러이다. Browserify도 Webpack과 유사한 성격의 모듈 번들러이지만 Webpack과 같은 웹 자원 압축이나 빌드 자동화 같은 기능은 없다.

복잡한 도구의 설치 및 설정을 해소하기 위해 뷰 코어 팀에서 CLI(Command Line Interface) 도구를 제공하게 되었다. 

```bash
$ npm install -g @vue/cli
```

위 명령어를 통해 뷰 CLI를 전역 설치를 한다.

```bash
$ vue create practice
$ cd practice
$ npm run serve
```

`practice` 이름으로 프로젝트를 생성하고 `$ npm run serve`를 입력하면 구동에 필요한 파일들이 변환되어 localhost로 접속이 된다.