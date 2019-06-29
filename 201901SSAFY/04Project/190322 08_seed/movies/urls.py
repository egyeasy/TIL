from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # project 7 - database
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_id>/delete/', views.delete_movie, name='delete_movie'),
    path('<int:movie_id>/scores/new/', views.create_score, name='create_score'),
    path('<int:movie_id>/scores/<int:score_id>/delete/', views.delete_score, name='delete_score'),

    # project 8 - seed
    path('new/', views.movie_new, name='movie_new'),
    path('<int:movie_id>/edit/', views.edit_movie, name='edit_movie'),
]