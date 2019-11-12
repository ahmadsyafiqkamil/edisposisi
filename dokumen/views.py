from builtins import super

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from .form import DokumenForm
from django.urls import reverse_lazy
from .models import Dokumen, Fungsi, Klasifikasi, JenisDokumen
from django_select2.forms import Select2MultipleWidget
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View


# Create your views here.
@method_decorator(login_required, name='dispatch')
class dashboard(generic.TemplateView):
    template_name = 'dokumen/dashboard.html'


# @method_decorator(csrf_exempt,name='dispatch')
@method_decorator(login_required, name='dispatch')
class BuatDokumen(generic.edit.CreateView):
    # http_method_names = "post"
    template_name = 'dokumen/buat-dokumen.html'
    form_class = DokumenForm

    def form_valid(self, form):
        # super(BuatDokumen, self).form_valid()
        post = form.save(commit=False)
        bulan = form.cleaned_data['tanggal'].strftime('%m')
        tahun = int(form.cleaned_data['tanggal'].strftime('%Y'))
        id_klasifikasi = form.cleaned_data['klasifikasi'].pk
        kode_klasifikasi = form.cleaned_data['klasifikasi'].kode
        kode_fungsi = form.cleaned_data['fungsi'].kode
        kode_dokumen = form.cleaned_data['jenis_dokumen'].kode
        nomor_surat = 0
        nomor_terakhir = Dokumen.objects.filter(klasifikasi=id_klasifikasi).aggregate(Max('nomor_surat'))
        tahun_terakhir = Dokumen.objects.filter(klasifikasi=id_klasifikasi).order_by('-tanggal').values_list("tanggal",
                                                                                                             flat=True)[
                         :1]
        if tahun_terakhir.first() is None:
            nomor_surat = 1
        elif tahun_terakhir.first().year <= tahun:
            nomor_surat = 1
        elif tahun_terakhir.first().year == tahun:
            if nomor_terakhir['nomor_surat__max'] is None:
                nomor_surat = 1
            else:
                nomor_surat = nomor_terakhir['nomor_surat__max'] + 1

        post.nomor_surat_lengkap = "{}.{}/{}/{}/{}/{}".format(kode_dokumen, nomor_surat, kode_klasifikasi, bulan,
                                                              tahun, kode_fungsi)
        
        print(self.request.POST.getlist('tujuan'))
        post.user = self.request.user
        post.nomor_surat = nomor_surat
        print("{}.{}/{}/{}/{}/{}".format(kode_dokumen, nomor_surat, kode_klasifikasi, bulan, tahun, kode_fungsi))
        post.save()
        form.save_m2m()
        return redirect('dokumen:dashboard')
    
    def form_invalid(self, form):
        print(form.errors)
        print(form.errors.as_data())
        print(self.request.POST.getlist('tujuan'))
        return HttpResponse(form.errors.as_data())
    
    # def post(self, request, *args, **kwargs):
    #     print(request.POST.getlist('tujuan'))


@method_decorator(login_required, name='dispatch')
class LaporanNotaDinas(generic.ListView):
    template_name = 'dokumen/laporan-nota-dinas.html'
    model = Dokumen
    
    # queryset = Dokumen.objects.filter(jenis_dokumen=4)
    def get_context_data(self, **kwargs):
        context = super(LaporanNotaDinas, self).get_context_data()
        context['data_nota_dinas'] = Dokumen.objects.filter(jenis_dokumen=4)
        
        context['jenis_dokumen'] = JenisDokumen.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class Laporan(generic.TemplateView):
    template_name = 'dokumen/laporan-dokumen.html'
    
    def get_context_data(self, **kwargs):
        context = super(Laporan, self).get_context_data()
        context['data_nota_dinas'] = Dokumen.objects.all()
        context['jenis_dokumen'] = JenisDokumen.objects.all()
        return context
    
@method_decorator(login_required, name='dispatch')
class LaporanSuratDinas(generic.ListView):
    template_name = 'dokumen/laporan-surat-dinas.html'
    model = Dokumen

    def get_context_data(self, **kwargs):
        context = super(LaporanSuratDinas, self).get_context_data()
        context['data_surat_dinas'] = Dokumen.objects.filter(jenis_dokumen=5)
        return context




