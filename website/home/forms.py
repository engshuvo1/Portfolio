from django import forms
from .models import *

class Contactforms(forms.ModelForm):
    class Meta:
        model = Contact
        # fields = ['name','email','message']
        fields = '__all__'