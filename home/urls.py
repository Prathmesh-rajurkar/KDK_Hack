from django.contrib import admin
from django.urls import path
# from django.conf.urls import patterns, url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.sign_in,name='login'),
    path('signup/',views.sign_up,name='signup'),
    path('posts/signout/',views.sign_out,name='signout'),
    path('posts/',views.posts,name='posts'),
    # path('roadbuddy/',('^media/(?PC:/Users/asus/Desktop/KDK-Hack/home/templates/home/media.*)$', 'django.views.static.serve',
    #              {'document_root': settings.MEDIA_ROOT}),)
    # path('',views.index,name='index'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
