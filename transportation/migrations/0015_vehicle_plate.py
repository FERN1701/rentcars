# Generated by Django 5.0.4 on 2024-10-11 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0014_alter_shops_latitude_alter_shops_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='plate',
            field=models.CharField(default=1, max_length=50, verbose_name='Plate Number'),
            preserve_default=False,
        ),
    ]
