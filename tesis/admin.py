from django.contrib import admin
from .models import Tesis, Usuario, Audit, Autor, Escuela, PalabraClave, Evaluador, Rol
#Aqui registrmaos los modelos que queremos ver en el panel administrador de django
admin.site.register(Tesis)
admin.site.register(Usuario)
admin.site.register(Audit)
admin.site.register(Escuela)
admin.site.register(PalabraClave)
admin.site.register(Evaluador)
admin.site.register(Rol)
