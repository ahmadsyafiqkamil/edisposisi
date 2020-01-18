from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class BuatSurat(generic.TemplateView):
    template_name = 'surat/buat-surat.html'