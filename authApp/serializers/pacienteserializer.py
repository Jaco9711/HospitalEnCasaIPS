from authApp.models.paciente import Paciente
from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('p_username', 'p_username', 'p_fecha_nacimiento', 'p_ciudad', 'p_direccion', ' p_latitud', 'p_longitud')