from .models import Service, Appointment
from .serializers import ServiceSerializer, AppointmentSerializer
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
    permission_classes = [permissions.IsAuthenticated]
