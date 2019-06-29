/*
변수 : 변수
리스트 : 배열
딕셔너리 : 오브젝트
*/

console.log(document.querySelector('span, div'))

// 배열
names = ['john', 'junse', 'dongyoung']
names[2]

names.length
//=> 3

names.push('boyoon')

names.pop()

names.shift() // popleft

names.unshift('donghoon') // 왼쪽에 넣기

names.join(" + ")

names.reverse() // 원본 순서 바꿔버리기



// 오브젝트
student = {
    'name': 'john',
    'age': 34,
    'address': '강남구',
    job: 'lecturer', // key 값을 알아서 string으로 변환해준다.
}
// {name: "john", age: 34, address: "강남구", job: "lecturer"}

student['name']
student['age']
student['job']


// 객체적 접근이 가능
student.name
student.address