# Generated by Django 5.1.3 on 2024-11-25 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userregistration_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistration',
            name='reset_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
