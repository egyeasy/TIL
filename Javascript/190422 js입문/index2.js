// 한줄 주석
/* 
    여러 줄 주석
*/
// alert("야!") // 경고 창
user_name = prompt("이름이 뭐야?")
user_input = prompt("나이를 입력해줘") // python의 input()
console.log(user_input)

console.log("너!") // 콘솔 창에 뜨는 것. django print문이 console창에 띄워주는 것과 같음.
document.write("임마!") // document 객체 안에 html 파일이 들어있음. html에 작성해준다.
document.write("<h1>임마!</h1>")
console.log(document.querySelector('h1')) // 찾기 기능. 인자로 태그이름 또는 셀렉터.
console.log(document.querySelector('h1').innerText) // 태그 안에 있는 텍스트만 가져올 수 있다.
document.querySelector('h1').innerText = "동영아!" // 원래 있던 내용을 바꿔준다.

if (user_input > 30) {   // type cohersion
    // alert('아재네')
    age = '아재네'
} else if (user_input > 20){
    // alert('학식이네')
    age = '학식이네'
} else {
    // alert('급식이네')
    age = '급식이네'
}
// document.querySelector('h1').innerText = user_name + "는 " + age
document.querySelector('h1').innerText = `${user_name}은(는) ${age}`

user_input2 = prompt("숫자를 입력해줘")

for (i = 0; i < user_input2; i++){ // i++ 대신 i+=1을 써도 된다. ++i를 쓰면 한번 더하고 작업을 수행. 다른 결과를 가져올 수 있다.
    document.write(`<p>${i}</p>`)
}

// console.log(i)
