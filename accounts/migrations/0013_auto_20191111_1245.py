# Generated by Django 2.2.7 on 2019-11-11 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20191111_1216'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='datauser',
            table='tbl_data_user',
        ),
        migrations.AlterModelTable(
            name='datauser_hs',
            table='tbl_data_user_hs',
        ),
        migrations.AlterModelTable(
            name='profle',
            table='tbl_profile',
        ),
    ]