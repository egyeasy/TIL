from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movies_id>/', views.detail, name='detail'),
    path('<int:movies_id>/edit/', views.edit, name='edit'),
    path('<int:movies_id>/delete/', views.delete, name='delete'),
]