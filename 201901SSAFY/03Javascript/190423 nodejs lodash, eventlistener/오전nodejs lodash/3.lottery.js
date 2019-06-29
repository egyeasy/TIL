var _ = require('lodash')
var numbers = _.range(1, 46)
console.log(numbers)
// node 3.lottery.js
var picks = _.sampleSize(numbers, 6)  // Camel case
console.log(`오늘의 행운의 번호는 ${picks}`)

var name = 'jack'
console.log(`제 이름은 ${name}`)
console.log('제 이름은 ' + name)

var baseURL = 'www.namer.com'
var article = '1'
console.log(`${baseURL}/${article}`)

