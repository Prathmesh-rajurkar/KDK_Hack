from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in,name='login'),
    path('signup/',views.sign_up,name='signup'),
    path('signout/',views.sign_out,name='signout'),
    path('posts/',views.posts,name='posts'),
    # path('',views.index,name='index'),

]