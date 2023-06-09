# Generated by Django 4.1.7 on 2023-04-21 04:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_rename_origin_flight_orgin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='flight',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='orgin',
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='flight',
            name='flight_number',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_booked', models.DateTimeField(auto_now_add=True)),
                ('seat_number', models.CharField(max_length=10)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.flight')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.passenger')),
            ],
        ),
    ]
