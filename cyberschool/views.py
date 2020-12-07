from django.shortcuts import render, redirect
from . import models, forms
# Create your views here.
def index(req):
    return render(req, 'cyberschool/index.html')
