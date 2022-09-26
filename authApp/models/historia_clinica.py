from django.db import models
from .paciente import Paciente

class Historia_Clinica(models.Model):
    hc_id = models.AutoField('ID historia clínica', primary_key=True, null=False)
    hc_paciente = models.ForeignKey(Paciente, related_name='historia_clinica', on_delete=models.CASCADE, unique=False, null=False)
    hc_fecha_hora = models.DateTimeField('Fecha hora historia clínica', auto_now=True, unique=False, null=False)
    hc_entorno = models.CharField('Entorno', max_length=50, unique=False, null=False)
    hc_diagnostico = models.CharField('Diagnóstico', max_length=100, unique=False, null=False)
    hc_recomendaciones = models.CharField('Recomendaciones', max_length=200, unique=False, null=False)