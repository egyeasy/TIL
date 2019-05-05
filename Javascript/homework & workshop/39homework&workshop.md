# 39 homework

1. 

```js
const name = '김싸피';
const hobby = '프로그래밍';

const student = {
    name: name,
    hobby: hobby,
    introduce: function () {
        return `이름은 ${this.name}, 취미는 ${this.hobby}`;
    }
}

console.log(student.introduce())
```

2. 

```js
function solveMe(...nums) {
    arr = []
    const result = () => {
        for (i = 1; i < nums.length; i++) {
            arr.push(nums[0] * nums[i])
        }
    }
    result()
    console.log(arr)
    return arr
}

const a = solveMe(2, 1, 2, 3, 4); // [2, 4, 6, 8]
const b = solveMe(5, 10, 20); // [50, 100]
console.log(a.concat(b)); // [2, 4, 6, 8, 50, 100]
```



# 39workshop

```js
class Monster {
    constructor(options) {
        this.name = options.name
        this.health = 100
    }
    

}
class Spider extends Monster {

    bite(monster) {
        monster.health -= 10;
    }
}

spidy = new Spider({ name: '거미인간'});
mob = new Monster({ name: '미니언'});

spidy.bite(mob);
console.log(spidy.name, spidy.health); // 거미인간 100
console.log(mob.name, mob.health); // 미니언 90
```

