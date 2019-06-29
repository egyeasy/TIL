# 35homework

1. ​					var		let		const

   reassign	  O			X			X

   rebind		 O			O			X

   update		O			O			O

   let 변수는 rebind와 update가 되지만 const 변수의 경우 rebind는 불가능하다. rebind를 할 필요없이 update만 해야 하는, 따라서 변경할 일이 적은(상수에 가까운) 변수는 const로 지정하고, 그 외에는 let으로 지정한다.

2. JSON은 속성-값 쌍 또는 키-값 쌍으로 이루어진 데이터 오브젝트를 전달하기 위해 인간이 읽을 수 있는 텍스트를 사용하는 개방형 표준 포맷이다. JSON을 JS에서  오브젝트로 사용할 수 있게 하기 위해서는 parsing 작업이 필요하다. 따라서 JSON은 그 자체로는 오브젝트와 다른 성질의 것이다.

3. 1) `myObject['key']`

   2) `myObject.key`

4. 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>
    <h1>Hello World!</h1>
    <script>
        // 1. h1 태그를 선택한 뒤, header라는 상수에 할당한다.
        const header = document.querySelector('h1')
        // 2. 브라우저 콘솔에 header 안의 내용을 출력한다.
        console.log(header.innerText)
        // 3. header 안의 내용을 'Happy Hacking!'으로 변경한다.
        document.querySelector('h1').innerText = 'Happy Hacking!'
    </script>
</body>
</html>
```





# 35workshop

```js
// This is Comment

function concat(str1, str2) {
    return `${str1} - ${str2}`
}

function checkLongStr(string) {
    if (string.length > 10) {
        return true
    } else {
        return false
    }
}

if (checkLongStr(concat('Happy', 'Hacking'))) {
    console.log('LONG STRING')
} else {
    console.log('SHORT STRING')
}
```

































