from django.db import models
from .usuario import Usuario
from .paciente import Paciente

class Familiar(models.Model):
    f_id = models.AutoField('ID familiar', primary_key=True, null=False)
    f_username = models.ForeignKey(Usuario, related_name='familiar', on_delete=models.CASCADE, max_length=30, null=False)
    f_paciente = models.ForeignKey(Paciente, related_name='familiar', on_delete=models.CASCADE, null=False)
    f_correo = models.EmailField('Correo familiar', max_length=50, unique=True, null=False)
    f_parentesco = models.CharField('Parentesco familiar', max_length=20, unique=False, null=False)