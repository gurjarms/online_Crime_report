from django.shortcuts import render, redirect
from django.views.generic import *
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Feedback_table, Fir, User
from django import forms
from .forms import Feedback_Form
from django.contrib.admin import widgets


# Create your views here.


def home(req):
    if req.session.get('MobileNO'):
        MobileNo = req.session.get('MobileNO')
    return render(req, 'home.html')


class criminal_list(TemplateView):
    template_name = 'top_10_criminals.html'


class criminal(TemplateView):
    template_name = 'list_of_criminals.html'


def contact(req):
    if req.method == "POST":
        form = Feedback_Form(req.POST)
        if form.is_valid():
            form.save()
            return redirect(contact)

    form = Feedback_Form()
    return render(req, 'contactus.html', {'form': form})


class Firview(ListView):
    model = Fir
    template_name = 'User/viewfir.html'
    ordering = ['-date_posted']


class FIR(CreateView, LoginRequiredMixin):
    model = Fir
    fields = [
        'Tehsil',
        'Police_station',
        'Criminal_address',
        'Criminal_name',
        'Criminal_mobile_No',
        'anonymous',
        'Name',
        'Permanent_address',
        'Mobile_NO',
        'place_of_crime',
        'Date',
        'Time',
        'TitleOfCrime',
        'content',
    ]
    success_url = "profile"
    template_name = 'User/FIR.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def DeleteProfile(req, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect(home)


def page_not_found(req):

    return render(req, '404.html')


def password_reset(req):

    return render(req, 'password_reset.html')
