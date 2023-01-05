from django.urls import path
from . import views







# URLS GO HERE

# Home page URL
urlpatterns = [
    path('', views.home, name='home'),

# About page 
    path('about/', views.about, name='about'),

]
