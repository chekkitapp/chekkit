# Generated by Django 2.0.7 on 2018-08-06 09:56

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_auto_20180806_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='UssdRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=15)),
                ('complaint', models.CharField(blank=True, choices=[('1', 'No complaint'), ('2', 'Product below quality'), ('3', 'Product too expensive')], max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('gateway', models.CharField(max_length=10)),
                ('data', jsonfield.fields.JSONField(default={})),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('product_line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.ProductLine')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='ussdrecord',
            unique_together={('session_id', 'gateway')},
        ),
    ]
