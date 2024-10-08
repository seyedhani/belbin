# Generated by Django 2.2 on 2024-08-23 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20240823_0542'),
    ]

    operations = [
        migrations.CreateModel(
            name='MQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numb', models.IntegerField()),
                ('ques', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Mainq',
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='Partq',
        ),
        migrations.AddField(
            model_name='mq',
            name='parts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Partq'),
        ),
    ]
