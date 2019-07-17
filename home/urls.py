from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
    path('', views.show_settings, name='show'),
    path('save/', views.save_settings, name='save'),
]
