from django.shortcuts import render
from tesis.forms import UsuarioForm
from tesis.models import Usuario
# Create your views here.


def users(request):
    if request.method == "GET":
        usuarios = Usuario.objects.all()
        form = UsuarioForm()
        return render(request, "usuarios.html", {'usuarios': usuarios, 'form': form})
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
