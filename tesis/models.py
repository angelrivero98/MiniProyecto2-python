from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

#Modelos que seran transformados a tablas de base de datos
class Rol(models.Model):
    nombre = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        db_table = 'rol'

    def __str__(self):
        return self.nombre


class Usuario(AbstractUser):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    REQUIRED_FIELDS = ['rol', 'email']

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return self.username


class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class Escuela(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'escuela'

    def __str__(self):
        return self.nombre


class PalabraClave(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'palabraclave'

    def __str__(self):
        return self.nombre


class Evaluador(Persona):
    cedula = models.IntegerField(unique=True)
    es_tutor = models.BooleanField(default=False)

    class Meta:
        db_table = 'evaluador'


class Autor(Persona):
    class Meta:
        db_table = 'autor'


class Tesis(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    fecha = models.DateField(default=timezone.now, null=False, blank=False)
    resumen = models.TextField(null=False, blank=False)
    calificacion = models.DecimalField(
        default=0.0, null=False, blank=False, max_digits=4, decimal_places=2)
    finalizada = models.BooleanField(default=False, null=False, blank=False)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    palabrasclave = models.ManyToManyField(
        PalabraClave)
    evaluadores = models.ManyToManyField(
        Evaluador, related_name='evaluadores')
    autores = models.ManyToManyField(Autor, related_name='autores')

    class Meta:
        db_table = 'tesis'

    def __str__(self):
        return self.nombre


class Audit(models.Model):
    fecha = models.DateTimeField('date created', auto_now_add=True)
    userCreador = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name='userCreador')
    userCreado = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name='userCreado', blank=True)
    tesis = models.ForeignKey(Tesis, on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = 'audit'
