# Generated by Django 3.2.6 on 2021-12-18 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created',
        ),
        migrations.RemoveField(
            model_name='user',
            name='demo_link',
        ),
        migrations.RemoveField(
            model_name='user',
            name='source_link',
        ),
    ]
