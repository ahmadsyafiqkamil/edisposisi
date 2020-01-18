#  Copyright (c) 2020.
#  Ahmad Syafiq Kamil

from . import views
from django.urls import path, include

app_name = 'surat'
urlpatterns = [
    path('buat-surat', views.BuatSurat.as_view(), name='buat-surat'),

]
