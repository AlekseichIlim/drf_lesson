# Generated by Django 4.2.2 on 2024-09-30 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0007_car_owner_moto_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='amount',
            field=models.IntegerField(default=1000, verbose_name='цена'),
        ),
    ]