from django.urls import path
from . import views


urlpatterns = [
    path("",views.index, name="index"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('logintype/', views.logintype, name='logintype'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('registeruser/', views.registeruser, name='registeruser'),
    path('appoinment/', views.appoinment, name='appoinment'),
    path('userdash/', views.userdash, name='userdash'),
    path('uploadprod/', views.uploadprod, name='uploadprod'),
    path('uploadserv/', views.uploadserv, name='uploadserv'),
    path('users/', views.users, name='users'),
    path('products/', views.products, name='products'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('addservice/', views.addservice, name='addservice'),
    path('createuser/', views.createuser, name='createuser'),
    path('delete_user/<str:pk>/', views.delete_user, name='delete_user'),
    path('delete_appointment/<str:pk>/', views.delete_appointment, name='delete_appointment'),
    path('delete/<str:pk>/', views.delete_product, name='delete_product'),
    path('delete_service/<str:pk>/', views.delete_service, name='delete_service'),
    path('makebill/<str:id>/', views.makebill, name='makebill'),
    path('newbill/', views.newbill, name='newbill'),

]