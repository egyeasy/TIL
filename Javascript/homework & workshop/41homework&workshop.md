# 41homework

1. `v-bind`
2. `v-for`, `v-if`



# 41workshop

id가 `app` 인 html element 내에 다음 코드를 추가한다.

```html
<ul>
  <li v-for="number in numbers" v-if="number % 2 === 0">
    {{ number }}
  </li>
</ul>
```

