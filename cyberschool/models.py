from django.db import models

# Create your models here.
class Schools(models.Model):
    school_name = models.CharField(max_length=100)
    nss = models.CharField(max_length=100)
    npsn = models.CharField(max_length=100)
    school_type_choice = [
        ("Sekolah_Nasional", "Sekolah_Nasional"),
        ("Sekolah_Nasional_Plus", "Sekolah_Nasional_Plus"),
        ("Sekolah_Internasional", "Sekolah_Internasional"),
        ("Sekolah_Alam", "Sekolah_Alam"),
        ("Madrasah", "Madrasah"),
        ("Sekolah_Rumah", "Sekolah_Rumah")
    ]
    school_type = models.CharField(max_length=25,
        choices = school_type_choice,
        default = '1')
    school_addres_street = models.CharField(max_length=100)
    school_addres_province = models.CharField(max_length=100)
    school_addres_city = models.CharField(max_length=100)
    school_addres_district = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    school_status = models.CharField(max_length=100)
    accreditation_score = models.CharField(max_length=100)