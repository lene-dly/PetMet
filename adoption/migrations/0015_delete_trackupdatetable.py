# Generated by Django 4.2 on 2024-11-25 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0014_rename_uthor_trackupdatetable_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TrackUpdateTable',
        ),
    ]
