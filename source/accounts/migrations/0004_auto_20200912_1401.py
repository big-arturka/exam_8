# Generated by Django 2.2 on 2020-09-12 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200912_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='github',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка на GitHub'),
        ),
    ]