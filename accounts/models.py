# accounts.models.py

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# class yang digunakan untuk membuat user baru dan superuser
# from dokumen.models import Fungsi
import dokumen


class UserManager(BaseUserManager):
    def create_user(self, email, password, user_name, user_nama_lengkap):
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
        user.user_nama_lengkap = user_nama_lengkap
        user.staff = False
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, user_name, user_nama_lengkap):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            user_name=user_name,
            user_nama_lengkap=user_nama_lengkap
        )
        user.admin = True
        user.staff = True
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
    user_nama_lengkap = models.CharField(max_length=255, blank=True, verbose_name="Nama Lengkap")
    admin = models.BooleanField(default=False)  # a superuser
    staff = models.BooleanField(default=False)  # a staffuser
    timestamp = models.DateTimeField(auto_now_add=True)
    # notice the absence of a "Password field", that's built in.
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'user_nama_lengkap']  # Email & Password are required by default.
    objects = UserManager()
    
    class Meta:
        db_table = 'tbl_user'
    
    def get_username(self):
        return self.user_name
    
    def get_full_name(self):
        return self.user_nama_lengkap
    
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


# model ini digunakan untuk mendefinisikan ulang user yang akan digunakan pada aplikasi ini
class Jabatan(models.Model):
    kode = models.CharField(max_length=2, verbose_name='Kode Jabatan')
    jabatan = models.CharField(max_length=255, verbose_name='Jabatan')


class Profle(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_foto = models.ImageField(upload_to='images/profile_picture')
    user_notifikasi_email = models.CharField(max_length=2, blank=True, verbose_name="Email Notifikasi")
    # fungsi = models.ForeignKey(, on_delete=models.CASCADE, related_name='fungsi_hs')
    # LS & THL
    jenis_pekerjaan = models.CharField(max_length=255, blank=True, null=True, verbose_name='Jenis Pekerjaan')
    awal_kontrak = models.DateField(verbose_name="Awal Kontrak" , blank=True, null=True,)
    akhir_kontrak = models.DateField(verbose_name="Akhir Kontrak" , blank=True, null=True,)
    kewarganegaraan = models.CharField(max_length=50, verbose_name="Kewarganegaraan", blank=True, null=True)
    pendidikan = models.CharField(max_length=50, blank=True, null=True, verbose_name="Pendidikan")
    jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE, related_name='kode_jabatan')
    # HS
    nip = models.CharField(max_length=50,  verbose_name="NIP", blank=True, null=True,)
    pangkat = models.CharField(max_length=255, verbose_name="Pangkat/Golongan" , blank=True, null=True,)
    tmt = models.DateField(verbose_name="TMT", blank=True, null=True)
    gelar_diplomatik = models.CharField(max_length=255, blank=True, null=True, verbose_name="Gelar Diplomatik" )
    tmt_gelar = models.DateField(verbose_name="TMT", blank=True, null=True)
    bulan_tiba = models.DateField(verbose_name="Bulan tiba di Perwakilan" , blank=True, null=True)
    
    class Meta:
        db_table = 'tbl_profile'
    
    def __str__(self):
        return self.user

# class DataUser(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='datauser')
#     jenis_pekerjaan = models.CharField(max_length=255, blank=True, null=True, verbose_name='Jenis Pekerjaan')
#     awal_kontrak = models.DateField(verbose_name="Awal Kontrak")
#     akhir_kontrak = models.DateField(verbose_name="Akhir Kontrak")
#     kewarganegaraan = models.CharField(max_length=50,verbose_name="Kewarganegaraan",blank=True,null=True)
#     pendidikan = models.CharField(max_length=50,blank=True,null=True,verbose_name="Pendidikan")
#
#     class Meta:
#         db_table = 'tbl_data_user'
#     def __str__(self):
#         return self.user
#
# class DataUser_HS(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='homestaff')
#     nip = models.CharField(max_length=50,verbose_name="NIP")
#     pangkat = models.CharField(max_length=255,verbose_name="Pangkat/Golongan")
#     tmt = models.DateField(verbose_name="TMT",blank=True,null=True)
#     gelar_diplomatik = models.CharField(max_length=255,blank=True,null=True,verbose_name="Gelar Diplomatik")
#     tmt_gelar = models.DateField(verbose_name="TMT", blank=True,null=True)
#     bulan_tiba = models.DateField(verbose_name="Bulan tiba di Perwakilan", )
#     # fungsi = models.ForeignKey(Fungsi,on_delete=models.CASCADE,related_name='fungsi_hs')
#
#     class Meta:
#         db_table = 'tbl_data_user_hs'
#
#     def __str__(self):
#         return self.user

# class DataUser(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='data_user')
#
#
# jenis_pekerjaan = models.CharField(max_length=255, blank=True, null=True, verbose_name='Jenis Pekerjaan')
# fungsi = models.ForeignKey(Fungsi, on_delete=models.CASCADE, related_name='kode_fungsi')
