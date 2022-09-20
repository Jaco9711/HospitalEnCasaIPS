from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    u_username = models.CharField('Usuario', primary_key=True, max_length=30, null=False)
    password = models.CharField('Contraseña', max_length=256, unique=False, null=False)
    u_perfil = models.CharField('Perfil usuario', max_length=20, unique=False, null=False)
    u_nombres = models.CharField('Nombres usuario', max_length=20,unique=False, null=False)
    u_apellidos = models.CharField('Apellidos usuario', max_length=20,unique=False, null=False)
    u_telefono = models.CharField('Teléfono usuario', max_length=15,unique=False, null=False)
    u_genero = models.CharField('Genero usuario', max_length=1,unique=False, null=True)
    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'u_username'