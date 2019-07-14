from django.shortcuts import render
from tesis.forms import UsuarioForm, AutorForm
from tesis.models import Usuario, Rol, Tesis, Autor, Evaluador
# Create your views here.


def users(request):
    if request.method == "GET":
        usuarios = Usuario.objects.all()
        roles = Rol.objects.all()
        form = UsuarioForm()
        return render(request, "usuarios.html", {'usuarios': usuarios, 'form': form, 'roles': roles})
    elif request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/users')
            except:
                pass
        else:
            form = UsuarioForm()
            return render(request, 'usuarios.html', {'form': form})

def tesis(request):
    if request.method == "GET":
        tesis = Tesis.objects.all()
        autores = Autor.objects.all()
        return render(request, "tesis.html", {'tesis': tesis, 'autores': autores})
    elif request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/tesis')
            except:
                pass
        else:
            form = AutorForm()
            return render(request, 'tesis.html', {'form': form})    

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
