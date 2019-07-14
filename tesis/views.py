from django.shortcuts import render, redirect
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
        # usuario = kargs.get('id', None)
        # if usuario == None:
        usuarios = Usuario.objects.all()
        form = UsuarioForm()
        return render(request, "usuarios.html", {'usuarios': usuarios, 'form': form})
        # else:
        #     usuario = Usuario.objects.filter(pk=usuario)
        #     form = UsuarioForm(usuario)
        #     return HttpResponse

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

    def put(self, request, *args, **kargs):
        form = UsuarioForm(request.PUT)
        print(kargs['id'])
        # if form.is_valid():
        #     user = Usuario.objects.filter(pk=kargs['id'])
        #     logging.info('El usuario se ha actualizado')


def delete_user(request, user_id):
    logging.info('Eliminando al usuario')
    user = Usuario.objects.filter(pk=user_id)
    user.delete()
    usuarios = Usuario.objects.all()
    form = UsuarioForm()
    return redirect('users')


def tesis(request):
    if request.method == "GET":
        tesis = Tesis.objects.all()
        autores = Autor.objects.all()
        return render(request, "tesis.html", {'tesis': tesis, 'autores': autores})
    elif request.method == "POST":
        formAutor = AutorForm(request.POST)
        if formAutor.is_valid():
            try:
                formAutor.save()
                return redirect('/tesis')
            except:
                pass
        else:
            formAutor = AutorForm()
            return render(request, 'tesis.html', {'formAutor': formAutor})    

# def create_autor(request):
#     if request.method == "POST":
#         form = AutorForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('/tesis')
#             except:
#                 pass
#         else:
#             form = AutorForm()
#             return render(request, 'tesis.html', {'form': form})
