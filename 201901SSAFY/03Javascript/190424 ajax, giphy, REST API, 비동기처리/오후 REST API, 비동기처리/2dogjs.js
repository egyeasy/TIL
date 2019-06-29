// 30분 뒤에 종료를 알리는 js 코드

function sleep() {
    let start = Date.now()
    while (Date.now() < start + 5000) {}  // 5초 동안 아무짓도 하지 말고 대기
}

function finish() {
    setTimeout(function() {
        console.log("수업이 종료되었습니다.")
    }, 3000)  // 1000마이크로세컨드 = 1초
    console.log("수업이 진행중입니다.") // 여기에 넣은건 기다리지 않고 바로 출력되게 됨
    // sleep()
    // console.log("수업이 종료되었습니다.")
}

console.log("수업 중")
finish()
console.log("땡땡땡")  // 시간 인자가 앞에 있을 때 -> 땡땡땡은 뜨는데 finish 내의 consolelog가 안됨.