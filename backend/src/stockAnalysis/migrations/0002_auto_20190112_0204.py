# Generated by Django 2.1.5 on 2019-01-12 02:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockAnalysis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockprice',
            old_name='symbol',
            new_name='sym',
        ),
        migrations.AlterField(
            model_name='stockprice',
            name='ts',
            field=models.DateField(default=datetime.datetime(2019, 1, 12, 2, 4, 20, 209130)),
        ),
    ]
