# Generated by Django 3.2.4 on 2021-06-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20210630_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='price',
            field=models.FloatField(default=500, null=True),
        ),
    ]
