#  11_Vue SPA

## 1. 목표

- Vue.js를 통한 Single Page Application 구축



## 2. 준비 사항

1. Vue.js
2. axios
3. 영화 Data 제공용 Django REST API server



## 3. 구현 사항 및 과정

### 영화 리스트업

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
    <div id="main">
        <div class="movie-entry-box">
            <div class="movie-entry" v-for="movie in movies">
                <p>{{ movie.title }}</p>
                <img :src="movie.poster_url" :alt="movie.title"/>
            </div>
        </div>
    </div>
    <script>
        const app = new Vue({
            el: '#main',
            data: {
                API_URL: 'http://70.12.107.80:8000/api/v1/',
                movies: [],
            },
            methods: {
                getMovies: function() {
                    axios.get(this.API_URL + 'movies/')
                        .then(response => {
                            this.movies = response.data
                        })
                }
            },
            created: function() {
                this.getMovies()
            }
        })
    </script>
</body>
</html>
```





### 영화 상세정보 구현

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
    <div id="main">
        <!-- list -->
        <h1>Movie App</h1>
        <div class="movie-entry-box" v-if="!isDetailPage">
            <div class="movie-entry" v-for="movie in movies" @click="setCurrentMovie(movie)">
                <p>{{ movie.title }}</p>
                <img :src="movie.poster_url" :alt="movie.title"/>
            </div>
        </div>

        <!-- detail -->
        <div class="movie-detail" v-if="isDetailPage">
            <h4>{{ currentMovie.title }}</h4>
            <img :src="currentMovie.poster_url" :alt="currentMovie.title"/>
            <p>{{ currentMovie.description }}</p>
            <p>누적관객: {{ currentMovie.audience }}</p>
            <p>장르: {{ currentMovie.genre }}</p>
            <textarea name="" id="" cols="30" rows="10"></textarea>
            <input type="number" min="0" max="5">
            <button type="button" @click="togglePage">Back</button>
        </div>
    </div>
    <script>
        const app = new Vue({
            el: '#main',
            data: {
                API_URL: 'http://70.12.107.80:8000/api/v1/',
                movies: [],
                isDetailPage: false, // flag
                currentMovie: {},
            },
            methods: {
                togglePage: function() {
                    this.isDetailPage = !this.isDetailPage
                },
                getMovies: function() {
                    axios.get(this.API_URL + 'movies/')
                        .then(response => {
                            this.movies = response.data
                        })
                },
                setCurrentMovie: function(movie) {
                    this.currentMovie = movie
                    this.togglePage()
                },
            },
            created: function() {
                this.getMovies()
            }
        })
    </script>
</body>
</html>
```





### 댓글 기능 구현

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
    <div id="main">
        <!-- list -->
        <h1>Movie App</h1>
        <div class="movie-entry-box" v-if="!isDetailPage">
            <div class="movie-entry" v-for="movie in movies" @click="setCurrentMovie(movie)">
                <p>{{ movie.title }}</p>
                <img :src="movie.poster_url" :alt="movie.title"/>
            </div>
        </div>

        <!-- detail -->
        <div class="movie-detail" v-if="isDetailPage">
            <h4>{{ currentMovie.title }}</h4>
            <img :src="currentMovie.poster_url" :alt="currentMovie.title"/>
            <p>{{ currentMovie.description }}</p>
            <p>누적관객: {{ currentMovie.audience }}</p>
            <p>장르: {{ currentMovie.genre }}</p>
            <textarea v-model="review.content"></textarea>
            <input type="number" min="0" max="5" v-model="review.score">
            <button type="button" @click="postReview(currentMovie.id)">Review 작성</button>
            <button type="button" @click="togglePage">Back</button>
        </div>
    </div>
    <script>
        const app = new Vue({
            el: '#main',
            data: {
                API_URL: 'http://70.12.107.80:8000/api/v1/',
                movies: [],
                isDetailPage: false, // flag
                currentMovie: {},
                review: {
                    content: '',
                    score: 0,
                }
            },
            methods: {
                togglePage: function() {
                    this.isDetailPage = !this.isDetailPage
                },
                getMovies: function() {
                    axios.get(this.API_URL + 'movies/')
                        .then(response => {
                            this.movies = response.data
                        })
                },
                setCurrentMovie: function(movie) {
                    this.currentMovie = movie
                    this.togglePage()
                },
                postReview: function(movieId) {
                    axios.post(`${this.API_URL}movies/${movieId}/scores/`, this.review)
                        .then(response => {
                            alert(reponse.data.message)
                            // 입력 form 초기화
                            this.review.content = ''
                            this.review.score = 0
                        })
                }
            },
            created: function() {
                this.getMovies()
            }
        })
    </script>
