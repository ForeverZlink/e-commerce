import imp
from django import forms

class New_User_Form(forms.Form):
    name = forms.CharField(max_length=255, unique=True, blank=False, null=False)
    date_of_born = forms.DateField(null=False,blank=False)
    email       = forms.EmailField()
    profision =  forms.CharField(max_length=255, unique=False,blank=False)

    