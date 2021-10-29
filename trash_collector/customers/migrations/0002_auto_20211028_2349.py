# Generated by Django 3.2.8 on 2021-10-28 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='County'),
        ),
        migrations.AddField(
            model_name='customer',
            name='county',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='County'),
        ),
        migrations.AddField(
            model_name='customer',
            name='latitude',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='customer',
            name='longitude',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zip_code',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Zip Code'),
        ),
    ]