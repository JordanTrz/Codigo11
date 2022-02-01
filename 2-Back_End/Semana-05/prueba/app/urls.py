from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('empleados/', views.showEmpleados, name="showEmpleados"),
    path('equipos/', views.showEquipos, name="showEquipos")
]