# Generated by Django 3.2.5 on 2023-10-20 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0009_alter_user_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.IntegerField(null=True),
        ),
    ]
