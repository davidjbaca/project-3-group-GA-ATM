from django.urls import path
from . import views







# URLS GO HERE
urlpatterns = [
    path('', views.home, name='home')
]
