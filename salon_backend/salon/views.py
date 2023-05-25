from .models import Service, Appointment, SubscriptionDetails, BusinessUser
from .serializers import (
    ServiceSerializer,
    AppointmentSerializer,
    SubscriptionDetailsSerializer,
    BusinessUserSerializer,
)
from rest_framework import permissions
from rest_framework import viewsets


class ServicesViewset(viewsets.ModelViewSet):
    """
    this return a list of service list available
    """

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [permissions.AllowAny]
        else:
            # permission_classes = [permissions.AllowAny,permissions.IsAdminUser]
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


class AppointmentViewset(viewsets.ModelViewSet):
    """

    this is used to view the appointments and create a new appointment

    """

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubsriptionViewsets(viewsets.ModelViewSet):
    """
    this is subscription based model where business have to create a subscription
    which will enable them to offer discounts on there product to retain customers

    """

    queryset = SubscriptionDetails.objects.all()
    serializer_class = SubscriptionDetailsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BusinessUserViewsets(viewsets.ModelViewSet):
    """
    this viewset will list and retrieve user who will have subscription details too
    """

    queryset = BusinessUser.objects.all()
    serializer_class = BusinessUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
