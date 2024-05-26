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
    # choosing_a_doctor = models.ForeignKey(
    #     Doctor,
    #     on_delete=models.CASCADE,
    #     verbose_name="vyberite vashego vracha",
    # )
    choosing_a_disease = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="vyberite vash diagnoz",
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    your_phone_number = models.CharField(max_length=100)
    your_email = models.EmailField(max_length=100)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    date_of_reservation = models.DateField(
        default=timezone.now,
    )

    def str(self):
        return f" {self.user} {self.check_in_date} {self.check_out_date} {self.date_of_reservation}"
