# Generated by Django 5.0.4 on 2024-11-20 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0055_rented_cars_out_garage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rented_cars',
            name='out_garage',
            field=models.DateTimeField(),
        ),
    ]
