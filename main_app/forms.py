from django.forms import ModelForm
from .models import Revenue

class RevenueForm(ModelForm):
  class Meta:
    model = Revenue
    fields = ['date', 'amount']