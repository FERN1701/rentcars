# Generated by Django 5.0.4 on 2024-11-19 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0045_rented_cars_car_fee_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rented_cars',
            name='payment_choice',
            field=models.IntegerField(choices=[(1, 'Onsite'), (2, 'Online')], default=1),
            preserve_default=False,
        ),
    ]
