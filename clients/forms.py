from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm

from clients.models import Client
class ClientForm(ModelForm):
    class Meta:
        model=Client
        fields =['email',]