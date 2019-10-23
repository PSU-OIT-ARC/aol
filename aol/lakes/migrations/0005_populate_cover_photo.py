# Generated by Django 2.2.2 on 2019-08-21 23:45

from django.db import migrations


# Note: This migration remains here for historical reasons.
#       Equivalent functionality is now available via the
#       admin action of the same name.
def populate_cover_photos(apps, schema_editor):
    Lake = apps.get_model('lakes', 'Lake')

    for record in Lake.objects.iterator():
        if not record.photo and record.photos.exists():
            record.photo = record.photos.all()[0]
            record.save()


class Migration(migrations.Migration):

    dependencies = [
        ('lakes', '0004_lake_photo'),
    ]

    operations = [
        migrations.RunPython(populate_cover_photos),
    ]
