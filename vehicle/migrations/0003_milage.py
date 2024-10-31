# Generated by Django 4.2.2 on 2024-09-17 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_moto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.PositiveIntegerField(verbose_name='пробег')),
                ('year', models.PositiveIntegerField(verbose_name='год регистрации')),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.car', verbose_name='автомобиль')),
                ('moto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.moto', verbose_name='мотоцикл')),
            ],
            options={
                'verbose_name': 'пробег',
                'verbose_name_plural': 'пробеги',
                'ordering': ('-year',),
            },
        ),
    ]
