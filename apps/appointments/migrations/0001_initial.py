# Generated by Django 5.0.6 on 2024-06-07 14:22

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('your_phone_number', models.CharField(max_length=100)),
                ('date_of_reservation', models.DateField(default=django.utils.timezone.now)),
                ('choosing_a_disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category', verbose_name='vyberite vash diagnoz')),
                ('choosing_a_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor', verbose_name='vyberite vashego vracha')),
            ],
        ),
    ]
