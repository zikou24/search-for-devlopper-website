# Generated by Django 3.2.6 on 2023-03-09 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_project_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created']},
        ),
    ]
