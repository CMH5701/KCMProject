from dataclasses import fields
from django import forms 
from .models import Cashbook

class CashbookForm(forms.ModelForm):
    class Meta:
        model = Cashbook
        fields = ['title' , 'content' ,'name']