from django.db import models
from datetime import datetime

# Create your models here.
class Schools(models.Model):
    school_name = models.CharField(max_length=100)
    nss = models.CharField(max_length=100)
    npsn = models.CharField(max_length=100)
    school_type_choice = [
        ("Sekolah Nasional", "Sekolah Nasional"),
        ("Sekolah Nasional Plus", "Sekolah Nasional Plus"),
        ("Sekolah Internasional", "Sekolah Internasional"),
        ("Sekolah Alam", "Sekolah Alam"),
        ("Madrasah", "Madrasah"),
        ("Sekolah Rumah", "Sekolah Rumah")
    ]
    school_type = models.CharField(max_length=25,
        choices = school_type_choice,
        default = '1')
    school_address_street = models.CharField(max_length=100)
    school_address_province = models.CharField(max_length=100)
    school_address_city = models.CharField(max_length=100)
    school_address_district = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    school_status = models.CharField(max_length=100)
    acreditation_score = models.CharField(max_length=100)

    def __str__(self):
		    return self.school_name

class Teachers(models.Model):
    # schools_name = models.CharField(max_length=100)
    nip = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    birth_place = models.CharField(max_length=100)
    birth_date = models.DateField(default=datetime.now)
    gender_choice = [
        ("L", "Laki-laki"),
        ("P", "Perempuan")
    ]
    gender = models.CharField(
        max_length = 25,
        choices = gender_choice,
        blank = True,
        null = True )
    status = models.CharField(max_length=100,)
    address = models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=100)
    golongan_choice = [
        ("1", "1A"), ("2", "1B"), ("3", "1C"), ("4", "1D"),
        ("5", "2A"), ("6", "2B"), ("7", "2C"), ("8", "2D"),
        ("9", "3A"), ("10", "3B"), ("11", "3C"), ("12", "3D"),
        ("13", "4A"), ("14", "4B"), ("15", "4C"), ("16", "4D")
    ]
    golongan = models.CharField(
        max_length = 50,
        choices = golongan_choice,
        blank = True,
        null = True )
    certificate_number = models.CharField(max_length=100)
    educational_qualifications = models.CharField(max_length=100)
    university = models.CharField(max_length=100)

# class Equipments(models.model):
#     jenis_ruangan_choice =[
#         ("Kepala Sekolah", "Kepala Sekolah"),
#         ("Wakil Kepala Sekolah", "Wakil Kepala Sekolah"),
#         ("Guru", "Guru"),
#         ("Perpustakaan", "Perpustakaan"),
#         ("Lab.IPA", "Lab.IPA"),
#         ("sekolah", "sekolah")
#         ("Gudang OR", "Gudang OR"),
#         ("Dapur", "Dapur"),
#         ("UKS", "UKS"),
#     ]
#     jenis_ruangan = models.CharField(max_length=50,
#         choices = jenis_ruangan_choice,
#         blank = True,
#         null = True )
#     jumlah = models.IntegerField(max_length=100)
#     ukuran = models.CharField(max_length=50)
#     kondisi_choice =[
#         ("baik", "Baik"),
#         ("rusak_ringan", "Rusak Ringan"),
#         ("rusak_sedang", "Rusak Sedang"),
#         ("rusak_berat", "Rusak Berat"),
#         ("rusak_total", "Rusak Total"),
#     ]
#     kondisi = models.CharField(max_length=50,
#         choices = kondisi_choice,
#         default = '1')