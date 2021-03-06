from django.urls import path
from . import views


urlpatterns = [
    path('genres/', views.genre_list),
    path('genres/<int:genre_id>/', views.genre_detail),
    path('movies/', views.movie_list),
    path('movies/<int:movie_id>/', views.movie_detail),
    path('scores/<int:score_id>/', views.detail_update_delete_score),
    path('movies/<int:movie_id>/scores/', views.create_score),
]