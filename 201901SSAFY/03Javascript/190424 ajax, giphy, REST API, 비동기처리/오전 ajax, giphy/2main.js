// 1. input 태그안의 값을 잡는다.
// const input = document.querySelector('#js-userinput');
// const value = input.value
// console.log(value)

const button = document.querySelector('#js-go')
const input = document.querySelector('#js-userinput')
const resultArea = document.querySelector('#result-area')

button.addEventListener('click', (e) => {  // event를 줄여서 e
    const value = input.value
    // console.log(`click : ${value}`)
    // pushToDom(value)
    searchAndPush(value)
})

input.addEventListener('keypress', (e) => {
    if (e.keyCode === 13) {  // enter = 13번 코드
        const value = input.value
        // console.log(`enter : ${value}`)
        // pushToDom(value)
        searchAndPush(value)
    }
})

// 2. Giphy API를 통해 data를 받아서 가공한다.
const searchAndPush = (keyword) => {  // 함수 안에 넣어줌. keyword를 안에서 선언하지 않고 인자로 만들어준다
    resultArea.innerHTML = null; // search 할 때마다 초기화
    const API_KEY = 'SbNqUCzzoaLl25zJ80gBTun5I7aXrGZq'
    // let keyword = 'matrix'
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${API_KEY}`

    // 데이터 요청
    const GiphyXHR = new XMLHttpRequest()
    GiphyXHR.open('GET', URL)
    GiphyXHR.send()

    // 이제 데이터를 받아온다
    GiphyXHR.addEventListener('load', (e) => {
        const rawData = e.target.response
        const parsedData = JSON.parse(rawData)
        console.log(parsedData)
        console.log(parsedData.data[0].images.fixed_height.url)
        // pushToDom(parsedData.data[2].images.fixed_height.url) // 이렇게 하나의 data 이미지를 보여줄 수 있다.
        for (data of parsedData.data) {
            console.log(data.images.fixed_height.url)
            pushToDom(data.images.fixed_height.url)
        }
    })

    console.log(123) // 이게 위의 console.log보다 더 일찍 출력하게 된다.

    // 3. gif 파일들을 index.html(DOM)에 밀어넣어서 보여준다.
    const pushToDom = (data) => {
        // resultArea.innerHTML = data  // 해당 태그에 넣겠다는 얘기
        // resultArea.innerHTML = `<img src="${data}"/>`
        // resultArea.innerHTML += `<img src="${data}"/>`  // 하나씩 더하기
        const img = document.createElement('img') // img 태그 만들기. <img></img>
        img.setAttribute('src', data) // <img src="${data}" />
        img.className = 'container-image' // container에 담기. setAttribute('class', 'container-image') 와 같은 작업
        resultArea.appendChild(img)  // child : 안쪽에 다른 element를 쌓는 것
    }
}


