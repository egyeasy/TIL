// useAxios.js

const URL = 'https://dog.ceo/api/breeds/image/random'
console.log(URL, axios)
// html에서 axios를 불러왔으므로 바로 접근 가능
axios.get(URL)  // AJAX call - 비동기적으로 동작. promise를 반환
    .then(response => {
        // console.log(response)  // 객체가 parsing 되어 반환
        // const imageUrl = response.data.message
        // const imageBox = document.querySelector('#img-div')
        // const image = document.createElement('img')
        // image.src = imageUrl
        // imageBox.appendChild(image)
    })

// TODO: 위 코드를 async-await로 바꾸기
const getImage = async () => {
    const res = await axios.get(URL)
    console.log(res)
    const imageUrl = res.data.message
    const imageBox = document.querySelector('#img-div')
    const image = document.createElement('img')
    image.src = imageUrl
    imageBox.appendChild(image)
}

// 3개 이미지 가능
getImage()
getImage()
getImage()
