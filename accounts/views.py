#  Copyright (c) 2019.
#  Ahmad Syafiq Kamil

from django.shortcuts import render,redirect
from django.views import generic
from django.contrib import auth
from django.http import Http404
from django.views import generic
from django.urls import reverse_lazy
from .models import User,ProfileUser
from .form import profileForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

# login function untuk view login
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(email=request.POST['email'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            # request.session['FULLNAME'] = user.get_full_name()
            request.session['USERNAME'] = user.get_username()
            request.session['ID_USER'] = user.get_id_user()
            # request.session['FOTO'] = user.get_foto()
            if user.is_admin:
                return redirect('dokumen:dashboard')
            elif user.is_staff or user.is_staff_dokumen:
                request.session['KODE_FUNGSI'] =ProfileUser.objects.values_list("fungsi", flat=True).get(user=user.pk)
                return redirect('dokumen:dashboard')
            else:
                raise Http404("halaman tidak ada")
        else:
            return render(request,'account/login.html',{'error':'cek username dan password anda'})
    else:
        return render(request,'account/login.html')

# register function untuk view register
def register(request):
    if request.method == 'POST':
        if request.POST['ps1'] == request.POST['ps2']:
            try:
                user = User.objects.get(email=request.POST['email'])
                return render(request,'account/register.html',{'error':'email sudah dipakai'})
            except User.DoesNotExist:
                user = User.objects.create_user(email=request.POST['email'],password=request.POST['ps1'],user_name=request.POST['username'])
                auth.login(request,user)
                return redirect('accounts:login')
        else:
            return render(request,'account/register.html',{'errorps':'password tidak sama'})
    else:
        return render(request,'account/register.html')

def logout(request):
    # if request.method == 'POST':
    auth.logout(request)
    return redirect('accounts:login')

class Profile(generic.edit.CreateView):
    model = ProfileUser
    form_class = profileForm
    template_name = 'account/profile.html'
    
    # def get_form_kwargs(self):
    #     kwargs = super(Profile, self).get_form_kwargs()
    #     kwargs.update({'user':self.request.user})
    #     return kwargs
    

        