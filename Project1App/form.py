from django.forms import ModelForm
from .models import Client  
from django import forms

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets ={
            'name': forms.TextInput(attrs ={'placeholder':'Name'}),
            'phone':forms.TextInput(attrs ={'placeholder':'Phone No.'}),
            'email':forms.TextInput(attrs ={'placeholder':'Email'}),            
            'web_description':forms.TextInput(attrs={'placeholder':'Website Description'})
        }

# def clean(self):
#     cd = self.cleaned_data

