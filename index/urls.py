from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('introduce/', views.introduce, name='introduce'),
    path('test1/', views.test1, name='test1'),
    path('test2/', views.test2, name='test2'),
    path('test3/', views.test3, name='test3'),
    path('test4/', views.test4, name='test4'),
    path('test5/', views.test5, name='test5'),
]