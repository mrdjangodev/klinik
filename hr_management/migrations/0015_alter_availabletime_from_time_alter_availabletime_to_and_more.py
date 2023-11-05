# Generated by Django 4.2.6 on 2023-11-03 03:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr_management', '0014_alter_availabletime_from_time_alter_availabletime_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletime',
            name='from_time',
            field=models.TimeField(default=datetime.time(8, 53, 50, 664721)),
        ),
        migrations.AlterField(
            model_name='availabletime',
            name='to',
            field=models.TimeField(default=datetime.time(8, 53, 50, 664721)),
        ),
        migrations.CreateModel(
            name='Attandance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrived_at', models.DateTimeField(auto_now_add=True)),
                ('left_at', models.DateTimeField(auto_now=True)),
                ('in_available_day', models.BooleanField(default=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_management.staff')),
            ],
        ),
    ]