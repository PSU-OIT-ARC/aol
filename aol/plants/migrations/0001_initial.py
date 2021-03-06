# Generated by Django 2.2.1 on 2019-05-21 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lakes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('normalized_name', models.CharField(max_length=255, unique=True)),
                ('common_name', models.CharField(max_length=255)),
                ('noxious_weed_designation', models.CharField(choices=[('', ''), ('A', 'ODA Class A'), ('B', 'ODA Class B'), ('Federal', 'Federal')], default='', max_length=255)),
                ('is_native', models.NullBooleanField(default=None)),
            ],
            options={
                'ordering': ('normalized_name',),
            },
        ),
        migrations.CreateModel(
            name='PlantObservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observation_date', models.DateField(null=True)),
                ('source', models.CharField(choices=[('CLR', 'Center for Lakes and Reservoir'), ('IMAP', 'iMapInvasives')], default='', max_length=255)),
                ('survey_org', models.CharField(max_length=255)),
                ('lake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plant_observations', to='lakes.Lake')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lakes', to='plants.Plant')),
            ],
            options={
                'verbose_name': 'invasive plant observation',
                'ordering': ('-observation_date',),
            },
        ),
    ]
