from dataclasses import fields
from django import forms 
from .models import Cashbook

class CashbookForm(forms.ModelForm):
    class Meta:
        model = Cashbook
        fields = ['title' , 'content' ,'name' ,'email']

    def init(self, args, **kwargs):
        super(CashbookForm, self).init(args, **kwargs)
        self.fields['title'].required = False