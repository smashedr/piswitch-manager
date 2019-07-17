from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('home.urls')),
]

urlpatterns += staticfiles_urlpatterns()
