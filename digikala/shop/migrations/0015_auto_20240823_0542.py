# Generated by Django 2.2 on 2024-08-23 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20240823_0537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Partq',
        ),
    ]
