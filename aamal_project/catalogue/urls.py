from django.urls import path,include
from . import views

app_name = "catalogue"


urlpatterns = [
    path('catalogue/', views.catalogue, name='catalogue'),
    path('products/', views.products, name='products'),
   
]
