# Generated by Django 5.0.2 on 2024-02-12 16:52

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_companyprofile_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
    ]
