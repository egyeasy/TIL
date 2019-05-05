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