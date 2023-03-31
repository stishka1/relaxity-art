from django import forms
from .models import *
from django.core.exceptions import ValidationError

class ActivateCodeForm(forms.Form):
    code = forms.CharField(required=True, help_text='XXXX-XXX', widget=forms.TextInput(attrs={'class': 'form-control shadow border-0', 'style': 'width: 269px; height: 72px; border-radius: 40px; text-align: center!important; font-size: 1.2rem; font-weight: 700;', 'placeholder': 'XXXX-XXX', 'value': ''}))
    quantity = forms.IntegerField(min_value=0, widget=forms.TextInput(attrs={'class': 'visually-hidden', 'value': '0'}))
    
    def clean_quantity(self):
        t = Code.objects.get(code=self.cleaned_data['code'])
        if t.quantity >= 99 :
            raise ValidationError('Vous avez entré le code 3 fois! Pour toutes questions: info@relaxity-art.fr')
        return t.quantity
    def clean_code(self):
        try:
            t = Code.objects.get(code=self.cleaned_data['code'])
        except:
            raise ValidationError('Code introuvable! Pour toutes questions contacter par email: info@relaxity-art.fr')
        return t.code