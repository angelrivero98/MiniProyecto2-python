from django.shortcuts import render, redirect
from django.views import View
from tesis.models import Usuario, Tesis, Autor, Evaluador, Audit
from tesis.forms import UsuarioForm, AutorForm, TesisForm
import logging
import datetime
# Create your views here.

# Esta funcion es para la creacion de usuarios donde se valida el formulario de usuario


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
                user = form.save()
                password = form.cleaned_data['password']
                user.set_password(password)
                user.is_staff = True
                user.is_active = True
                user.is_superuser = True
                user.save()
                usuarios = Usuario.objects.all()
                return render(request, "usuarios.html", {'usuarios': usuarios})
            except:
                logging.error('Error guardando el usuario.')
                pass
        else:
            logging.error(
                'Error creando el usuario. El formulario no es válido' + str(request.POST))
            return render(request, 'crear_usuario.html', {'form': form})

#Funcion para editar el usuario dependiendo del id
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
                user.update(username=form.cleaned_data['username'])
                if form.cleaned_data['password']:
                    user.set_password(form.cleaned_data['password'])
                user.update(email=form.cleaned_data['email'])
                user.update(rol=form.cleaned_data['rol'])
                logging.info('El usuario fue actualizado')
                usuarios = Usuario.objects.all()
                return render(request, "usuarios.html", {'usuarios': usuarios})
            except:
                logging.error('Error guardando el usuario.')
                return render(request, 'crear_usuario.html', {'form': form})
        else:
            logging.error(
                'Error creando el usuario. El formulario no es válido' + str(request.POST))
            return render(request, 'crear_usuario.html', {'form': form})

#Funcion que permite obtener el listado de los usuarios de la base de datos
def get_users(request):
    usuarios = Usuario.objects.all()
    return render(request, "usuarios.html", {'usuarios': usuarios})

#Funcion que permite eliminar el usuario segun el id
def delete_user(request, user_id):
    logging.info('Eliminando al usuario')
    user = Usuario.objects.filter(pk=user_id)
    user.delete()
    return redirect('users')

# Esta funcion es para la creacion de tesis donde se valida el formulario de tesis


def create_tesis(request):
    if request.method == 'GET':
        form = TesisForm()
        print('Obtener formulario')
        logging.info(form)
        return render(request, 'crear_tesis.html', {'form': form})
    else:
        logging.info('Creando tesis')
        form = TesisForm(request.POST)
        if form.is_valid():
            try:
                logging.info('La tesis fue creada')
                form.save()
                tesis = Tesis.objects.all()
                return render(request, "tesis.html", {'tesis': tesis})
            except Exception as e:
                print(e)
                logging.error('Error guardando la tesis.')
                return render(request, 'crear_tesis.html', {'form': form})
        else:
            logging.error(
                'Error creando la tesis. El formulario no es válido' + str(request.POST))
            return render(request, 'crear_tesis.html', {'form': form})

#Vista donde se muesta la lista de tesis, donde definimos sus metodos para el get y el post
class TesisView(View):

    def get(self, request, *args, **kargs):
        tesis = Tesis.objects.all()
        return render(request, "tesis.html", {'tesis': tesis})

    def post(self, request, *args, **kargs):
        tesis = Tesis.objects.all()
        return render(request, "tesis.html", {'tesis': tesis})

#Funcion que permite crear un autor segun el formulario indicasdo
def postAutor(request):
    if request.method == "POST":
        formAutor = AutorForm(request.POST)
        if formAutor.is_valid():
            try:
                formAutor.save()
                return redirect('tesis')
            except:
                return render(request, 'createAutor.html', {'formAutor': formAutor})
                pass
    formAutor = AutorForm()
    return render(request, 'createAutor.html', {'formAutor': formAutor})
