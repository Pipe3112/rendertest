from rest_framework import viewsets, permissions
from .serializers import AppointmentSerializer
from .models import Appointments

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.AllowAny]
