# Generated by Django 4.0.5 on 2022-06-29 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_alter_scope_is_main_alter_scope_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статьи'},
        ),
    ]