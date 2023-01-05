from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Atm

from django.http import HttpResponse

# Create your views here.

# Home
def home(request):
    return render(request, 'home.html')

# About
def about(request):
    return render(request, 'about.html')

class AtmCreate(LoginRequiredMixin, CreateView):
    model = Atm

    fields = ['Location', 'Address', 'Business Fee', 'Surcharge']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def signup(request):
  error_message = ''
  if request.method == 'POST':
   
    form = UserCreationForm(request.POST)
    if form.is_valid():
      
      user = form.save()
      
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


@login_required
def atms_index(request): 
    atms = Atm.objects.filter(user=request.user)
    return render(request, 'atms/index.html', {'atms': atms})

@login_required
def atms_detail(request, atm_id):

  atm = Atm.objects.get(id=atm_id)
 
  return render(request, 'atms/detail.html', {'atm': atm})
