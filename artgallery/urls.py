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
    path('orderlistcustomer/', views.orderlistcustomer, name='orderlistcustomer'),
    path('orderlistadmin/', views.orderlistadmin, name='orderlistadmin'),
    path('customeractions/', views.customeractions, name='customeractions'),
    path('adminactions/', views.adminactions, name='adminactions'),
    # path('adminmail/', views.adminmail, name='adminmail'),
    path('adminstock/', views.adminstock, name='adminstock'),
    path('adminsales/', views.adminsales, name='adminsales'),
    path('orderinsert/', views.orderinsert, name='orderinsert'),
    path('stockinsert/', views.stockinsert, name='stockinsert'),
    path('stockview/', views.stockview, name='stockview'),
    path('about/', views.about, name='about'),
    path('sendmail/', views.sendmail, name='sendmail'),
    path('updateorder/(?P<order_id>[0-9]+)',views.updateorder,name='updateorder'),
    path('updatestock/<stock_id>',views.updatestock,name='updatestock'),
    path('purchaseinsert/', views.purchaseinsert, name='purchaseinsert'),
    path('purchaseview/', views.purchaseview, name='purchaseview'),
    path('report/', views.report, name='report'),
    path('viewreports/', views.viewreports, name='viewreports'),
]

