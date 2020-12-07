# Generated by Django 2.2 on 2020-11-30 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schools',
            name='school_type',
            field=models.CharField(choices=[('Sekolah_Nasional', 'Sekolah Nasional'), ('Sekolah_Nasional_Plus', 'Sekolah Nasional_Plus'), ('Sekolah_Internasional', 'Sekolah Internasional'), ('Sekolah_Alam', 'Sekolah Alam'), ('Madrasah', 'Madrasah'), ('Sekolah_Rumah', 'Sekolah Rumah')], default='1', max_length=25),
        ),
    ]
