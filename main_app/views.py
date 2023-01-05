from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Atm

from django.http import HttpResponse

# Create your views here.

# Home
def home(request):
    return render(request, 'home.html')

# About
def about(request):
    return render(request, 'about.html')

class AtmCreate(CreateView):
    model = Atm

    fields = ['Location', 'Address', 'Business Fee', 'Surcharge']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)