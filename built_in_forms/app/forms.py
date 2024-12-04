from django import forms
from .models import user

class normal_form(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()

class model_form(forms.ModelForm):
    class Meta:
        model=user
        fields='__all__'
        # feilds=['name','age','place']