#  Copyright (c) 2019.
#  Ahmad Syafiq Kamil

# Generated by Django 2.2.7 on 2019-12-10 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dokumen', '0002_auto_20191205_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tujuandokumen',
            name='status',
            field=models.IntegerField(blank=True, default=0, max_length=5, null=True, verbose_name='Status'),
        ),
    ]
