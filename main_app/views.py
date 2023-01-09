from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Atm, Revenue, CashInput
from .forms import RevenueForm, CashInputForm

from django.http import HttpResponseRedirect

# Create your views here.

# Home


def home(request):
    return render(request, 'home.html')

# About


def about(request):
    return render(request, 'about.html')


class AtmCreate(LoginRequiredMixin, CreateView):
    model = Atm

    fields = ['name', 'location_type', 'address', 'business_fee', 'surcharge']
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AtmUpdate(LoginRequiredMixin, UpdateView):
    model = Atm
    fields = ['location', 'address', 'business_fee', 'surcharge']


class AtmDelete(LoginRequiredMixin, DeleteView):
    model = Atm
    success_url = '/atms/'


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


# The ability to show only the user's ATMs as this is sensitive financial data.
@login_required
def atms_index(request):
    atms = Atm.objects.filter(user=request.user)
    return render(request, 'atms/index.html', {'atms': atms})


@login_required
def atms_detail(request, atm_id):

    atm = Atm.objects.get(id=atm_id)

    cashinput_form = CashInputForm()
    revenue_form = RevenueForm()

    return render(request, 'atms/detail.html', {'atm': atm, 'revenue_form': revenue_form, 'cashinput_form': cashinput_form})


# REVENUE STUFF

def add_revenue(request, atm_id):
    form = RevenueForm(request.POST)
    # validdate form
    if form.is_valid():
        # don't save the form to the db until it
        # has the atm_id assigned
        new_revenue = form.save(commit=False)
        new_revenue.atm_id = atm_id
        new_revenue.save()
    return redirect('detail', atm_id=atm_id)

# DELETE REVENUE


class DeleteRevenue(LoginRequiredMixin, DeleteView):
    model = Revenue

    def get_success_url(self):
        atm = self.object.atm
        return reverse_lazy('detail', kwargs={'atm_id': atm.id})

    # success_url = get_absolute_url
    # def get_success_url(request, atm_id):
    #     return HttpResponseRedirect(reverse('/atms/', kwargs={atm_id:atm_id}))


# CASH INPUT STUFF
def add_cashinput(request, atm_id):
    form = CashInputForm(request.POST)
    # validdate form
    if form.is_valid():
        # don't save the form to the db until it
        # has the atm_id assigned
        new_cashinput = form.save(commit=False)
        new_cashinput.atm_id = atm_id
        new_cashinput.save()
    return redirect('detail', atm_id=atm_id)


class DeleteCashinput(LoginRequiredMixin, DeleteView):
    model = CashInput
    
    def get_success_url(self):
        atm = self.object.atm
        return reverse_lazy('detail', kwargs={'atm_id': atm.id})
