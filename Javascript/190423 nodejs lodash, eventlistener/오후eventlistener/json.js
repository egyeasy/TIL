// JSON & javascript object

/*
1. JSON : 파일포맷 & 단순 문자열(string)
"{
    coffee: 'Americano',
    iceCream: 'Red Velvet'   
}"
이런 형식의 데이터 포맷, 또는 단순 문자열을 json이라고 한다.
이걸 javascript object로 변환하는 과정이 있게 된다.

2. Javascript Object: Javascript 코드가 읽을 수 있는 오브젝트
*/

const stringObject = JSON.stringify({"coffee": "Americano", "iceCream": "Red Velvet"})
// const stringObject = JSON.stringify({'coffee': 'Americano', 'iceCream': 'Red Velvet'}) // 홑따옴표로 만들어도 쌍따옴표로 출력된다 -> 쌍따옴표로 만들자!
console.log(stringObject)

JSONData = '{"coffee": "Americano", "iceCream": "Red Velvet"}'
const parsedData = JSON.parse(JSONData)
console.log(parsedData.coffee)