const teemo = document.querySelector('#teemo')

console.log(typeof(teemo)) // object. not tag

// 티모를 클릭하면, "출동준비"라고 한다.

// 클릭이라는 이벤트가 일어나면 반응하게 함. 두번째 인자는 이벤트가 발생시 실행할 함수.
teemo.addEventListener('click', function() {
    alert('출동준비!')
})

let x = 0
let y = 0

// document에 대해 이뤄지는 이벤트를 알아서 받아서 print할 수 있다.
document.addEventListener('keydown', function(event) {
    // console.log(event)
    console.log(event.keyCode)
    // document.write(`<h1>${event.keyCode}</h1>`)
    if (event.keyCode === 38) {
        y += 30
        teemo.style.marginBottom = `${y}px`
    } else if (event.keyCode === 40) {
        y -= 30
        teemo.style.marginBottom = `${y}px`
    } else if (event.keyCode === 39) {
        x += 30
        teemo.style.marginLeft = `${x}px`
    } else if (event.keyCode === 37) {
        x -= 30
        teemo.style.marginLeft = `${x}px`
    }
})