from . import views
from django.urls import path, include

app_name = 'dokumen'
urlpatterns = [
    path('dashboard',views.dashboard.as_view(), name='dashboard'),
    path('buat-dokumen',views.BuatDokumen.as_view(), name='buat-dokumen'),
    # path('buat-dokumen',views.BuatDokumen, name='buat-dokumen'),

#     laporan
    path('laporan-nota-dinas',views.LaporanNotaDinas.as_view(), name='laporan-nota-dinas'),
    path('laporan-nota-diplomatik',views.LaporanNotaDiplomatik.as_view(), name='laporan-nota-diplomatik'),

    path('laporan-surat-dinas',views.LaporanSuratDinas.as_view(), name='laporan-surat-dinas'),
    path('laporan-surat-perintah',views.LaporanSuratPerintah.as_view(), name='laporan-surat-perintah'),
    path('laporan-surat-perintah-kerja',views.LaporanSuratPerintahKerja.as_view(), name='laporan-surat-perintah-kerja'),
    path('hapus-spk/<slug:slug>',views.HapusSPK.as_view(), name='hapus-spk'),

    path('edit-dokumen/<slug:slug>',views.EditDokumen.as_view(), name='edit-dokumen'),
    path('hapus-dokumen/<slug:slug>',views.HapusSuratDinas.as_view(), name='hapus-dokumen'),
]

