from django import forms
from .models import Autor

class Autoform(forms.Form):
    nombre = forms.CharField(max_length=60, label='Nombre del autor:')
    edad = forms.IntegerField(max_value=120, required=False)
    email = forms.EmailField(max_length=50)
    
class AutorModelform(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'edad', 'email']
