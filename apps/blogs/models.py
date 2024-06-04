from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image_for_blogs = models.ImageField(
        upload_to='blogs/',
        verbose_name="Фото",
    )
    creation_date = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата создания"
    )
    def __str__(self):
        return self.title

