# Generated by Django 3.0.5 on 2020-04-19 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lectors', '0013_auto_20200419_1242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lector',
            old_name='lectors1/',
            new_name='media/lectors1/',
        ),
    ]
