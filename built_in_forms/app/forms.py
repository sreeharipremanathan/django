from django import forms

class normal_form(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()