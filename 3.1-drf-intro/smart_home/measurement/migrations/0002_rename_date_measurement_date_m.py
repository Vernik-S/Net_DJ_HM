# Generated by Django 4.0.6 on 2022-07-14 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='date',
            new_name='date_m',
        ),
    ]
