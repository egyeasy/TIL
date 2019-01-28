# homework

1. (2) Cascading Style Sheets
2. T T F
3. rem
4. 예제의 `div p`는 후손 셀렉터 방식으로 div 태그 내의 모든 태그 요소들에 대해 해당 속성을 적용하는 방식이다. `div > p`는 자식 셀렉터 방식으로 div 태그의 바로 하위에 있는 p 태그에 대해서만 해당 속성을 적용하는 방식이다.



# workshop

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>workshop</title
    <style>
        #ssafy > p:nth-of-type(2) {
            color: red;
        }
    </style>
</head>
<body>
    <div id="ssafy">
        <h2>어떤게 선택될까?</h2>
        <p>첫번째 단락</p>
        <p>두번째 단락</p>
        <p>세번째 단락</p>
        <p>네번째 단락</p>
    </div>
</body>
</html>
```

