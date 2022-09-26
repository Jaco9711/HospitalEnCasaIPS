from authApp.models.personal_salud import Personal_Salud
from rest_framework import serializers

class Personal_SaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_Salud
        fields = ('ps_username', 'ps_rol', 'ps_especialidad')