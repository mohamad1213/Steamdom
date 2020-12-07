from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms
from . import models

class InternationalForm(ModelForm):
    class Meta :
        model = models.International
        exclude=[]
class NationalForm(ModelForm):
    class Meta :
        model = models.National
        exclude=[]
class LocalForm(ModelForm):
    class Meta :
        model = models.Local
        exclude=[]
