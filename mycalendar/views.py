from rest_framework import viewsets, permissions
from .models import Appointments
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointments.objects.all().order_by("start_date")
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.AllowAny]
