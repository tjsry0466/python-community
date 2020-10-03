from django.urls import path
from . import views

app_name = 'index'
urlpatterns = [
    path('', views.index, name='index'),
    path('board/', views.post_list, name='post_lit'),
]
