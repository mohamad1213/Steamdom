from django.shortcuts import render, redirect
from . import models, forms
# from forms import SchoolForm,SchoolupdateForm

def index(req):
    schools = models.Schools.objects.all()
    return render(req, 'initiation/index.html',{
        'data': schools, 
    })
def input(req):
    form_input =  forms.SchoolForm()

    if req.POST:
        form_input = forms.SchoolForm(req.POST)
        if form_input.is_valid():
            form_input.save()
            return redirect ('/initiation/')

    return render(req, 'initiation/input.html',{
        'form': form_input,
    })

def detail(req, id):
    school = models.Schools.objects.filter(pk=id).first()    
    return render(req, 'initiation/detail.html', {
        'data': school,
    })

def delete(req, id):
    models.Schools.objects.filter(pk=id).delete()
    return redirect('/initiation/')

def update(req, id):
    if req.POST:
        form = models.Schools.objects.filter(pk=id).update(
            school_name=req.POST['school_name'],
            nss=req.POST['nss'],
            npsn=req.POST['npsn'],
            school_type=req.POST['school_type'],
            school_address_street=req.POST['school_address_street'],
            school_address_district=req.POST['school_address_district'],
            school_address_city=req.POST['school_address_city'],
            school_address_province=req.POST['school_address_province'],
            telephone=req.POST['telephone'],
            website=req.POST['website'],
            email=req.POST['email'],
            school_status=req.POST['school_status'],
            acreditation_score=req.POST['acreditation_score'],
        )
        return redirect('/initiation/')

    school = models.Schools.objects.filter(pk=id).first()    
    return render(req, 'initiation/update.html', {
        'data': school,
    })
