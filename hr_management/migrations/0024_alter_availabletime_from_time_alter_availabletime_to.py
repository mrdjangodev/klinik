# Generated by Django 4.2.6 on 2023-11-25 14:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_management', '0023_alter_availabletime_from_time_alter_availabletime_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletime',
            name='from_time',
            field=models.TimeField(default=datetime.time(19, 30, 48, 264995)),
        ),
        migrations.AlterField(
            model_name='availabletime',
            name='to',
            field=models.TimeField(default=datetime.time(19, 30, 48, 264995)),
        ),
    ]
