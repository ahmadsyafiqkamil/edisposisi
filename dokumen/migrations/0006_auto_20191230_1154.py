# Generated by Django 2.2.7 on 2019-12-30 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dokumen', '0005_dokumen_tujuan_eksternal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokumen',
            name='pejabat_penandatangan',
            field=models.CharField(max_length=255, verbose_name='Pembuat Dokumen'),
        ),
    ]