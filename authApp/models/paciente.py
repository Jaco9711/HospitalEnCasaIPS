from django.db import models
from .usuario import Usuario
from .personal_salud import Personal_Salud

class Paciente(models.Model):
    p_id = models.AutoField('ID paciente', primary_key=True, null=False)
    p_username = models.ForeignKey(Usuario, related_name='paciente', on_delete=models.CASCADE, max_length=30, null=False)
    p_personal_salud = models.ForeignKey(Personal_Salud, related_name='paciente', on_delete=models.CASCADE, unique=False, null=False)
    p_fecha_nacimiento = models.DateField('Fecha nacimiento paciente', unique=False, null=False)
    p_ciudad = models.CharField('Ciudad paciente', max_length=20, unique=False, null=False)
    p_direccion = models.CharField('Direccion paciente', max_length=40, unique=False, null=False)
    p_latitud = models.CharField('Latitud paciente', max_length=15, unique=False, null=True)
    p_longitud = models.CharField('Longitud paciente', max_length=15, unique=False, null=True)