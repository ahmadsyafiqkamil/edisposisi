#  Copyright (c) 2019.
#  Ahmad Syafiq Kamil

from . import views
from django.urls import path, include

app_name = 'dokumen'
urlpatterns = [
	path('dashboard', views.dashboard.as_view(), name='dashboard'),
	path('buat-dokumen', views.BuatDokumen.as_view(), name='buat-dokumen'),
	
	path('edit-dokumen/<slug:slug>', views.EditDokumen.as_view(), name='edit-dokumen'),
	path('hapus-dokumen/<slug:slug>', views.HapusSuratDinas.as_view(), name='hapus-dokumen'),
	path('laporan-dokumen/', views.Laporan.as_view(), name='laporan-dokumen'),
	path('batal-dokumen', views.BatalDokumen.as_view(), name='batal-dokumen'),
	path('baca-dokumen', views.BacaDokumen.as_view(), name='baca-dokumen'),
	path('detail-dokumen/<slug:slug>', views.DetailDokumen.as_view(), name='detail-dokumen'),
	
	

]
