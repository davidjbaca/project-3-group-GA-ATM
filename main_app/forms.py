from django.forms import ModelForm
from .models import Revenue, CashInput
from crispy_forms.helper import FormHelper
from django import forms

class RevenueForm(ModelForm):
  class Meta:
    model = Revenue
    fields = ['date', 'amount']
    widgets = {
        'date': forms.DateInput(attrs={'type': 'date'})
    }


class CashInputForm(ModelForm):
  class Meta:
    model = CashInput
    fields = ['date', 'amount']
    widgets = {
        'date': forms.DateInput(attrs={'type': 'date'})
    }