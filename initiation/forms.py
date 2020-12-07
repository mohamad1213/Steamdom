from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput
from . import models

class SchoolForm(ModelForm):
    class Meta :
        model = models.Schools
        exclude=[]

class TeacherForm(ModelForm):
    class Meta :
        model = models.Teachers
        exclude=[]
        widgets = {
            'birth_date': DatePickerInput(format='%Y-%m-%d').start_of('event days'),
        }
