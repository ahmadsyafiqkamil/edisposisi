#  Copyright (c) 2019.
#  Ahmad Syafiq Kamil

from django import forms
from .models import User, ProfileUser


# class registerForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields= ['email','user_name','user_nama_lengkap']

class profileForm(forms.ModelForm):
	# tmt = forms.DateField(
	# 	widget=forms.DateInput(
	# 		format=('%Y-%m-%d'),
	# 		attrs={'id': 'datepicker'}
	# 	)
	# )
	#
	# tmt_gelar = forms.DateField(
	# 	widget=forms.DateInput(
	# 		format=('%Y-%m-%d'),
	# 		attrs={'id': 'datepicker1'}
	# 	)
	# )
	# awal_kontrak = forms.DateField(
	# 	widget=forms.DateInput(
	# 		format=('%Y-%m-%d'),
	# 		attrs={'id': 'datepicker2'}
	# 	)
	# )
	#
	# akhir_kontrak = forms.DateField(
	# 	widget=forms.DateInput(
	# 		format=('%Y-%m-%d'),
	# 		attrs={'id': 'datepicker3'}
	# 	)
	# )
	# bulan_tiba = forms.DateField(
	# 	widget=forms.DateInput(
	# 		format=('%Y-%m-%d'),
	# 		attrs={'id': 'datepicker4'}
	# 	)
	# )
	class Meta:
		model = ProfileUser
		fields = [
			# 'user',
			# 'nip',
			'user_foto',
			'user_nama_lengkap',
			# 'jenis_pekerjaan',
			'fungsi',
			# 'jabatan',
			# 'awal_kontrak',
			# 'akhir_kontrak',
			# 'kewarganegaraan',
			# 'bulan_tiba',
			# 'gelar_diplomatik',
			# 'pangkat',
			# 'pendidikan',
			# 'tmt',
			# 'tmt_gelar'
		]
	
	widgets = {
		'user_foto': forms.ClearableFileInput(
			attrs={
				'class': 'file-styled'
			}
		
		),
		
		
	}
	# def __init__(self ,*args, **kwargs):
	# 	user = kwargs.pop('user')
	# 	super(profileForm, self).__init__(*args,**kwargs)
	# 	self.fields['user'].queryset = User.objects.get(user.pk)