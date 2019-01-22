# Intro to WEB Service



### 월드 와이드 웹(WWW, W3)

인터넷에 연결된 / 컴퓨터들을 통해 / 사람들이 정보를 공유할 수 있는 공간. by Tim Berners Lee



### 서버 (Server)

우리는 서버컴퓨터에서 요청과 응답을 처리(해서 사용자에게 html 문서를 전달)할 프로그램을 개발할 것이다. 지금까지는 Flask를 써왔고, 앞으로는 django를 활용할 것. AWS 등 클라우드 서비스에는 접속자 수 폭증했을 때 용량을 늘려주는 기능이 있음.



- 사용자(client)는 웹 브라우저에 의해 해석(render)된 페이지를 보게 됨.



### 요청의 종류

1. 줘라 (GET)
2. 받아라 (POST)



### Static Web

모든 사람이 동일한 내용을 보는 웹. 모든 요청에 대해 동일한 응답을 준다.



### Dynamic Web

앞으로 만들 것. 요청에 맞는 응답을 준다.



### web developer extension

웹개발에 꼭 필요한 크롬 익스텐션. information - view document outline 등 유용한 기능. outline 순서대로 시각장애인들이 웹페이지 읽음.





### Web Browser

탐색기와 비슷하다. 웹에 있는 정보들을 찾아다니는 것.

정보들의 주소가 ip주소. 도메인 네임에 대응되는 ip 주소가 있다.

우리는 도메인 네임을 사기 위해 **AWS Route 53**을 쓰게 될 것. 도메인 관리하기 굉장히 편리.



### IP(Internet Protocol)

8비트의 숫자로 구성된 숫자의 집합으로, 각자가 가지고 있는 주소와 동일.





### 도메인 네임

도메인 네임을 주소창에 치게 되면 엄청나게 큰 도메인 네임 서비스의 서버(엑셀 시트 비슷한 곳)로 가서 대응되는 ip를 찾는다.





### W3C - 웹 표준

html, css 표준이 정리되어 있다.



### Mozilla MDN web docs : 여기 가서 보는 것을 추천

html 등에 대한 방대한 learning source 있음.





### HTML(Hyper Text Markup Language)

Hypertext : 문서간 linking이 되어있는 것. 문서 간 넘어다닐 수 있다.

http는 html을 주고 받는 규칙. transfer protocol

웹 페이지를 작성하기 위한 역할 표시 언어





### Self-closing element

닫는 태그가 없는 태그

```html
<img src=''/>
```



### DOM트리 **

태그는 중첩되어 사용 가능하며, 다음과 같은 관계를 갖는다.

![DOM Tree](https://tuftsdev.github.io/WebProgramming/notes/dom_tree.gif)



### 시맨틱태그(semantic tags) **

개발자 및 사용자 뿐만 아니라 검색엔진(구글, 네이버) 등에 의미 있는 정보를 

html5에서부터 중요한 요소.

마케팅에서 쓰이는 **검색엔진최적화(SEO)**  - '패스트캠퍼스' 검색하면 '멀티캠퍼스'와 다르게 하위 카테고리들이 구글 검색창에서부터 정리돼서 나온다. 'pocu' 검색 시 id가 한글로 나오고, h1 태그가 많아서 브라우저에서 잘 못 잡는다.. 원래는 가장 중요한 것 하나만 있어야 함.

![HTML5 Semantic Elements](https://www.w3schools.com/Html/img_sem_elements.gif)

header : 맨 위에 헤더
article : 내용물
aside : 추가 정보. 이 안에 footer가 들어가기도.



### html 작성해보기

! + tab 하면 양식 자동완성

/strike, /s : 취소선

/hr : 수평선

ul>li*2 + enter : 원하는 만큼 리스트





# CSS - Cascading Style Sheets

html은 정보와 구조화(뼈대), CSS는 styling(살집). 각자 문법이 다른 별개의 언어. 하지만 html 없는 css는 무의미.



앞에서 html 라인 안에 넣은 styling은 inline styling

```css
<li style="list-style-type: circle">HTML</li>
```



### 기본 사용법

Selector { property1: value1; property2: value2}

```css
h1 {color:blue; font-size:15px}
```

구분자는 ; (세미콜론).
value에는 1) 키워드 2) 크기단위(px) 3) 색깔 이 들어갈 수 있다

color는 글자에만 적용된다.



head 밑에

```html
<style>
    li {
        color: darkcyan
    }
</style>
```

cascading : 폭포수가 떨어지듯이 우선 적용. 위와 같은 방식으로 적용해도 inline이 있을 경우 inline이 우선된다. 보다 상세하고 세밀하게 정의한 규칙이 더 우선적으로 적용된다.

poiemaWeb에 관련 설명이 잘 나와있음 => 한글 문서 중 html css 최고



### 총 세가지의 방법이 있다!!!(중요)

1. inline
2. head - style
3. 파일 따로 만들어서 /link



### px

##### 디바이스별로 픽셀의 크기는 제각각!

