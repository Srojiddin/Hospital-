from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.doctors.models import Doctor
from apps.categories.models import Category
from django.conf import settings


class Appointment (models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    fullname = models.CharField(max_length=100)
    your_phone_number = models.CharField(max_length=100)
    choosing_a_doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
    )
    choosing_a_disease = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    date_of_reservation = models.DateField(
        default=timezone.now,
    )

    def str(self):
        return f" {self.user} {self.date_of_reservation}"


class Contact(models.Model):
    ...