#  Copyright (c) 2019.
#  Ahmad Syafiq Kamil

from builtins import super, slice

# from Tools.scripts.patchcheck import status
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from .form import DokumenForm, EditForm
from django.urls import reverse_lazy
from .models import Dokumen, Fungsi, Klasifikasi, JenisDokumen, TujuanDokumen
from django_select2.forms import Select2MultipleWidget
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from accounts.models import ProfileUser


# Create your views here.
@method_decorator(login_required, name='dispatch')
class dashboard(generic.TemplateView):
	template_name = 'dokumen/dashboard.html'
	
	def get_context_data(self, **kwargs):
		context = super(dashboard, self).get_context_data()
		if self.request.user.is_admin:
			context['data_surat_masuk'] = Dokumen.objects.exclude(status=3)
			context['data_surat_keluar'] = Dokumen.objects.exclude(status=3)
		elif self.request.user.is_staff:
			Dokumen.objects.exclude(status=3).filter(fungsi=38).values('tujuandokumen__status')
			context['data_surat_keluar'] = Dokumen.objects.exclude(status=3).filter(
				fungsi=ProfileUser.objects.get(user=self.request.user.pk).fungsi.pk)
			context['data_surat_masuk'] = Dokumen.objects.exclude(status=3).filter(
				tujuan=ProfileUser.objects.get(user=self.request.user.pk).fungsi.pk).values('nomor_surat_lengkap','klasifikasi__kode','klasifikasi__nama_klasifikasi','pejabat_penandatangan','tujuandokumen__status','slug')
			# context['coba'] = data

		return context


@method_decorator(login_required, name='dispatch')
class BuatDokumen(generic.edit.CreateView):
	# http_method_names = "post"
	template_name = 'dokumen/buat-dokumen.html'
	form_class = DokumenForm
	
	def get_form_kwargs(self):
		kwargs = super(BuatDokumen, self).get_form_kwargs()
		kwargs.update({'user': self.request.user})
		if self.request.user.is_admin:
			kwargs.update({'fungsi': ''})
		elif self.request.user.is_staff:
			kwargs.update({'fungsi': ProfileUser.objects.get(user=self.request.user.pk)})
		return kwargs
	
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
		nomor = Dokumen.objects.filter(klasifikasi=id_klasifikasi, tanggal__year=tahun).aggregate(Max('nomor_surat'))
		nomor_terakhir = nomor['nomor_surat__max']
		tahun_terakhir = Dokumen.objects.filter(klasifikasi=id_klasifikasi).order_by('-tanggal').values_list("tanggal",
		                                                                                                     flat=True)[
		                 :1]
		
		print(nomor_terakhir)
		# print(tahun_terakhir.first().year)
		print(tahun)
		
		# ini masih masalah
		if tahun_terakhir.first() is None:
			print("1", tahun_terakhir.first())
			nomor_surat = 1
		
		elif tahun_terakhir.first().year == tahun:
			print("3", tahun_terakhir.first())
			if nomor_terakhir == 0:
				nomor_surat = 1
			else:
				nomor_surat = nomor_terakhir + 1
		
		elif tahun_terakhir.first().year <= tahun:
			print("2", tahun_terakhir.first())
			nomor_surat = 1
		
		print("nomor surat baru", nomor_surat)
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
class HapusSuratDinas(generic.edit.DeleteView):
	model = Dokumen
	slug_field = 'slug'
	success_url = reverse_lazy('dokumen:laporan-surat-dinas')
	template_name = 'delete.html'


@method_decorator(login_required, name='dispatch')
class BatalDokumen(generic.View):
	def get(self, request):
		slug = request.GET.get('slug', None)
		# Dokumen.objects.get(slug = slug).delete()
		Dokumen.objects.filter(slug=slug).update(status="3")
		data = {
			'deleted': True
		}
		return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class BacaDokumen(generic.View):
	def get(self, request):
		print(self.request.user.pk)
		print(ProfileUser.objects.get(user=self.request.user.pk).fungsi)
		# print(TujuanDokumen.objects.get(dokumen__slug='d2ku12201913', fungsi=25))
		
		fungsi = ProfileUser.objects.values_list("fungsi", flat=True).get(user=self.request.user.pk)
		slug = request.GET.get('slug', None)
		a = TujuanDokumen.objects.get(dokumen__slug=slug, fungsi=fungsi)
		a.status = 1
		a.save()
		data = {
			'read': True
		}
		return JsonResponse(data)


