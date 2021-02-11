from django.urls import path
from . import views

app_name="ecommerce_app"


urlpatterns = [
  path('all', views.GetAllProducts, name="GetAllProducts"),
  path('product/<pk>', views.GetOneProducts, name="GetOneProducts"),
  path('categories', views.Get_Categories, name="Get_Categories"),
  path('categories/<pk>', views.GetProducts_InCategory, name="GetProducts_InCategory"),
]