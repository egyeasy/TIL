from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:user_pk>', views.detail, name='detail'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('<int:user_pk>/followers/', views.followers, name='followers'),
    path('<int:user_pk>/followings/', views.followings, name='followings'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]