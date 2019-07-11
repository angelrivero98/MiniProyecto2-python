from django.contrib import admin
from .models import Tesis, Usuario, Audit, Autor, Escuela, PalabraClave, Tutor

admin.site.register(Tesis)
admin.site.register(Usuario)
admin.site.register(Audit)
admin.site.register(Escuela)
admin.site.register(PalabraClave)
admin.site.register(Tutor)