# Generated by Django 5.0.4 on 2024-10-10 10:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0008_shops_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shops',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myshops', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='Vehicle Image')),
                ('img2', models.ImageField(upload_to='Vehicle Image')),
                ('img3', models.ImageField(upload_to='Vehicle Image')),
                ('img4', models.ImageField(upload_to='Vehicle Image')),
                ('img5', models.ImageField(upload_to='Vehicle Image')),
                ('categories', models.CharField(choices=[('toyota', 'Toyota'), ('honda', 'Honda'), ('mitsubishi', 'Mitsubishi'), ('chevrolet', 'Chevrolet')], max_length=50)),
                ('transmission', models.CharField(choices=[('manual', 'Manual'), ('auto', 'Automatic'), ('semi', 'Semi')], max_length=50)),
                ('seat', models.IntegerField(choices=[('2', '2 Seater'), ('4', '4 Seater'), ('5', '5 Seater'), ('6', '6 Seater'), ('8', '8 Seater')])),
                ('color_description', models.CharField(max_length=150, verbose_name='Color desccription')),
                ('model_car', models.CharField(max_length=50, verbose_name='Car Model')),
                ('chasis_number', models.CharField(max_length=50, verbose_name='Chasis Number')),
                ('vin_no', models.CharField(max_length=50, verbose_name='Vin Number')),
                ('vehicle_type', models.CharField(max_length=50, verbose_name='Vehicle Type')),
                ('shop_belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopvehicles', to='transportation.shops', verbose_name='Shop Vehicles')),
            ],
        ),
    ]
