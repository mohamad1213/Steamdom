# Generated by Django 2.2 on 2020-12-01 04:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiation', '0006_auto_20201201_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='birth_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]