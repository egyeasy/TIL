# Web/Mobile sub PJT 1

## 개발 환경 설정

### 사용할 기술 스택

- Vue.js



### 사용할 환경

- NPM

  node.js 홈페이지에서 다운로드

- Vue.js, Vue-cli

  ```bash
  npm install
  npm install -g yarn
  npm install -g @vue/cli
  npm install vue
  npm install -g firebase-tools
  npm run serve
  ```

- Visual Studio Code

- Jira



## 190701 월

### 구현사항

- Header, Footer 삽입(Vuetify)
- fontawesome npm 설치 및 아이콘 활성화
- 홈버튼 네비게이션 기능
- navbar 메뉴 네비게이션 기능



### package.json

- serve : 개발 모드에 쓰는 명령어. Vue-cli는 Vue에서 제공하는 개발 표준. 기본 Vue 환경을 통합해주는 통합 환경. 

  build : 배포 모드에 쓰는 명령어



### 구조 설명

- 하나의 html 파일 안에서 모든 UI가 제공될 것

- App.vue 실행(루트 코드) -> 컨테이너 안에서 모든 것이 이뤄짐.

  App.vue 폴더 안에는 많은 것을 넣지 말 것. 하위 Vue에서 설정하면 됨

- component - 각 뷰에서 공통적으로 사용하는 것. 컴포넌트 단위의 개발을 통해 중복 코드를 최소화. 버튼을 우리 프로젝트에 맞게 설정하는 작업 등이 여기서 진행될 것. 

- Vue 상태 관리는 꼭 이번주에 마스터해볼 것(Vuex)

- router-view : SPA에서 url처럼 페이지 전환이 가능하게 만들어줌. `router.js`에서 url들이 매핑된 것을 볼 수 있다.

- 렌더링의 순서

  index.html -> main.js -> App.vue

  `main.js`의 `h` - createElement의 약어

- export default - es6 module에 관련된 문서 찾아볼 것

- `<style scoped>` 해당 Vue에서만 적용되는 style 옵션





### 프로젝트 생성

- class-style component : typescript를 활용하는 것. vue에 익숙해지기 전까지는 사용X
- Typescript 썼으면 TSLint를 써야 함
- config for Babel -> 위의 선택지가 밖으로 빼서 저장하는 것. 혹은 package.json 안에 저장할 수 있다.



- 현재는 typescript를 많이 쓰는 추세
- `vue ui`라는 명령어를 치면 GUI를 통해 쉽게 프로젝트를 만들 수 있다.

- chrome 디버깅 툴 - Vue.js devtool -> 개발자 도구에 Vue라는 탭이 생긴 것을 확인할 수 있다.
- webpack - 빌드를 도와주던 과거의 라이브러리. Vue 2.0이 나오면서 안 써도 되게 됨 -> 편해짐



### Vuetify

- bootstrap과 같은 Vue ui component

- 프로젝트에 이미 Vuetify 코드가 섞여있다.

- 문서를 한번 찾아보도록 하자.

- `v-app`은 vuetify의 문법

- dialog 컴포넌트가 편리하다

- 치명적인 단점 - Customize하기 불편하다

- grid system도 지원

  픽셀 단위의 조정 - 디자이너와 갈등이 생길 수 있는 지점

  -> 전문화된 팀은 grid system이나 design system을 적용하여 문제를 최소화



### App.vue

- 여기서 `<style>`을 정의하면 전역에 적용된다.
- 헤더와 푸터를 여기에 직접 넣어주면 된다.
- `v-content`는 vuetify 레이아웃을 위한 것



### 그밖에

- 다른 페이지로의 이동 - 1) `<router-link>`  2) `this.$route.go() or push()`

- 부모-자식 컴포넌트 간 데이터 교환 -> 아주 중요!!





# 190702 화

### 구현사항

- protfolio writer page - page, router,simplemde
- favicon 구현 시도(실패)
- top으로 올라가는 버튼 구현 - window.scrollTop, eventListener



### 반응형 웹 구현

- Vuetify를 통해서도 할 수 있다
- display, grid system을 활용해볼 것





## 190703 수

### 구현사항

- 반응형 웹사이트 구현
  1. 모바일 사이즈에서 About Me 이미지 hidden
  2. 모바일 사이즈에서 hidden된 이미지 영역을 텍스트 영역으로 변환
  3. 모바일 사이즈에서 Home 화면의 About Me 텍스트 가운데 정렬
  4. 가로 사이즈에 따라 텍스트 사이즈 자동 조절
- styleus 적용 시도(실패)



### 레퍼런스

- 글씨 줄이기를 위한 방법(stylus 설치 포함) - https://stackoverflow.com/questions/52086822/change-font-size-in-vuetify-based-on-viewport

  http://vuejs.kr/jekyll/update/2017/01/17/vuejs-external-css-library/







## 190704 목

- 반응형 웹사이트 구현
  1. 모바일 사이즈에서 4행 1열 노출로 변경
  2. 태블릿 사이즈에서 2행 2열 노출로 변경
- 모바일 사이즈에서 3단 바 네비게이션 아이콘(햄버거 메뉴) 구현
- Home 버튼 아이콘 구현
- 코드 레벨 네비게이션 영역을 Header 컴포넌트로 분리
- favicon 변경 구현
- 포트폴리오, 포스트 리스트에서 타이틀은 한 줄, 설명은 4줄 표시로 구현(Vue Line Clamp)
- git repository 이름이 개행되지 않도록 설정(Vue Line Clamp)



### 강의

- Vuex는 정말 중요하다

  - add 버튼은 store에 데이터를 넣기만 하고,

    실제 개수를 나타내는 UI는 store의 데이터를 참조하기만 해도 상태관리가 가능.

  - computed에서 데이터를 가져올 것.

  - `this.$store.dispatch('addPortfolio', item)`, `this.$store.commit('setPortfolioList', list)`

  - created -> this.load -> this.$store.commit

    computed -> return this.$store.



### 레퍼런스, 라이브러리

- Vue Line Clamp

  텍스트 최대 line 수 설정

  https://www.npmjs.com/package/vue-line-clamp

- 부모-자식 컴포넌트 간 데이터 송수신

  http://www.devkuma.com/books/pages/1175

  https://joshua1988.github.io/vue-camp/vue/event-emit.html





## 190705 금

- 즐겨찾기에 추가하기 버튼을 제작 및 포트폴리오 사이트를 즐겨찾기로 등록하는 기능 추가(alert로 메시지만 띄우는 형태로 구현)
- 구글 크롬 외의 브라우저로 접속 시 "해당 사이트는 크롬에 최적화 되어 있습니다."라는 메시지를 노출 구현