from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('introduce/', views.introduce, name='introduce'),
    path('room/', views.room, name='room'),
    path('travel/', views.travel, name='travel'),
    path('fac/', views.fac, name='fac'),
    path('reservation/', views.reservation, name='reservation'),
    path('location', views.location, name='location'),
    path('reservating/', views.reservating, name='reservating'),

    path('room/101/', views.room101, name='room101'),
    path('room/201/', views.room201, name='room201'),
    path('room/301/', views.room301, name='room301'),

]