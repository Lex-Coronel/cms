# Generated by Django 3.2.4 on 2021-06-30 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_auto_20210630_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='delivery',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
