from django.urls import path
from . import views

app_name = 'sns'

urlpatterns = [
    # posting model
    path('', views.posting_list, name='posting_list'),
    path('<int:posting_id>/', views.posting_detail, name='posting_detail'),
    path('create/', views.create_posting, name='create_posting'),
    # comment model
    path('<int:posting_id>/comment/create/', views.create_comment, name='create_comment'),
]