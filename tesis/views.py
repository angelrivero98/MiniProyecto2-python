from django.shortcuts import render
from tesis.forms import UsuarioForm, FormInicio
from tesis.models import Usuario, Rol, Tesis
from tesis.filters import SearchFilter
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = FormInicio(request.POST)
        if form.is_valid():
            return render(request, 'home.html', {'form': form})
    else:
        # form = FormInicio()
        # return render(request, 'home.html', {'form': form})
        filter = SearchFilter(request.GET, queryset=Tesis.objects.all())
        return render(request, 'home.html', {'filter': filter})


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