@method_decorator(login_required, name='dispatch')
class EditDokumen(generic.edit.UpdateView):
	slug_field = 'slug'
	form_class = EditForm
	model = Dokumen
	template_name = 'dokumen/update-dokumen.html'
	
	def get_form_kwargs(self):
		kwargs = super(EditDokumen, self).get_form_kwargs()
		kwargs.update({'user': self.request.user})
		if self.request.user.is_admin:
			kwargs.update({'fungsi': ''})
		elif self.request.user.is_staff:
			kwargs.update({'fungsi': ProfileUser.objects.get(user=self.request.user.pk)})
		return kwargs
	
	def form_valid(self, form):
		post = form.save(commit=False)
		bulan = form.cleaned_data['tanggal'].strftime('%m')
		tahun = int(form.cleaned_data['tanggal'].strftime('%Y'))
		id_klasifikasi = form.cleaned_data['klasifikasi'].pk
		kode_klasifikasi = form.cleaned_data['klasifikasi'].kode
		kode_fungsi = form.cleaned_data['fungsi'].kode
		kode_dokumen = form.cleaned_data['jenis_dokumen'].kode
		nomor_surat = 0
		nomor = Dokumen.objects.filter(klasifikasi=id_klasifikasi, tanggal__year=tahun).aggregate(Max('nomor_surat'))
		nomor_terakhir = nomor['nomor_surat__max']
		tahun_terakhir = Dokumen.objects.filter(klasifikasi=id_klasifikasi).order_by('-tanggal').values_list("tanggal",
		                                                                                                     flat=True)[
		                 :1]
		id_klasifikasi_terakhir = Dokumen.objects.get(slug=self.kwargs.get('slug')).klasifikasi_id
		print("id slug ", self.kwargs.get('slug'))
		print("id klasifikasi terakhir ", id_klasifikasi_terakhir)
		#
		if id_klasifikasi == id_klasifikasi_terakhir:
			nomor_surat = nomor_terakhir
		else:
			print(nomor_terakhir)
			print(tahun)
			# ini masih masalah
			if tahun_terakhir.first() is None:
				print("1", tahun_terakhir.first())
				nomor_surat = 1
			
			elif tahun_terakhir.first().year == tahun:
				print("3", tahun_terakhir.first())
				if nomor_terakhir == 0:
					nomor_surat = 1
				else:
					nomor_surat = nomor_terakhir + 1
			
			elif tahun_terakhir.first().year <= tahun:
				print("2", tahun_terakhir.first())
				nomor_surat = 1
		
		print("nomor surat baru", nomor_surat)
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
		return self.render_to_response(self.get_context_data(form=form))



@method_decorator(login_required, name='dispatch')
class DetailDokumen(generic.DetailView):
	template_name = 'dokumen/detail-dokumen.html'
	model = Dokumen

	def get_context_data(self, **kwargs):
		context = super(DetailDokumen, self).get_context_data(**kwargs)
		context['tujuan'] = TujuanDokumen.objects.get(fungsi=self.request.session['KODE_FUNGSI'],dokumen=Dokumen.objects.get(slug=self.kwargs.get('slug')).pk)
		context['dokumen'] = Dokumen.objects.get(slug=self.kwargs.get('slug'))
		return context

@method_decorator(login_required, name='dispatch')
class DetailDokumenKeluar(generic.DetailView):
	model = Dokumen
	template_name = 'dokumen/detail-dokumen-keluar.html'

	def get_context_data(self, **kwargs):
		print(self.kwargs.get('slug'))
		context = super(DetailDokumenKeluar, self).get_context_data(**kwargs)
		context['data_tujuan'] = TujuanDokumen.objects.filter(dokumen__slug=self.kwargs.get('slug'))
		a = Dokumen.objects.values_list('tujuan_eksternal',flat=True).get(slug=self.kwargs.get('slug'))
		print(a)
		if a is None :
			context['tujuan_eksternal']  = None
		else:
			url = a
			data = url.split("#")
			context['tujuan_eksternal'] = data

			print(a)
		return context

