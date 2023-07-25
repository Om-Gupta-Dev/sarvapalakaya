from django import forms
from phonenumber_field.formfields import PhoneNumberField

from main.models import *


class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ('name', 'phone', 'email', 'query')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'value': '+91'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'query': forms.Textarea(attrs={'class': 'form-control'}), }
