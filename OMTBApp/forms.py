from django import forms 
from OMTBApp.models import Movie,Customer,Shows

#here We Creating From for Out Model
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields="__all__"
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
class ShowsForm(forms.ModelForm):
    class Meta:
        model=Shows
        fields='__all__'
