from django.contrib import admin

# Import/register your models here:
# Model 1 is Atm, Model 2 is Revenue.
from .models import Atm, Revenue
admin.site.register(Atm)
admin.site.register(Revenue)
