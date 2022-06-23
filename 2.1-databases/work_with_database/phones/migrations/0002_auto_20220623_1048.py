# Generated by Django 3.2.4 on 2022-06-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='release_date',
            field=models.DateField(default='1990-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
