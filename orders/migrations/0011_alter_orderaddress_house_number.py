# Generated by Django 5.0.2 on 2024-02-21 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_orderitem_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderaddress',
            name='house_number',
            field=models.CharField(max_length=20),
        ),
    ]