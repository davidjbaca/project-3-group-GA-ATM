from django.urls import path
from . import views







# URLS GO HERE

# Home page URL
urlpatterns = [
    path('', views.home, name='home'),

# About page 
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('atms/', views.atms_index, name='index'),
    path('atms/<int:atm_id>/', views.atms_detail, name='detail'),
    path('atms/create/', views.AtmCreate.as_view(), name='atms_create'),


    

]
