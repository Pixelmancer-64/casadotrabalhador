from django import forms
from django.forms import ModelForm, ValidationError
from .models import *

class CadastroVagasForm(ModelForm):    
    class Meta:
        model = Vaga_Emprego
        exclude = ['dt_inclusao']