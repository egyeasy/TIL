# 01_layout

### Navigation Bar

- navbar component 활용

  `fixed-top` class를 통해 sticky navigation bar 구현

- Home, 친구 평점 보러가기, Log In 메뉴는 `ml-auto` 클래스를 통해 우측 정렬

- 나눔 고딕 글꼴 사용



### Header

- jumbotron-fluid component 활용
  `background-size: 100%`를 통해 background image가 좌우로 꽉 차게 설정
  `text-align`, `align-items` : 텍스트 가운데 정렬
- 도현 글꼴 사용



### Footer

- navbar component 활용
  `fixed-bottom` class를 통해 sticky footer 구현
- `button onclick="location.href='#'"`를 통해 헤더로 가는 버튼 구현
- 도현 글꼴 사용







# 02_movie

### subtitle

- h3 태그
- hr 태그 - 밑줄 구현



### card view

- card component 활용
  `col-**-**` 를 통해 반응형 페이지 구현
  카드 내 영역별 구분선은 디폴트로 구분선이 있는 component 사용해서 구현
- 개별 card에 col-12를 적용하고 각 카드를 또 하나의 클래스로 감싸서 카드 간 margin 확보
- `d-inline` class를 통해 영화 제목, 평점 한 줄에 표현







# 03_detail_view

### modal

- 카드별로 이미지 태그마다 `data-target`, `data-toggle` 지정하여 modal 연결
  modal별로 id를 다르게 하여 상세 정보 페이지가 중복되지 않게 설정
- carousel component 활용하여 영화 사진 표시
  carousel별로 id를 다르게 설정해야 각각의 carousel이 잘 작동함
- 이미지 외의 상세 정보는 card component를 활용하여 표시