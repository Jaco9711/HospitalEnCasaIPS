from django.db import models
from .usuario import Usuario

class Personal_Salud(models.Model):
    ps_id = models.AutoField('ID personal salud', primary_key=True, null=False)
    ps_username = models.ForeignKey(Usuario, related_name='personal_salud', on_delete=models.CASCADE, max_length=30, null=False)
    ps_rol = models.CharField('Rol personal salud', max_length=20, unique=False, null=False)
    ps_especialidad = models.CharField('Especialidad personal salud', max_length=40, unique=False, null=False)