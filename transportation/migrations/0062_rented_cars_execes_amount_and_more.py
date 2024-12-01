# Generated by Django 5.0.4 on 2024-11-30 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0061_rented_cars_execes_hrs_rented_cars_paid_excess'),
    ]

    operations = [
        migrations.AddField(
            model_name='rented_cars',
            name='execes_amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rented_cars',
            name='paid_excess',
            field=models.CharField(default='none', max_length=50),
        ),
    ]
