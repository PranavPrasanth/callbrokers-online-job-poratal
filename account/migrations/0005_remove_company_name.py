# Generated by Django 4.0.1 on 2022-03-12 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_customer_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='name',
        ),
    ]