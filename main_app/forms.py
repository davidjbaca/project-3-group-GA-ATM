from django.forms import ModelForm
from .models import Revenue, CashInput

class RevenueForm(ModelForm):
  class Meta:
    model = Revenue
    fields = ['date', 'amount']


class CashInputForm(ModelForm):
  class Meta:
    model = CashInput
    fields = ['date', 'amount']