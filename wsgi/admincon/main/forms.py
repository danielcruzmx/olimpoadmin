__author__ = 'daniel_cruz'

from django import forms
from models import Condominio

class CondominioForm(forms.Form):
    condominios = forms.ModelChoiceField(queryset=Condominio.objects.all())