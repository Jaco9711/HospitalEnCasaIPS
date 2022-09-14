from authApp.models.historia_clinica import Historia_Clinica
from rest_framework import serializers

class Historia_ClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia_Clinica
        fields = ('hc_paciente', 'hc_entorno', 'hc_diagnostico', 'hc_recomendaciones')