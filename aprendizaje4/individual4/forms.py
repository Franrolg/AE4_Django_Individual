from django import forms

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