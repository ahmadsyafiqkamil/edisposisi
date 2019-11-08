# accounts.models.py

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# from dokumen.models import Fungsi

# class yang digunakan untuk membuat user baru dan superuser
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
        user.user_name=user_name
        user.user_nama_lengkap=user_nama_lengkap
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
    user_foto = models.CharField(max_length=255, blank=True, verbose_name="Foto Pengguna")
    user_notifikasi_email = models.CharField(max_length=2, blank=True, verbose_name="Email Notifikasi")
    # koordinator_fungsi = models.CharField(max_length=2, blank=True, verbose_name="Koordinator Fungsi")
    # fungsi_kode = models.CharField(max_length=2, blank=True, verbose_name="Kode Fungsi")
    # fungsi_kode = models.ForeignKey(Fungsi,on_delete=models.CASCADE,related_name="kode_fungsi",verbose_name="Kode Fungsi")
    # user_status = models.CharField(max_length=2, blank=True, verbose_name="Status Pengguna")
    # user_menerima_disposisi = models.CharField(max_length=2, blank=True, verbose_name="Dapat Menerima Disposisi")
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
    def get_foto(self):
        return self.user_foto
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



