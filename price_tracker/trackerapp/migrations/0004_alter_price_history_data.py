# Generated by Django 3.2.7 on 2021-10-13 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackerapp', '0003_alter_price_history_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price_history',
            name='data',
            field=models.JSONField(),
        ),
    ]