</body>
</html>
```





### 영화 상세정보와 함께 리뷰와 평점 확인

GET scores를 통해 listup 해야한다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
    <div id="main">
        <!-- list -->
        <h1>Movie App</h1>
        <div class="movie-entry-box" v-if="!isDetailPage">
            <div class="movie-entry" v-for="movie in movies" @click="setCurrentMovie(movie)">
                <p>{{ movie.title }}</p>
                <img :src="movie.poster_url" :alt="movie.title"/>
            </div>
        </div>

        <!-- detail -->
        <div class="movie-detail" v-if="isDetailPage">
            <h4>{{ currentMovie.title }}</h4>
            <img :src="currentMovie.poster_url" :alt="currentMovie.title"/>
            <p>{{ currentMovie.description }}</p>
            <p>누적관객: {{ currentMovie.audience }}</p>
            <p>장르: {{ currentMovie.genre.name }}</p>
            <!-- 리뷰 리스트 -->
            <hr />
            <div v-for="movieReview in movieReviews">
                <p>{{ movieReview.content }}</p>
                <p>Score: {{ movieReview.score }}</p>
            <hr />
            </div>

            <!-- 리뷰 입력창 -->
            <textarea v-model="review.content"></textarea>
            <input type="number" min="0" max="5" v-model="review.score">
            <button type="button" @click="postReview(currentMovie.id)">Review 작성</button>
            <button type="button" @click="togglePage">Back</button>
        </div>
    </div>
    <script>
        const app = new Vue({
            el: '#main',
            data: {
                API_URL: 'http://70.12.107.80:8000/api/v1/',
                movies: [],
                isDetailPage: false, // flag
                currentMovie: {},
                review: {
                    content: '',
                    score: 0,
                },
                movieReviews: [],
            },
            methods: {
                togglePage: function() {
                    this.isDetailPage = !this.isDetailPage
                },
                getMovies: function() {
                    axios.get(this.API_URL + 'movies/')
                        .then(response => {
                            this.movies = response.data
                        })
                },
                setCurrentMovie: function(movie) {
                    this.currentMovie = movie
                    console.log(this.currentMovie)
                    this.togglePage()
                    this.getMovieReviews(movie.id)
                },
                postReview: function(movieId) {
                    axios.post(`${this.API_URL}movies/${movieId}/scores/`, this.review)
                        .then(response => {
                            alert(reponse.data.message)
                            // 입력 form 초기화
                            this.review.content = ''
                            this.review.score = 0
                            // 작성한 댓글도 바로 리스트업
                            this.getMovieReview(movieId)
                        })
                },
                getMovieReviews: function(movieId) {
                    axios.get(`${this.API_URL}movies/${movieId}/scores/`)
                        .then(response => {
                            this.movieReviews = response.data
                        })
                }
            },
            created: function() {
                this.getMovies()
            }
        })
    </script>
</body>
</html>
```



