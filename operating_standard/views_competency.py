from django.shortcuts import render, redirect
from . import models, forms
from django.forms import modelformset_factory   
def index_nasional(req):

    national = models.National.objects.all()
    return render (req, 'competency/national/index.html',{
        'data': national, 
    })
def index_internasional(req):
    international = models.International.objects.all()

    return render (req, 'competency/international/index.html',{
        'data': international, 
    })

def index_local(req):
    local = models.Local.objects.all()

    return render (req, 'competency/local/index.html',{
        'data': local, 
    })


def input_nasional(req):
    form_input =  forms.NationalForm()

    if req.method == 'POST':
        form_input = forms.NationalForm(req.POST)
        if form_input.is_valid():
            form_input.save()
            return redirect ('/competency_nasional/')
    return render(req, 'competency/national/input.html',{
        'form_national': form_input,
    })

def input_international(req):
    form_input =  forms.InternationalForm()

    if req.POST:
        form_input = forms.InternationalForm(req.POST)
        if form_input.is_valid():
            form_input.save()
            return redirect ('/competency_international/')

    return render(req, 'competency/international/input.html',{
        'form_international': form_input,
    })

def input_local(req):
    form_input =  forms.LocalForm()

    if req.POST:
        form_input = forms.LocalForm(req.POST)
        if form_input.is_valid():
            form_input.save()
            return redirect ('/competency_local/')

    return render(req, 'competency/local/input.html',{
        'form_local': form_input,
    })


def detail_nasional(req, id):
    national = models.National.objects.filter(pk=id).first()    
    return render(req, 'competency/national/detail.html', {
        'data': national,
    })

def detail_international(req, id):
    international = models.International.objects.filter(pk=id).first()    
    return render(req, 'competency/international/detail.html', {
        'data': international,
    })

def detail_local(req, id):
    local = models.Local.objects.filter(pk=id).first()    
    return render(req, 'competency/local/detail.html', {
        'data': local,
    })


def delete_nasional(req, id):
    models.International.objects.filter(pk=id).delete()
    return redirect('/competency_international/')

# def update_nasional(req, id):
#     if req.POST:
#         form = models.National.objects.filter(pk=id).update(
#             country_of_origin_national=req.POST['country_of_origin_national'],
#             title_national=req.POST['title_national'],
#             npsn=req.POST['npsn'],
#             year_of_curricullum_national=req.POST['year_of_curricullum_national'],
#             subject_national=req.POST['subject_national'],
#             level_national=req.POST['level_national'],
#             kompetensi_inti_national=req.POST['kompetensi_inti_national'],
#             kompetensi_dasar_national=req.POST['kompetensi_dasar_national'],
#             content_national=req.POST['content_national'],
#         return redirect('/competency_nasional/')

#     national = models.National.objects.filter(pk=id).first()    
#     return render(req, 'competency/national/update.html', {
#         'data': national,
#     })
