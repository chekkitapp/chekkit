# Generated by Django 2.0.7 on 2018-08-06 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20180806_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_number',
            field=models.IntegerField(blank=True, default=762965, null=True),
        ),
    ]
