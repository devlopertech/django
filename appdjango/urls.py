from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views




urlpatterns = [
    
    path('',views.index,name='shop-home'),
    path('signup', views.signup, name='submit'),
    path('login', views.userlogin,name='login'),
    path('logout', views.handelLogout, name="handleLogout"),
]