#  Copyright (c) 2019.
#  Ahmad Syafiq Kamil

from django import forms
from django.conf import settings
from django.forms import ModelMultipleChoiceField

from .models import Dokumen, Fungsi
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput, MonthPickerInput
from django_select2.forms import Select2MultipleWidget
from dokumen.models import Klasifikasi, Fungsi, Dokumen, JenisDokumen


class DokumenForm(forms.ModelForm):
	tanggal = forms.DateField(
		widget=forms.DateInput(
			format=('%Y-%m-%d'),
			attrs={'id': 'datepicker'}
		)
	)
	
	class Meta:
		model = Dokumen
		fields = ('jenis_dokumen', 'klasifikasi', 'fungsi', 'tujuan', 'tanggal', 'pejabat_penandatangan', 'perihal',
		          'file_dokumen')
		
		widgets = {
			'jenis_dokumen': forms.Select(
				attrs={
					'class': 'form-control'
				}
			),
			'klasifikasi': forms.Select(
				attrs={
					'class': 'form-control'
				}
			),
			'fungsi': forms.Select(
				attrs={
					'class': 'form-control'
				}
			),
			'perihal': forms.Textarea(
				attrs={
					'class': 'form-control',
					'cols': '40',
					'row': '10'
				}
			),
			'file_dokumen': forms.ClearableFileInput(
				attrs={
					'class': 'file-styled'
				}
				
			),
			'tujuan': forms.SelectMultiple(
				attrs={
					'class': 'js-example-basic-multiple'
				}
			)
			
		}
		
		labels = {
			'jenis_dokumen': 'Jenis Dokumen',
			'klasifikasi': 'Kode Klasifikasi',
			'fungsi': 'Kode Fungsi',
			'tujuan': 'Tujuan Dokumen',
			'tanggal': 'Tanggal',
			'pejabat_penandatangan': 'Pejabat Penandatangan',
			'perihal': 'Perihal Dokumen',
			'file_dokumen': 'File'
		}
