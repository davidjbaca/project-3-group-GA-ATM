from django.contrib import admin

# Import/register your models here:

from .models import Atm
admin.site.register(Atm)
