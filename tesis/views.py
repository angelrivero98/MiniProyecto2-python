from django.shortcuts import render, redirect
from django.views import View
from tesis.models import Usuario, Tesis, Autor, Evaluador, Audit
from tesis.forms import UsuarioForm, FormInicio, AutorForm
from tesis.filters import SearchFilter
import logging
import datetime
# Create your views here.


def create_user(request):
    if request.method == "GET":
        form = UsuarioForm()
        return render(request, "crear_usuario.html", {'form': form})
    else:
        logging.info('Creando usuario')
        data = request.POST.copy()
        data['date_joined'] = datetime.datetime.now()
        form = UsuarioForm(data)
        if form.is_valid():
            try:
                logging.info('El usuario fue creado')
                form.save()
                usuarios = Usuario.objects.all()
                if request.user.is_authenticated:
                    audit = Audit(fecha=datetime.datetime.now(),userCreador=request.user, userCreado=form.instance)
                    audit.save()
                return render(request, "usuarios.html", {'usuarios': usuarios})
            except:
                logging.error('Error guardando el usuario.')
                pass
        else:
            logging.error(
                'Error creando el usuario. El formulario no es válido' + str(request.POST))
            return render(request, 'crear_usuario.html', {'form': form})


def update_user(request, user_id):
    users = Usuario.objects.filter(pk=user_id)
    user = users[0]
    if request.method == "GET":
        form = UsuarioForm()
        form.fields['username'].initial = user.username
        form.fields['email'].initial = user.email
        form.fields['rol'].initial = user.rol
        return render(request, "crear_usuario.html", {'form': form})
    else:
        logging.info('Actualizando usuario')
        data = request.POST.copy()
        data['date_joined'] = datetime.datetime.now()
        form = UsuarioForm(data)
        if form.is_valid():
            try:
                user.username = form.cleaned_data['username']
                if form.cleaned_data['password']:
                    user.password = form.cleaned_data['password']
                user.email = form.cleaned_data['email']
                user.rol = form.cleaned_data['rol']
                user.save()
                logging.info('El usuario fue actualizado')
                usuarios = Usuario.objects.all()
                return render(request, "usuarios.html", {'usuarios': usuarios})
            except:
                logging.error('Error guardando el usuario.')
                pass
        else:
            logging.error(
                'Error creando el usuario. El formulario no es válido' + str(request.POST))
            return render(request, 'crear_usuario.html', {'form': form})


def get_users(request):
    usuarios = Usuario.objects.all()
    return render(request, "usuarios.html", {'usuarios': usuarios})


def delete_user(request, user_id):
    logging.info('Eliminando al usuario')
    user = Usuario.objects.filter(pk=user_id)
    user.delete()
    usuarios = Usuario.objects.all()
    form = UsuarioForm()
    return redirect('users')

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


