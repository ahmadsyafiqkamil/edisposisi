# Generated by Django 2.2.7 on 2020-01-17 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_fungsi'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='korfung',
            field=models.BooleanField(default=False),
        ),
    ]
