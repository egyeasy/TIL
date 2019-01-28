# bootstrap

우선 download source 해서 압축 풀기 -> dist\css\ 내에 우리가 쓰려고 하는 모든 파일 위치. 맨위 bootstrap.css만 신경쓰면 된다. 복사해서 작업하고 있는 폴더에 붙여넣기

html 파일 내 head에 추가 : `<link rel="stylesheet" href="bootstrap.css">`

bootstrap 적용하면 원래 태그의 margin이 사라진다. 글자 색깔, 크기도 변경됨.

min 파일은 css를 컴퓨터가 효율적으로 실행할 수 있게 압축된 텍스트.

소스 폴더 내 bootstrap-reboot.min은 기존 html css 요소들 모두 제거하는 기능



- bootstrap documentation을 교과서처럼 생각할 것(layout, content, component를 많이 보게 될 것)
- freecodecamp, w3schools.com(-> bootstrap 4)에 bootstrap 커리큘럼이 있다.
- bootstrap의 대안으로는 google material design이 있다.
- start bootstrap에서 테마를 가져올 수 있다.



### btn

이름에 해당하는 btn 클래스를 다 비워놨다. 사용자가 원하는 대로 정의하라는 것.



### class 여러 개

`class="btn btn-warning"` : btn, btn-warning의 프로퍼티가 중복되면 css 파일 내에서 선언된 순서대로 적용된다. html 내의 link와 style 사이의 관계는 뭐가 더 선언이 일찍 되었느냐(어떤 태그가 먼저 오느냐)에 따라 결정된다. (선언이 앞에 있으면 먼저 적용 -> 뒤에 있는 태그에 의해 override 됨)



- documentation - components - buttons 에서 button에 대한 속성, 클래스 등을 찾아볼 수 있다.



### CDN - Content Delivery(Distribution) Network

CDN 활용을 통해 Bootstrap에 작성된 CSS, JS를 활용하자!

1) 속도가 빠르다 -> 가까운 서버에서 받아온다.

2) 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐

3) 적절한 수준의 캐시 설정으로 빠르게 로딩할 수 있음 -> 부트스트랩을 쓰는 다른 웹페이지를 방문했다면 빠르게 로딩.



### Components

documentation - components에서 여러 요소들을 가지고 올 수 있다.

**lorempixel** : 엑박 사진들 처리할 때 쓸 것. `src="<http://lorempixel.com/400/200>"` lorem ipsum은 표준 채우기 텍스트(더미 텍스트)



### Color

9가지 정도. primary, secondary, warning, danger 등



### Position

기본적으로 태그 포지션은 static(나중에 다시 설명)



### layout - Grid system

bootstrap에서 중요한 것. 그리드를 잘 잡아서 한 줄에 몇 개 보여줄 것인지 정리해야한다.

1) Overview
그리드를 이용하기 위해서는 container라는 큰 박스에 넣어두고 써야 함

-12 column을 자주 쓴다. 약수가 많아서 그리드를 나누기 좋기 때문.

-container - row 안에 만든 div는 display: block임에도 inline처럼 가로로 쌓인다. 이건 상위의 /row에 `display: flex` 때문인데, 이게 있으면 하위 element들은 block이어도 block 풀린다.

-모바일에서 아래로 stacking 시키고 싶다 -> `col-sm-4`

-`mx-1`으로 조정하면 그리드 끝의 요소들이 밀려나게 된다 -> `px-1`으로 수정

-대체로 스크린 최소 가로폭인 1200px 정도로 사이트 컨텐츠의 폭을 잡는다. `container-fluid`는 가로로 그리드 꽉 채운다.



- css froggy : flex 내부에서 컨텐트들을 굉장히 자유롭게 움직일 수 있다. `

