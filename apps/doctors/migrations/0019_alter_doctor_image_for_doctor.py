# Generated by Django 5.0.6 on 2024-05-25 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0018_alter_doctor_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image_for_doctor',
            field=models.ImageField(blank=True, null=True, upload_to='doctors_media/', verbose_name='Фото'),
        ),
    ]