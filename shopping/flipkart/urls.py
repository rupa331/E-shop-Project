from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('signin',views.signup,name='sign_up'),
    path('lohin',views.login,name='login'),

]