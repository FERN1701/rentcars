# Generated by Django 5.0.4 on 2024-10-11 10:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0023_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='categories',
            field=models.CharField(choices=[('toyota', 'Toyota'), ('honda', 'Honda'), ('mitsubishi', 'Mitsubishi'), ('chevrolet', 'Chevrolet'), ('ford', 'Ford'), ('nissan', 'Nissan'), ('bmw', 'BMW'), ('mercedes_benz', 'Mercedes-Benz'), ('audi', 'Audi'), ('volkswagen', 'Volkswagen'), ('hyundai', 'Hyundai'), ('kia', 'Kia'), ('tesla', 'Tesla'), ('subaru', 'Subaru'), ('mazda', 'Mazda'), ('volvo', 'Volvo'), ('lexus', 'Lexus'), ('porsche', 'Porsche'), ('ferrari', 'Ferrari'), ('lamborghini', 'Lamborghini'), ('land_rover', 'Land Rover'), ('jaguar', 'Jaguar'), ('infiniti', 'Infiniti'), ('acura', 'Acura'), ('jeep', 'Jeep'), ('dodge', 'Dodge'), ('ram', 'Ram'), ('chrysler', 'Chrysler'), ('buick', 'Buick'), ('gmc', 'GMC'), ('cadillac', 'Cadillac'), ('peugeot', 'Peugeot'), ('renault', 'Renault'), ('citroen', 'Citroën'), ('fiat', 'Fiat'), ('alfa_romeo', 'Alfa Romeo'), ('suzuki', 'Suzuki'), ('skoda', 'Škoda'), ('seat', 'SEAT'), ('bentley', 'Bentley'), ('rolls_royce', 'Rolls-Royce'), ('aston_martin', 'Aston Martin'), ('maserati', 'Maserati'), ('lotus', 'Lotus'), ('mclaren', 'McLaren'), ('bugatti', 'Bugatti'), ('saab', 'Saab'), ('opel', 'Opel')], max_length=50),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='seat',
            field=models.IntegerField(choices=[(2, '2 Seater'), (4, '4 Seater'), (5, '5 Seater'), (6, '6 Seater'), (7, '7 Seater'), (8, '8 Seater'), (9, '9 Seater'), (10, '10 Seater')]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='transmission',
            field=models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automatic'), ('semi', 'Semi-Automatic'), ('cvt', 'Continuously Variable Transmission (CVT)'), ('dual_clutch', 'Dual-Clutch Transmission (DCT)'), ('tiptronic', 'Tiptronic'), ('electric', 'Electric')], max_length=50),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.CharField(choices=[('sedan', 'Sedan'), ('suv', 'SUV (Sport Utility Vehicle)'), ('hatchback', 'Hatchback'), ('coupe', 'Coupe'), ('convertible', 'Convertible'), ('wagon', 'Wagon'), ('pickup', 'Pickup Truck'), ('van', 'Van'), ('motorcycle', 'Motorcycle'), ('bus', 'Bus'), ('truck', 'Truck'), ('minivan', 'Minivan'), ('crossover', 'Crossover'), ('electric', 'Electric Vehicle'), ('hybrid', 'Hybrid Vehicle'), ('sports', 'Sports Car')], max_length=50, verbose_name='Vehicle Type'),
        ),
        migrations.CreateModel(
            name='driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drivers_license', models.ImageField(upload_to='Drivers License')),
                ('phone_number', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_driver', to=settings.AUTH_USER_MODEL, verbose_name='Account Driver')),
                ('shop_under', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopdriver', to='transportation.shops', verbose_name='Shop Driver')),
            ],
        ),
    ]
