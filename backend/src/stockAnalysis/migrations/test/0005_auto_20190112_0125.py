# Generated by Django 2.1.5 on 2019-01-12 01:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockAnalysis', '0004_auto_20190112_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockprice',
            name='ts',
            field=models.DateField(default=datetime.datetime(2019, 1, 12, 1, 25, 54, 263343)),
        ),
    ]
