### flex 공부 정리

flex는 네모 세계의 html 요소를 다룰 때 행과 열을 좀 더 자유자재로 컨트롤하고자 만들어졌다.



justify-content : 주축을 따라 정렬하는 방식을 정의(flex-start, flex-end, center, stretch, space-around, space-between, space-evenly)

align-items : 반대축을 따라 정렬하는 방식을 정의(flex-start, flex-end, center, stretch)



**flex-direction** : 주축과 시작점을 바꾸는 느낌? reverse를 하면 순서가 바뀔뿐만 아니라 반대방향에서부터 정렬이 시작된다. 뒤집히는 효과(row, row-reverse, column, column-reverse)



order: flex 내의 일련 요소들 중 하나를 택해서 순서를 지정. 지정된 아이들 사이에서 순위가 정해지는 것이고 정해지지 않은 애들은 order: 0으로 디폴트.

align-self: 값이 align-items에서 사용하는 값과 동일한데 개별 요소에 한해 적용



**flex-wrap**: 주축을 따라서 요소들이 넘칠 때 넘겨주는 옵션. 디폴트는 nowrap으로 넘겨지지 않고 요소가 컨테이너 내에 넘친다. wrap을 하면 넘치는 부분에 한해 줄바꿈. wrap-reverse는 이상하게도 줄바꿈을 한다음 반대축을 따라(횡으로) 뒤집어버림.



flex-flow = **flex-direction** + **flex-wrap**

align-content = wrap 이후 여러 줄 사이를 조정. 횡축을 따라 justify-content를 시행한다고 보면 됨(flex-start, flex-end, center, stretch, space-around, space-between, space-evenly)