from django.forms import ModelForm
from .models import Revenue, CashInput
from bootstrap_datepicker_plus.widgets import DatePickerInput

class RevenueForm(ModelForm):
  class Meta:
    model = Revenue
    fields = ['date', 'amount']
    widgets = {
        'date': DatePickerInput()
    }


class CashInputForm(ModelForm):
  class Meta:
    model = CashInput
    fields = ['date', 'amount']
    widgets = {
        'date': DatePickerInput()
    }