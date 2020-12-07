from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms
from . import models

class SchoolForm(ModelForm):
    class Meta :
        model = models.Schools
        exclude=[]
