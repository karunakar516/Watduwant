# Generated by Django 3.2.5 on 2023-11-07 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_recharge_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appointment',
            name='wallet_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recharge',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recharge',
            name='wallet_status',
            field=models.BooleanField(default=False),
        ),
    ]
