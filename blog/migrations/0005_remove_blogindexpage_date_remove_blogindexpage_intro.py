# Generated by Django 4.2.7 on 2024-01-21 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpagegalleryimage_author_blogpage_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogindexpage',
            name='date',
        ),
        migrations.RemoveField(
            model_name='blogindexpage',
            name='intro',
        ),
    ]
