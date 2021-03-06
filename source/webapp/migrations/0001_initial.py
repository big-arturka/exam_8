# Generated by Django 2.2 on 2020-09-26 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('category', models.CharField(choices=[('food', 'Еда'), ('tech', 'Бытовая техника'), ('other', 'Разное'), ('tools', 'Инструменты')], default='other', max_length=40, verbose_name='Категория')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_pics', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
