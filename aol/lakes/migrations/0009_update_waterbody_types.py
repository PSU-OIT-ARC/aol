# Generated by Django 2.2.2 on 2019-09-04 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lakes', '0008_migrate_computed_status_properties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lake',
            name='waterbody_type',
            field=models.IntegerField(choices=[(0, 'unknown'), (493, 'estuary'), (378, 'ice mass'), (390, 'lake/pond'), (361, 'playa'), (436, 'reservoir'), (466, 'swamp/marsh')], default=0),
        ),
    ]