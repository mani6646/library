# Generated by Django 4.1.7 on 2023-04-20 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='flights',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='flight',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='passengers',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='duration',
        ),
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='flight',
            name='origin',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Airport',
        ),
        migrations.DeleteModel(
            name='Passenger',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
