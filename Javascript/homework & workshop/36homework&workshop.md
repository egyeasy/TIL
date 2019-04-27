# 36homework

1. 1) `document.querySelector()` : 인자로 전달한 css 선택자에 해당하는 첫 번째 element 객체를 반환. 결과가 없다면 null을 반환.

   2) `document.querySelectorAll()` : 인자로 전달한 css 선택자와 하나라도 일치하는 각 element 객체의 Nodelist를 반환
   
2. click : 해당 element를 마우스로 클릭

   mouseover : 해당 element나 그 자식 element 위에 마우스 포인터를 가져다놓음

   mouseout : 해당 element나 그 자식 element로부터 마우스 포인터를 떼어놓음

   mousemove : 마우스 포인터가 해당 element 위에서 움직임

   keypress : 키보드 키를 누름

   keydown : 키보드 키를 누르고 있는 상태

   keyup : 키보드 키를 누르고 있던 중에 뗌

   load : 오브젝트가 로드되었을 때

   scroll : 해당 element의 스크롤 바가 스크롤 되었을 때

   change : form element의 내용이나 select tag의 선택 여부, 체크 여부 등이 바뀌었을 때

3. `innerHTML +=` 가 `appendChild()`보다 로드가 느리다. `innerHTML` 은 타겟 element의 내용을 완전히 rebuild하지만, `appendChild()` 는 DOM이나 타겟 element 또는 node들에 대해 complete rebuilding을 수행하지 않기 때문이다.



# 36workshop

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Clicked</title>
</head>
<body>
    <h1>0</h1>
    <button id="change-btn">Click it</button>
    <script>
        const button = document.querySelector('#change-btn')
        const header = document.querySelector('h1')
        let clickCount = 0
        button.addEventListener('click', () => {
            clickCount++
            header.innerText = clickCount
        })
    </script>
</body>
</html>
```













