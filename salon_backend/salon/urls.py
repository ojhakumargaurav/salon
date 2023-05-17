from django.contrib import admin
from django.urls import path
from . import views 
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'service', views.ServicesViewset)
router.register(r'appointment', views.AppointmentViewset)


