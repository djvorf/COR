# Generated by Django 3.0.5 on 2020-04-09 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectors', '0003_auto_20200403_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='lector',
            name='shortinfo',
            field=models.TextField(default='null', verbose_name='Краткая информация'),
        ),
    ]