function hello() {
    return "hello"
}

// hello()

multiply = function(a, b) {
    return a * b
}

multi = multiply

multi(5, 5)
// => 25
multiply(5, 5)
// => 25

typeof(multi)
// => "function"