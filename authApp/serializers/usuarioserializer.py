from authApp.models.usuario import Usuario
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('u_username', 'u_contrasena', 'u_perfil', 'u_nombres', 'u_apellidos', 'u_telefono', 'u_genero')