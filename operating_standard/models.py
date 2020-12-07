from django.db import models
from django.db import models

# Create your models here.
class National(models.Model):
   COUNTRY_NATIONAL = (
      ('RI', 'Indonesia'),
   )
   country_of_origin_national = models.CharField(max_length=3, choices=COUNTRY_NATIONAL, default='')
   title_national = models.CharField(max_length=200, unique=True)
   year_of_curricullum_national = models.CharField(max_length=10)
   subject_national = models.CharField(max_length=100)
   LEVEL_NATIONAL = (
      ('01', 'SD1'),
      ('02', 'SD2'),
      ('03', 'SD3'),
      ('04', 'SD4'),
      ('05', 'SD5'),
      ('06', 'SD6'),
      ('07', 'SMP1'),
      ('08', 'SMP2'),
      ('09', 'SMP3'),
      ('10', 'SMA1'),
      ('11', 'SMA2'),
      ('12', 'SMA3'),
   )
   level_national = models.CharField(max_length=3, choices=LEVEL_NATIONAL, default='')
   KI_NATIONAL = (
      ('1', 'Sikap Spiritual'),
      ('2', 'Sikap Sosial'),
      ('3', 'Pengetahuan'),
      ('4', 'Keterampilan'),
   )
   kompetensi_inti_national = models.CharField(max_length=1, choices=KI_NATIONAL, default='')
   kompetensi_dasar_national = models.IntegerField()
   content_national = models.TextField(max_length=8000)

class International(models.Model):
   COUNTRY_INTERNATIONAL = (
      ('USA', 'America'),
      ('AUS', 'Australia'),
   )
   country_of_origin_international = models.CharField(max_length=4, choices=COUNTRY_INTERNATIONAL)
   title_international = models.CharField(max_length=200, unique=True)
   year_of_curriculum_international = models.CharField(max_length=10)
   subject_international = models.CharField(max_length=100)
   LEVEL_INTERNATIONAL = (
      ('01', 'SD1'),
      ('02', 'SD2'),
      ('03', 'SD3'),
      ('04', 'SD4'),
      ('05', 'SD5'),
      ('06', 'SD6'),
      ('07', 'SMP1'),
      ('08', 'SMP2'),
      ('09', 'SMP3'),
      ('10', 'SMA1'),
      ('11', 'SMA2'),
      ('12', 'SMA3'),
   )
   level_international = models.CharField(max_length=2, choices=LEVEL_INTERNATIONAL)
   content_international = models.TextField(max_length=8000)

class Local(models.Model):
   COUNTRY_LOCAL = (
      ('RI', 'Indonesia'),
      ('USA', 'America'),
      ('AUS', 'Australia'),
   )
   country_of_origin_local = models.CharField(max_length=4, choices=COUNTRY_LOCAL)
   title_local = models.CharField(max_length=200, unique=True)
   year_of_curricullum_local = models.CharField(max_length=10)
   subject_local = models.CharField(max_length=100)
   LEVEL_LOCAL = (
      ('01', 'SD1'),
      ('02', 'SD2'),
      ('03', 'SD3'),
      ('04', 'SD4'),
      ('05', 'SD5'),
      ('06', 'SD6'),
      ('07', 'SMP1'),
      ('08', 'SMP2'),
      ('09', 'SMP3'),
      ('10', 'SMA1'),
      ('11', 'SMA2'),
      ('12', 'SMA3'),
   )
   level_local = models.CharField(max_length=3, choices=LEVEL_LOCAL)
   content_local = models.TextField(max_length=8000)