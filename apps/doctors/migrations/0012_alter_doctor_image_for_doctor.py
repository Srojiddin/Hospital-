# Generated by Django 5.0.6 on 2024-05-24 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0011_remove_doctor_specialization_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image_for_doctor',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Фото'),
        ),
    ]