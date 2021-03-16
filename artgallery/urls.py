from django.urls import path
from artgallery import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.registerCustomer,name='registercustomer'),
    path('login/',views.customerLogin,name='customerLogin'),
    path('customised/', views.customisedproduct, name='customisedproduct'),
    path('logout/', views.customerLogout, name='logout'),
    path('customerdetail/', views.customerdetail, name='customerdetail'),
    path('login_admin/', views.adminLogin, name='adminLogin'),
    path('orderlist/', views.orderlist, name='orderlist'),



]