@method_decorator(login_required, name='dispatch')
class Laporan(generic.TemplateView):
	template_name = 'dokumen/laporan-dokumen.html'

	def get_context_data(self, **kwargs):
		context = super(Laporan, self).get_context_data()
		if self.request.user.is_admin:
			context['data_nota_dinas'] = Dokumen.objects.all()
		elif self.request.user.is_staff:
			print(ProfileUser.objects.get(user=self.request.user.pk).fungsi.pk)
			context['data_nota_dinas'] = Dokumen.objects.filter(
				fungsi=ProfileUser.objects.get(user=self.request.user.pk).fungsi.pk)
		# context['jenis_dokumen'] = JenisDokumen.objects.all()
		return context
# tidak dipakai

# Batal Dokumen

# def bataldokumen(request,slug):
#     if request.method ==  'POST' and request.is_ajax():
#         try:
#             update = Dokumen.objects.get(slug = slug)
#             update.status = 3
#             update.save()
#             return JsonResponse({'status':'Success', 'msg': 'save successfully'})
#         except:
#             return JsonResponse({'status':'Fail', 'msg': 'Objects doesnt update'})
#     else:
#         return JsonResponse({'status':'Fail', 'msg':'Not a valid request'})


# @method_decorator(login_required, name='dispatch')
# class LaporanSuratDinas(generic.ListView):
#     template_name = 'dokumen/laporan-surat-dinas.html'
#     model = Dokumen
#
#     def get_context_data(self, **kwargs):
#         context = super(LaporanSuratDinas, self).get_context_data()
#         context['data_surat_dinas'] = Dokumen.objects.filter(jenis_dokumen=5)
#         return context
#
#
# @method_decorator(login_required, name='dispatch')
# class LaporanNotaDinas(generic.ListView):
#     template_name = 'dokumen/laporan-nota-dinas.html'
#     model = Dokumen
#
#     # queryset = Dokumen.objects.filter(jenis_dokumen=4)
#     def get_context_data(self, **kwargs):
#         context = super(LaporanNotaDinas, self).get_context_data()
#         context['data_nota_dinas'] = Dokumen.objects.filter(jenis_dokumen=4)
#
#         context['jenis_dokumen'] = JenisDokumen.objects.all()
#         return context
#
# @method_decorator(login_required, name='dispatch')
# class LaporanNotaDiplomatik(generic.ListView):
#     template_name = 'dokumen/laporan-nota-diplomatik.html'
#     model = Dokumen
#
#     def get_context_data(self, **kwargs):
#         context = super(LaporanNotaDiplomatik, self).get_context_data()
#         context['data_surat_dinas'] = Dokumen.objects.filter(jenis_dokumen=1)
#         return context
#
#
# @method_decorator(login_required, name='dispatch')
# class LaporanSuratPerintah(generic.ListView):
#     template_name = 'dokumen/laporan-surat-perintah.html'
#     model = Dokumen
#
#     def get_context_data(self, **kwargs):
#         context = super(LaporanSuratPerintah, self).get_context_data()
#         context['data_surat_perintah'] = Dokumen.objects.filter(jenis_dokumen=2)
#         return context
#
#
# @method_decorator(login_required, name='dispatch')
# class LaporanSuratPerintahKerja(generic.ListView):
#     template_name = 'dokumen/laporan-surat-perintah-kerja.html'
#     model = Dokumen
#
#     def get_context_data(self, **kwargs):
#         context = super(LaporanSuratPerintahKerja, self).get_context_data()
#         context['data_surat_perintah_kerja'] = Dokumen.objects.filter(jenis_dokumen=3)
#         return context
#
# @method_decorator(login_required, name='dispatch')
# class HapusSPK(generic.edit.DeleteView):
#     model = Dokumen
#     slug_field = 'slug'
#     success_url = reverse_lazy('dokumen:laporan-surat-perintah-kerja')
#     template_name = 'delete.html'
