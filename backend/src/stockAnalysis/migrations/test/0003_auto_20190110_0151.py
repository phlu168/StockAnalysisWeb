# Generated by Django 2.1.5 on 2019-01-10 01:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockAnalysis', '0002_auto_20190110_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockprice',
            name='ts',
            field=models.DateField(default=datetime.datetime(2019, 1, 10, 1, 51, 16, 973714)),
        ),
    ]
