# Generated by Django 4.2.2 on 2024-10-01 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0008_car_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='moto',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
