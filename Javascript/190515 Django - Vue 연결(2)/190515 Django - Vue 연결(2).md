# 190515 Django - Vue 연결(2)

## c9 last_pang - Instagram

### views.py

```python
from django.http import JsonResponse



@login_required
def follow(request, user_id):
    # User라고 쓸 수 없다.
    person = get_object_or_404(get_user_model(), pk=user_id)
    # 만약 이미 팔로우한 사람이라면
    if request.user in person.followers.all():
        # 언팔
        person.followers.remove(request.user)
    # 아니면
    else:
        # 팔로우
        person.followers.add(request.user)
    return redirect('profile', person.username)


@login_required
def vue_follow(request, user_id):
    # follow를 시키거나, unfollow 시키거나 => JSON으로 받아서 => Vue를 통해 render
    # 아래는 위 함수와 같다.
    person = get_object_or_404(get_user_model(), pk=user_id)
    # 만약 이미 팔로우한 사람이라면
    if request.user in person.followers.all():
        # 언팔
        person.followers.remove(request.user)
        followed = False
    # 아니면
    else:
        # 팔로우
        person.followers.add(request.user)
        followed = True
    return JsonResponse({'followed': followed})

```



### urls.py

```python
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('login/', views.login, name="login"),
    path('delete/', views.delete, name="delete"),
    # 팔로우 대상id/follow
    path('<int:user_id>/follow/', views.follow, name="follow"),
    path('<int:user_id>/vuefollow/', views.vue_follow),
    path('change_profile/', views.change_profile, name="change_profile"),
]
```





### profile.html

```html

          <div id="app">
            <div>[[ text ]]</div>
            <!-- 버튼을 클릭하면 팔로우할 수 있는 버튼 -->
            <button @click="follow({{ profile.id }})" class="btn btn-info">팔로우</button>
          </div>


  <script>
    const app = new Vue({
      delimiters: ['[[', ']]'],
      el: '#app',
      data: {
        'text': '뷰 작동한다리',
        followed: false,
      },
      methods: {
        follow: function(profile_id) {
          axios.get(`/accounts/${profile_id}/vuefollow/`)
            .then((response)=>{
              console.log(response)
              return response.data  // return 되는 data도 promise로 나오게 되는 함수다
            })
            .then((data) => {
              this.followed = data.followed
            })
          // console.log(`${profile_id}번 유저 팔로우 했다리`)
        }
      }
    })
  </script>
```



v-bind 써서 `:class="{'클래스이름': true/false}"`

true/false 자리의 변수(boolean)에 따라 클래스를 넣을지 안 넣을지 조건을 정해줄 수 있다.



## 라이프사이클 - beforeMount

맨 처음 페이지가 랜더링될 때 팔로우/언팔 여부의 초기값을 알아내서 넣어주고 싶다.

Vue js가 Mount 되기 전에 작업을 추가해줘야 함.

follow 여부를 django에게 물어보고 받아오는 함수를 만든다.

### profile.html

```html
  <script>
    const app = new Vue({
      delimiters: ['[[', ']]'],
      el: '#app',
      data: {
        'text': '뷰 작동한다리',
        followed: false,
      },
      methods: {
        follow: function(profile_id) {
          axios.get(`/accounts/${profile_id}/vuefollow/`)
            .then((response)=>{
              console.log(response)
              return response.data  // return 되는 data도 promise로 나오게 되는 함수다
            })
            .then((data) => {
              this.followed = data.followed
            })
          // console.log(`${profile_id}번 유저 팔로우 했다리`)
        },
        checkFollow: function(profile_id) {
          axios.get(`/accounts/${profile_id}/checkfollow`)
        }
      },
      beforeMount: function() {
        // django에게 물어봐서 follow 여부를 확인하고, 해당되는 값을 보여준다.
        
      }
    })
  </script>
```



### urls.py

```python
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('login/', views.login, name="login"),
    path('delete/', views.delete, name="delete"),
    # 팔로우 대상id/follow
    path('<int:user_id>/follow/', views.follow, name="follow"),
    path('<int:user_id>/vuefollow/', views.vue_follow),
    path('<int:user_id>/checkfollow/', views.check_follow),
    path('change_profile/', views.change_profile, name="change_profile"),
]
```





### views.py

```python
@login_required
def check_follow(request, user_id):
    person = get_object_or_404(get_user_model(), pk=user_id)
    if request.user in person.followers.all():
        followed = True
    else:
        followed = False
    return JsonResponse({'followed': followed})
```



### profile.html

```html
          <div id="app">
            <div>[[ text ]]</div>
            <!-- 버튼을 클릭하면 팔로우할 수 있는 버튼 -->
            <button @click="follow({{ profile.id }})" :class="{'btn': true, 'btn-info': !followed, 'btn-primary': followed}">팔로우</button>
          </div>

  <script>
    const app = new Vue({
      delimiters: ['[[', ']]'],
      el: '#app',
      data: {
        'text': '뷰 작동한다리',
        followed: '',
      },
      methods: {
        follow: function(profile_id) {
          axios.get(`/accounts/${profile_id}/vuefollow/`)
            .then((response)=>{
              console.log(response)
              return response.data  // return 되는 data도 promise로 나오게 되는 함수다
            })
            .then((data) => {
              this.followed = data.followed
            })
          // console.log(`${profile_id}번 유저 팔로우 했다리`)
        },
        checkFollow: function(profile_id) {
          axios.get(`/accounts/${profile_id}/checkfollow`)
            .then((response) => {
              return response.data
            })
            .then((data) => {
              console.log(data.followed)
              this.followed = data.followed
            })
        }
      },
      beforeMount: function() {
        // django에게 물어봐서 follow 여부를 확인하고, 해당되는 값을 보여준다.
        this.checkFollow({{ profile.id }})
      }
    })
  </script>
```



그래도 새로고침하면 색깔이 원래거였다가 바뀌는 것이 보인다.

이건 `beforeCreate` `beforeMount`로도 해결할 수 없어서,

`v-show`로 보여주지 않고 있다가 django로 보낸 followed 받아오기 작업이 끝났을 때 보여줄 것이다.



```html

          <div id="app">
            <div>[[ text ]]</div>
            <!-- 버튼을 클릭하면 팔로우할 수 있는 버튼 -->
            <button v-show="loading" @click="follow({{ profile.id }})" :class="{'btn': true, 'btn-info': !followed, 'btn-primary': followed}">팔로우</button>
          </div>



  <script>
    const app = new Vue({
      delimiters: ['[[', ']]'],
      el: '#app',
      data: {
        'text': '뷰 작동한다리',
        followed: true,
        loading: false
      },
      methods: {
        follow: function(profile_id) {
          axios.get(`/accounts/${profile_id}/vuefollow/`)
            .then((response)=>{
              console.log(response)
              return response.data  // return 되는 data도 promise로 나오게 되는 함수다
            })
            .then((data) => {
              this.followed = data.followed
            })
          // console.log(`${profile_id}번 유저 팔로우 했다리`)
        },
        checkFollow: function(profile_id) {
          axios.get(`/accounts/${profile_id}/checkfollow`)
            .then((response) => {
              return response.data
            })
            .then((data) => {
              console.log(data.followed)
              this.followed = data.followed
              this.loading = true
            })
        }
      },
      beforeMount: function() {
        // django에게 물어봐서 follow 여부를 확인하고, 해당되는 값을 보여준다.
        this.checkFollow({{ profile.id }})
      }
    })
  </script>
```

















