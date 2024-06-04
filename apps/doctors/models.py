from django.db import models
from django.utils import timezone

from apps.categories.models import Category


class Doctor(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Имя"
    )
    lastname = models.CharField(
        max_length=30,
        verbose_name="Фамилия"
    )
    age = models.PositiveSmallIntegerField(
        verbose_name="Возраст"
    )
    choosing_a_specialization = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Выберите специализацию",
    )
    experience = models.PositiveSmallIntegerField(
        verbose_name="Опыт работы"
    )
    image_for_doctor = models.ImageField(
        upload_to="doctors_media/",
        verbose_name="Фото",
    )
    creation_date = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата создания"
    )

    class Meta:
        verbose_name = "Доктор "
        verbose_name_plural = "Докторы"

    def __str__(self):
        return self.name

