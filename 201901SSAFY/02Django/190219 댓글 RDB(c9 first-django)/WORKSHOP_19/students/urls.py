from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('<int:student_id>/edit/', views.edit, name='edit'),
    path('<int:student_id>/update/', views.update, name='update'),
    path('<int:student_id>/delete/', views.delete, name='delete'),
]