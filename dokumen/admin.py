#  Copyright (c) 2019.
#  Ahmad Syafiq Kamil

from django.contrib import admin
from .models import Dokumen,Fungsi,JenisDokumen,Klasifikasi

# Register your models here.
admin.site.register(Klasifikasi)
admin.site.register(Fungsi)
admin.site.register(Dokumen)