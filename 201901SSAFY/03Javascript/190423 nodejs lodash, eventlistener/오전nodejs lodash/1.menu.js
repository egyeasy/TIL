var _ = require('lodash')
var menus = ['짜장면', '짬뽕', '볶음밥'] // Array 배열
menus[0]
// lodash로 python random.choice를 구현해보자
var pick = _.sample(menus)  // 랜덤으로 하나 꺼냄
console.log(pick)
console.log(`오늘의 메뉴는 ${pick}입니다.`) // string interpolation : 백틱 사용