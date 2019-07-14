from django.shortcuts import render
from django.views import View
from tesis.models import Usuario, Tesis, Autor, Evaluador
from tesis.forms import UsuarioForm, FormInicio, AutorForm
from tesis.filters import SearchFilter
import logging
import datetime
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = FormInicio(request.POST)
        if form.is_valid():
            return render(request, 'home.html', {'form': form})
    else:
        form = FormInicio()
        return render(request, 'home.html', {'form': form})


class UsersView(View):

    def get(self, request, *args, **kargs):
        usuarios = Usuario.objects.all()
        form = UsuarioForm()
        return render(request, "usuarios.html", {'usuarios': usuarios, 'form': form})

    def post(self, request, *args, **kargs):
        logging.info('Creando usuario')
        data = request.POST.copy()
        data['date_joined'] = datetime.datetime.now()
        form = UsuarioForm(data)
        if form.is_valid():
            try:
                logging.info('El usuario fue creado')
                form.save()
                usuarios = Usuario.objects.all()
                form = UsuarioForm()
                return render(request, "usuarios.html", {'usuarios': usuarios, 'form': form})
            except:
                logging.error('Error guardando el usuario.')
                pass
        else:
            logging.error(
                'Error creando el usuario. El formulario no es válido' + str(request.POST))
            return render(request, 'usuarios.html', {'form': form})
                  
class TesisView(View):

    
    def get(self, request, *args, **kargs):
        tesis = Tesis.objects.all()
        autores = Autor.objects.all()
        return render(request, "tesis.html", {'tesis': tesis, 'autores': autores})

    def post(self, request, *args, **kargs):
        tesis = Tesis.objects.all()
        autores = Autor.objects.all()
        return render(request, "tesis.html", {'tesis': tesis, 'autores': autores})     

def postAutor(request):
    if request.method == "POST":
        formAutor = AutorForm(request.POST)
        if formAutor.is_valid():
            try:
                formAutor.save()
                return redirect('tesis')
            except:
                pass
    formAutor = AutorForm()
    return render(request, 'createAutor.html', {'formAutor': formAutor})        


