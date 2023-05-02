from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.models import User
from .forms import FormularioUsuario, RegistrarUsuarioForm

# Create your views here.

class IndexView(CreateView):
    model = User
    template_name = "index.html"
    fields = ['first_name', 'last_name', 'email']

def index(request):
    return render(request, 'index.html')

def lista_usuarios(request):
    lista_usuarios = User.objects.all()
    return render(request, 'lista_usuario.html', {'usuarios': lista_usuarios})
    
def formulario_usuario(request):
    if request.method == "POST":
        form = RegistrarUsuarioForm(data=request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
        return redirect('lista usuarios')
    else:
        form = RegistrarUsuarioForm()
        return render(request, 'usuario.html', {'form': form})