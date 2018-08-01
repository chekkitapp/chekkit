# Generated by Django 2.0.7 on 2018-08-01 16:17

from django.db import migrations, models

import accounts.models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0005_auto_20180731_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='code',
            field=models.IntegerField(editable=False, unique=True, validators=[accounts.models.validate_code_length]),
        ),
    ]
