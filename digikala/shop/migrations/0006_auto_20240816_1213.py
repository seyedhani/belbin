# Generated by Django 2.2 on 2024-08-16 19:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20240816_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 8, 16, 12, 13, 1, 442680)),
        ),
    ]
