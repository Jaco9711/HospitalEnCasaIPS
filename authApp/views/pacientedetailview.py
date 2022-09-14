from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from authApp.models.paciente import Paciente
from authApp.serializers.pacienteserializer import PacienteSerializer
class PacienteDetailView(generics.RetrieveAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    

    def get(self, request, *args, **kwargs):


 

        return super().get(request, *args, **kwargs)