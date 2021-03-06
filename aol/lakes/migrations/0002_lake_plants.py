# Generated by Django 2.2.1 on 2019-05-21 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mussels', '0001_initial'),
        ('plants', '0001_initial'),
        ('lakes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lake',
            name='mussels',
            field=models.ManyToManyField(through='mussels.MusselObservation', to='mussels.Mussel'),
        ),
        migrations.AddField(
            model_name='lake',
            name='plants',
            field=models.ManyToManyField(through='plants.PlantObservation', to='plants.Plant'),
        ),
    ]
