# Generated by Django 3.2.7 on 2021-10-07 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price_history',
            name='data',
            field=models.JSONField(default={}),
        ),
    ]
