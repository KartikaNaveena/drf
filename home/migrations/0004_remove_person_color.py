# Generated by Django 4.1.4 on 2023-01-11 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_person_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='color',
        ),
    ]
