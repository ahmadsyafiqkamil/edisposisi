# Generated by Django 2.2.6 on 2019-10-31 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20191031_0815'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='tbl_user',
        ),
    ]