from django.urls import path
from . import views

urlpatterns = [
    # /api/v1/musics
    path('musics/', views.music_list),
    # /api/v1/musics/1
    path('musics/<int:music_id>/', views.music_detail),
]