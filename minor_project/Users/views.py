from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm, UserVaryfyForm
from .models import Profile, User, UserMobileNo
from Crime_Report.models import Fir
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from random import *
from django.conf import settings
from django.core import mail
from django import forms


# Create your views here.

def send_otp(req):
    return render(req, 'User/send_otp.html')


def mailsending(req):
    otp = randrange(11111, 99999)
    email = req.POST.get('email', False)
    msg = 'Your OTP is {}'.format(otp)
    sending = mail.send_mail('varification code', msg, settings.EMAIL_HOST_USER, [ email], fail_silently=False)
    req.session['otp'] = otp
    req.session['email'] = email
    messages.success(req, f'OTP sent successfully')
    temp = True

    return render(req, 'User/send_otp.html', {'temp': temp})


def Varify(req):
    if req.POST:
        email = req.session.get('email', False)
        userotp = req.POST.get('userotp')
        otp = req.session.get('otp', False)
        if str(otp) == userotp:
            messages.success(req, f'now you can register')
            del req.session['otp']
            return redirect('register')
        else:
            messages.error(req, f' Wrong OTP please enter correct otp')

    return render(req, 'User/send_otp.html')


def register(req):
    if req.method == "POST":
        u_fm = UserRegisterForm(req.POST, instance=req.user.id)
        # if req.session['otp']:
        #     del req.session['otp']
        if u_fm.is_valid():
            MobileNo = u_fm.cleaned_data['Mobile_No']
            req.session['MobileNo'] = MobileNo
            username = req.POST['username']
            req.session['Username'] = username
            u_fm.save()
            return redirect('login')
        else:
            messages.error(req, f'Error in Sign in')

    form = UserRegisterForm()
    return render(req, 'User/register.html', {'form': form})


class profile(ListView):
    model = Fir
    name = 'mahi'
    template_name = 'User/profile.html'
    ordering = ['-date_posted']

    def get(self, request, *args, **kwargs):
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {'p_form': p_form}
        return render(request, 'User/profile.html', context)


def UploadImage(req):
    if req.method == 'POST':
        p_form = ProfileUpdateForm(
            req.POST, req.FILES, instance=req.user.profile)
        if p_form.is_valid():
            p_form.save()

            Pic = p_form.cleaned_data['image']
            pic = Profile(image=Pic)
            p_form.save()
            pic.save
            messages.success(req, f'Your Profile pic is updated!')
            return redirect('profile')


def UpdateProfile(req):
    if req.user.is_authenticated:
        currunt_user = User.objects.get(id=req.user.id)
        form = UserRegisterForm(req.POST or None, instance=currunt_user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(req, user)
            messages.success(req, f'Your account has been updated!')

            return redirect('profile')

        return render(req, 'User/UpdateProfile.html', {'u_form': form})


