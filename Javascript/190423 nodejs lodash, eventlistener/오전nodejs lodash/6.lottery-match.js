const _ = require('lodash')
const luckyNumbers = [5, 7, 32, 2, 36, 26]
const numbers = _.range(1, 46)
console.log(numbers)
// node 3.lottery.js
const picks = _.sampleSize(numbers, 6)  // 6개의 랜덤 번호 => 배열
// console.log(`오늘의 행운의 번호는 ${picks}`)


// 동훈
function match() {
    const numbers = _.range(1, 46)
    const picks = _.sampleSize(numbers, 6)
    console.log(`오늘의 행운의 번호는 ${picks}`)
    const lucky = _.size(_.intersection(luckyNumbers, picks))
    return lucky
}

console.log(match())

// jason
function match() {
    const numbers = _.range(1, 46)
    const picks = _.sampleSize(numbers, 6)
    let count = 0
    for (pick of picks) {
        if (_.includes(luckyNumbers, pick)) {
        // 또는 if (luckyNumbers.includes(pick)) {
            count += 1
        }
    }
    console.log(`My numbers ${picks}`)
    console.log(`Lucky numbers ${luckyNumbers}`)
    console.log(`Matches ${count}`)
}

match()