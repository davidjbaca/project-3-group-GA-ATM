from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# GEOCODER MAPBOX
import geocoder

access_token = 'pk.eyJ1IjoiYXRtd29ya3MiLCJhIjoiY2xjcHE4Z2FxNGs0ODNxcDRyaWxybGNpcCJ9.D3CXUrooyNKlRV62OY6EIQ'



# Create your models here.


class Atm(models.Model):
    name = models.CharField(max_length=100)
    location_type = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    business_fee = models.IntegerField()
    surcharge = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'atm_id': self.id})


class Revenue(models.Model):
    date = models.DateField()
    amount = models.IntegerField()
    # yearly = models.IntegerField()

    atm = models.ForeignKey(Atm, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']



class CashInput(models.Model):
    date = models.DateField('Date Cash Added')
    amount = models.IntegerField()

    atm = models.ForeignKey(Atm, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    

# MAPBOX ADDRESS MODEEL
class Address(models.Model):

    # get relationship working and then try to get a form to work 
    address = models.CharField(max_length=100)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    # add geo coder converter to convert address to lon and lat

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=access_token)
        g = g.latlng
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)