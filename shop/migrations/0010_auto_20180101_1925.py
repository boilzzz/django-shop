# Generated by Django 2.0 on 2018-01-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20180101_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='base_photo',
            field=models.CharField(default='avatar-1.png', max_length=255, verbose_name='Аватар по умолчанию'),
        ),
    ]
