# Generated by Django 2.0 on 2017-12-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20171218_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.CharField(default='0', max_length=255, verbose_name='Цена'),
        ),
    ]
