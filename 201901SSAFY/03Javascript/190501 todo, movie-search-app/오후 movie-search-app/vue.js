// https://www.themoviedb.org/
const API_KEY = '88f1070777b1fdd9907d7213d1f516b1'
const URL = `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}`
const IMG_URL = 'https://image.tmdb.org/t/p/w500'

axios.get(URL)
    .then(response => {
        console.log(response.data)
        const movies = response.data.results
    })

// 1. 빈 movies를 가지고 있는 vue 인스턴스 생성
// 2. created 함수가 실행되면서 api를 통해 movies를 가져옴
// 3. vue의 movies 안에 가져온 movies 데이터를 할당
// 4. vue의 데이터에 변화가 생기면서 새롭게 렌더링
const app = new Vue({
    el: '#main',
    data: {
        query: '',
        movies: []
    },
    // 함수를 정의하는 곳, caching이 됨 
    computed: {
        filteredMovies: function() {
            // return this.movies  // 그냥 data 그대로 반환해서 vue가 알고 있는지 테스트
            // query로 filtering한 movie만 반환

            // for 문을 도는 코드
            // const filtered = []
            // const query = this.query.trim().toLowerCase()
            // for (const movie of this.movies) {
            //     if (movie.title.trim().toLowerCase().includes(query)) {
            //         filtered.push(movie)
            //     }
            // }

            // return filtered

            // for 문 안 도는 코드
            // if (this.query === '') {  // '' <= 사용자가 검색을 안함
            if (!this.query) {
                return this.movies
            }

            const query = this.query.trim().toLowerCase()
            // callback 함수에서 반환되는 값이 true인 아이템만으로 새로운 배열 생성
            const filtered = this.movies.filter(movie => {
                return movie.title.toLowerCase().trim().includes(query)
            })
            return filtered
        }
    },
    // Vue 인스턴스가 생성되고 난 후 실행하는 함수
    async created() {
        const response = await axios.get(URL)
        const movies = response.data.results
        // this.movies = movies
        console.log(movies)
        // poster image url을 수정해주는 작업
        // map: callback 함수에서 return 되는 아이템으로 새롭게 배열을 만듦
        this.movies = movies.map(movie => {
            return { title: movie.title, image: IMG_URL + movie.poster_path}
        })
        console.log(this.movies)
    }
})