# Generated by Django 4.2.7 on 2023-11-24 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_customuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='date_registered',
            new_name='date_joined',
        ),
    ]
