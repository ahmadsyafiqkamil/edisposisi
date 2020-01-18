#  Copyright (c) 2019.
#  Ahmad Syafiq Kamil

# accounts.models.py

from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)

# class yang digunakan untuk membuat user baru dan superuser
# from dokumen.models import Fungsi
import dokumen


class UserManager(BaseUserManager):
	def create_user(self, email, password,user_name):
		"""
		Creates and saves a User with the given email and password.
		"""
		if not email:
			raise ValueError('Users must have an email address')
		
		if not password:
			raise ValueError('Users must have an password')
		
		user = self.model(
			email=self.normalize_email(email),
		)
		user.set_password(password)
		user.user_name = user_name
		user.admin = False
		user.staff = False
		user.staff_dokumen = False
		user.korfung = False
		user.save(using=self._db)
		return user
	
	def create_superuser(self, email, password, user_name):
		"""
		Creates and saves a superuser with the given email and password.
		"""
		user = self.create_user(
			email,
			password=password,
			user_name=user_name,
			
		)
		user.admin = True
		user.staff = True
		user.staff_dokumen = True
		user.korfung = True
		user.save(using=self._db)
		return user


# class yang mendefinisikan tabel user
class User(AbstractBaseUser):
	email = models.EmailField(
		verbose_name='Alamat Email',
		max_length=255,
		unique=True,
	)
	user_name = models.CharField(max_length=255, blank=True, verbose_name="Nama Pengguna")
	# user_nama_lengkap = models.CharField(max_length=255, blank=True, verbose_name="Nama Lengkap")
	admin = models.BooleanField(default=False)  # a superuser
	staff = models.BooleanField(default=False)  # a staffuser
	staff_dokumen = models.BooleanField(default=False)  # a staffuser
	korfung = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True)
	fungsi = models.ForeignKey(to='dokumen.Fungsi', on_delete=models.CASCADE, related_name='fungsi_pengguna')
	# notice the absence of a "Password field", that's built in.


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['user_name', 'user_nama_lengkap']  # Email & Password are required by default.
	objects = UserManager()
	
	class Meta:
		db_table = 'tbl_user'
	
	def __str__(self):
		return self.email
	# def get_username(self):
	# 	return self.user_name
	
	# def get_full_name(self):
	#     return self.user_nama_lengkap
	
	def get_id_user(self):
		return self.pk
	
	# def get_fungsi(self):
	#     return Fungsi.objects.get(koordinator=self.get_id_user())
	# def get_menerima_disposisi(self):
	#     return self.user_menerima_disposisi
	# def get_kode_fungsi(self):
	#     return self.fungsi_kode
	# def get_status_user(self):
	#     return self.user_status
	# def get_koordinator_fungsi(self):
	#     return self.koordinator_fungsi
	
	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True
	
	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True
	
	@property
	def is_admin(self):
		"Is the user a admin member?"
		return self.admin
	
	@property
	def is_staff(self):
		"Is the user a admin member?"
		return self.staff

	@property
	def is_staff_dokumen(self):
		"Is the user a admin member?"
		return self.staff_dokumen

	@property
	def is_korfung(self):
		"Is the user a admin member?"
		return self.korfung

	def get_full_name(self):
		# return ProfileUser.objects.get(user=self.pk)
		return self.user_name


# model ini digunakan untuk mendefinisikan ulang user yang akan digunakan pada aplikasi ini
# class Jabatan(models.Model):
# 	kode = models.CharField(max_length=2, verbose_name='Kode Jabatan')
# 	jabatan = models.CharField(max_length=255, verbose_name='Jabatan')
#
# 	class Meta:
# 		db_table = 'tbl_jabatan'
#
# 	def __str__(self):
# 		return self.jabatan


# class ProfileUser(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
# 	user_nama_lengkap = models.CharField(max_length=255, blank=True, verbose_name="Nama Lengkap")
# 	user_foto = models.ImageField(upload_to='images/profile_picture',blank=True,null=True)
# 	user_notifikasi_email = models.CharField(max_length=2, blank=True, verbose_name="Email Notifikasi")
# 	fungsi = models.ForeignKey(to='dokumen.Fungsi', on_delete=models.CASCADE, related_name='fungsi_user')
# 	# HS
# 	# nip = models.CharField(max_length=50, verbose_name="NIP", blank=True, null=True, )
# 	# pangkat = models.CharField(max_length=255, verbose_name="Pangkat/Golongan", blank=True, null=True, )
# 	# tmt = models.DateField(verbose_name="TMT", blank=True, null=True)
# 	# gelar_diplomatik = models.CharField(max_length=255, blank=True, null=True, verbose_name="Gelar Diplomatik")
# 	# tmt_gelar = models.DateField(verbose_name="TMT", blank=True, null=True)
# 	# bulan_tiba = models.DateField(verbose_name="Bulan tiba di Perwakilan", blank=True, null=True)
# 	# # LS & THL
# 	# jenis_pekerjaan = models.CharField(max_length=255, blank=True, null=True, verbose_name='Jenis Pekerjaan')
# 	# awal_kontrak = models.DateField(verbose_name="Awal Kontrak", blank=True, null=True, )
# 	# akhir_kontrak = models.DateField(verbose_name="Akhir Kontrak", blank=True, null=True, )
# 	# kewarganegaraan = models.CharField(max_length=50, verbose_name="Kewarganegaraan", blank=True, null=True)
# 	# pendidikan = models.CharField(max_length=50, blank=True, null=True, verbose_name="Pendidikan")
# 	# jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE, related_name='kode_jabatan',blank=True,null=True)
#
#
# 	class Meta:
# 		db_table = 'tbl_profile'
#
# 	def __str__(self):
# 		return self.user_nama_lengkap
#
# 	def get_fungsi(self):
# 		return self.fungsi.pk