from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
    path('', views.show_home, name='index'),
    path('redis/', views.show_redis, name='redis'),
    path('saveredis/', views.save_redis, name='saveredis'),
    path('wifi/', views.show_wifi, name='wifi'),
    path('savewifi/', views.save_wifi, name='savewifi'),
]
