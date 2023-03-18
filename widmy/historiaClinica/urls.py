from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('hclinicas/', views.hclinica_list),
        path('activas',views.activas, name='activas'), 
    ]
    #path('', views.historiasclinicas_view, name='historiasclinicas_view'),
    #path('<int:pk>', views.historiaclinica_view, name='historiaclinica_view'),
    #path('activas',views.activas, name='activas')]