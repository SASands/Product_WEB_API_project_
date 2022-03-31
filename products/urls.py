from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list),
    path('', views.products_list.<int:pk>),
    
]