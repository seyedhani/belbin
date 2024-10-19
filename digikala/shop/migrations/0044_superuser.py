# Generated by Django 5.1.1 on 2024-09-19 11:08

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0043_result'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_numb', models.CharField(max_length=12)),
                ('gender', models.CharField(choices=[('man', 'man'), ('woman', 'woman'), ('rather not to say', 'rather not to say')], default='man', max_length=30)),
                ('date', models.DateField(default=datetime.date.today)),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.result')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
