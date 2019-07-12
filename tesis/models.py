from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    rol = models.CharField(max_length=255, blank=False, null=False)
    REQUIRED_FIELDS = ['rol', 'email']

    class Meta:
        db_table = 'usuario'


class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Escuela(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'escuela'


class PalabraClave(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'palabraclave'


class Evaluador(Persona):
    cedula = models.IntegerField(unique=True)
    es_tutor = models.BooleanField(default=False)

    class Meta:
        db_table = 'evaluador'


class Autor(Persona):
    class Meta:
        db_table = 'autor'


class Tesis(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    palabasclave = models.ManyToManyField(
        PalabraClave)
    evaluadores = models.ManyToManyField(
        Evaluador, related_name='evaluadores')
    tutor = models.ForeignKey(
        Evaluador, on_delete=models.CASCADE, related_name='tutor')

    class Meta:
        db_table = 'tg'


class Audit(models.Model):
    fecha = models.DateTimeField('date created', auto_now_add=True)
    userCreador = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name='userCreador')
    userCreado = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name='userCreado')
    tesis = models.ForeignKey(Tesis, on_delete=models.CASCADE)

    class Meta:
        db_table = 'audit'
