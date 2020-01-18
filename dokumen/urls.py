#  Copyright (c) 2019.
#  Ahmad Syafiq Kamil

# from . import views
from .view import view_print, views, view_korfung
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
    path('detail-dokumen-keluar/<slug:slug>', views.DetailDokumenKeluar.as_view(), name='detail-dokumen-keluar'),

    # 	print
    path('print/<slug:slug>', view_print.PrintDokumen, name='print'),
    # path('print/<slug:slug>', view_print.print.as_view(),name = 'print')

    # 	korfung
    path('korfung/dashboard', view_korfung.Dashboard.as_view(), name='dashboard-korfung'),
    path('korfung/detail/<slug:slug>', view_korfung.DetailDokumen.as_view(), name='detail-korfung'),
    path('korfung/ttd', view_korfung.TandatanganDokumen.as_view(), name='ttd-korfung'),


]