### 장르별 영화 목록을 제공

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
    <div id="main">
        <!-- list -->
        <h1>Movie App</h1>
        <div class="movie-entry-box" v-if="!isDetailPage">
            <button type="button" @click="getMovies">전체</button>
            <button type="button" v-for="genre in genres" @click="setGenre(genre.id)">{{ genre.name }}</button>
            <div class="movie-entry" v-for="movie in movies" @click="setCurrentMovie(movie)">
                <p>{{ movie.title }}</p>
                <img :src="movie.poster_url" :alt="movie.title"/>
            </div>
        </div>

        <!-- detail -->
        <div class="movie-detail" v-if="isDetailPage">
            <h4>{{ currentMovie.title }}</h4>
            <img :src="currentMovie.poster_url" :alt="currentMovie.title"/>
            <p>{{ currentMovie.description }}</p>
            <p>누적관객: {{ currentMovie.audience }}</p>
            <p>장르: {{ currentMovie.genre.name }}</p>
            <!-- 리뷰 리스트 -->
            <hr />
            <div v-for="movieReview in movieReviews">
                <p>{{ movieReview.content }}</p>
                <p>Score: {{ movieReview.score }}</p>
            <hr />
            </div>

            <!-- 리뷰 입력창 -->
            <textarea v-model="review.content"></textarea>
            <input type="number" min="0" max="5" v-model="review.score">
            <button type="button" @click="postReview(currentMovie.id)">Review 작성</button>
            <button type="button" @click="togglePage">Back</button>
        </div>
    </div>
    <script>
        const app = new Vue({
            el: '#main',
            data: {
                API_URL: 'http://70.12.107.80:8000/api/v1/',
                movies: [],
                isDetailPage: false, // flag
                currentMovie: {},
                review: {
                    content: '',
                    score: 0,
                },
                movieReviews: [],
                genres: []
            },
            methods: {
                togglePage: function() {
                    this.isDetailPage = !this.isDetailPage
                },
                getMovies: function() {
                    axios.get(this.API_URL + 'movies/')
                        .then(response => {
                            this.movies = response.data
                        })
                },
                setCurrentMovie: function(movie) {
                    this.currentMovie = movie
                    console.log(this.currentMovie)
                    this.togglePage()
                    this.getMovieReviews(movie.id)
                },
                postReview: function(movieId) {
                    axios.post(`${this.API_URL}movies/${movieId}/scores/`, this.review)
                        .then(response => {
                            alert(reponse.data.message)
                            // 입력 form 초기화
                            this.review.content = ''
                            this.review.score = 0
                            // 작성한 댓글도 바로 리스트업
                            this.getMovieReview(movieId)
                        })
                },
                getMovieReviews: function(movieId) {
                    axios.get(`${this.API_URL}movies/${movieId}/scores/`)
                        .then(response => {
                            this.movieReviews = response.data
                        })
                },
                getGenres: function() {
                    axios.get(`${this.API_URL}genres/`)
                        .then(response => {
                            this.genres = response.data
                        })
                },
                setGenre: function(genreId) {
                    axios.get(`${this.API_URL}genres/${genreId}/`)
                        .then(response => {
                            console.log(response.data.movies)
                            this.movies = response.data.movies
                        })
                }
            },
            created: function() {
                this.getMovies()
                this.getGenres()
            }
        })
    </script>
</body>
</html>
```



### 평균 평점 제공

computed 사용

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
        <!-- detail -->
        <div class="movie-detail" v-if="isDetailPage">
            <h4>{{ currentMovie.title }}</h4>
            <img :src="currentMovie.poster_url" :alt="currentMovie.title"/>
            <p>{{ currentMovie.description }}</p>
            <p>누적관객: {{ currentMovie.audience }}</p>
            <p>장르: {{ currentMovie.genre.name }}</p>
            <p>평점: {{ averageScore }}</p>
        </div>
    </div>
    <script>
            computed: {
                averageScore: function() {
                    let sum = 0
                    this.movieReviews.forEach(review => {
                        sum = sum + review.score
                    })
                    return sum / this.movieReviews.length
                }
            },
    </script>
</body>
</html>
```





