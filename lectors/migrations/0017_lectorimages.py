# Generated by Django 3.0.5 on 2020-04-29 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lectors', '0016_auto_20200419_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='LectorImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='lector_image/', verbose_name='Изображение')),
                ('lector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectors.Lector', verbose_name='Лекция')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