@method_decorator(login_required, name='dispatch')
class LaporanNotaDiplomatik(generic.ListView):
    template_name = 'dokumen/laporan-nota-diplomatik.html'
    model = Dokumen

    def get_context_data(self, **kwargs):
        context = super(LaporanNotaDiplomatik, self).get_context_data()
        context['data_surat_dinas'] = Dokumen.objects.filter(jenis_dokumen=1)
        return context


@method_decorator(login_required, name='dispatch')
class LaporanSuratPerintah(generic.ListView):
    template_name = 'dokumen/laporan-surat-perintah.html'
    model = Dokumen

    def get_context_data(self, **kwargs):
        context = super(LaporanSuratPerintah, self).get_context_data()
        context['data_surat_perintah'] = Dokumen.objects.filter(jenis_dokumen=2)
        return context


@method_decorator(login_required, name='dispatch')
class LaporanSuratPerintahKerja(generic.ListView):
    template_name = 'dokumen/laporan-surat-perintah-kerja.html'
    model = Dokumen

    def get_context_data(self, **kwargs):
        context = super(LaporanSuratPerintahKerja, self).get_context_data()
        context['data_surat_perintah_kerja'] = Dokumen.objects.filter(jenis_dokumen=3)
        return context


@method_decorator(login_required, name='dispatch')
class HapusSuratDinas(generic.edit.DeleteView):
    model = Dokumen
    slug_field = 'slug'
    success_url = reverse_lazy('dokumen:laporan-surat-dinas')
    template_name = 'delete.html'


@method_decorator(login_required, name='dispatch')
class HapusSPK(generic.edit.DeleteView):
    model = Dokumen
    slug_field = 'slug'
    success_url = reverse_lazy('dokumen:laporan-surat-perintah-kerja')
    template_name = 'delete.html'

@method_decorator(login_required, name='dispatch')
class EditDokumen(generic.edit.UpdateView):
    slug_field = 'slug'
    form_class = DokumenForm
    model = Dokumen
    template_name = 'dokumen/update-dokumen.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        bulan = form.cleaned_data['tanggal'].strftime('%m')
        tahun = int(form.cleaned_data['tanggal'].strftime('%Y'))
        id_klasifikasi = form.cleaned_data['klasifikasi'].pk
        kode_klasifikasi = form.cleaned_data['klasifikasi'].kode
        kode_fungsi = form.cleaned_data['fungsi'].kode
        kode_dokumen = form.cleaned_data['jenis_dokumen'].kode
        nomor_surat = 0
        nomor_terakhir = Dokumen.objects.filter(klasifikasi=id_klasifikasi).aggregate(Max('nomor_surat'))
        tahun_terakhir = Dokumen.objects.filter(klasifikasi=id_klasifikasi).order_by('-tanggal').values_list("tanggal",
                                                                                                             flat=True)[
                         :1]
        if tahun_terakhir.first() is None:
            nomor_surat = 1
        elif tahun_terakhir.first().year <= tahun:
            nomor_surat = 1
        elif tahun_terakhir.first().year == tahun:
            if nomor_terakhir['nomor_surat__max'] is None:
                nomor_surat = 1
            else:
                nomor_surat = nomor_terakhir['nomor_surat__max'] + 1

        post.nomor_surat_lengkap = "{}.{}/{}/{}/{}/{}".format(kode_dokumen, nomor_surat, kode_klasifikasi, bulan,
                                                              tahun, kode_fungsi)
        # tes = self.request.POST.getlist('tujuan')
        # for x in tes:
        #     print(x)
        print(self.request.POST)
        post.user = self.request.user
        post.nomor_surat = nomor_surat
        print("{}.{}/{}/{}/{}/{}".format(kode_dokumen, nomor_surat, kode_klasifikasi, bulan, tahun, kode_fungsi))
        post.save()
        return redirect('dokumen:dashboard')

    def form_invalid(self, form):
        print(form.errors)
        return HttpResponse(form.errors)
