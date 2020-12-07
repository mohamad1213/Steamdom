from django.shortcuts import render, redirect
from . import models, forms
from bootstrap_datepicker_plus import DatePickerInput

# from forms import SchoolForm,TeachersForm

def index(req):
    teacher = models.Teachers.objects.all()
    return render(req, 'teachers/index.html',{
        'data': teacher, 
    })
def input(req):
    form_input =  forms.TeacherForm()

    if req.POST:
        form_input = forms.TeacherForm(req.POST)
        if form_input.is_valid():
            form_input.save()
            return redirect ('/teachers/')

    return render(req, 'teachers/input.html',{
        'form_teacher': form_input,
    })

def detail(req, id):
    teacher = models.Teachers.objects.filter(pk=id).first()    
    return render(req, 'teachers/detail.html', {
        'data': teacher,
    })

def delete(req, id):
    models.Teachers.objects.filter(pk=id).delete()
    return redirect('/teachers/')

# def update(req, id):
#     if req.POST:
#         form = models.Teachers.objects.filter(pk=id).update(
#             school_name=req.POST['school_name'],
#             nss=req.POST['nss'],
#             npsn=req.POST['npsn'],
#             school_type=req.POST['school_type'],
#             school_address_street=req.POST['school_address_street'],
#             school_address_district=req.POST['school_address_district'],
#             school_address_city=req.POST['school_address_city'],
#             school_address_province=req.POST['school_address_province'],
#             telephone=req.POST['telephone'],
#             website=req.POST['website'],
#             email=req.POST['email'],
#             school_status=req.POST['school_status'],
#             acreditation_score=req.POST['acreditation_score'],
#         )
#         return redirect('/teachers/')

#     school = models.Teachers.objects.filter(pk=id).first()    
#     return render(req, 'teachers/update.html', {
#         'data': school,
#     })
