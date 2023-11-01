# Generated by Django 4.2.6 on 2023-10-31 15:12

import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hr_management.validators


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_customuser_options'),
        ('departments', '0002_room_roomstuff'),
        ('hr_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorSpecialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='specializations/doctors/image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StaffSpecialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='specializations/staffs/image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='insurance_policy_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='insurance_provider',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(blank=True, upload_to='staffs/images/')),
                ('working', models.BooleanField(default=True)),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=25)),
                ('salary_currency', models.IntegerField(choices=[(0, 'UZS'), (1, 'USD'), (2, 'EUR')], default=0)),
                ('barcode_data', models.CharField(blank=True, max_length=100, unique=True)),
                ('barcode_file_path', models.CharField(blank=True, max_length=255, unique=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='departments.department')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hr_management.staffspecialization')),
            ],
            options={
                'abstract': False,
            },
            bases=('account.customuser',),
        ),
        migrations.CreateModel(
            name='AvailableTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thoursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default=1)),
                ('from_time', models.TimeField(default=datetime.time(20, 12, 22, 216810))),
                ('to', models.TimeField(default=datetime.time(20, 12, 22, 216810))),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_management.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('staff_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hr_management.staff')),
                ('position', models.IntegerField(choices=[(0, 'Junior'), (1, 'Senior'), (2, 'Consultant'), (3, 'Surgeon'), (4, 'Head Doctor')], default=0)),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hr_management.doctorspecialization')),
            ],
            options={
                'abstract': False,
            },
            bases=('hr_management.staff',),
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('_file', models.FileField(upload_to='achievements/docs/', validators=[hr_management.validators.validate_file_type, hr_management.validators.validate_file_size])),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_management.doctor')),
            ],
        ),
    ]