# Generated by Django 2.2 on 2024-08-23 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20240823_0529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pq', models.CharField(max_length=1000)),
            ],
        ),
    ]
