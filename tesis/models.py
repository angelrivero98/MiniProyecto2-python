from django.db import models

class Usuario(models.Model):
    user = models.CharField(max_length=255)
    psw = models.CharField(max_length=255)
    rol = models.CharField(max_length=255)

    class Meta:
        db_table = 'user'

class Escuela(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'escuela'

class PalabraClave(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'palabraclave'

class Tutor(models.Model):
    cedula = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)

    class Meta:
        db_table = 'tutor'

class Autor(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)

    class Meta:
        db_table = 'autor'

class Tesis(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    escuela = models.ForeignKey(Escuela,on_delete=models.CASCADE)
    palabraclave = models.ForeignKey(PalabraClave,on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor,on_delete=models.CASCADE)

    class Meta:
        db_table = 'tg'


class Audit(models.Model):
    fecha = models.DateTimeField('date created', auto_now_add=True)
    userCreador = models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name='userCreador')
    userCreado = models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name='userCreado')
    tesis = models.ForeignKey(Tesis,on_delete=models.CASCADE)

    class Meta:
        db_table = 'audit'