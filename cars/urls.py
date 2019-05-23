from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    
    path('cars/', views.vehicle_list),
    path('cars/<int:vehicle_id>/', views.vehicle_show), 
    path('cars/form/', views.vehicle_form),  
    path('cars/<int:vehicle_id>/edit/', views.vehicle_edit),
    path('cars/delete/<int:vehicle_id>/', views.vehicle_delete),

    path('manufacturer/', views.manufacturer_list),
    path('manufacturer/<int:manufacturer_id>/', views.manufacturer_show), 
    path('manufacturer/form/', views.manufacturer_form),
    path('manufacturer/<int:manufacturer_id>/edit/', views.manufacturer_edit),
    path('manufacturer/delete/<int:manufacturer_id>/', views.manufacturer_delete),

    path('fuel/', views.fuel_list),
    path('fuel/<int:fuel_id>/', views.fuel_show), 
    path('fuel/form/', views.fuel_form),
    path('fuel/<int:fuel_id>/edit/', views.fuel_edit),
    path('fuel/delete/<int:fuel_id>/', views.fuel_delete)

]