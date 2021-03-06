# Generated by Django 4.0.3 on 2022-03-16 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0002_alter_reservation_flight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrival_city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='operating_airlines',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='middle_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
