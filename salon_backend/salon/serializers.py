from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Service, Appointment, BusinessUser, SubscriptionDetails


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BusinessUser
        fields = ["url", "username", "email", "name", "subscription_type"]


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ["name", "image_url", "price", "description"]


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"


class SubscriptionDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        Model = SubscriptionDetails
        fields = "__all__"


class BusinessUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        Model = BusinessUser
        fields = "__all__"
