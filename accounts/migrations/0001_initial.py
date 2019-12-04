# Generated by Django 2.2.7 on 2019-12-02 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Alamat Email')),
                ('user_name', models.CharField(blank=True, max_length=255, verbose_name='Nama Pengguna')),
                ('admin', models.BooleanField(default=False)),
                ('staff', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tbl_user',
            },
        ),
        migrations.CreateModel(
            name='Jabatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=2, verbose_name='Kode Jabatan')),
                ('jabatan', models.CharField(max_length=255, verbose_name='Jabatan')),
            ],
            options={
                'db_table': 'tbl_jabatan',
            },
        ),
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_nama_lengkap', models.CharField(blank=True, max_length=255, verbose_name='Nama Lengkap')),
                ('user_foto', models.ImageField(blank=True, null=True, upload_to='images/profile_picture')),
                ('user_notifikasi_email', models.CharField(blank=True, max_length=2, verbose_name='Email Notifikasi')),
            ],
            options={
                'db_table': 'tbl_profile',
            },
        ),
    ]
