# Generated by Django 2.1.5 on 2019-01-12 02:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockAnalysis', '0003_auto_20190112_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockprice',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 1, 12, 2, 8, 28, 877190)),
        ),
        migrations.AlterField(
            model_name='stockprice',
            name='sym',
            field=models.CharField(default='symbol', max_length=10),
        ),
    ]
