# Generated by Django 2.0.7 on 2018-08-02 05:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0027_auto_20180801_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_number',
            field=models.IntegerField(blank=True, default=357370, null=True),
        ),
    ]