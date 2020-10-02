from django import forms
from .models import Scan


# class ScanForm(forms.Form):
#     code = forms.CharField(max_length=150, label='Код', widget=forms.TextInput(attrs={"class": "form-control"}))


class ScanForm(forms.ModelForm):
    class Meta:
        model = Scan
        #fields = '__all__'
        fields = ['code']
        widgets = {
            'code': forms.TextInput(attrs={"class": "form-control", 'autofocus': 'True'})
        }

# 'autofocus': 'True'