# Generated by Django 3.2.4 on 2021-06-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='pay_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending', max_length=200, null=True),
        ),
    ]
