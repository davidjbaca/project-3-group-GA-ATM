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
    path('atms/<int:pk>/update/', views.AtmUpdate.as_view(), name='atms_update'),
    path('atms/<int:pk>/delete/', views.AtmDelete.as_view(), name='atms_delete'),

    # REVENUE
    path('atms/<int:atm_id>/add_revenue',
         views.add_revenue, name='add_revenue'),
    path('atms/revenue/<int:pk>/delete/',
         views.DeleteRevenue.as_view(), name='revenue_delete'),


    # CASH INPUTS
    path('atms/<int:atm_id>/add_cashinput',
         views.add_cashinput, name='add_cashinput'),
    path('atms/cashinput/<int:pk>/delete/',
         views.DeleteCashinput.as_view(), name='cashinput_delete'),
]
