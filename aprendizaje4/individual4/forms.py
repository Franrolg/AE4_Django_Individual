from django import forms
from django.contrib.auth.models import User

class FormularioUsuario(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True, 
                             widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class':'form-control'}), 
                             error_messages={'required': 'El nombre es obligatorio', 
                                             'max_length': 'El nombre no puede tener más de 50 caracteres'})
    apellido = forms.CharField(label="Apellido", max_length=50, required=True, 
                             widget=forms.TextInput(attrs={'placeholder': 'Apellido', 'class':'form-control'}), 
                             error_messages={'required': 'El apellido es obligatorio', 
                                             'max_length': 'El apellido no puede tener más de 50 caracteres'})
    email = forms.EmailField(label='Email', max_length=100, required=True, 
                             widget=forms.TextInput(attrs={'placeholder': 'Email', 'class':'form-control'}), 
                             error_messages={'required': 'El email es obligatorio', 
                                             'max_length': 'El email no puede tener más de 100 caracteres'})

class RegistrarUsuarioForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

        labels = {'username': 'Usuario', 'first_name': 'Nombre', 'last_name': 'Apellido', 'email': 'Correo Electrónico', 'password': 'Contraseña'}

        widgets = {'username': forms.TextInput(attrs={'placeholder': 'Usuario', 'class':'form-control'}),
                  'first_name': forms.TextInput(attrs={'placeholder': 'Nombre', 'class':'form-control'}),
                  'last_name': forms.TextInput(attrs={'placeholder': 'Apellido', 'class':'form-control'}),
                  'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class':'form-control'}),
                  'password': forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class':'form-control'})
                  }
        
        help_texts = {
            'username': None
        }