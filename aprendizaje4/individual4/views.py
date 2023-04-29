from django.shortcuts import render
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

class FormularioUsuarioView(TemplateView):
    template_name = 'usuario.html'

    def get_context_data(self, **kwargs):
        context = super(FormularioUsuarioView, self).get_context_data(**kwargs)
        context['form'] = FormularioUsuario()
        return context

    def post(self, request, *args, **kwargs):
        form = FormularioUsuario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            print('Formulario de Usuario válido')
            print(nombre, apellido, email)
        return render(request, self.template_name, {'form': form})
    
def formulario_usuario(request):
    if request.method == "POST":
        form = RegistrarUsuarioForm(data=request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
        return render(request, 'usuario.html', {'respuesta': 'ok'})
    else:
        form = RegistrarUsuarioForm()
        return render(request, 'usuario.html', {'form': form})