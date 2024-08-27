# Generated by Django 2.2 on 2024-08-25 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_mainq'),
    ]

    operations = [
        migrations.CreateModel(
            name='AggrQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtext', models.CharField(max_length=400)),
                ('main_q', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='part', to='shop.MainQ')),
            ],
        ),
    ]
