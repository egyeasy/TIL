# 42homework

1. `:href`
2. `@click`
3. `computed` 속성은 해당 속성이 종속된 대상이 변경될 때 함수를 실행한다. 이 때 종속 대상을 따라 캐싱이 이루어지게 된다. `watch` 속성은 Vue 인스턴스의 데이터 변경을 관찰하고 이에 반응하는 보다 일반적인 속성이다. `computed` 속성은 계산해야 하는 목표 데이터를 정의하는 방식(선언형 프로그래밍), `watch` 속성은 감시할 데이터를 지정하고 그 데이터가 바뀌면 특정한 함수를 실행하는 방식(명령형 프로그래밍)이다.



# 42workshop

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>42workshop</title>
</head>
<body>
    <div id="app">
        <button @click="addNum">+1</button>
        <p>Counter: {{ count }}</p>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        let app = new Vue({
            el: '#app',
            data: {
                count: 0,
            },
            methods: {
                addNum: function() {
                    this.count++
                }
            }
        })
    </script>
</body>
</html>
```

