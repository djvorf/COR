# Generated by Django 3.0.5 on 2020-04-11 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectors', '0004_lector_shortinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='lector',
            name='numperpart',
            field=models.TextField(default='null', verbose_name='Номер главы'),
        ),
    ]