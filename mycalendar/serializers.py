from rest_framework import serializers
from .models import Appointments

class AppointmentSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="name")
    start = serializers.DateField(source="start_date")
    end = serializers.DateField(source="end_date")
    classNames = serializers.CharField(source="status", allow_blank=True, required=False)

    class Meta:
        model = Appointments
        fields = ("id", "title", "start", "end", "classNames", "comments")
