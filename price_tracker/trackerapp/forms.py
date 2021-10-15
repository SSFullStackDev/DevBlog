from django import forms
from .models import price_history

class DataForm(forms.ModelForm):
    class Meta:
        model = price_history
        fields =  ['title', 'data']
