# Generated by Django 4.0.5 on 2022-06-29 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_scope_options_article_tags_alter_scope_article_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Тематика', 'verbose_name_plural': 'Тематики'},
        ),
    ]
