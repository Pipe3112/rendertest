from rest_framework import serializers
from mycalendar.models import Appointments  # 👈 importar bien el modelo

class AppointmentSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='name')  # name → title
    start = serializers.DateField(source='start_date')  # start_date → start
    end = serializers.DateField(source='end_date')  # end_date → end
    classNames = serializers.CharField(source='status')  # status → classNames

    class Meta:
        model = Appointments
        fields = ('id', 'title', 'start', 'end', 'classNames')
