from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Atm(models.Model):
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    business_fee = models.IntegerField()
    surcharge = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'atm_id': self.id})
