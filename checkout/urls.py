from django.urls import path
from . import views

app_name="checkout"


urlpatterns = [
    path("", views.add_to_order)
]