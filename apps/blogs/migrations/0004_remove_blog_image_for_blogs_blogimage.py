# Generated by Django 5.0.6 on 2024-06-04 23:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_blog_image_for_blogs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image_for_blogs',
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blogs/')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_images', to='blogs.blog')),
            ],
        ),
    ]
