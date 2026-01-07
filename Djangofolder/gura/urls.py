from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.app1,name='app1'),
    # path('/order',views.app1,name='order')
    # here /order means app1/order
]
