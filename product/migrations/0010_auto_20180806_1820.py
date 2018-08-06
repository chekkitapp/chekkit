# Generated by Django 2.0.7 on 2018-08-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0009_auto_20180806_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_number',
            field=models.IntegerField(blank=True, default=112710, null=True),
        ),
        migrations.AlterField(
            model_name='productline',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]