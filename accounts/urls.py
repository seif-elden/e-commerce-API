from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name="accounts"


urlpatterns = [
    path('address/create', views.api_add_address, name="Creat_Address"),
    path('address/<pk>/delete', views.api_delet_address, name="Delete_Address"),
    path('address/<pk>/edit', views.api_edit_address, name="edit_Address"),
    path('address/<pk>', views.api_get_address, name="One_Address"),
    path('address', views.GetAllAddress, name="All_Address"),

    path('user/create', views.CreatUser, name="CreatUser"),
    path('user/login', obtain_auth_token, name="login"),
    path('user/info', views.GET_User, name="GET_User"),
    path('user/update', views.Edit_User, name="Edit_User"),
]