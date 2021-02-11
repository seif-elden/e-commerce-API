from django.urls import path
from . import views

app_name="cart"


urlpatterns = [
    path('', views.GetAllProducts_in_cart),
    path('add', views.add_to_cart),
    path('update/<pk>', views.update_quantity),
    path('delete/<pk>', views.delet_item_from_cart),
]