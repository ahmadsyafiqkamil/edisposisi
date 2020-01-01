#  Copyright (c) 2019.
#  Ahmad Syafiq Kamil

from django.db import models
from accounts.models import User
from django.utils.text import slugify
from django.urls import reverse
from .validators import validate_file_extension




# Create your models here.

# class fungsi(models.Model):
#     nama = models.CharField(max_length=255, blank=True, verbose_name="Nama Fungsi")
#     koordinator = models.CharField(max_length=255, blank=True, verbose_name="Koordinator Fungsi")
class Klasifikasi(models.Model):
    kode = models.CharField(max_length=5, verbose_name='Kode Klasifikasi')
    nama_klasifikasi = models.CharField(max_length=100, verbose_name='Nama Klasifikasi')

    class Meta:
        db_table = 'tbl_klasifikasi'

    def __str__(self):
        return "{} - {}".format(self.kode,self.nama_klasifikasi)

    # def get_kode(self):
    #     return self.kode

class Fungsi(models.Model):
    kode = models.CharField(max_length=10, verbose_name='Kode Fungsi')
    fungsi = models.CharField(max_length=100, verbose_name='Fungsi / Bidang Teknis')
    koordinator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='koordinator',
                                    verbose_name='Koordinator Fungsi')

    class Meta:
        db_table = 'tbl_fungsi'

    def __str__(self):
        return self.fungsi


class JenisDokumen(models.Model):
    kode = models.CharField(max_length=10, verbose_name='Kode Dokumen')
    jenis_dokumen = models.CharField(max_length=255, verbose_name='Jenis Dokumen')

    class Meta:
        db_table = 'tbl_jenis_dokumen'

    def __str__(self):
        return self.jenis_dokumen


class Dokumen(models.Model):
    pilihan_status = [
        ('0','BELUM DIPROSES'),
        ('1','PROSES'),
        ('2','DISPOSISI'),
        ('3','BATAL'),

    ]
    slug = models.SlugField(unique=True)
    nomor_surat_lengkap = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nomor Surat Lengkap')
    nomor_surat = models.IntegerField(verbose_name='Nomor Surat')
    tanggal = models.DateField(verbose_name='Tanggal')
    pejabat_penandatangan = models.CharField(max_length=255, verbose_name='Pembuat Dokumen')
    tujuan = models.ManyToManyField(Fungsi, through='TujuanDokumen',through_fields=('dokumen', 'fungsi'), related_name='tujuan_dokumen')
    # tujuan = models.ManyToManyField(Fungsi, verbose_name='Tujuan Dokumen')
    perihal = models.TextField(blank=True, null=True, verbose_name='Perihal')
    fungsi = models.ForeignKey(Fungsi, on_delete=models.CASCADE, verbose_name='Fungsi',related_name='fungsi_pengirim')
    jenis_dokumen = models.ForeignKey(JenisDokumen, on_delete=models.CASCADE, verbose_name='Jenis Dokumen',related_name='jenis')
    klasifikasi = models.ForeignKey(Klasifikasi, on_delete=models.CASCADE, verbose_name='Tujuan Dokumen',related_name='klasifikasi_dokumen')
    file_dokumen = models.FileField(upload_to='document/%Y-%m-%d/',validators=[validate_file_extension])
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,verbose_name='Pengirim', related_name='pengirim')
    tujuan_eksternal = models.TextField(blank=True,null=True, verbose_name='Tujuan Eksternal')
    status = models.CharField(max_length=10,choices=pilihan_status, default=0,null=True)
    
    def save(self, *args,**kwargs):
        self.slug = slugify(self.nomor_surat_lengkap)
        super(Dokumen,self).save(*args,**kwargs)

    class Meta:
        db_table ='tbl_dokumen'

    def __str__(self):
        return self.nomor_surat_lengkap
    
  

class TujuanDokumen(models.Model):
    # status
    # 0 = unread
    # 1 = readS
    dokumen = models.ForeignKey(Dokumen, on_delete=models.CASCADE)
    fungsi = models.ForeignKey(Fungsi, on_delete=models.CASCADE)
    status = models.IntegerField(verbose_name="Status",null=True,blank=True,default=0)
    class Meta:
        db_table = 'tbl_tujuan_dokumen'
    
    
