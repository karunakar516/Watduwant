# Generated by Django 3.2.5 on 2023-11-06 15:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_recharge'),
    ]

    operations = [
        migrations.AddField(
            model_name='recharge',
            name='created_at',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
