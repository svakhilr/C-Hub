# Generated by Django 5.0.2 on 2024-02-27 11:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_companyprofile_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WorkerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='worker/profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='worker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('max_amount_per_hour', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_negotialble', models.BooleanField(default=True)),
                ('job_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.jobtype')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_profile', to='users.workerprofile')),
            ],
        ),
    ]