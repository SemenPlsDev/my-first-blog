from django.urls import path
from . import views

urlpatterns = [
    #мы связали view под именем post_list с корневым URL-адресом ''
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]